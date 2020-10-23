'''
Created on 19 okt. 2020

@author: Gerben Rienk
'''
from utils.dictfile import DictFile
from utils.odk_api import OdkApi
from utils.file_writer import FileWriter

import xmltodict
import json
import datetime

def get_submissions_and_data():
    # read the configuration in a dict
    configuration = DictFile('odk.conFig').read(verbose=False)
    # use the configuration to set up a connector to the odk-api
    odkapi = OdkApi(configuration)
    # now read all the forms we're interested in 
    with open('../config/form_ids.json') as json_file:
        all_forms = json.load(json_file)
            
    # loop through the forms and collect the submissions for each          
    for one_form in all_forms['forms']:
        # construct the file-name
        date_stamp = datetime.datetime.now().strftime("%Y%m%d")
        data_file_name = '../output_files/%s_%s.json' % (one_form['form_id'], date_stamp)
        # initiate the data-file
        data_file = FileWriter(data_file_name)
        # initiate all submission-data
        all_submission_data = []
        
        # request the submission-ids
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
                        data_response = odkapi.submissions.get_data(one_form['form_id'], one_form['group_name'], one_id, verbose=False)
                        data_dict = xmltodict.parse((data_response.text))
                        data_dict_subset = data_dict['submission']['data']
                        all_submission_data.append(data_dict_subset)
                else:
                    # we have only one submission in this form
                    one_id = submissions_dict['idChunk']['idList']['id']
                    data_response = odkapi.submissions.get_data(one_form['form_id'], one_form['group_name'], one_id, verbose=False)
                    data_dict = xmltodict.parse((data_response.text))
                    data_dict_subset = data_dict['submission']['data']
                    all_submission_data.append(data_dict_subset)
                
                # now write the collected data to the file
                if one_form['indent'] == 0:
                    data_file.append_to_file(json.dumps(all_submission_data))
                else:
                    data_file.append_to_file(json.dumps(all_submission_data, indent=one_form['indent']))
                    
                    
if __name__ == '__main__':
    get_submissions_and_data()