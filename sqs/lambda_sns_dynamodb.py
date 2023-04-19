import json
import boto3
import requests
dynamodb = boto3.client('dynamodb')
sns_message = boto3.client('sns')

def lambda_handler(event, context):
    res = requests.get('https://nllah1ta4l.execute-api.us-east-1.amazonaws.com/testing/SQS_message', auth=('user', 'pass'))
    dict = res.text
    dict = res.json()
    message_id = dict.get('MessageId')
    timestamp = dict.get('ResponseMetadata', {}).get('HTTPHeaders', {}).get('date')
    print(message_id)
    print(timestamp)


    dynamodb.put_item(
       TableName='SNS_Messages',
        Item={
                    'MessageId': {'S': message_id},
                    'Timestamp': {'S': timestamp},
                    }
                )


    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

