'''
Doc string bitches
'''
import requests
import xml.etree.ElementTree as ET

class ApiCall(object):
    """
    Docstring
    """

    def __init__(self, endpoint, request_parameters, auth_tokens):
        self.request_parameters = request_parameters
        self.auth_tokens = auth_tokens
        self.endpoint = endpoint

    def call(self):
        """
        Docstring
        """
        return self.response_to_xml(requests.get(self.endpoint,
                                                 self.request_parameters,
                                                 auth=(self.auth_tokens[0], self.auth_tokens[1])))

    def call_without_params(self):
        return self.response_to_xml(requests.get(self.endpoint, auth=(self.auth_tokens[0], self.auth_tokens[1])))

    def response_to_xml(self, response):
        if response and response.status_code is 200:
            return ET.fromstring(response.content)