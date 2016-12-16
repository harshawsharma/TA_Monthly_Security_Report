#Current Pre-req:

1. Create Environment Variables Role_Name (name of the role to assume) and Account_Number (AWS Account Number to assume the role from)
2. IAM Steps:
  1. Give Lambda role the following permission:
  
      ```json
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
      ```
      
  3. In the Secondary account where you want this script to execute, create a cross-account role and allow the Primary Account number to access. Also, give it access to TA (I gave it admin rights for now).
