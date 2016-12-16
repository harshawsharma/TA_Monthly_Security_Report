import boto3


def authenticate_support(x):
    supportclient = boto3.client('support',
                                 region_name='us-east-1',
                                 aws_access_key_id=x['AccessKeyId'],
                                 aws_secret_access_key=x['SecretAccessKey'],
                                 aws_session_token=x['SessionToken'],
                                 )
    return trusted_advisor_checks(supportclient)


def trusted_advisor_checks(y):
    response_checkids = y.describe_trusted_advisor_checks(
        language='en'
    )
    for listobjects in response_checkids['checks']:
        if listobjects['category'] == 'security':
            extracted_checkids = listobjects['id']
            # Only for the extracted checkids refresh the current status and print it
            response_refreshstatus = y.describe_trusted_advisor_check_refresh_statuses(
                checkIds=[
                    extracted_checkids
                ]
            )
            print response_refreshstatus

    return


