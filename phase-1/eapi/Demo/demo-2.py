#!/usr/bin/python3

from pprint import pprint as pp
from EapiClientLib import EapiClient

switch = EapiClient( disableAaa=True, privLevel=15)

response = switch.runCmds('latest', ['show version'])
pp(response)