from boto3.dynamodb.conditions import Key, Attr
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('mytable')

# Scan operation with filter
response_scan = table.scan(
    FilterExpression=Attr('UserID').eq('user123')
)
print("Scan results:", response_scan['Items'])

# Query operation (recommended)
response_query = table.query(
    KeyConditionExpression=Key('UserID').eq('user123')
)
print("Query results:", response_query['Items'])
