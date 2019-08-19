import json
import smtplib, ssl
from github import Github


def save_config(github_access_token):
	with open('mail_requests/config.json', 'w+') as config_file:
		access_token_json = '{' + f'"githubAccessToken": "{github_access_token}"' + '}'
		config_file.write(access_token_json)


def get_access_token():
	with open('mail_requests/config.json', 'r') as github_access_token_file:
		data = json.load(github_access_token_file)
		return data['githubAccessToken']


def get_number_of_pull_requests(github_access_token):
	g = Github(github_access_token)
	repo = g.get_repo('Axway/axway-open-docs')
	pull_requests = repo.get_pulls(state='open', base='master')
	return pull_requests.totalCount


def send_email(number_of_pull_reqeusts):
	port = 465
	password = input('Please enter your password:\n')
	context = ssl.create_default_context()

	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
		server.login("pullrequestsemailer@gmail.com", password)
		sender_email = 'pullrequestsemailer@gmail.com'
		receiver_email = "uzaira960@gmail.com"
		message = f"{number_of_pull_reqeusts}"
		server.sendmail(sender_email, receiver_email, message)
