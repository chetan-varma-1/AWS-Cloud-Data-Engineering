from boto3.dynamodb.conditions import Key, Attr
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('mytable')

# Update: Add a new attribute (address) and increment a numeric one (login_count)
table.update_item(
    Key={'UserID': 'user123', 'Timestamp': '2025-08-27T17:30:00'},
    UpdateExpression="SET address = :addr ADD login_count :inc",
    ExpressionAttributeValues={
        ':addr': '456 Main St',
        ':inc': 2
    }
)

# Conditional Update: Only if item exists (this checks if the attribute exists)
table.update_item(
    Key={'UserID': 'user123', 'Timestamp': '2025-08-27T17:30:00'},
    UpdateExpression="SET last_login = :ts",
    ExpressionAttributeValues={
        ':ts': '2025-08-27T17:10:00'
    },
    ConditionExpression=Attr('UserID').exists()
)