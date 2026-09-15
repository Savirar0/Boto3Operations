import boto3

s3 = boto3.client('s3', region_name='ap-south-1')
REGION = 'ap-south-1'

BUCKET_1 = 'demo-bucket-alpha-90541'
BUCKET_2 = 'demo-bucket-beta-90541'


def create_bucket(bucket_name):
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={'LocationConstraint': REGION}
    )
    print(f"[+] Bucket created: {bucket_name}")


def delete_bucket_with_contents(bucket_name):
    response = s3.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in response:
        objects_to_delete = [{'Key': obj['Key']} for obj in response['Contents']]
        s3.delete_objects(Bucket=bucket_name, Delete={'Objects': objects_to_delete})
        print(f"[-] Cleared all contents/folders from '{bucket_name}'.")
    
    s3.delete_bucket(Bucket=bucket_name)
    print(f"[-] Bucket deleted: {bucket_name}")


# 1. Create S3 bucket & create a folder inside it
create_bucket(BUCKET_1)
s3.put_object(Bucket=BUCKET_1, Key='my_empty_folder/')
print(f"[+] Created folder 'my_empty_folder/' in '{BUCKET_1}'")

# 2. Delete empty folder from S3 bucket
s3.delete_object(Bucket=BUCKET_1, Key='my_empty_folder/')
print(f"[-] Deleted empty folder 'my_empty_folder/' from '{BUCKET_1}'")

# 3. Delete empty S3 bucket
s3.delete_bucket(Bucket=BUCKET_1)
print(f"[-] Empty bucket deleted: {BUCKET_1}\n")

# 4. Create a new bucket & add a folder structure to it
create_bucket(BUCKET_2)
s3.put_object(Bucket=BUCKET_2, Key='documents/archive/')
print(f"[+] Created folder 'documents/archive/' in '{BUCKET_2}'")

# 5. Delete S3 bucket containing folders (clears contents first, then deletes bucket)
delete_bucket_with_contents(BUCKET_2)