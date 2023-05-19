#!/usr/bin/env python3.11

# this script will start ec2 instances based off of tags 

import boto3
import sys
import os

ec2 = boto3.client('ec2')

regions = [region['RegionName']
           for region in ec2.describe_regions()['Regions']] 

# start instances in us-east-1 with Key labeled 'tag' and Value labeled 'swarm_node'
filters = [{
            'Name': 'tag:swarm_node',
            'Values': ['true']
        }
    ]
for region in regions:
    ec2 = boto3.resource('ec2', region_name=region)
    instances = ec2.instances.filter(Filters=filters)
    for instance in instances:
        instance.start()
        print(f"started instance: {instance.id} in {region}")

