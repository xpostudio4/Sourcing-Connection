import datetime

from django.contrib.auth.models import User
from django.utils import unittest, timezone
from django.test import TestCase

from companies.models import Company
from contacts.models import Contact, Contact_Urls
from location.models import Country, City, Region

# ModelTests

class ContactModelTest(TestCase):
    def test_creating_new_contact_and_saving_it_to_the_database(self):
        # Test creating a new event object.
        user = User.objects.create(username="johndoe")
        country = Country.objects.create(name ='Nowhere')
        region = Region.objects.create(region_name="How cares", country=country)
        city = City.objects.create(city_name='WonderLand', country=country, region_name=region)
        contact = Contact()
        contact.user = user
        contact.fr_name = "John"
        contact.ls_name = "Doe"
        contact.m_name = ""
        contact.email = ""
        contact.overview = ""
        contact.photo_profile = ""
        contact.phone = ""
        contact.country = country
        contact.city = city
        contact.degrees = ""
        contact.lt_contact = ""
        contact.tags = ""
        contact.company = None
        contact.latech_contact = ""
        contact.financial_organization = ""
        contact.government_organization = ""
        contact.title = ""
        contact.industry = ""
        contact.technology = ""
        contact.application = ""
        # Testing __unicode__ method
        self.assertEquals(unicode(contact.fr_name +" "+contact.ls_name), 'John Doe')

class ContactUrlsModelTest(TestCase):
    def test_creating_new_contacturl_and_saving_it_to_the_database(self):
        user = User(username="johndoe")
        contact = Contact(user)
        contact_url = Contact_Urls()
        contact_url.latech_contact = contact
        contact_url.ld_url = 'http://www.linkedin.com/pub/jearel-alcantara/26/22/b11'
        contact_url.t_url = 'http://twitter.com/jeasoft'
        contact_url.blog_url = "http://jeasoft.wordpress.com"
        contact_url.ext_url = ""
    

