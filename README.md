# odk_aggregate_extract

This repository will be used to create a script that will extract data from an odk-aggregate-server, version 2.0.5.
For this we will send requests to the api using two end-points: /view/submissionList and /view/downloadSubmission

I built further on the answers that were kindly provided on https://forum.getodk.org/t/authentication-to-odk-via-python/2224/6 

We will use xmltodict, so in eclipse: Window -> Preferences and in the pop-up window, navigate to PyDev -> Interpreters -> Python Interpreter
Click button manage-with-pip and enter xmltodict

The result will be two sets of files: one in xml format and one in json format.

## preparations
To use the scripts you should have access to the odk-aggregate-api. Create in config a file called odk.config. And you should have a list of form-id in config/form_ids.json.
Furthermore you should create a folder "output_files"
