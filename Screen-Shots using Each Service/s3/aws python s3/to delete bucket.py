import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Your bucket name
bucket_name = 'myawspracticechetan1'

# Delete the bucket (make sure bucket is empty)
s3.delete_bucket(Bucket=bucket_name)

print(f"Deleted bucket '{bucket_name}'")
