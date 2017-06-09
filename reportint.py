import time
from modules.api_call import ApiCall
from modules.get_apps import get_apps


report_request_parameters = []
tokens = []

api_endpoints = {
    'Generate Report': 'https://analysiscenter.veracode.com/api/3.0/generateflawreport.do',
    'Download Report': 'https://analysiscenter.veracode.com/api/3.0/downloadflawreport.do'
}

schema_definitions = {
    'Applist': 'https://analysiscenter.veracode.com/resource/2.0/applist.xsd',
    'Generate Report': 'https://analysiscenter.veracode.com/resource/1.0/archerreportrequest.xsd',
    'Download Report': 'https://analysiscenter.veracode.com/resource/2.0/archerreport.xsd'
}

def setup_request_params(app_ids):
    for app in app_ids:
        report_request_parameters.append(
            (('app_id_list', app), ('scan_type', 'static'))
        )

def request_reports(report_request_parameters):
    for request_parameter in report_request_parameters:
        generate_report = ApiCall(api_endpoints['Generate Report'],
                                  request_parameter,
                                  schema_definitions['Generate Report']).call()
        tokens.append(generate_report.getroot().attrib['token'])
    time.sleep(180)
    for token in tokens:
        get_reports_for_app(token)

def get_reports_for_app(token):
    download_report = ApiCall(api_endpoints['Download Report'],
                              [('token', token)],
                              schema_definitions['Download Report']).call()
    nsmap = {
        'a': 'http://www.archer-tech.com/'
    }
    flaws = download_report.getroot().find('a:Record', namespaces=nsmap).find('a:flaws', namespaces=nsmap)
    parse_flaws(flaws)

def parse_flaws(flaws):
    for flaw in flaws.iterdescendants():
        for record in flaw.getchildren():
            # for flaw in flaws:
            test = record
            test = ""

if not tokens:
    app_ids = get_apps(schema_definitions['Applist'])
    setup_request_params(app_ids)
    request_reports(report_request_parameters)