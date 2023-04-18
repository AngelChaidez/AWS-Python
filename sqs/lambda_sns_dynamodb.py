import boto3
import requests
dynamodb = boto3.client('dynamodb')
sns_message = boto3.client('sns')



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





    


        

"""
# Extract relevant data from the SNS message

sns_message = event['Records'][0]['Sns']['Message']
# Assuming the SNS message is in JSON format, you can parse it to extract the data
data = json.loads(sns_message)
md5_of_message_body = data['MD5OfMessageBody']
message_id = data['MessageId']
# Extract other relevant data as needed

# Create an item to be stored in DynamoDB
item = {
    'MD5OfMessageBody': {'S': md5_of_message_body},
    'MessageId': {'S': message_id},
    # Add other attributes as needed
}

# Store the item in DynamoDB
dynamodb.put_item(TableName='SNS_Messages', Item=item)

 
"""