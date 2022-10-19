#!/usr/bin/python3

from pprint import pprint as pp
from jsonrpclib import Server
import yaml
from cvprac.cvp_client import CvpClient
from jinja2 import Template, Environment, FileSystemLoader
import ssl
import uuid
from datetime import datetime
import time
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

DEVICE_IPS = [
    'leaf1',
    'leaf2',
    'leaf3', 
    'leaf4'
]

# Update the credentials based on your Lab Setup
USERNAME = 'arista'
PASSWORD = 'arista'

TEMPLATE_FILE = 'leaf-mlag-template.j2'

def generate_cli_config():
    # Load JINJA Template
    j2_loader = FileSystemLoader(searchpath='./')
    j2_env = Environment(loader=j2_loader, trim_blocks=True)
    j2_template = j2_env.get_template(TEMPLATE_FILE)

    for device in DEVICE_IPS:
        with open('./structured_configs/{}.yaml'.format(device)) as stream:
            yaml_vars = yaml.safe_load(stream)
        print("\nGenerated configuration for {} switch\n".format(device))
        print(j2_template.render(yaml_vars))
        with open('./intended_configs/{}.cfg'.format(device), "w") as fobj:
            fobj.write(j2_template.render(yaml_vars))

def upload_configlets():
    client = CvpClient()
    client.connect(nodes=['cvp'], username=USERNAME, password=PASSWORD)
    for device in DEVICE_IPS:
        with open('./intended_configs/{}.cfg'.format(device)) as stream:
            configlet = stream.read()
        client.api.add_configlet('Phase-1-MLAG-{}'.format(device), configlet)
    configlet_list = client.api.search_configlets("Phase-1-MLAG")
    print("\nFollowing configlets uploaded to CVP\n.")
    for configlet in configlet_list['data']:
        print(configlet['name'])

def assign_configlets():
    taskList = []
    client = CvpClient()
    client.connect(nodes=['cvp'], username=USERNAME, password=PASSWORD)
    for device in DEVICE_IPS:
        switch = client.api.get_device_by_name(device + '.atd.lab')
        configlet = client.api.get_configlet_by_name('Phase-1-MLAG-{}'.format(device))
        result = client.api.apply_configlets_to_device("", switch, [configlet])
        if result['data']['status'] == 'success':
            print("\nSuccessfully assigned configlet {} to device {}.\n".format('Phase-1-MLAG-{}'.format(device), device))
            taskList.append(result['data']['taskIds'][0])
    return taskList

def execute_tasks(taskList):
    cc_id = str(uuid.uuid4())
    name = f"Change_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    client = CvpClient()
    client.connect(nodes=['cvp'], username=USERNAME, password=PASSWORD)
    print("\nCreating Change Control\n")
    client.api.change_control_create_for_tasks(cc_id, name, taskList, series=False)

    approve_note = "Approving CC via cvprac for Phase-1-Jinja-challenge-lab"
    client.api.change_control_approve(cc_id, notes=approve_note)

    print("\nExecuting Change Control\n")
    start_note = "Start CC via cvprac for Phase-1-Jinja-challenge-lab"
    client.api.change_control_start(cc_id, notes=start_note)
    print("\nChange Control Executed\n")

def check_mlag():
    for device in DEVICE_IPS:
        switch = Server( "https://{}:{}@{}/command-api".format(
            USERNAME,
            PASSWORD,
            device
        ) )
        result = switch.runCmds('latest', ['show mlag'], 'json')[0]
        print("\nSwitch {} MLAG State is {} & {}\n".format(device, result['state'], result['negStatus']))

if __name__ == '__main__':
    # load YAML & JINJA to render the CLI output
    generate_cli_config()

    # upload the configs to CVP as configlets
    upload_configlets()

    # Map the configlets to respective devices
    taskList = assign_configlets()
    
    # Create & Execute Change Control
    execute_tasks(taskList)

    # Check MLAG Status
    time.sleep(60) # wait for sometime before we probe the switches.
    check_mlag()