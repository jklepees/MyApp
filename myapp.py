#!/usr/bin/python3

import sys
import json
import requests
import boto3

#AWS DB Variables and such.
#Check to see if table exists. If not then create it. 
dynamodb_client = boto3.client('dynamodb')
#I need to set up the correct db so that it points to my local db. 
try:
    response = dynamodb_client.create_table(
        AttributeDefinitions=[
            {
                'AttributeName': 'Domain',
                'AttributeType': 'S',
            },
            {
                'AttributeName': 'SubDomain',
                'AttributeType': 'S',
            },
        ],
        KeySchema=[
            {
                 'AttributeName': 'Domain',
                'KeyType': 'HASH',
            },
            {
                'AttributeName': 'SubDomain',
                'KeyType': 'RANGE',
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapcityUnits': 5,
        },
        TableName='SubdomainList',
    )
except dynamodb_client.exceptions.ResourceInUseException as e:
    print(e)
    pass

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