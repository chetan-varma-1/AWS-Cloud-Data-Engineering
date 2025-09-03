import time
import boto3
from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Projects')

def time_scan(attribute, value):
    start = time.time()
    response = table.scan(FilterExpression=Attr(attribute).eq(value))
    end = time.time()
    print(f"Scan took {end - start:.4f}s, found {response['Count']} items.")
def time_query(index_name, attribute, value):
    start = time.time()
    response = table.query(
        IndexName=index_name,
        KeyConditionExpression=Key(attribute).eq(value)
    )
    end = time.time()
    print(f"Query took {end - start:.4f}s, found {response['Count']} items.")


# Usage example:
time_scan('EmployeeDepartment', 'DeptA')
time_query('EmployeeDeptGSI', 'EmployeeDepartment', 'DeptA')
