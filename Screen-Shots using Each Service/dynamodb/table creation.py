import boto3
client = boto3.client('dynamodb')
table = client.create_table(
    TableName='customers',
        KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'S'
        }
    ],
    BillingMode='PAY_PER_REQUEST'
    )
print("table sucessfully created")
