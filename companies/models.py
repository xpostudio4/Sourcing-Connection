from django.db import models
from django.contrib.auth.models import User
from taxonomy.models import *
from location.models import *
from django.forms import ModelForm
from django.template import defaultfilters
from taggit.managers import TaggableManager
# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=80, unique= True)
    slug = models.SlugField(max_length=80, unique= True)
 #       help_text='Unique value for Company page URL, created from name.')
    #logo = models.ImageField()
    description = models.TextField(blank=True)
    value_proposition = models.CharField(max_length=144, blank=True)
    overview = models.CharField(max_length=512, blank=True)
#    created_by = models.ForeignKey(User, related_name="LATech user")
    #Input into Contacts table, point back to Company
    management = models.CharField(max_length=144, blank=True)
    web_url = models.URLField(blank=True)
    blog_url = models.URLField(blank=True)
    twitter_username = models.CharField(max_length=512, blank=True)
    main_phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    #Comma separated list from Industry table
    industries = models.CharField(max_length=512, blank=True)
#    industries = TaggableManager(verbose_name='Industries', through=IndustryTaggedItem, blank=True)
    #Comma separated list from Technologies table
    technologies = models.CharField(max_length=512, blank=True)
#    technologies = TaggableManager(verbose_name='Technologies', through=TechnologyTaggedItem, blank=True)

    #Comma separated list from Category table
    categories = models.CharField(max_length=512, blank=True)

    #Comma separated list from Application table
    applications = models.CharField(max_length=512, blank=True)
   
    #Comma separated list from Tags table, also accept new tags input by users ("folksonomy")
    tags = models.CharField(max_length=512, blank=True)
#    tags = TaggableManager(blank=True)

    #Comma separated list of entries from Company table
    #competitors = models.Foreignkey("")
    competitors = models.CharField(max_length=512, blank=True)

    #Comma separated list of <City, address, phone #>
    offices = models.CharField(max_length=512, blank=True)

    #Input into Contacts table, point back to Company
    # Need to be modified in the future
    # others_people = models.ForeignKey("Contact")
    
    #set of multiple <Date, Value, Round> entries (i.e. 2/12/12, $2.5M, A)
    funding = models.CharField(max_length=512, blank=True)

    #Comma separated list of entries from Company table
    acquisition = models.CharField(max_length=512, blank=True)

    #Comma separated list of products/services
    product = models.CharField(max_length=512, blank=True)
    #prod_ser_img = models.ManyToManyField("")

    #Comma separated list of certifications from Certification Table
    #certification = models.ForeignKey("Certification")
    certification = models.CharField(max_length=512, blank=True)
    
    #Comma separated list of Customers form Company Table
    customer = models.CharField(max_length=512, blank=True)

    #Comma separated list of entries from project table
#    project = models.ManyToManyField("Project")
#    links = models.ForeignKey("URLs")

    #<Person, Phone, email>
    contact = models.CharField(max_length=512, blank=True)
    
    # Visible for LATech members
    scalability_rating = models.IntegerField(blank=True, null=True)
    expansion_rating = models.IntegerField(blank=True, null=True)
    physical_plant_rating = models.IntegerField(blank=True, null=True)
    profilatibily_rating = models.IntegerField(blank=True, null=True)
    ret_talent_rating = models.IntegerField(blank=True, null=True)
    financials_rating = models.IntegerField(blank=True, null=True)
    rating_of_ownership = models.IntegerField(blank=True, null=True)
    gtb_overall_rating = models.IntegerField(blank=True, null=True)

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

class CompanyForm(ModelForm):
    class Meta:
       model = Company
       exclude = ['slug']

class Office(models.Model): 
    city = models.ForeignKey(City, related_name="location", blank=True)
    address = models.CharField(max_length=512, blank=True)
    phone = models.CharField(max_length=512, blank=True)

    def __unicode__(self):
        return self.address
