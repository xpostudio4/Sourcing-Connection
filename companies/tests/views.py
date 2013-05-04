from django.test import Client, TestCase
from companies.models import Company

class CompanyCreateTest(TestCase):
	pass

class CompanyViewTest(TestCase):
	def test_company_existence(self):
		company =  Company.objects.create(name="PruebaTest", slug="pruebatest")

		client = Client()
		response = client.get('/companies/%s' % company.slug)

		self.assertIn(company.name, response.content)