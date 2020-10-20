'''
Created on 20180818

@author: GerbenRienk
'''
import os

class FileWriter(object):
    '''
    Reporter object that creates a file
    to which lines can be added reporting the activities of oodkoc4,
    so it can be sent at the end of the day
    '''

    def __init__(self, file_name='../logs/report.txt'):
        '''
        Constructor
        '''
        self.file_name=file_name
        if os.path.exists(file_name):
            mode = 'a'
        else:
            mode = 'w'
        self._file = open(file_name, mode) 
        self._file.close()
        
        
    def append_to_file(self, text_to_add='*'):
        '''add the text to the file'''
        
        with open(self.file_name, 'a') as f:
            f.write(text_to_add)
                
        return None
    
    def close_file(self):
        self._file.close()
        return None