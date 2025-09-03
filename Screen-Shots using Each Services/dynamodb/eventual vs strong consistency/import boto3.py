import boto3


dynamodb = boto3.client("dynamodb", region_name="ap-south-1")
response = dynamodb.get_item(
    TableName="forum-application",
    Key={
        "postid": {"S": "102"},
        "commentid": {"S": "2"}
    },
    ConsistentRead=True
)

if 'Item' in response:
    print(response['Item'])
else:
    print("Item not found.")
