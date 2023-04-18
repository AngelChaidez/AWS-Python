#!/usr/bin/ env python3.11

import boto3
import random 
from datetime import datetime
from botocore.exceptions import ClientError
import logging

# create a sqs connection
sqs_client = boto3.client('sqs')

# generate an SQS name based on todays date
name = "SQS_"
todays_date = datetime.now().strftime("%Y-%m-%d")
name += todays_date

# logging the client connection
logging.basicConfig(filename='translate.log',level=logging.DEBUG)



def create_sqs(client):   
    response = sqs_client.create_queue(
        QueueName=name)
    print(f"Queue created : {name}")
    

if __name__ == "__main__":
    create_sqs(sqs_client)
