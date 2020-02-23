import botostubs
import boto3
from botocore.exceptions import ClientError
import logging


ec2_client = boto3.client('ec2') #type: botostubs.EC2
response = ec2_client.describe_instances()['Reservations']
response_describe_regions = ec2_client.describe_regions()['Regions']
instances=[]
instance_ids=[]
regions= []
key_to_be_added={'Key': 'Accessibility', 'Value': 'Public'}

for i in range(len(response_describe_regions)):
    region = response_describe_regions[i]['RegionName']
    regions.append(region)

for region in regions:
    ec2 = boto3.client('ec2',region_name=region)#type: botostubs.EC2
    response = ec2.describe_instances()['Reservations']
    if response:
        for i in range(len(response)):
            instance = response[i]['Instances']
            instances.append(instance)
    for instance in instances:
        if(key_to_be_added not in instance[0]['Tags']):
            print(instance[0]['Tags'],instance[0]['InstanceId'])
            print("Adding tags.......")
            ec2.create_tags(Resources=[instance[0]['InstanceId']],Tags=[key_to_be_added])