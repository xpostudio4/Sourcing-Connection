import os
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.template import defaultfilters
from taxonomy.models import *
from location.models import *
from django.core.files.storage import FileSystemStorage
from storagess.backends.gs import GSBotoStorage


# Detecting Heroku Deployment
if os.getenv('HEROKU_ENV') == 'True':
    gs = GSBotoStorage()
else:
    gs = FileSystemStorage()

class Company(models.Model):
    EMPLOYEE_QUANTITY_CHOICES = (
        (1, "1 - 10"),
        (2, "11 - 50"),
        (3, "51 - 150"),
        (4, "151 - 500"),
        (5, "501 - 1000"),
        (6, "1001 - 5000"),
        (7, "+ 5001"),
    )

    COMPANY_STATUS_CHOICES = (
        ("", "-----"),
        (1, "GTB-0"),
        (2, "GTB-1"),
        (3, "GTB-2"),
        (4, "GTB-3"),
        (5, "GTB-4"),
    )


    name = models.CharField(max_length=80, unique= True)
    slug = models.SlugField(max_length=80, unique= True)
#    logo = models.ImageField(blank=True, null=True, upload_to="images/company_imgs/")
    logo = models.ImageField(blank=True, null=True, storage=gs, upload_to="images/companies_imgs/")
    description = models.TextField(blank=True)
    value_proposition = models.CharField(max_length=144, blank=True)
    overview = models.CharField(max_length=512, blank=True)
    company_status = models.IntegerField(choices=COMPANY_STATUS_CHOICES, blank=True, null=True)
    employee_quantity = models.IntegerField(choices=EMPLOYEE_QUANTITY_CHOICES, blank=True, null=True)
#    created_by = models.ForeignKey(User, related_name="LATech user")
    web_url = models.URLField(blank=True)
    blog_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True)
    main_phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    #Comma separated list from Industry table
    industries = models.CharField(max_length=512, blank=True)
#    industries = TaggableManager(verbose_name='Industries', through=IndustryTaggedItem, blank=True)
    #Comma separated list from Technologies table
    technologies = models.CharField(max_length=512, blank=True)
#    technologies = TaggableManager(verbose_name='Technologies', through=TechnologyTaggedItem, blank=True)

    #Comma separated list from Category table
    categories = models.ForeignKey(Category, related_name="Categories", null=True, blank=True)

    #Comma separated list from Application table
    applications = models.CharField(max_length=512, blank=True)
   
    #Comma separated list from Tags table, also accept new tags input by users ("folksonomy")
    tags = models.CharField(max_length=512, blank=True)
#    tags = TaggableManager(blank=True)
    
    #Comma separated list of entries from Company table
    #competitors = models.Foreignkey("")

    #Company Country
    country = models.ForeignKey(Country, related_name="Company Country", null=True, blank=True)
            
    #Comma separated list of <City, address, phone #>
    offices = models.CharField(max_length=512, blank=True)

    #Input into Contacts table, point back to Company
    # Need to be modified in the future
    # others_people = models.ForeignKey("Contact")
    
    #Comma separated list of entries from Company table
    acquisition = models.CharField(max_length=512, blank=True)

    #Comma separated list of products/services
    product = models.CharField(max_length=512, blank=True)
    #prod_ser_img = models.ManyToManyField("")

    #Comma separated list of certifications from Certification Table
    #certification = models.ForeignKey("Certification")
    certification = models.CharField(max_length=512, blank=True)

    award = models.CharField(max_length=512, blank=True)
    
    #Comma separated list of Customers form Company Table
    customer = models.CharField(max_length=512, blank=True)

    #Comma separated list of entries from project table
#    project = models.ManyToManyField("Project")
#    links = models.ForeignKey("URLs")

    #<Person, Phone, email>
    contact = models.CharField(max_length=512, blank=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.name)
        super(Company, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
          return ("/company/%s/" % self.slug)
 
    class Meta:
         verbose_name_plural = "Companies"
         ordering = ['id']

class CompanyRating(models.Model):
    # Visible for LATech members
    company = models.ForeignKey(Company, related_name="Ratings for Companies")
    scalability_rating = models.IntegerField(blank=True, null=True)
    expansion_rating = models.IntegerField(blank=True, null=True)
    physical_plant_rating = models.IntegerField(blank=True, null=True)
    profilatibily_rating = models.IntegerField(blank=True, null=True)
    ret_talent_rating = models.IntegerField(blank=True, null=True)
    financials_rating = models.IntegerField(blank=True, null=True)
    rating_of_ownership = models.IntegerField(blank=True, null=True)
    gtb_overall_rating = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return str(self.company) + " Ratings"

ROUND_CHOICES = (
    ('Seed','Seed'), ('Angel','Angel'), 
    ('Series A','Series A'),('Series B','Series B'),
    ('Series C','Series C'), ('Series D','Series D'),
    ('Series E','Series E'), ('Series F','Series F'), 
    ('Series G','Series G'), ('Private Equity','Private Equity'), 
    ('Grant','Grant'),('Debt','Debt'), 
    ('Venture Round','Venture Round'),('Post IPO Equity','Post IPO Equity'), 
    ('Post IPO Debt','Post IPO Debt') 
    )

class Management(models.Model):
    company = models.ForeignKey(Company, related_name="Management of the company")
    full_name = models.CharField(max_length=56)
    title = models.CharField(max_length=56)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return str(self.company) + " : " + self.full_name

class Funding(models.Model):
    company = models.ForeignKey(Company, related_name="Funds Delivered to", blank=True)
    round = models.CharField(max_length=16, choices=ROUND_CHOICES, default = 'Seed')
    raised = models.CharField(max_length=45)

    def __unicode__(self):
        return str(self.company) +" : " + self.round

#Comented for future uses
#class Round(models.Model):
#   round = models.CharField(max_length=50)


class Competitors(models.Model):
    company = models.ForeignKey(Company, related_name="Source Company", blank=True)
    name = models.ForeignKey(Company, related_name="Competitor")

    def __unicode__(self):
        return str(self.company) +":" + str(self.name)

    class Meta:
         verbose_name_plural = "Competitors"


class Office(models.Model):
    company = models.ForeignKey(Company, blank=True)
    description = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=512, blank=True)
    address_2 = models.CharField(max_length=512, blank=True)
    city = models.ForeignKey(City, related_name="location", blank=True, null=True)
    phone = models.CharField(max_length=512, blank=True)
    zip_code = models.CharField(max_length=512, blank=True)
    country = models.ForeignKey(Country, related_name = "Office Country", null=True,  blank=True)
 
    
    def __unicode__(self):
        return str(self.company)+ ": Address No."+ str(self.id)+" :"+ self.description

class AccessCompanyProfile(models.Model):
    contact = models.ForeignKey(User, related_name = "Contact User")
    company = models.ManyToManyField(Company, related_name = "Companies ")

    def __unicode__(self):
        return str(self.contact) + ":" + str(self.company.all()[0])
        
class ContactCompany(models.Model):
    company = models.ForeignKey(Company, related_name = "Contact Company")
    first_name = models.CharField(max_length=255, blank=True, verbose_name="First Name")
    last_name = models.CharField(max_length=255, blank=True, verbose_name="Last Name")
    contact = models.ForeignKey('contacts.Contact', blank=True, null=True, related_name = "Contact's Profile")

    def __unicode__(self):
        return str(self.first_name +" "+ self.last_name)

    class Meta:
         verbose_name_plural = "Contact Company"

class ProfileCompletion(models.Model):
    """The purpose of this class is to calculate the percentage of completion of the profile of companies."""
    
    company = models.ForeignKey(Company, related_name='Company Profile Completion ')
    completion = models.DecimalField(max_digits=3, decimal_places=2)

    def __unicode__(self):
        return str(self.company)+ ":" + str(int(self.completion*100))+ "%"
