import os
from modules.api_call import ApiCall

api_endpoints = {
    "Generate Report": "https://analysiscenter.veracode.com/api/3.0/generateflawreport.do",
    "Download Report": "https://analysiscenter.veracode.com/api/3.0/downloadflawreport.do"
}

app_ids = {

}

report_request_parameters = [
    ('app_id_list', ','.join(app_ids)),
    ('scan_type', 'static'),
]

auth_tokens = (
    os.environ['veracodeapiuser'],
    os.environ['veracodeapipass']
)

# generate_report = ApiCall(api_endpoints['Generate Report'], report_request_parameters, auth_tokens)
#
# generated_report =  generate_report.call()
token = '' #generated_report.attrib['token']

# download_report = requests.get(str(api_endpoints['Download Report'] + '?token='), auth=(auth_tokens[0], auth_tokens[1]))
download_report = ApiCall(api_endpoints['Download Report'], [('token', token)], auth_tokens)
report = download_report.call()
