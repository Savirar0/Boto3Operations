# AWS S3 File Operations with Boto3

A modular Python project demonstrating Amazon Web Services (AWS) S3 bucket and object lifecycle management using the `boto3.client('s3')` API.

This repository covers programmatic bucket creation, virtual folder management, object I/O operations (upload, in-memory read, download, delete), and full account cleanup scripts.

---

## Key Features & Capabilities

* **Pure Client Interface:** Built exclusively with `boto3.client('s3')` to ensure low-level API compatibility and predictable behavior.
* **Region-Aware Bucket Management:** Programmatic bucket creation with explicit region constraints (`ap-south-1`) and `head_bucket` existence checks.
* **Virtual Folder Handling:** Demonstrates both explicit (zero-byte folder objects) and implicit key prefix structures in S3.
* **In-Memory & Disk I/O:** Supports reading text content directly into memory via `get_object()` streams without writing to disk, as well as local file downloads.
* **Environment Reset Utility:** Includes an automated purge script (`s3_master_delete.py`) to clear objects and delete buckets for clean development resets.

---

## Project Structure

```text
BOTO3 file operations/
├── functions/
│   ├── __init__.py
│   ├── Bucket_Folder_Creation.py  # Create buckets & virtual folders
│   ├── get_all_buckets_info.py    # List all buckets in the AWS account
│   ├── get_bucket_contents.py     # List objects within a specific bucket/prefix
│   └── text_file_operations.py    # Upload, read, download, & delete objects
├── textFiles/
│   └── text1.txt                  # Sample local text file for testing
├── s3_demo_1.py                   # Main workflow demo script
├── s3_master_delete.py            # Account reset script (deletes all S3 resources)
└── README.md                      # Project documentation