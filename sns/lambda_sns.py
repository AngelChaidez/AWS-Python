#!/usr/bin/ env python3.11
import json

def lambda_handler(event, context):
    # TODO implement
    import boto3

    sns = boto3.client('sns')
    
    sns_message = sns.publish(
    TopicArn='arn:aws:sns:us-east-1:758719472525:SNS_SQS_2023-04-18DRO9C',
    Message='SNS_SQS_2023 has received a message',
    Subject='New SQS messages',
    )
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

