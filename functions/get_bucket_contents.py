import boto3
import logging
from botocore.exceptions import ClientError

def list_bucket_contents(bucket, prefix=''):
    s3 = boto3.client('s3')
    try:
        response = s3.list_objects_v2(Bucket=bucket, Prefix=prefix)
        
        if 'Contents' in response:
            print(f"Found {response['KeyCount']} object(s) in '{bucket}':")
            keys = []
            for item in response['Contents']:
                print(f" - {item['Key']} ({item['Size']} bytes)")
                keys.append(item['Key'])
            return keys
        else:
            print(f"Bucket '{bucket}' is empty or prefix '{prefix}' matches no files.")
            return []
            
    except ClientError as e:
        logging.error(e)
        return False