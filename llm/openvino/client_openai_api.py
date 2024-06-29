import requests
import json,os,sys

base_url = "http://localhost:8000"


def create_chat_completion(messages, use_stream=False):
    data = {
        "model": 'tq-gpt', 
        "messages": messages,  
        "stream": use_stream,  
        "max_tokens": 1000, 
        "temperature": 0.6, 
        "top_p": 0.1, 
    }

    response = requests.post(f"{base_url}/v1/chat/completions", json=data, stream=use_stream)
    if response.status_code == 200:
        if use_stream:
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')[6:]
                    try:
                        response_json = json.loads(decoded_line)
                        content = response_json.get("choices", [{}])[0].get("delta", {}).get("content", "")
                        print(content)
                    except:
                        print("Special Token:", decoded_line)
        else:
            decoded_line = response.json()
            content = decoded_line.get("choices", [{}])[0].get("message", "").get("content", "")
            return content
    else:
        print("Error:", response.status_code)
        return None



def main():
    question = '''你好'''
    messages = [
            {
              "role": "user",
              "content": question
            }
    ]
    r = create_chat_completion(messages,False)
    print(r)



if __name__=='__main__':
    main()
