#!/usr/bin/ env python3.11

# This script will create a dynamodb table on our AWS account, I am using VScode and am using 
# the AWS toolkit extension that allows me to connect to my AWS account
import os 
import boto3
from botocore.exceptions import ClientError

dynamoDB = boto3.client('dynamodb')

try:
    table = dynamoDB.create_table(
        AttributeDefinitions = [
            {
                'AttributeName' : 'MessageId',
                'AttributeType' : 'S'
            },
            {
                'AttributeName': 'Timestamp',
                'AttributeType': 'S'
            },
        ],
        TableName='SNS_Messages',
            KeySchema=[
                {
                    'AttributeName': 'MessageId',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'Timestamp',
                    'KeyType': 'RANGE'
                }
            ],
        
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }     
    )
    print("Table created successfully")
except ClientError as e:
    print(e.message)