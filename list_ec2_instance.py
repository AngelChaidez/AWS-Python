#!/usr/bin/env python3.11

import boto3
from botocore.exceptions import ClientError

# list all ec2 instances
ec2 = boto3.client('ec2')
response = ec2.describe_instances()['Reservations']
for reservation in response:
    for instance in reservation['Instances']:
        print(instance['InstanceId'])
        print(instance['State']['Name'])
        print(instance['State']['Code'])
        print(instance['PrivateIpAddress'])
        print(instance['PublicIpAddress'])
        print(instance['PrivateDnsName'])
        print(instance['PublicDnsName'])
        print(instance['InstanceType'])
        print(instance['KeyName'])
        print(instance['Placement']['AvailabilityZone'])
        print(instance['Placement']['GroupName'])
        print(instance['Placement']['Tenancy'])
        print(instance['LaunchTime'])