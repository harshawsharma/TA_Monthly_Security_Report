import boto3


def authenticate_support(creds):
    supportclient = boto3.client('support',
                                 region_name='us-east-1',
                                 aws_access_key_id=creds['AccessKeyId'],
                                 aws_secret_access_key=creds['SecretAccessKey'],
                                 aws_session_token=creds['SessionToken'],
                                 )
    return trusted_advisor_checks(supportclient)


def trusted_advisor_checks(support):
    response_checkids = support.describe_trusted_advisor_checks(
        language='en'
    )
    for listobjects in response_checkids['checks']:
        if listobjects['category'] == 'security':
            extracted_checkids = listobjects['id']
            # Only for the extracted checkids refresh the current status and print it
            response_refreshstatus = support.describe_trusted_advisor_check_refresh_statuses(
                checkIds=[
                    extracted_checkids
                ]
            )
            print response_refreshstatus

    return


