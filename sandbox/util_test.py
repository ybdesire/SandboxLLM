import requests
import json,os,sys

base_url = "http://localhost:8000"


def create_chat_completion(messages, use_stream=False):
    data = {
        "model": 'sandboxllm', 
        "messages": messages,  
        "stream": use_stream,  
        "max_tokens": 1000, 
        "temperature": 0.6, 
        "top_p": 0.1, 
    }

    response = requests.post(f"{base_url}/v1/chat/completions", json=data, stream=use_stream)
    if response.status_code == 200:
        c = ''
        if use_stream:
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')[6:]
                    try:
                        response_json = json.loads(decoded_line)
                        content = response_json.get("choices", [{}])[0].get("delta", {}).get("content", "")
                        c += content
                        # print(content, end='')
                    except:
                        # print("\nSpecial Token:", decoded_line)
                        pass
            # print()
            return c
        else:
            decoded_line = response.json()
            content = decoded_line.get("choices", [{}])[0].get("message", "").get("content", "")
            # print(content, end='')
            return content
    else:
        print("Error:", response.status_code)
        return None

corpus_list = []
file_list = os.listdir('corpus')
file_list.sort()

file_list = ['1c4989acfd741d3d1612b3495e087a2c.json.txt', '2be5b0bcd650b276dd197f02f194876d.json.txt', '24c94559b2c3b1a22b0b8a4b6447df2d.json.txt', '699489a273ecf23f09fea4babde36521.json.txt', 'bc38dc28ee84904c66a5655b02c7aea2.json.txt', 'c723391b16bdca24384b43ffcdefafaa.json.txt', 'e0b0b3355219780122099a6666ce8439.json.txt', 'e7f6331f695ce1992adab166351bcd4a.json.txt', 'e8ab096460fe259317cf58a12caf041a.json.txt', 'e98c8b0f0eec953b09c355bd6835c4e7.json.txt', 'e104f17530f4a20def398c53ae5665ea.json.txt']

for file in file_list:
    filepath = os.path.join('corpus', file)
    # print(file)
    with open(filepath, 'r') as f:
        buf = f.read()
        corpus_list.append(buf)

answer_dict = {
    0: {
        'bool': {
            'Does this sample hit the Yara rule? Please answer no or yes.': True,
            'Does this sample hit the IDS traffic rule? Please answer no or yes.': False,
            'Does this sample have high-risk behaviors? Please answer no or yes.': True,
            'Does this sample dropped files? Please answer no or yes.': False,
        },
        
        'summary': {
            'What is the md5 of this sample?': ['1c4989acfd741d3d1612b3495e087a2c'],
            'How long does it take to analyze this sample?': ['124'],
            'Which Yara rules does this sample hit?': ['embedded_win_api', 'powershell'],
            'What are the high-risk behaviors of this sample?': ['martian_command_process',],
            'What are the suspicious behaviors of this sample?': ['guard page', 'hidden window', 'long command line'],
        }
    
    },
    1: {
        'bool': {
            'Does this sample hit the Yara rule? Please answer no or yes.': True,
            'Does this sample hit the IDS traffic rule? Please answer no or yes.': False,
            'Does this sample have high-risk behaviors? Please answer no or yes.': False,
            'Does this sample dropped files? Please answer no or yes.': True,
        },
        
        'summary': {
            'What is the md5 of this sample?': ['2be5b0bcd650b276dd197f02f194876d'],
            'How long does it take to analyze this sample?': ['82'],
            'Which Yara rules does this sample hit?': ['powershell'],
            'What are the high-risk behaviors of this sample?': ['does not',],
            'What are the suspicious behaviors of this sample?': ['guard page'],
            'What files does this sample drop?': ['049802f3d3a6803f'],
        }
    
    },
    2: {
        'bool': {
            'Does this sample hit the Yara rule? Please answer no or yes.': True,
            'Does this sample hit the IDS traffic rule? Please answer no or yes.': False,
            'Does this sample have high-risk behaviors? Please answer no or yes.': True,
            'Does this sample dropped files? Please answer no or yes.': True,
            'Does this sample have network behavior? Please answer no or yes.': True,
        },
        
        'summary': {
            'What is the md5 of this sample?': ['24c94559b2c3b1a22b0b8a4b6447df2d'],
            'How long does it take to analyze this sample?': ['119'],
            'Which Yara rules does this sample hit?': ['powershell'],
            'What are the high-risk behaviors of this sample?': ['a binary', 'command shell', 'scheduled task'],
            'What files does this sample drop?': ['ddf3085658167a79', 'e72b788676bbe447', '34944b82a449df4f', '1ef07109704d9ab0'],
            'What is the most common extension for the files dropped by this sample?': ['ps1'],
            'Which IP addresses was visited by this sample?': ['45.154.98.194'],
            'Which domain names are queried in this sample?': ['services.work.gd'],
            'What are the query results of services.work.gd?': ['45.154.98.194'],
        }
    },
    3: {
        'bool': {
            'Does this sample hit the Yara rule? Please answer no or yes.': False,
            'Does this sample hit the IDS traffic rule? Please answer no or yes.': False,
            'Does this sample have high-risk behaviors? Please answer no or yes.': True,
            'Does this sample dropped files? Please answer no or yes.': True,
            'Does this sample have network behavior? Please answer no or yes.': True,
        },
        
        'summary': {
            'What is the md5 of this sample?': ['699489a273ecf23f09fea4babde36521'],
            'How long does it take to analyze this sample?': ['114'],
            'What are the high-risk behaviors of this sample?': ['creates_user_folder_exe', 'process_martian', 'self_delete_bat'],
            'What files does this sample drop?': ['c6fc91e5b6d5391b', '955f70ea652c851f', '51f663012e3953d5', 'ef8a6ee994950ce3', '13b9d99d97449e76'],
            'What is this sample self-deleting file?': ['zilkofux.cmdline'],
            'What is the file created by this sample in the user directory?': ['zilkofux.dll'],
            'Which IP addresses was visited by this sample?': ['82.61.9.223'],
            'What is the protocol between the sample and 82.61.9.223?': ['tcp'],
        }
    },
    4: {
        'bool': {
            'Does this sample hit the Yara rule? Please answer no or yes.': False,
            'Does this sample hit the IDS traffic rule? Please answer no or yes.': False,
            'Does this sample have high-risk behaviors? Please answer no or yes.': True,
            'Does this sample dropped files? Please answer no or yes.': True,
            'Does this sample have network behavior? Please answer no or yes.': True,
        },
        
        'summary': {
            'What is the md5 of this sample?': ['bc38dc28ee84904c66a5655b02c7aea2'],
            'How long does it take to analyze this sample?': ['133'],
            'What is the machine name of the virtual machine': ['win7_office2013'],
            'What are the high-risk behaviors of this sample?': ['executable file', 'martian processes', 'delete', 'executed files'],
            'What files does this sample drop?': ['f2c563322c4d6a4c', '514d1775e96df441', 'c6a747c1a08365ed', '0417cd88fd2d8feb', 'c9c055a1290d6f73', '939abf80f24d35fe'],
            'What is this sample self-deleting file?': ['gndvu4bb.cmdline'],
            'What is the file created by this sample in the user directory?': ['gndvu4bb.dll'],
            'Which IP and domain was visited by this sample?': ['198.185.159.145', 'bemnyc.com'],
            'What is the protocol between the sample and bemnyc.com?': ['http'],
            'Which dns query IP of the domain: bemnyc.com did the sample finally choose to establish a session with?': ['198.185.159.145'],
        }
    },
}

question_count = 0
pass_count = 0


print('filename,question,answer,expect,pass?')
for idx in answer_dict:    
    
    # print(f"========= {idx} =========")
    corpus = corpus_list[idx]
    
    for _type in answer_dict[idx]:
        for question, answer in answer_dict[idx][_type].items():
            gpt_question = f'''
The text between ****SANDBOX_REPORT_START**** and ****SANDBOX_REPORT_END**** below is the analysis report output by the dynamic sandbox after sample is run. Please refer to this analysis report. answer the questions. If the question cannot be answered based on the report, answer "The question can not be found in the report.

****SANDBOX_REPORT_START****

{corpus}

****SANDBOX_REPORT_END****
    
question：{question}
            '''
            
            messages = [
                    {
                    "role": "user",
                    "content": gpt_question
                    }
            ]
            
            question_count += 1
            
            gpt_answer = create_chat_completion(messages, True)
            print(file_list[idx], end=',')
            
            question = question.replace('"', r'""')
            gpt_answer = gpt_answer.replace('"', r'""').replace('\n', '\\n')
            if isinstance(answer, str):
                answer = answer.replace('"', r'""')
            
            print(f"\"{question}\"", end=',')
            print(f"\"{gpt_answer}\"", end=',')    
            print(f"\"{answer}\"", end=',')
            
            is_pass = False
            
            if _type == 'bool':
                if answer:
                    if any(word in gpt_answer for word in ['Yes', 'yes']):
                        is_pass = True
                        pass_count += 1
                else:
                    if any(word in gpt_answer for word in ['No', 'The question can not be found in the report.', 'no']):
                        is_pass = True
                        pass_count += 1
            
            elif _type == 'summary':
                if all(keyword.lower() in gpt_answer.lower() for keyword in answer):
                    is_pass = True
                    pass_count += 1
            
            if is_pass:
                print('yes')
            else:
                print('no')


print("\n\nTotal questions: ", question_count)
print("Passed: ", pass_count)
print("Pass rate:", pass_count / question_count)
