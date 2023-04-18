#!/usr/bin/ env python3.11

# This script will send messages to an SQS queue

import boto3 
import json
import random
from datetime import datetime
from botocore.exceptions import ClientError
import string



todays_date = datetime.now().strftime("%Y-%m-%d")
message = todays_date +"".join(random.choices(string.ascii_letters + string.digits, k=5))
sqs = boto3.client('sqs')
print(message)

response = sqs.send_message(
QueueUrl='https://sqs.us-east-1.amazonaws.com/758719472525/SQS_2023-04-17',
MessageBody= (f"Sucessfully sent: {message}")
)
mbody =json.dumps(response, indent=4)
json_message = json.dumps(response, indent=4)


