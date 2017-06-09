import os
from StringIO import StringIO

import requests

from lxml import etree
import urllib2

class ApiCall(object):
    """
    The ApiCall class is a generic wrapper for making calls to the Veracode API
    """

    def __init__(self, endpoint, request_parameters, xml_schema_url):
        """

        :param endpoint: the API endpoint to be called
        :param request_parameters: request specific parameters for the API endpoint defined by parameter endpoint
        :param xml_schema_url: the XSD URL for the endpoint request this instantiation will be retrieving
        """

        self.request_parameters = request_parameters
        self.auth_tokens = (
            os.environ['veracodeapiuser'],
            os.environ['veracodeapipass2']
        )
        self.endpoint = endpoint
        # self.parser = etree.XMLParser(ns_clean=True)
        self.schema = etree.XMLSchema(
                        etree.fromstring(urllib2.urlopen(xml_schema_url).read()))

    def call(self):
        """
        the call method initiates the API call and returns an XML object from the validated response
        """
        return self.response_to_xml(requests.get(self.endpoint,
                                                 self.request_parameters,
                                                 auth=(self.auth_tokens[0], self.auth_tokens[1])))

    def response_to_xml(self, response):
        """
        The response_to_xml method simply validates the incoming response data, if it validates then we will pass
        the XML response back to the caller.
        :param response: the API call response that we're processing
        :return: a lxml object for further processing
        """
        if response and response.status_code is 200:
            data = etree.parse(StringIO(response.content))
            if(self.schema.validate(data)):
                return data