#!/usr/bin/env python3.11
import sys
sys.path.append("/usr/local/lib/python3.11/dist-packages (1.2.0)")
import boto3
import os
from botocore.exceptions import ClientError
import schedule
import datetime
import time
import time


ec2 = boto3.client('ec2')

regions = [region['RegionName']
           for region in ec2.describe_regions()['Regions']]

# create a cron job to stop all running instances on desired schedule
def cron_job():
    for region in regions:
        ec2_resource = boto3.resource('ec2', region_name=region)
        print("Region :", region)

        instances = ec2_resource.instances.filter(
                Filters=[{'Name': 'instance-state-name',
                        'Values': ['running']}])
        
        # stop all running instances
        for instance in instances:
            instance.stop()
            print("Instance stopped:", instance.id)


if __name__ == '__main__':
    # schedule a cron job to stop all running instances on desired schedule
    # on fridays at 10p
    cron_job()
