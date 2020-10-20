'''
Created on 19 okt. 2020

@author: Gerben Rienk
'''

class DictFile(object):
    '''
    classdocs
    '''


    def __init__(self, dict_file_name, rel_path=''):
        '''
        Constructor
        '''
        self.dict_file_name = dict_file_name
        if rel_path == '':
            rel_path = '../config'
        self.rel_path = rel_path
        
    def read(self, verbose=False):
        """
        Rel_path is the relative path to folder config;
        by default it is assumed that folder config is a sibling of the current folder,
        but this can be specified if otherwise. 
        """
        myDict = {}
        try:
            # read the file from disk
            with open(self.rel_path + '/' + self.dict_file_name) as f:
                for line in f:
                    # comment lines start with a #
                    if line[0] != "#":
                        # only look at lines we can process
                        if len(line.split()) == 2:
                            (key, val) = line.split()
                            myDict[key] = val
                # we're done, so close the file
                f.close()
        except:
            print('could not open file %s in %s/' % (self.dict_file_name, self.rel_path))
        if verbose == True:
            print('read resulted in %s' % myDict)   
        return myDict    