import os
from modules.api_call import ApiCall

api_endpoints = {
    "Generate Report": "https://analysiscenter.veracode.com/api/3.0/generateflawreport.do",
    "Download Report": "https://analysiscenter.veracode.com/api/3.0/downloadflawreport.do"
}

auth_tokens = (
    os.environ['veracodeapiuser'],
    os.environ['veracodeapipass']
)


report = [
    ('token', '')
]