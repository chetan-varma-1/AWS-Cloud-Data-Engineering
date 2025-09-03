import boto3
from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Projects')

# Batch insert 10 sample items
def batch_insert_items():
    with table.batch_writer() as batch:
        for i in range(10):
            batch.put_item(Item={
                'ProjectName': 'ProjectX',
                'TaskID': f'Task{i}',
                'Status': 'IN_PROGRESS' if i % 2 == 0 else 'COMPLETED',
                'EmployeeDepartment': 'DeptA' if i % 3 == 0 else 'DeptB'
            })
    print("Batch insert completed.")

# Get an item
def get_item(project_name, task_id):
    response = table.get_item(Key={'ProjectName': project_name, 'TaskID': task_id})
    return response.get('Item')

# Update item status
def update_item_status(project_name, task_id, new_status):
    response = table.update_item(
        Key={'ProjectName': project_name, 'TaskID': task_id},
        UpdateExpression='SET #s = :new_status',
        ExpressionAttributeNames={'#s': 'Status'},
        ExpressionAttributeValues={':new_status': new_status},
        ReturnValues='UPDATED_NEW'
    )
    print(f"Updated status for {task_id}: {response['Attributes']}")

# Delete item
def delete_item(project_name, task_id):
    table.delete_item(Key={'ProjectName': project_name, 'TaskID': task_id})
    print(f"Deleted {task_id}.")

# Scan with filter function
def find_tasks_by_status(status):
    response = table.scan(
        FilterExpression=Attr('Status').eq(status)
    )
    return response.get('Items')

# Example calls:
batch_insert_items()
print(get_item('ProjectX', 'Task0'))
update_item_status('ProjectX', 'Task0', 'COMPLETED')
delete_item('ProjectX', 'Task9')
print(find_tasks_by_status('IN_PROGRESS'))
