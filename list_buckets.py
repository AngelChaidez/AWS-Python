#!/usr/bin/env python3.11
# this is a test of the emergency broadcast system

import boto3
from botocore.exceptions import ClientError

# listing all s3 buckets
s3 = boto3.client('s3')
response = s3.list_buckets()
buckets = response["Buckets"]

# list all of our buckets
for bucket in buckets:
    print(bucket["Name"])
    print(bucket["CreationDate"])
    print(response["Owner"]["DisplayName"])


     
   

    

    
         
       

    

