import boto3

s3 = boto3.client('s3')

bucket_name = 'myawspracticechetan1'
file_name = r'C:\Users\cheta\Desktop\sql practice2.txt'  # raw string for Windows path

object_name = 'sql_practice2.txt'  # This is how it will be stored in S3

s3.upload_file(file_name, bucket_name, object_name)

print(f"Uploaded '{file_name}' to bucket '{bucket_name}' as '{object_name}'")
