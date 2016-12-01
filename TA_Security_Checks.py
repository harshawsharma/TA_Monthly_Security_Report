import boto3

accountnumber= raw_input('Enter the Account Number: ')
rolename= raw_input('Enter Role Name to assume: ')
rolesession=accountnumber+rolename

# create an STS client object that represents a live connection to the STS service
sts_client = boto3.client('sts')

# Call the assume_role method of the STSConnection object and pass the role ARN and a role session name.
assumedRoleObject = sts_client.assume_role(
    RoleArn="arn:aws:iam::"+accountnumber+":role/"+rolename,
    RoleSessionName=rolesession
)

# From the response that contains the assumed role, get the temporary credentials that can be used to make subsequent API calls
credentials = assumedRoleObject['Credentials']

# Create Support Client, region name is mandatory. This client is available only in us-east.
# PASS the temp credentials of assumed role as arguments. From this point onwards these keys and thereby the
# corresponding account will be used

support = boto3.client('support',
                       region_name='us-east-1',
                       aws_access_key_id=credentials['AccessKeyId'],
                       aws_secret_access_key=credentials['SecretAccessKey'],
                       aws_session_token=credentials['SessionToken'],
                       )

# Obtain a list of all available checkids for Trusted Advisor.
response_checkids = support.describe_trusted_advisor_checks(
    language='en'
)

#Go through the dictionary list and extract the checkids only for the security category
for listobjects in response_checkids['checks']:
    if listobjects['category'] == 'security':
        extracted_checkids = listobjects['id']

    #Only for the extracted checkids refresh the current status and print it
        response_refreshstatus = support.describe_trusted_advisor_check_refresh_statuses(
            checkIds=[
                extracted_checkids
            ]
        )
        print response_refreshstatus
