import boto3

# Create S3 client
s3 = boto3.client('s3')

# Your S3 bucket
bucket_name = "myawspracticechetan1"

# Files to upload
files = [
    r"C:\Users\cheta\Desktop\sql practice2.txt",
    r"C:\Users\cheta\Desktop\DT20256479023_Application.pdf"
]

# Upload each file
for file_path in files:
    file_name = file_path.split("\\")[-1]  # Extract just the filename
    s3.upload_file(file_path, bucket_name, file_name)
    print(f"Uploaded {file_path} to s3://{bucket_name}/{file_name}")

print("All files uploaded successfully.")
