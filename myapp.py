#!/usr/bin/python3

import sys
import json
import requests

# Define my variables
domain = ""
subdomain = ""
url = 'https://crt.sh//?q=%.'
url2 = '&output=json'

# Take user input from the CLI. This will be used for the request to crt.sh
domain = sys.argv[1]

r = requests.get(url + domain + url2)
jsondata = json.loads(r.text)
for (key,value) in enumerate(jsondata):
    print(value['name_value'])