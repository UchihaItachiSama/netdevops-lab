#!/usr/bin/python2

from pprint import pprint as pp
from jsonrpclib import Server

switch = Server( 'unix:/var/run/command-api.sock' )

response = switch.runCmds('latest', ['show version'])
pp(response)