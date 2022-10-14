#!/usr/bin/python3

from pprint import pprint as pp
from jsonrpclib import Server
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

switch = Server( 'https://{}:{}@{}/command-api'.format(
    'arista',
    'arista',
    '192.168.0.12'
) )

response = switch.runCmds('latest', ['show version'])
pp(response)