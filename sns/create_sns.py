#!/usr/bin/ env python3.11

# import a function from another module will be used to generate a name at random
import boto3
import os
import sys
from botocore.exceptions import ClientError
sys.path.append("sqs") 
from create_sqs import create_service_name


sns_client = boto3.client('sns')
sns_name = create_service_name('SNS_SQS_')
print(sns_name)

try:
    response = sns_client.create_topic(
        Name = sns_name)
    print(f"SNS topic created successfully : {sns_name}")
except ClientError as e:
    print(e.message)