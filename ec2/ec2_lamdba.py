#!/usr/bin/env python3.11

import boto3
import os
from botocore.exceptions import ClientError

ec2 = boto3.resource('ec2')
AMI = os.environment['AMI']
INSTANCE_TYPE = os.environment['INSTANCE_TYPE']
KEY_NAME = os.environment['KEY_NAME']
SUBNET_ID = os.environment['SUBNET']



# Create an ec2 instance
def lambda_handler(event, context):
    instance = ec2.create_instance(
        ImageId = AMI,
        InstanceType = INSTANCE_TYPE,
        KeyName = KEY_NAME,
        SubnetId = SUBNET_ID,
        MaxCount = 1,
        MinCount = 1
    )
    print("Created EC2 instance", instance[0].id)