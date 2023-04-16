#!/usr/bin/ envpython3.11
# this is a test of the emergency broadcast system
import os
import boto3
from botocore.exceptions import ClientError

# listing all s3 buckets
s3 = boto3.client('s3')
response = s3.list_buckets()
buckets = response["Buckets"]

# add item to a bucket
print(os.getcwd())

filename = 'The Office Season 4.txt'
bucket_name = 'testbucket-4.11.2023'

with open(filename, 'rb') as data:
    s3.upload_fileobj(data, bucket_name, filename)
    print("Uploading bucket " + bucket_name)

     
# list all of our buckets
for bucket in buckets:
    print(bucket["Name"])
    print(bucket["CreationDate"])
    print(bucket["Key"])
    
response_object = s3.list_objects(
    Bucket= "testbucket-4.11.2023")

print(response_object) 

    
         
       

    

