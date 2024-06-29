import argparse

from optimum.utils import NormalizedTextConfig, NormalizedConfigManager
from optimum.intel.openvino import OVModelForCausalLM
from optimum.intel.openvino.utils import OV_XML_FILE_NAME

from transformers import (PretrainedConfig, AutoTokenizer, AutoConfig,
                          TextIteratorStreamer, StoppingCriteriaList, StoppingCriteria)

from typing import Optional, Union, Dict, List, Tuple
from pathlib import Path
from threading import Thread
import torch

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from flask import request
import json
from flask import stream_with_context, request



app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task', location='args')
parser2 = reqparse.RequestParser()
parser2.add_argument('messages', location='args', type=list)



class StopOnTokens(StoppingCriteria):
    def __init__(self, token_ids):
        self.token_ids = token_ids

    def __call__(
            self, input_ids: torch.LongTensor, scores: torch.FloatTensor, **kwargs
    ) -> bool:
        for stop_id in self.token_ids:
            if input_ids[0][-1] == stop_id:
                return True
        return False


class OVCHATGLMModel(OVModelForCausalLM):
    """
    Optimum intel compatible model wrapper for CHATGLM2
    """

    def _reshape(
            self,
            model: "Model",
            *args, **kwargs
    ):
        shapes = {}
        for inputs in model.inputs:
            shapes[inputs] = inputs.get_partial_shape()
            shapes[inputs][0] = -1
            input_name = inputs.get_any_name()
            if input_name.startswith('beam_idx'):
                continue
            if input_name.startswith('past_key_values'):
                shapes[inputs][1] = -1
                shapes[inputs][2] = 2
            elif shapes[inputs].rank.get_length() > 1:
                shapes[inputs][1] = -1
        model.reshape(shapes)
        return model



parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('-h',
                    '--help',
                    action='help',
                    help='Show this help message and exit.')
parser.add_argument('-m',
                    '--model_path',
                    default='output\chatglm3ov',
                    required=False,
                    type=str,
                    help='Required. model path')
parser.add_argument('-l',
                    '--max_sequence_length',
                    default=4096,
                    required=False,
                    type=int,
                    help='Required. maximun length of output')
parser.add_argument('-d',
                    '--device',
                    default='GPU',
                    required=False,
                    type=str,
                    help='Required. device for inference')
args = parser.parse_args()
model_dir = args.model_path

ov_config = {"PERFORMANCE_HINT": "LATENCY",
             "NUM_STREAMS": "1", "CACHE_DIR": ""}

tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)

print("====Compiling model====")
ov_model = OVCHATGLMModel.from_pretrained(
    model_dir,
    device=args.device,
    ov_config=ov_config,
    config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
    trust_remote_code=True,
)

streamer = TextIteratorStreamer(
    tokenizer, timeout=60.0, skip_prompt=True, skip_special_tokens=True
)
stop_tokens = [0, 2]
stop_tokens = [StopOnTokens(stop_tokens)]


def convert_history_to_token(history: List[Tuple[str, str]]):

    messages = []
    for idx, (user_msg, model_msg) in enumerate(history):
        if idx == len(history) - 1 and not model_msg:
            messages.append({"role": "user", "content": user_msg})
            break
        if user_msg:
            messages.append({"role": "user", "content": user_msg})
        if model_msg:
            messages.append({"role": "assistant", "content": model_msg})

    model_inputs = tokenizer.apply_chat_template(messages,
                                                 add_generation_prompt=True,
                                                 tokenize=True,
                                                 return_tensors="pt")
    return model_inputs


history = []
print("====Starting conversation====")

    





class OpenAIAPI(Resource):
    def get(self):
        args = parser.parse_args()
        return {'messages': args['messages'], 'http':'get'}

    def post(self):
        args = request.get_json()
        print('=======received message : ')
        #return {'content': args['messages'][0]['content'], 'http':'post'}
        content = args['messages'][0]['content']
        print(args)
        print('end received message=======')
        history = []
        input_text = content
        print("ChatGLM3-6B-OpenVINO:", end=" ")
        history = history + [[input_text, ""]]
        model_inputs = convert_history_to_token(history)
        generate_kwargs = dict(
            input_ids=model_inputs,
            max_new_tokens=10240,
            temperature=0.1,
            do_sample=True,
            top_p=1.0,
            top_k=5,
            repetition_penalty=1.1,
            streamer=streamer,
            stopping_criteria=StoppingCriteriaList(stop_tokens)
        )

        t1 = Thread(target=ov_model.generate, kwargs=generate_kwargs)
        t1.start()
        print('start thread =======')

        partial_text = ""
        for new_text in streamer:
            new_text = new_text
            print(new_text, end="", flush=True)
            partial_text += new_text
        print("\n")
        history[-1][1] = partial_text


        return {'choices': [{'message':{'content':partial_text}}], 'http':'post'}


api.add_resource(OpenAIAPI, '/v1/chat/completions')
print('api started')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port='8000',debug=False)


