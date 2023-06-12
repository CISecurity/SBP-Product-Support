Find the Latest CIS AMIs using a Python Script

CIS has created a proof-of-concept Python script that uses the AWS API to discover the latest CIS AMI offered in the AWS Marketplace for a named benchmark. 
We encourage anyone using CIS AMIs in the AWS marketplace to use either this script, or something like it, so that you can be assured that you're always using the latest released AMI for that particular benchmark line.

This script has been tested and run via AWS CLI. Please remember to set up your unique AWS configuration prior to running this script via command prompt. Information regarding how to do this can be found here: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html.

The code relies on the boto3 library and this can be installed via $ python -m pip install boto3.
For more information on how to install boto3 please review the following documentations: https://pypi.org/project/boto3/ ; https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html
