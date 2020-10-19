'''
Created on 19 okt. 2020

@author: Gerben Rienk
'''
from utils.dictfile import DictFile

def get_submissions_and_data():
    print('start')
    configuration = DictFile('odk.conFig').read()
    print(configuration)
    print('cycle')

if __name__ == '__main__':
    get_submissions_and_data()