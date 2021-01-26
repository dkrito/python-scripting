#!/usr/bin/env python3

import re
import operator
import subprocess
import sys
import pandas as pd

def retrieve_messages(pattern, num):

    #log_f=sys.argv[1]
    allmatches = {}
    
    with open("syslog.log", "r") as f:
        if num == 1:
            for line in f.readlines():
                match = re.search(pattern, line)
                if match != None:
                    if match.group(2) in allmatches:
                        allmatches[match.group(2)] += 1
                    else:
                        allmatches.update({match.group(2):1})
        else:
            result = re.findall(pattern, f.read())
            for match in result:
                log_type = match[0]
                log_user = match[1]
                if not log_user in allmatches:
                    allmatches.update({log_user:{"INFO": 0, "ERROR": 0}})
                
                allmatches[log_user][log_type] += 1 

    f.close()
    
    return allmatches

def sort_dict(to_sort):

    sorted_dict = {}
    sorted_dict = sorted(to_sort.items(), key = operator.itemgetter(1), reverse=True)

    return sorted_dict

def main():
    
    user_pattern_EM = r'(ERROR):\s(.*)\('
    user_pattern_IE = r'(ERROR|INFO):\s.*\((\w*)\)'

    user_log1 = retrieve_messages(user_pattern_EM, 1)
    user_log2 = retrieve_messages(user_pattern_IE, 2)
    
    sorted_user_log1 = sort_dict(user_log1)

    df1 = pd.DataFrame(sorted_user_log1)
    df2 = pd.DataFrame(user_log2).transpose()
    
    df1.to_csv('error_message.csv', index=False, header=['Error', 'Count'])
    df2.to_csv('user_statistics.csv', index_label='Username')
    
main()