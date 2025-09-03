import boto3
import json

# --- CONFIG ---
source_bucket = "manishpractice01"
replica_bucket = "manishhost01replica"
source_region = "ap-south-1"
replica_region = "ap-southeast-1"  # different region for replication
iam_role_arn = "arn:aws:iam::123456789012:role/MyS3ReplicationRole"  # replace with your IAM role

s3 = boto3.client("s3", region_name=source_region)

# 1. Create replica bucket (if not exists)
try:
    s3_replica = boto3.client("s3", region_name=replica_region)
    s3_replica.create_bucket(
        Bucket=replica_bucket,
        CreateBucketConfiguration={"LocationConstraint": replica_region}
    )
    print(f"Replica bucket '{replica_bucket}' created in {replica_region}.")
except s3.exceptions.BucketAlreadyOwnedByYou:
    print(f"Replica bucket '{replica_bucket}' already exists in your account.")

# 2. Apply lifecycle policy to source bucket
lifecycle_config = {
    "Rules": [
        {
            "ID": "MoveToIAAndExpire",
            "Status": "Enabled",
            "Filter": {"Prefix": ""},
            "Transitions": [{"Days": 30, "StorageClass": "STANDARD_IA"}],
            "Expiration": {"Days": 365}
        }
    ]
}
s3.put_bucket_lifecycle_configuration(
    Bucket=source_bucket,
    LifecycleConfiguration=lifecycle_config
)
print("Lifecycle policy applied to source bucket.")

# 3. Enable versioning (Required for replication)
s3.put_bucket_versioning(
    Bucket=source_bucket,
    VersioningConfiguration={"Status": "Enabled"}
)
s3_replica.put_bucket_versioning(
    Bucket=replica_bucket,
    VersioningConfiguration={"Status": "Enabled"}
)
print("Versioning enabled on both buckets.")

# 4. Add replication configuration
replication_config = {
    "Role": iam_role_arn,
    "Rules": [{
        "ID": "ReplicateAll",
        "Status": "Enabled",
        "Priority": 1,
        "DeleteMarkerReplication": {"Status": "Enabled"},
        "Filter": {},
        "Destination": {
            "Bucket": f"arn:aws:s3:::{replica_bucket}",
            "StorageClass": "STANDARD"
        }
    }]
}
s3.put_bucket_replication(
    Bucket=source_bucket,
    ReplicationConfiguration=replication_config
)
print(f"Replication from {source_bucket} → {replica_bucket} configured.")
