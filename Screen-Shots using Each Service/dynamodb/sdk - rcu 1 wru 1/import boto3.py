import boto3
# Initialize DynamoDB client with your preferred region
client = boto3.client('dynamodb', region_name='ap-south-1')  # Change region if needed

table_name = 'table-on-demand'





# Step 2: Write 10 items rapidly to the table
def write_items():
    for i in range(10):
        item = {
            'Id': {'S': str(i)},
            'Attribute': {'S': f'Value{i}'}
        }
        client.put_item(TableName=table_name, Item=item)
        print(f'Wrote item {i}')
        # Optional: slight delay to modulate speed
        # time.sleep(0.1)

if __name__ == '__main__':
    
    write_items()
