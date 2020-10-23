'''
Created on 20180818

@author: GerbenRienk
'''
import os

class FileWriter(object):
    '''
    Class that creates a file to which the odk-data can be written,
    in one single action
    '''

    def __init__(self, file_name='../logs/report.txt'):
        '''
        provide the file-name
        '''
        self.file_name=file_name
        if os.path.exists(file_name):
            os.remove(file_name)
        
        mode = 'w'
        self._file = open(file_name, mode) 
        self._file.close()
        
        
    def append_to_file(self, text_to_add='*'):
        '''add the text to the file'''
        
        with open(self.file_name, 'a') as f:
            f.write(text_to_add)
        self._file.close()        
        return None
    
    def close_file(self):
        self._file.close()
        return None