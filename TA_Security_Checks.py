import boto3

checks = ["nNauJisYIT", "c9D319e7sG", "Pfx0RwqBli", "vjafUGJ9H0", "N425c450f2",
          "N430c450f2", "a2sEc6ILx", "xSqX82fQu", "12Fnkpl8Y5", "DqdJqYeRm5",
          "Yw2K9puPzl", "zXCkfM1nI3", "7DAFEmoDos","HCP4007jGY", "1iG5NDGVre",]

supportcli = boto3.client('support')

refresh = supportcli.describe_trusted_advisor_check_refresh_statuses(
    checkIds = checks
)

for cids in checks:
	results = supportcli.describe_trusted_advisor_check_result(
		checkId = cids,
		language ='en'
        )
	print results