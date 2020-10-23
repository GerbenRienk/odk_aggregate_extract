'''
Created on 23 okt. 2020

@author: Gerben Rienk
'''
import json
from utils.file_writer import FileWriter

if __name__ == '__main__':
    my_output = FileWriter('../output_files/data_1234.json')
    submissions = []
    a = {"ka1":"va1"}
    b = {"kb1":"vb1"}
    # print(json.dumps(a))
    submissions.append(a)
    submissions.append(b)
    my_output.append_to_file(json.dumps(submissions))
    
    # print(json.dumps(submissions, indent=2))