import os
import sys
import json

def level_to_str(level:int) -> str:
    if level > 2:
        return "high-risk"
    elif level == 2:
        return "suspicious"
    else:
        return "normal"

def generate_basic_info(d:dict) -> str:
    if 'info' not in d:
        return
    
    corpus_list = []
    filename = None
    md5 = None
    score = None
    package = None
    duration = None
    machine_name = None
    platform = None
    machine_manager = None
    
    if 'target' in d:
        file = d['target'].get('file')
        if file:
            filename = file.get('name')
            md5 = file.get('md5')
    
    score = d['info'].get('score')
    package = d['info'].get('package')
    duration = d['info'].get('duration')
    platform = d['info'].get('platform')
    
    if 'machine' in d['info']:
        machine_name = d['info']['machine'].get('name')
        machine_manager = d['info']['machine'].get('manager')
    
    if filename:
        corpus_list.append(f'The sample filename is {filename}')
    
    if package:
        corpus_list.append(f'file format is {package}')
    
    if md5:
        corpus_list.append(f'md5 is {md5}')
    
    if platform:
        corpus_list.append(f'platform is {platform}')    
    
    if duration:
        corpus_list.append(f'duration of the analysis is {duration} seconds')
    
    if machine_name:
        corpus_list.append(f'machine name is {machine_name}')
    
    if machine_manager:
        corpus_list.append(f'machine manager is {machine_manager}')    

    if score:
        corpus_list.append(f'and the report score is {score} points')    
        
    if corpus_list:
        corpus = ", ".join(corpus_list) + '.'
        return corpus

def generate_behavior(d:dict) -> str:
    if 'signatures' not in d:
        return
    
    summary_corpus = 'The sample produces the following behavior during analysis:\n'
    for signature in d['signatures']:
        corpus = ''
                
        name = signature['name']
        
        desc = signature['description']
        severity = level_to_str(signature['severity'])
        marks = signature['marks']
        
        # - [进程名] 该行为描述为：[描述] 样本在运行过程中
        corpus += f"- {name}, the risk level is {severity}, the description is: {desc}. "
        
        if name == 'network_http':
            corpus += f"The details are as follows:\n"
            for mark in marks:
                if 'request' in mark:
                    request = mark['request'].replace('\r', '\\r').replace('\n', '\\n')
                    corpus += f"\t[*] The request is: {request}\n"
        
        elif name == 'network_cnc_http':
            corpus += f"The details are as follows:\n"
            for mark in marks:
                corpus += f"\t[*] The suspicious features is {mark['suspicious_features']}, suspicious request is {mark['suspicious_request']}\n"

        elif name == 'creates_exe':
            corpus += f"The details are as follows:\n"
            for mark in marks:
                corpus += f"\t[*] The created file is {mark['ioc']}\n"  
                
        elif name == "self_delete_bat":
            corpus += f"The details are as follows:\n"
            for mark in marks:
                corpus += f"\t[*] The self-deleted file is {mark['ioc']}\n"
        
        elif name == 'creates_user_folder_exe':
            corpus += f"The details are as follows:\n"
            for mark in marks:
                corpus += f"\t[*] The created file file is {mark['ioc']}\n"
        
        elif name == 'ipurl_in_string':
            corpus += f"The details are as follows:\n"
            for mark in marks:
                corpus += f"\t[*] The ioc is {mark['ioc']}\n"
        
        summary_corpus += corpus + '\n'
    
    return summary_corpus

def generate_drop(d:dict) -> str:
    if 'dropped' not in d:
        return
    
    summary_corpus = 'The sample dropped the following files during analysis:\n'
    for dropped in d['dropped']:
        corpus = ''
        
        corpus += f"- The dropped file name is {dropped['name']}, "
        corpus += f"filepath is {dropped['filepath']}, "
        corpus += f"size is {dropped['size']} bytes, "
        corpus += f"md5 is {dropped['md5']}, "
        corpus += f"filetype is \"{dropped['type']}\"."
    
        summary_corpus += corpus + '\n'
    
    return summary_corpus

def generate_network(d:dict) -> str:
    if 'network' not in d:
        return
    
    summary_corpus = 'The sample network traffic information is as follows:\n'
    
    tcp_list = None
    udp_list = None
    http_list = None
    dns_list = None
    
    if 'tcp' in d['network']:
        tcp_list = d['network']['tcp']
    
    if 'udp' in d['network']:
        udp_list = d['network']['udp']
    
    if 'http' in d['network']:
        http_list = d['network']['http']
    
    if 'dns' in d['network']:
        dns_list = d['network']['dns']
    
    for tcp in tcp_list:        
        summary_corpus += f"- The session protocol is tcp, source address is {tcp['src']}, source port is {tcp['sport']}, target address is {tcp['dst']}, target port is {tcp['dport']}, initiating process is {tcp['process_name']}.\n"
    
    for udp in udp_list:
        summary_corpus += f"- The session protocol is udp, source address is {udp['src']}, source port is {udp['sport']}, target address is {udp['dst']}, target port is {udp['dport']}, initiating process is {udp['process_name']}.\n"
    
    for http in http_list:
        data = http['data'].replace('\r', '\\r').replace('\n', '\\n')
        
        summary_corpus += f"- The session protocol is http, method is {http['method']}, version is {http['version']}, host is {http['host']}, port is {http['port']}, data is {data}, uri is {http['uri']}, path is {http['path']}.\n"
    
    for dns in dns_list:
        summary_corpus += f"- The session protocol is dns, query domain is {dns['request']}, type is {dns['type']}"

        if dns['answers']:
            summary_corpus += ', answers are as follows:\n'
            for answer in dns['answers']:
                summary_corpus += f"\t[*] answer is {answer['data']}, type is {answer['type']}\n"
        else:
            summary_corpus += ', answer is empty.\n'
        
    return summary_corpus

def generate_yara(d:dict) -> str:
    if 'target' not in d:
        return
    
    if 'file' not in d['target']:
        return
    
    if 'yara' not in d['target']['file'] or not d['target']['file']['yara']:
        return
    
    yara_list = d['target']['file']['yara']
    summary_corpus = 'The sample hits the following YARA rules:\n'
    
    # This sample hits rule xxx, description is xxx, and the hit content is xxx
    for yara in yara_list:
        name = yara['name']
        desc = yara['meta']['description']
        strings = yara['strings']
        
        corpus = f"- The sample hits yara rule \"{name}\", description is \"{desc}\", and the hit content is {strings}\n"
        
        summary_corpus += corpus
    
    return summary_corpus
    
    
def main():
    root = 'reports'
    corpus_dir = 'corpus'

    for file in os.listdir(root):
        filepath = os.path.join(root, file)
        corpus_path = os.path.join(corpus_dir, file+'.txt')

        with open(filepath, 'rb') as f:
            d = json.load(f)

        with open(corpus_path, 'w') as f:
            corpus = ''

            basic_info = generate_basic_info(d)
            if basic_info:
                corpus += basic_info
                corpus += '\n\n'

            yara = generate_yara(d)
            if yara:
                corpus += yara
                corpus += '\n\n'

            behavior = generate_behavior(d)
            if behavior:
                corpus += behavior
                corpus += '\n\n'

            drop = generate_drop(d)
            if drop:
                corpus += drop
                corpus += '\n\n'

            network = generate_network(d)
            if network:
                corpus += network
                corpus += '\n\n'
            
            f.write(corpus)

if __name__ == "__main__":
    main()
