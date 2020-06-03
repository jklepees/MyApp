#!/usr/bin/python3

import sys
import json
import requests
import boto3

#Removed the part where i check/create a table. It is not needed as the table will be created prior to. 
# AWS DynamoDB information should go here. TO be used in the for statment.
if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
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
    #print(value['name_value'])
    subdomain = value['name_value']
    table = dynamodb.Table('SubDomains')
    response = table.put_item(
        Item={
            "SubDomain": subdomain,
            "Domain": domain
        }
    )
    print("subdomain")