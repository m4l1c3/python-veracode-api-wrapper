import xml.etree.ElementTree as ET
from modules.api_call import ApiCall

api_endpoints = {
    'Get Apps': 'https://analysiscenter.veracode.com/api/5.0/getapplist.do'
}

get_app_parameters = [
    ('include_user_info', 'true')
]

def get_apps(schema_defitinition):
    apps = ApiCall(api_endpoints['Get Apps'], get_app_parameters, schema_defitinition).call()
    namespace = '{https://analysiscenter.veracode.com/schema/2.0/applist}'
    return [x.attrib['app_id'] for x in apps.findall('{0}app'.format(namespace))]