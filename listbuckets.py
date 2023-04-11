# this is a test of the emergency broadcast system
import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')
response = s3.list_buckets()['Buckets']
for bucket in response:
    print(bucket['Name'])

