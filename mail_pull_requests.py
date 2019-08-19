import os
from github import Github
from mail_requests import utils


def main():
	if 'config.json' not in os.listdir(os.getcwd()+'/mail_requests'):
		github_access_token = input('Please enter a valid GitHub access token:\n')
		utils.save_config(github_access_token)

	github_access_token = utils.get_access_token()
	number_of_pull_requests = utils.get_number_of_pull_requests(github_access_token)
	utils.send_email(number_of_pull_requests)


if __name__ == '__main__':
	main()
