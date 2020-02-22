from botocore.exceptions import ClientError
import boto3
import botostubs
import logging

s3 = boto3.client('s3') #type: botostubs.S3
s3_list_buckets = s3.list_buckets()
default_encryption_json = (open("encryptionFile.txt")).read()

for bucket in s3_list_buckets['Buckets']:
    bucket_name = bucket['Name']
    try:
       s3.get_bucket_encryption(Bucket=bucket_name)['ServerSideEncryptionConfiguration']
       print(bucket_name," has",s3.get_bucket_encryption(Bucket=bucket_name)['ServerSideEncryptionConfiguration'])
    except ClientError as e:
        s3.put_bucket_encryption(ServerSideEncryptionConfiguration=default_encryption_json,Bucket=bucket_name)
        print("No Server side encryption exists for ",bucket_name)
        
    
