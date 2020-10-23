'''
Created on 21 Oct 2020

@author: Gerben Rienk
'''
from utils.dictfile import DictFile
from utils.odk_api import OdkApi

import xmltodict
import json

def get_forms():
    # read the configuration in a dict
    configuration = DictFile('odk.conFig').read(verbose=False)
    # use the configuration to set up a connector to the odk-api
    odkapi = OdkApi(configuration)
    forms_response = odkapi.forms.list(verbose=True)
    if forms_response.status_code != 200:
        print('something went wrong when requesting the list of forms.')
    else:
        all_forms = xmltodict.parse(forms_response.text)
        print(json.dumps(all_forms, indent=2))
    t = odkapi.forms.xml('KoCoFilterpapier-2', True)
    print(t)
if __name__ == '__main__':
    get_forms()