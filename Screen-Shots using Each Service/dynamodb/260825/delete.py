from boto3.dynamodb.conditions import Key, Attr
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('mytable')
# Delete a specific item by key
table.delete_item(
    Key={'UserID': 'user123', 'Timestamp': '2025-08-27T17:30:00'}
)

# Conditional Delete: Only if status is 'inactive'
table.delete_item(
    Key={'UserID': 'user123', 'Timestamp': '2025-08-27T17:30:00'},
    ConditionExpression=Attr('status').eq('inactive')
)