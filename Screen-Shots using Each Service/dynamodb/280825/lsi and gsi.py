import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')

def create_table_with_indexes():
    try:
        table = dynamodb.create_table(
            TableName='Projects',
            KeySchema=[
                {'AttributeName': 'ProjectName', 'KeyType': 'HASH'},
                {'AttributeName': 'TaskID', 'KeyType': 'RANGE'}
            ],
            AttributeDefinitions=[
                {'AttributeName': 'ProjectName', 'AttributeType': 'S'},
                {'AttributeName': 'TaskID', 'AttributeType': 'S'},
                {'AttributeName': 'Status', 'AttributeType': 'S'},  # For LSI
                {'AttributeName': 'EmployeeDepartment', 'AttributeType': 'S'}  # For GSI
            ],
            LocalSecondaryIndexes=[
                {
                    'IndexName': 'StatusLSI',
                    'KeySchema': [
                        {'AttributeName': 'ProjectName', 'KeyType': 'HASH'},
                        {'AttributeName': 'Status', 'KeyType': 'RANGE'}
                    ],
                    'Projection': {'ProjectionType': 'ALL'}
                }
            ],
            GlobalSecondaryIndexes=[
                {
                    'IndexName': 'EmployeeDeptGSI',
                    'KeySchema': [
                        {'AttributeName': 'EmployeeDepartment', 'KeyType': 'HASH'}
                    ],
                    'Projection': {'ProjectionType': 'ALL'},
                    'ProvisionedThroughput': {'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
                }
            ],
            ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
        )
        table.wait_until_exists()
        print(f"Table {table.table_name} created with LSI and GSI.")
    except ClientError as e:
        print(f"Error: {e.response['Error']['Message']}")

# Call the function to create the table
create_table_with_indexes()
