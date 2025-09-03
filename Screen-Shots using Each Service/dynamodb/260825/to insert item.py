import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('mytable')

# Create/insert an item
table.put_item(
    Item={
        'UserID': 'user123',
        'Timestamp': '2025-08-27T17:30:00',
        'address': '123 Main St',
        'login_count': 1,
        'status': 'active'
    }
)
