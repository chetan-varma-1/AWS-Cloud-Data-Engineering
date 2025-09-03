import boto3
client=boto3.client('s3')
response=client.list_objects_v2(
    Bucket='myawspracticechetan1'
)
for obj in response.get('Contents',[]):
    print(obj['Key'])