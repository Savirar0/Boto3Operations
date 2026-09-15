import boto3
from functions.get_bucket_contents import list_bucket_contents

def bucketsInfo():
    s3 = boto3.resource('s3')
    i=1
    for bucket in s3.buckets.all():
        print(f"Bucket {i}: {bucket.name}\n")
        list_bucket_contents(bucket.name)
        
