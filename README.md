#Current Pre-req:

1) Run this locally. Subsequent versions will be for Lambda.

2) IAM Steps.
2a) Create IAM user and configure local cli to use it
2b) Give IAM user the following permission:

                    {
                        "Version": "2012-10-17",
                        "Statement": [
                            {
                                "Effect": "Allow",
                                "Action": "sts:AssumeRole",
                                "Resource": "*"
                            }
                        ]
                    }
                    
2c) In the Secondary account where you want this script to execute, create a cross-account role and allow the Primary             Account number to access. Also, give it access to TA (I gave it admin rights for now).
    
