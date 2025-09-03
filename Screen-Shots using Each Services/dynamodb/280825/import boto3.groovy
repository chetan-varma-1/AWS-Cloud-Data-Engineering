import boto3

client = boto3.client('dynamodb')

response = client.create_table(
    TableName='sampletable',
    KeySchema=[
        {'AttributeName': 'id', 'KeyType': 'HASH'},    # Partition key
        {'AttributeName': 'name', 'KeyType': 'RANGE'}  # Sort key
    ],
    AttributeDefinitions=[
        {'AttributeName': 'id', 'AttributeType': 'S'},
        {'AttributeName': 'name', 'AttributeType': 'S'},
        {'AttributeName': 'location', 'AttributeType': 'S'}  # Attribute for LSI
    ],
    LocalSecondaryIndexes=[
        {
            'IndexName': 'loc-index',
            'KeySchema': [
                {'AttributeName': 'id', 'KeyType': 'HASH'},
                {'AttributeName': 'location', 'KeyType': 'RANGE'}
            ],
            'Projection': {
                'ProjectionType': 'ALL'
            }
        }
    ],
    GlobalSecondaryIndexes=[
        {
            'IndexName': 'name',
            'KeySchema': [
                {'AttributeName': 'name', 'KeyType': 'HASH'}
            ],
            'Projection': {
                'ProjectionType': 'ALL'
            },
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
)
