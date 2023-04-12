#!/usr/bin/env python3.11
# this script is used to create a new enviroment in cloud 9 with name = "cloud9-" + 
# todays date

import boto3
from botocore.exceptions import ClientError
from datetime import datetime

name = "cloud9-"
todays_date = datetime.now().strftime("%Y-%m-%d")



cloud9 = boto3.client('cloud9')

response = cloud9.create_environment_ec2(
    name= name + todays_date,
    instanceType='t2.micro',
    imageId='amazonlinux-2-x86_64',
    
)
