from boto3.dynamodb.conditions import Key
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('mytable')

# 1. Get all items for partition key 'user123'
response_all = table.query(
    KeyConditionExpression=Key('UserID').eq('user123')
)
print("All items for user123:")
for item in response_all['Items']:
    print(item)

# 2. Get items where sort key (Timestamp) begins with '2025-08-21'
response_begins_with = table.query(
    KeyConditionExpression=Key('UserID').eq('user123') & Key('Timestamp').begins_with('2025-08-21')
)
print("\nItems for user123 with Timestamp starting '2025-08-21':")
for item in response_begins_with['Items']:
    print(item)

# 3. Get items where sort key is between '2025-08-20T00:00:00' and '2025-08-22T23:59:59'
response_between = table.query(
    KeyConditionExpression=Key('UserID').eq('user123') &
                           Key('Timestamp').between('2025-08-20T00:00:00', '2025-08-22T23:59:59')
)
print("\nItems for user123 with Timestamp between 2025-08-20 and 2025-08-22:")
for item in response_between['Items']:
    print(item)
