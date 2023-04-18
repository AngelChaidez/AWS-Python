#!/usr/bin/ env python3.11

# This script will send messages to an SQS queue through a lambda function. I will be called/triggered 
# by an HTTP API gateway. The messages will be displayed in the format of todays date with random 5 
# characters and numbers.

import boto3 
import json
import random
from datetime import datetime
from botocore.exceptions import ClientError
import string

# Use today's date format to create a string representation along wih a random 5 character long 
# string to be added to the date e.g. "2023-04-18-g3JUR"

todays_date = datetime.now().strftime("%Y-%m-%d")
message = todays_date +"-" + "".join(random.choices(string.ascii_letters + string.digits, k=5))
sqs = boto3.client('sqs')

# This is the def lambda_handler that will be used for creating a message object to be sent to 
# an SQS queue. Our message object will be sent over to our designated SQS queue via its Queue
# URL
response = sqs.send_message(
QueueUrl='https://sqs.us-east-1.amazonaws.com/758719472525/SQS_2023-04-17',
MessageBody= (f"Sucessfully sent: {message}")
)
mbody =json.dumps(response, indent=4)
json_message = json.dumps(response, indent=4)


