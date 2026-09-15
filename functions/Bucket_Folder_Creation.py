import boto3
import logging
from botocore.exceptions import ClientError

def create_bucket(bucket_name, region='ap-south-1'):
    s3 = boto3.client('s3', region_name=region)
    try:
        s3.head_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' already exists.")
        return True
    except ClientError as e:
        error_code = int(e.response['ResponseMetadata']['HTTPStatusCode'])
        if error_code == 404:
            s3.create_bucket(
                Bucket=bucket_name, 
                CreateBucketConfiguration={'LocationConstraint': region}
            )
            print(f"Bucket '{bucket_name}' created successfully in {region}.")
            return True
        elif error_code == 403:
            print(f"Error: Bucket name '{bucket_name}' is taken by another AWS user.")
            return False
        else:
            print(f"Unexpected error: {e}")
            return False

def create_folder(bucket_name, folder_name):
    s3 = boto3.client('s3')
    formatted_folder = f"{folder_name.rstrip('/')}/"
    
    try:
        s3.head_bucket(Bucket=bucket_name)
        s3.put_object(Bucket=bucket_name, Key=formatted_folder)
        print(f"Folder '{formatted_folder}' created in bucket '{bucket_name}'.")
        return True
    except ClientError as e:
        error_code = int(e.response['ResponseMetadata']['HTTPStatusCode'])
        if error_code == 404:
            print(f"Error: Specified bucket '{bucket_name}' does not exist.")
        else:
            print(f"Unexpected error: {e}")
        return False