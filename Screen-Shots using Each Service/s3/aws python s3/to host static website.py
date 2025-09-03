import boto3
import json

# --- CONFIG ---
bucket_name = "manishpractice01"  # must be globally unique
region = "ap-south-1"

# Create S3 client
s3 = boto3.client("s3", region_name=region)

# 1. Create bucket
s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={"LocationConstraint": region}
)
print(f"Bucket '{bucket_name}' created in {region}.")

# 2. Disable Block Public Access
s3.put_public_access_block(
    Bucket=bucket_name,
    PublicAccessBlockConfiguration={
        'BlockPublicAcls': False,
        'IgnorePublicAcls': False,
        'BlockPublicPolicy': False,
        'RestrictPublicBuckets': False
    }
)
print("Public access block disabled.")

# 3. Enable static website hosting
s3.put_bucket_website(
    Bucket=bucket_name,
    WebsiteConfiguration={
        "IndexDocument": {"Suffix": "index.html"},
        "ErrorDocument": {"Key": "error.html"}
    }
)
print("Static website hosting enabled.")

# 4. Upload website files
html_index = "<html><body><h1>Welcome to Manish's S3 Website!</h1></body></html>"
html_error = "<html><body><h1>404 - Page not found</h1></body></html>"

s3.put_object(Bucket=bucket_name, Key="index.html", Body=html_index, ContentType="text/html")
s3.put_object(Bucket=bucket_name, Key="error.html", Body=html_error, ContentType="text/html")
print("index.html and error.html uploaded.")

# 5. Apply public read policy
bucket_policy = {
    "Version": "2012-10-17",
    "Statement": [{
        "Sid": "PublicReadGetObject",
        "Effect": "Allow",
        "Principal": "*",
        "Action": "s3:GetObject",
        "Resource": f"arn:aws:s3:::{bucket_name}/*"
    }]
}

s3.put_bucket_policy(
    Bucket=bucket_name,
    Policy=json.dumps(bucket_policy)
)
print("Public read policy applied.")

# 6. Print website URL
print(f"Website URL: http://{bucket_name}.s3-website.{region}.amazonaws.com")
