#!/usr/bin/ env python3.11

# This script will create a dynamodb table on our AWS account, I am using VScode and am using 
# the AWS toolkit extension that allows me to connect to my AWS account
import os 
import boto3
from botocore.exceptions import ClientError


# Create a DynamoDB table, if it exists then we exit
separator = "================"

dynamodb = boto3.client('dynamodb')
"""
try:
    table = dynamodb.create_table(
        AttributeDefinitions=[
            {
                'AttributeName': 'Season_Episode_Number',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'Episode_Title',
                'AttributeType': 'S'
            },
        ],
        TableName='The_Office_Season_4',
        KeySchema=[
            {
                'AttributeName': 'Season_Episode_Number',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'Episode_Title',
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
    print(e)
"""
# add a singular item to our table
item = {
    'Season_Episode_Number':{
    'S':'04E01'
    },
    'Episode_Title':{
    'S':'Fun Run (1)'
    },
    'My_Rating':{
    'N':'8.1'
    }
}
dynamodb.put_item(TableName='The_Office_Season_4', Item=item)

print("Item added to table successfully")

# add the rest of our table with the batchwriteitem I will write the rest of the episodes in one batch
try:
    create_table = dynamodb.batch_write_item(
    RequestItems = {
   "The_Office_Season_4":[
      {
         "PutRequest":{
            "Item":{
               "Season_Episode_Number":{
                  "S":"04E02"
               },
               "Episode_Title":{
                  "S":"Fun Run (2)"
               },
               "My_Rating":{
                  "N":"8.1"
               }
            }
         }
      },
      {
         "PutRequest":{
            "Item":{
               "Season_Episode_Number":{
                  "S":"04E03"
               },
               "Episode_Title":{
                  "S":"Dunder Mifflin Infinity (1)"
               },
               "My_Rating":{
                  "N":"7.8"
               }
            }
         }
      },
      {
         "PutRequest":{
            "Item":{
               "Season_Episode_Number":{
                  "S":"04E04"
               },
               "Episode_Title":{
                  "S":"Dunder Mifflin Infinity (2)"
               },
               "My_Rating":{
                  "N":"7.5"
               }
            }
         }
      },
      {
         "PutRequest":{
            "Item":{
               "Season_Episode_Number":{
                  "S":"04E05"
               },
               "Episode_Title":{
                  "S":"Launch Party (1)"
               },
               "My_Rating":{
                  "N":"8.2"
               }
            }
         }
      },
      {
         "PutRequest":{
            "Item":{
               "Season_Episode_Number":{
                  "S":"04E06"
               },
               "Episode_Title":{
                  "S":"Launch Party (2)"
               },
               "My_Rating":{
                  "N":"8.2"
               }
            }
         }
      },
      {
         "PutRequest":{
            "Item":{
               "Season_Episode_Number":{
                  "S":"04E07"
               },
               "Episode_Title":{
                  "S":"Money (1)"
               },
               "My_Rating":{
                  "N":"8.0"
               }
            }
         }
      },
      {
         "PutRequest":{
            "Item":{
               "Season_Episode_Number":{
                  "S":"04E08"
               },
               "Episode_Title":{
                  "S":"Money (2)"
               },
               "My_Rating":{
                  "N":"7.9"
               }
            }
         }
      },
      {
         "PutRequest":{
            "Item":{
               "Season_Episode_Number":{
                  "S":"04E09"
               },
               "Episode_Title":{
                  "S":"Local Ad"
               },
               "My_Rating":{
                  "N":"7.8"
               }
            }
         }
      },
      {
         "PutRequest":{
            "Item":{
               "Season_Episode_Number":{
                  "S":"04E010"
               },
               "Episode_Title":{
                  "S":"Branch Wars"
               },
               "My_Rating":{
                  "N":"7.9"
               }
            }
         }
         
      }
   ]
    
} 
 
) 

except ClientError as e:
    print(e)

print("Table created successfully")

"""
# Scan our table and print out all the items
print("Scanning table")
print(separator*10,"\n" ,dynamodb.scan(TableName='The_Office_Season_4'), "\n", separator*10)



print("Querying table to return an item")
# Querying our table for specific items
query_table = dynamodb.query(
    TableName='The_Office_Season_4', 
    KeyConditionExpression='Season_Episode_Number = :val', 
    ExpressionAttributeValues={
        ':val': {'S': '04E01'}})
print(separator*10, "\n Printing query for Season 04E01 \n", query_table, "\n", separator*10)

# Delete an item from the table dynamodb table 
delete_response = dynamodb.delete_item(
    TableName='The_Office_Season_4', 
    Key={'Season_Episode_Number':{'S':'04E01'},'Episode_Title':{'S':'Fun Run (1)'}})

print("Deleting following item from table: \n", separator*10, delete_response, "\n", separator*10)

# Scanning table to verify deleted item 
print(dynamodb.scan(TableName='The_Office_Season_4'))


# Query table for item deleted
new_query_table = dynamodb.query(
    TableName='The_Office_Season_4', 
    KeyConditionExpression='Season_Episode_Number = :val', 
    ExpressionAttributeValues={
    ':val': {'S': '04E01'}})
print(separator*10, "\n Printing query for Season 04E01 \n", new_query_table, "\n", separator*10)


# Delete the table from the database
delete_table = dynamodb.delete_table(TableName = 'The_Office_Season_4')
print("Deleting table: \n", separator*10, delete_table, "\n", separator*10)



#verify deletion of table
print(dynamodb.scan(TableName='The_Office_Season_4'))

"""