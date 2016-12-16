import boto3
import os

from trustedadvisor import authenticate_support

accountnumber = os.environ['Account_Number']
rolename = os.environ['Role_Name']
rolesession = accountnumber + rolename


def lambda_handler(event, context):
    sts_client = boto3.client('sts')
    assumerole = sts_client.assume_role(
        RoleArn="arn:aws:iam::" + accountnumber + ":role/" + rolename,
        RoleSessionName=rolesession
    )

    credentials = assumerole['Credentials']

    return authenticate_support(credentials)
