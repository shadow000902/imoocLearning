# -*- coding: utf-8 -*-
import requests

BASE_URL = 'https://api.github.com'

def construct_url(end_point):
	return '/'.join([BASE_URL, end_point])

def basic_auth():
	response = requests.get(construct_url('user'), auth=('username', 'password'))
	print response.text
	print response.request.headers

def basic_oauth():
	headers = {'Authorization': 'token 964b5bb2d22c54018bcd45956286f029503f378f'}
	response = requests.get(construct_url('user/emails'), headers=headers)
	print response.request.headers
	print response.text
	print response.status_code

from requests.auth import AuthBase

class GithubAuth(AuthBase):

	def __init__(self, token):
		self.token = token

	def __call__(self, r):
		r.headers['Authorization'] = ' '.join(['token', self.token])
		return r

def oauth_advanced():
	auth = GithubAuth('964b5bb2d22c54018bcd45956286f029503f378f')
	response = requests.get(construct_url('user/emails'), auth=auth)
	print response.text

oauth_advanced()