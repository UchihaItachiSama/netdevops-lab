#!/usr/bin/python3

import yaml
from jinja2 import Template, Environment
import json

template = """
{% if management_api_http is defined and management_api_http is not none %}
management api http-commands
{%     if management_api_http.enable_http is defined %}
{%         if management_api_http.enable_http == true %}
   protocol http
{%         elif management_api_http.enable_http == false %}
   no protocol http
{%         endif %}
{%     endif %}
{%     if management_api_http.enable_https is defined %}
{%         if management_api_http.enable_https == true %}
   protocol https
{%         elif management_api_http.enable_https == false %}
   no protocol https
{%         endif %}
{%     endif %}
{%     if management_api_http.enable_unix_socket is defined %}
{%         if management_api_http.enable_unix_socket == true %}
   protocol unix-socket
{%         elif management_api_http.enable_unix_socket == false %}
   no protocol unix-socket
{%         endif %}
{%     endif %}
{%     for vrf in management_api_http.enable_vrfs | sort %}
   !
   vrf {{ vrf }}
      no shutdown
{%     endfor %}
!
{% endif %}
"""

JSON_INPUT = """
{
    "management_api_http": {
        "enable_http": false,
        "enable_https": true,
        "enable_unix_socket": true,
        "enable_vrfs": [
          "default",
          "MGMT"
        ]
    }
}
"""

YAML_INPUT = '''
management_api_http:
  enable_http: false
  enable_https: true
  enable_unix_socket: true
  enable_vrfs:
    - default
    - MGMT
'''

if __name__ == '__main__':    
    j2_template = Template(template, trim_blocks=True)
    
    print("\nRender using JSON input")
    print(j2_template.render(json.loads(JSON_INPUT)))

    print("\nRender using YAML input")
    print(j2_template.render(yaml.safe_load(YAML_INPUT)))