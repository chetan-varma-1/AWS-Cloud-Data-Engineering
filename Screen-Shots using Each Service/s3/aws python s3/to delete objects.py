import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Your bucket name
bucket_name = 'myawspracticechetan1'

# The object (file) to delete from the bucket
object_name = 'sql_practice2.txt'

# Delete the object from the bucket
s3.delete_object(Bucket=bucket_name, Key=object_name)

print(f"Deleted '{object_name}' from bucket '{bucket_name}'")
