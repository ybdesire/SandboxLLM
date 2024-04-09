import iocextract
import os


def get_ioc_from_query(content):
    result = {'md5':[], 'sha1':[], 'sha256':[]}
    try:
        for x in iocextract.extract_md5_hashes(content):
            result['md5'].append(x.lower())
        for x in iocextract.extract_sha1_hashes(content):
            result['sha1'].append(x.lower())
        for x in iocextract.extract_sha256_hashes(content):
            result['sha256'].append(x.lower())
    except Exception as e:
        print(e)
    print('get_ioc_from_query:', result)
    return result



def get_processed_query(content):
    try:
        ioc_result = get_ioc_from_query(content)
        md5_list = ioc_result['md5']
        if md5_list==[]: 
            return content
        elif len(md5_list)>0:
            md5 = md5_list[0].lower()
            return get_prompt_with_kb(md5)+" Question: "+content
        else:
            return content
    except Exception as e:
        print(e)
        return content


def get_prompt_with_kb(md5):
    s = ''
    try:
        with open(os.path.join(os.path.dirname(__file__), 'doc_{0}.txt'.format(md5.lower())), 'r', encoding='utf-8') as fr:
            s = fr.read()
            print('load knowledge {0} success, content length is {1}'.format(md5, len(s)))
    except Exception as e:
        try:
            with open(os.path.join(os.path.dirname(__file__), '{0}.txt'.format(md5.lower())), 'r', encoding='unicode_escape') as fr:
                s = fr.read()
                print('load knowledge {0} success, content length is {1}'.format(md5, len(s)))
        except Exception as e:
            print(e)
        
    prompt = '''The text between ****SANDBOX_REPORT_START**** and ****SANDBOX_REPORT_END**** below is the analysis report output by the dynamic sandbox after sample {0} is run. Please refer to this analysis report. answer the questions. If the question cannot be answered based on the report, answer "The question cannot be found in the report."
****SANDBOX_REPORT_START****
{1}
****SANDBOX_REPORT_END****
'''.format(md5, s)
    return prompt




