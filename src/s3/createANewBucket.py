"""
Sample script to create S3 buckets in a region
Default region is supposed to be us-east-1.
pre-reqs : aws cli is installed and configured.

"""
import boto3
import botostubs
from botocore.exceptions import ClientError
import logging

s3 = boto3.client('s3') # type: botostubs.S3
bucketName = ''
region = 'us-east-2'



try:
    s3.head_bucket(Bucket=bucketName)
    print("Exiting as the bucket already exists")
except:
    print("Creating a new bucket since it doesn't exist....")
    try:
        if region is None:
            s3 = boto3.client('s3')#type: botostubs.S3
            s3.create_bucket(Bucket=bucketName)
            print("Bucket created: "+ bucketName)
        else:
            s3 = boto3.client('s3',region_name=region)
            location = {'LocationConstraint':region}
            s3.create_bucket(Bucket=bucketName,CreateBucketConfiguration=location)
            print("Bucket created: "+ bucketName)
    except ClientError as e:
        logging.error(e)

    
