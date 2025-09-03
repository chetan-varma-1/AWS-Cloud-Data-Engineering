import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Your bucket name
bucket_name = 'myawspracticechetan1'

# The key (filename) of the file stored in S3
object_name = 'sql_practice2.txt'

# Local path where the file will be saved after download
download_path = r'C:\Users\cheta\Downloads\downloaded_sql_practice2.txt'  # Use raw string for Windows path

# Download file from S3 bucket
s3.download_file(bucket_name, object_name, download_path)

print(f"Downloaded '{object_name}' from bucket '{bucket_name}' to local path '{download_path}'")
