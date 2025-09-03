import boto3
from botocore.exceptions import ClientError

# Initialize clients
autoscaling = boto3.client('application-autoscaling')
dynamodb = boto3.resource('dynamodb')

TABLE_NAME = 'ProvisionedTable'
RESOURCE_ID = f'table/{TABLE_NAME}'

def update_auto_scaling(min_capacity=2, max_capacity=10, target_utilization=75.0):
    try:
        # Update scalable target with new min and max capacity
        autoscaling.register_scalable_target(
            ServiceNamespace='dynamodb',
            ResourceId=RESOURCE_ID,
            ScalableDimension='dynamodb:table:WriteCapacityUnits',
            MinCapacity=min_capacity,
            MaxCapacity=max_capacity
        )
        print(f"Updated scalable target: min={min_capacity}, max={max_capacity}")

        # Update scaling policy with new target utilization
        autoscaling.put_scaling_policy(
            PolicyName=f'{TABLE_NAME}-write-auto-scaling-policy',
            ServiceNamespace='dynamodb',
            ResourceId=RESOURCE_ID,
            ScalableDimension='dynamodb:table:WriteCapacityUnits',
            PolicyType='TargetTrackingScaling',
            TargetTrackingScalingPolicyConfiguration={
                'TargetValue': target_utilization,
                'PredefinedMetricSpecification': {
                    'PredefinedMetricType': 'DynamoDBWriteCapacityUtilization'
                },
                'ScaleInCooldown': 60,
                'ScaleOutCooldown': 60
            }
        )
        print(f"Updated scaling policy: target utilization = {target_utilization}%")
    except ClientError as e:
        print(f"Error updating auto scaling: {e.response['Error']['Message']}")

def put_100_items():
    table = dynamodb.Table(TABLE_NAME)
    try:
        for i in range(100):
            table.put_item(Item={'PK': f'Item{i}', 'Data': 'sample'})
            
        print("100 items inserted successfully.")
    except ClientError as e:
        print(f"Failed to write items: {e.response['Error']['Message']}")

if __name__ == '__main__':
    update_auto_scaling()
    put_100_items()
