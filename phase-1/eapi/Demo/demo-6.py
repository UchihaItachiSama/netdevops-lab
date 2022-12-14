#!/usr/bin/python3

from pprint import pprint as pp
import pyeapi
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

# Update the credentials based on your Lab Setup
USERNAME = 'arista'
PASSWORD = 'arista'

node = pyeapi.connect(host='leaf1', username=USERNAME, password=PASSWORD, return_node=True)

response = node.enable('show version')

pp(response)