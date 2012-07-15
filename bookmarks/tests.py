"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client

class ViewTest(TestCase):
	fixtures = ['test_data.json']
	
	def setUp(self):
		self.client = Client()

	# def test_register_page(self):
	# 	data = {
	# 		'username': 'test_user',
	# 		'email': 'test@example.com',
	# 		'password': 'pass123',
	# 		'verify': 'pass123'
	# 		}
	# 	response = self.client.post('/register/', data)
	# 	self.assertEqual(response.status_code, 302)

	def test_bookmark_save(self):
		response = self.client.login('/save/', 'geaden', 'sFrancis')
		self.assertTrue(response)
		data = {
			'url': 'http://www.example.com/',
			'title': 'Test URL',
			'tags': 'test-tag'
		}
		response = self.client.post('/save/', data)
		self.assertEqual(response.status_code, 302)
		response = self.client.get('/user/geaden/')
		self.assertTrue('Test URL' in response.content)
		self.assertTrue('test-tag' in response.content)

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
