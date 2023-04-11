#!/usr/bin/env python3.11

import boto3
from botocore.exceptions import ClientError

cloudformation = boto3.client('cloudformation')

response = cloudformation.describe_stacks()
stacks = response['Stacks']

for stack in stacks:
    print(stack['StackName'])
    
    



