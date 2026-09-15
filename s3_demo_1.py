import os
from functions.get_all_buckets_info import bucketsInfo
from functions.Bucket_Folder_Creation import create_bucket, create_folder
from functions.text_file_operations import upload_file, read_file, download_file, delete_file

bucket_name = 'first-bucket-demo-90541'
create_bucket(bucket_name)

folder_name = 'f1'
create_folder(bucket_name, folder_name)

print(f"Created bucket '{bucket_name}' with folder '{folder_name}'. Verifying...\n")
bucketsInfo()
local_file = 'textFiles/text1.txt'
file_name = os.path.basename(local_file)            
s3_object_key = f"{folder_name}/{file_name}"    

print("\nUploading file to S3...")
upload_file(local_file, bucket_name, object_name=s3_object_key)

print("\nReading file from S3:")
content = read_file(local_file, bucket_name, object_name=s3_object_key)
print(content)

print("\nDownloading file locally:")
download_file('downloads/text1.txt', bucket_name, object_name=s3_object_key)

print("\nDeleting file from S3:")
delete_file(local_file, bucket_name, object_name=s3_object_key)