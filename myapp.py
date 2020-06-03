#!/usr/bin/python3

import sys
import json
import urllib.request
import urllib.parse

# Define my variables
domain = ""
subdomain = ""
url = 'https://crt.sh//?q='

# Take user input from the CLI. This will be used for the request to crt.sh
domain = sys.argv[1]

req = urllib.request.urlopen('url' + 'domain')
print(req.read().decode('utf-8'))