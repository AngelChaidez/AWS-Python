#!/usr/bin/ env python3.11

import boto3
import random 
import string
from datetime import datetime
from botocore.exceptions import ClientError
import logging

# create a sqs connection
sqs_client = boto3.client('sqs')

# generate an SQS name based on todays date
def create_service_name(name):
    todays_date = datetime.now().strftime("%Y-%m-%d")
    name += todays_date+ "".join(random.choices(string.ascii_letters + string.digits, k=5))
    return name

# logging the client connection
logging.basicConfig(filename='translate.log',level=logging.DEBUG)

# Create an SQS queue in the format of "SQS_todays_date" eg. "SQS_4-18-2023"

def create_sqs(client):  
    name = "SQS_"
    sqs_name= create_service_name(name)
    response = sqs_client.create_queue(
        QueueName=name)
    print(f"Queue created : {sqs_name}")
    logging.info(f"Successfully created an SQS Queue {name}")
    

if __name__ == "__main__":
     create_sqs(sqs_client)
    
