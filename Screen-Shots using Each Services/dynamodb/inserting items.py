import boto3
client = boto3.client('dynamodb')
item = client.put_item(
    TableName='customer',
    Item={
        "id": {'S': '101'},
        "fname": {'S':"vijay"},
        "lname": {'S': "varma"},
        "age": {'N': '42'},
        "occupation": {'S': "trainee"},
        "email": {'S': "bob@gmail.com"}
    }
)
print("sucessfully inserted")