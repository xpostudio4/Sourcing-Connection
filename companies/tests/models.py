import datetime

from django.utils import unittest, timezone
from django.test import TestCase

from companies.models import Company, CompanyLink, CompanyRating, Management, Funding, Acquisition, Competitors
from companies.models import Certification, Customer, Office, ContactCompany, ProfileCompletion, Award
from location.models import Country
from taxonomy.models import Category

# ModelTests

class CompanyModelTest(TestCase):
    def test_creating_new_company_and_saving_it_to_the_database(self):
        # Test creating a new event object.
        category = Category.objects.create(name="Software", slug="software")
        #user = User.objects.create(username="fulano")
        country = Country.objects.create(name="America")
        company = Company()
        company.name ="Stance Data"
        company.slug = "stance-data"
        company.logo = "" #ImageField(blank=True, null=True, storage=gs, upload_to="images/companies_imgs/")
        company.overview = ""
        company.value_proposition = ""
        company.description = ""
        company.company_status = 2 #= IntegerField(choices=COMPANY_STATUS_CHOICES, blank=True, null=True)
        company.employee_quantity = 2 #IntegerField(choices=EMPLOYEE_QUANTITY_CHOICES, blank=True, null=True)
        company.main_phone = ""
        company.email = "info@stancedata.com"
        company.industries = ""
        company.technologies = ""
        company.categories = category #ForeignKey(Category, related_name="Categories", null=True, blank=True)
        company.applications =""
        company.tags = ""
        company.country = country
        company.product = ""
        company.contact = ""
        # Testing __unicode__ method
        self.assertEquals(unicode(company.name), 'Stance Data')

class CompanyLinkModelTest(TestCase):
    def test_creating_new_companylink_and_saving_it_to_the_database(self):
        companylink = CompanyLink()
        company = Company.objects.create(name="Americana", slug="americana")

        companylink.web_url = "tu abuela"
        companylink.linkedin_url = ""
        companylink.blog_url = ""
        companylink.twitter_url = ""
        companylink.facebook_link = ""
        #company_companylink = companylink.company_set.all()

class CompanyRatingModelTest(TestCase):
    def test_creating_new_companyrating_and_saving_it_to_the_database(self):
        company_rating = CompanyRating()
        company = Company.objects.create(name="Americana", slug="americana")
        company_rating.company = company
        company_rating. scalability_rating = 2
        company_rating.expansion_rating = 1
        company_rating.physical_plant_rating = 9
        company_rating.profilatibily_rating = 5
        company_rating.ret_talent_rating = 3
        company_rating.financials_rating = 3
        company_rating.rating_of_ownership = 2
        company_rating.gtb_overall_rating = 2

class ManagementModelTest(TestCase):
    def test_creating_new_management_and_saving_it_to_the_database(self):
        company = Company.objects.create(name="Americana", slug="americana")
        management = Management()
        management.company = company
        management.full_name = "Jearel Alcantara"
        management.title = "Ing"
        management.start_date = datetime.date.today
        management.end_date = datetime.date.today

class FundingModelTest(TestCase):
    def test_creating_new_funding_and_saving_it_to_the_database(self):
        company = Company.objects.create(name="Americana", slug="americana")
        funding = Funding()
        funding.company = company
        funding.round = "Series A" 
        raised = "1,100,100"

class AcquisitionModelTest(TestCase):
    def test_creating_new_companyrating_and_saving_it_to_the_database(self):
        company = Company.objects.create(name="Americana", slug="americana")
        acquisition = Acquisition()
        acquisition.company = company
        acquisition.name = "Google"
        acquisition.price = ""
        acquisition.acquired_date = datetime.date.today()
        acquisition.terms = ""

class CompetitorsModelTest(TestCase):
    def test_creating_new_companyrating_and_saving_it_to_the_database(self):
        company = Company.objects.create(name="Americana", slug="americana")
        competitors = Competitors()
        competitors.company = company
        competitors.name = "Microsoft"

class CertificationModelTest(TestCase):
    def test_creating_new_certification_and_saving_it_to_the_database(self):
        company = Company.objects.create(name="Americana", slug="americana")
        certification = Certification()
        certification.company = company
        certification.name = "Company of the Year"

class CustomerModelTest(TestCase):
    def test_creating_new_companyrating_and_saving_it_to_the_database(self):
        company = Company.objects.create(name="Americana", slug="americana")
        customer = Customer()
        customer.company = company
        customer.name = "John Doe"

class AwardModelTest(TestCase):
    def test_creating_new_companyrating_and_saving_it_to_the_database(self):
        company = Company.objects.create(name="Americana", slug="americana")
        award = Award()
        award.company = company
        award.name = "Company of the Year"
        award.date = datetime.date.today()

# ViewsTest

#class CompanyViewTest(TestCase):