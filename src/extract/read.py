'''
Created on 19 okt. 2020

@author: Gerben Rienk
'''
from utils.dictfile import DictFile
from utils.odk_api import OdkApi
from utils.file_writer import FileWriter

import xmltodict
import json

def get_submissions_and_data():
    # read the configuration in a dict
    configuration = DictFile('odk.conFig').read(verbose=False)
    # use the configuration to set up a connector to the odk-api
    odkapi = OdkApi(configuration)
    # now read all the forms we're interested in 
    with open('../config/form_ids.json') as json_file:
        all_forms = json.load(json_file)
            
    # collect the submission for each            
    for one_form in all_forms['forms']:
        my_file = FileWriter('../logs/t.txt')
        my_file.append_to_file(one_form['form_id'] + '\n')
        complete_response = odkapi.submissions.list(one_form['form_id'], verbose=False)
        if complete_response.status_code != 200:
            print('for %s we did not get the expected 200, but %s.' % (one_form['form_id'], complete_response.status_code))
        else:
            submissions_dict=xmltodict.parse(complete_response.text)
            # check if there are any submissions at all
            if not submissions_dict['idChunk']['idList'] is None:
                # we can have just one submission, or a list
                if type(submissions_dict['idChunk']['idList']['id']) is list: 
                    all_ids = submissions_dict['idChunk']['idList']['id']
                    for one_id in all_ids:
                        the_data = odkapi.submissions.get_data(one_form['form_id'], one_form['group_name'], one_id, verbose=False)
                        my_file.append_to_file(json.dumps(xmltodict.parse((the_data.text)), indent=4))
                else:
                    # we have only one submission in this form
                    one_id = submissions_dict['idChunk']['idList']['id']
                    the_data = odkapi.submissions.get_data(one_form['form_id'], one_form['group_name'], one_id, verbose=False)
                    my_file.append_to_file(json.dumps(xmltodict.parse((the_data.text)), indent=4))
                    
                    
if __name__ == '__main__':
    get_submissions_and_data()