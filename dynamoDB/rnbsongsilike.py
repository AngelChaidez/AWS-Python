import boto3

 

dynamodb = boto3.resource('dynamodb')
table = boto3.client('dynamodb')

try:
    table = dynamodb.create_table(
        TableName='rnb_songs_i_like',
        KeySchema=[
            {
                'AttributeName': 'album',
                'KeyType': 'HASH'  #Partition key
            },
            {
                'AttributeName': 'artist',
                'KeyType': 'RANGE'  #Sort key
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'album',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'artist',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
# except if table already exists
except Exception as e:
    print("Error creating table: ",e)

item = {'album':{'S':'Forever My Lacy'},
        'artist':{'S':'Jodeci'},
        'info':{'M':{'year':{'S':'1991'},
                     'album':{'S':'Forever My Lacy'}}}}
       


# Add item to the dyanmodb table
table.put_item(TableName = 'rnb_songs_i_like', Item= item)

