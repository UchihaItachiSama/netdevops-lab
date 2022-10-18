#!/usr/bin/python3

import yaml
from jinja2 import Template, Environment, FileSystemLoader
import json

TEMPLATE_FILE = "mlag-template.j2"

YAML_FILE = './leafs.yaml'

if __name__ == '__main__':    
    j2_loader = FileSystemLoader(searchpath='./')
    j2_env = Environment(loader=j2_loader, trim_blocks=True)
    j2_template = j2_env.get_template(TEMPLATE_FILE)

    with open(YAML_FILE) as file_obj:
        yaml_vars = yaml.safe_load(file_obj)

    print(j2_template.render(yaml_vars))