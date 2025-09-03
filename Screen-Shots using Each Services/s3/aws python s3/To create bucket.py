import boto3

s3 = boto3.client('s3')

bucket_name = 'myawspracticechetan1'  # Put your unique bucket name here as a string

response = s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'}
)
print("Bucket created:", response)


