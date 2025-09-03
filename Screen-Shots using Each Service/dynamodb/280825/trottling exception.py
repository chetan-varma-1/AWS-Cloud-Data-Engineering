import boto3
from botocore.exceptions import ClientError
from botocore.config import Config

my_config = Config(
    retries={
        'max_attempts': 1,  # disables retries
        'mode': 'standard'
    }
)

dynamodb = boto3.resource('dynamodb', config=my_config)
table = dynamodb.Table('ProvisionedTable')

#to create table
def create_provisioned_table():
    try:
        table = dynamodb.create_table(
            TableName='ProvisionedTable',
            KeySchema=[{'AttributeName': 'PK', 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'PK', 'AttributeType': 'S'}],
            ProvisionedThroughput={
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }
        )
        table.meta.client.get_waiter('table_exists').wait(TableName='ProvisionedTable')
        print("Table created and active.")
    except ClientError as e:
        print(f"Failed to create table: {e.response['Error']['Message']}")

def put_sample_items():
    table = dynamodb.Table('ProvisionedTable')
    try:
        for i in range(100):  # fewer writes for simplicity
            table.put_item(Item={'PK': f'Item{i}', 'Data': 'sample'})
        print("Items inserted successfully.")
    except ClientError as e:
        print(f"Failed to write items: {e.response['Error']['Message']}")

if __name__ == '__main__':
    create_provisioned_table()
    put_sample_items()
