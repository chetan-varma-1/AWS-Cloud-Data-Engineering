import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName='mytable',
    KeySchema=[
        {
            'AttributeName': 'UserID',
            'KeyType': 'HASH'  # Partition key
        },
        {
            'AttributeName': 'Timestamp',
            'KeyType': 'RANGE'  # Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'UserID',
            'AttributeType': 'S'  # String
        },
        {
            'AttributeName': 'Timestamp',
            'AttributeType': 'S'  # String
        }
    ],
    BillingMode='PAY_PER_REQUEST'
)

# Wait for table creation
table.wait_until_exists()
print("Table 'mytable' has been created and is ready.")
