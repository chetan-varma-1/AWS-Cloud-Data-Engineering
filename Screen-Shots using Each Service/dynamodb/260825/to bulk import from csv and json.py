import csv
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('mytable')

# Bulk insert from CSV
with open('ToInsertCSV.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    with table.batch_writer() as batch:
        for row in reader:
            # Convert string numbers to integers where necessary
            row['login_count'] = int(row['login_count'])
            batch.put_item(Item=row)

# Bulk insert from JSON
with open('ToInsertJSON.json', 'r') as jsonfile:
    items = json.load(jsonfile)
    with table.batch_writer() as batch:
        for item in items:
            batch.put_item(Item=item)
