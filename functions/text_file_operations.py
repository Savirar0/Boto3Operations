import boto3
import os
from botocore.exceptions import ClientError
import logging

#uploading
def upload_file(file_name, bucket, object_name=None):
    if object_name is None:
        object_name=os.path.basename(file_name)

    s3=boto3.client('s3')
    try:
        response = s3.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

#reading
def read_file(file_name, bucket,object_name=None):
    if object_name is None:
        object_name=file_name

    s3=boto3.client('s3')
    try:
        response= s3.get_object(Bucket=bucket, Key=object_name)
        print(response)
        content = response['Body'].read().decode('utf-8')
        return content
    except ClientError as e:
        logging.error(e)
        return False

#downloading
def download_file(file_name, bucket,object_name=None):
    if object_name is None:
        object_name=file_name

    s3=boto3.client('s3')
    try:
        s3.download_file(bucket, object_name, file_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


#deleting
def delete_file(file_name, bucket, object_name=None):
    if object_name is None:
        object_name=file_name
    s3=boto3.client('s3')
    try:
        s3.delete_object(Bucket=bucket, Key=object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


