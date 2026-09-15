#This code deletes all the buckets
import boto3
s3 = boto3.client('s3')
for bucket in s3.list_buckets().get('Buckets', []):
    name = bucket['Name']
    objects = s3.list_objects_v2(Bucket=name).get('Contents', [])
    
    if objects:
        s3.delete_objects(
            Bucket=name,
            Delete={'Objects': [{'Key': obj['Key']} for obj in objects]}
        )
    
    s3.delete_bucket(Bucket=name)
    print(f"Deleted: {name}")