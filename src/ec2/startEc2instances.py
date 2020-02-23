import botostubs
import boto3
from botocore.exceptions import ClientError
import logging

"""
Get the list of instance ids in a region
"""

ec2_client = boto3.client('ec2') #type: botostubs.EC2
response = ec2_client.describe_instances()['Reservations']
response_describe_regions = ec2_client.describe_regions()['Regions']
instances=[]
instance_ids=[]
regions= []


def start_ec2_instances_all_regions():
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
                instance_ids.append(instance[0]['InstanceId'])
                if(instance[0]['State']['Name']=='stopped'):
                    print("Stoppped instance : ",instance[0]['InstanceId'], "Starting this ..")
                    ec2.start_instances(InstanceIds=[instance[0]['InstanceId']])
                else:
                    print("Active instances: ",instance[0]['InstanceId'])


start_ec2_instances_all_regions()
