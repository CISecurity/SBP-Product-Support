# This work is being published by CIS and is covered by Creative Commons BY-NC-SA 4.0.
# See https://protect-us.mimecast.com/s/tcd3CkRjG9iYAXVWT25fvb?domain=creativecommons.org for full details.
#
# This code relies on the boto3 library: https://protect-us.mimecast.com/s/cRmxClYkJjUOmPJns9w6ZN?domain=boto3.readthedocs.io
# You may need to `pip install boto3` before this script will work.
import boto3
import re
import json

ec2client = boto3.client('ec2', region_name='us-east-1')
awsMarketplaceId = '679593333241'

# AC TEST - The Image ID used by the CIS Ubuntu 22.04 HIs
ubuntu2204HardenedImageID = '*80ec131e-1631-4b92-92cc-ef35c56c3ec8*'

# Replace benchmarkName and profileLevel values with what you're looking for
benchmarkName = 'CIS Microsoft Windows Server 2012 R2 Benchmark'
profileLevel = 'Level 1'
amiNamePattern = benchmarkName + '.*' + profileLevel + '*'


# Find AMIs of a specific name pattern
cis_amis = ec2client.describe_images(
    DryRun=False,
    Owners=[awsMarketplaceId],
    Filters=[
        {
            'Name': 'name',
            'Values': [ubuntu2204HardenedImageID]
        }
        ]
)
latest_version = -1
latest_ami = []
local_versions = []

# AC - DEBUG - print all results with readable JSON formatting
print(json.dumps(cis_amis, indent=4))

if cis_amis['Images']:
    # For each of the AMIs with names matching the above pattern, get all local versions
    for ami in iter(cis_amis['Images']):
        # Get the full version for the AMI, which includes the Benchmark version and the local AMI version
        full_version = re.findall("v\d.\d.\d.\d", ami['Name'])
        # Collect the local version number from the full version
        local_version_number = int(re.split(r'\.', full_version[0])[3])
        # Keep only the latest (largest) local version and associated AMI
        if (latest_version < 0) or (latest_version < local_version_number):
            latest_version = local_version_number
            latest_ami = ami
    # For demonstration, we're printing the image name and ID
    # A Real-world scenario would, at this point, create an instance using the discovered AMI ID
    print(latest_ami['Name'])
    print(latest_ami['ImageId'])
    
else:
    print("No images to display")
