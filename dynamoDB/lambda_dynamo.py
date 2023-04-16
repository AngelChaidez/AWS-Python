import boto3
from botocore.exceptions import ClientError
import json
from decimal import Decimal



dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('The_Office_Season_4')

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)

def lambda_handler(event, context):
    http_method = event['httpMethod']
    
    if http_method == 'GET':
        try:
            response = table.scan()
            items = response['Items']
            return {
                'statusCode': 200,
                'body': json.dumps(items, cls=DecimalEncoder, indent=4, sort_keys=True)
            }
        except ClientError as e:
            print(e.response['Error']['Message'])
            return {
                'statusCode': 500,
                'body': json.dumps({'error': e.response['Error']['Message']})
            }
        except Exception as e:
            print(str(e))
            return {
                'statusCode': 500,
                'body': json.dumps({'error': str(e)})
            }
    elif http_method == 'POST':
        try:
            item = json.loads(event['body'])
            table.put_item(Item=item)
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Item added successfully'})
            }
        except ClientError as e:
            print(e.response['Error']['Message'])
            return {
                'statusCode': 500,
                'body': json.dumps({'error': e.response['Error']['Message']})
            }
        except Exception as e:
            print(str(e))
            return {
                'statusCode': 500,
                'body': json.dumps({'error': str(e)})
            }
    elif http_method == 'DELETE':
        try:
            item_key = json.loads(event['body'])
            response = table.delete_item(Key=item_key)
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Item deleted successfully'})
            }
        except ClientError as e:
            print(e.response['Error']['Message'])
            return {
                'statusCode': 500,
                'body': json.dumps({'error': e.response['Error']['Message']})
            }
        except Exception as e:
            print(str(e))
            return {
                'statusCode': 500,
                'body': json.dumps({'error': str(e)})
            }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Unsupported HTTP method'})
        }
