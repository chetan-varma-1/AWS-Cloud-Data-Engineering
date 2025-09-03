import boto3
client = boto3.client('dynamodb')
table = client.create_table(
    TableName='customer',
        KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH' # Partition key
        },
        {
            'AttributeName': 'email',
            'KeyType': 'RANGE' #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'S'
        },
        {
           'AttributeName': 'email',
            'AttributeType': 'S' 
        }
    ],
    BillingMode='PROVISIONED',
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
    )
print("table sucessfully created")