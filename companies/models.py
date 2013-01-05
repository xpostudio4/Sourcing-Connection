from django.db import models
from taxonomy.models import *
from location.models import *
# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=80)
    #logo = models.ImageField()
    description = models.TextField(blank=True)
    value_proposition = models.CharField(max_length=144, blank=True)
    overview = models.CharField(max_length=512, blank=True)


    #Input into Contacts table, point back to Company
    management = models.CharField(max_length=144, blank=True)
    web_url = models.URLField(blank=True)
    blog_url = models.URLField(blank=True)
    twitter_username = models.CharField(max_length=512, blank=True)
    main_phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    #Comma separated list from Industry table
    industries = models.CharField(max_length=512, blank=True)

    #Comma separated list from Technologies table
    tech_area = models.CharField(max_length=512, blank=True)

    #Comma separated list from Category table
    category = models.ForeignKey(Category, related_name="categories", blank=True)

    #Comma separated list from Application table
    application = models.ForeignKey(Application, related_name="categories", blank=True)

   
    #Comma separated list from Tags table, also accept new tags input by users ("folksonomy")
    tag = models.ManyToManyField(Tag, related_name="tags", blank=True)
    
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
    scalability_rating = models.IntegerField(blank=True)
    expansion_rating = models.IntegerField(blank=True)
    physical_plant_rating = models.IntegerField(blank=True)
    profilatibily_rating = models.IntegerField(blank=True)
    ret_talent_rating = models.IntegerField(blank=True)
    financials_rating = models.IntegerField(blank=True)
    rating_of_ownership = models.IntegerField(blank=True)
    gtb_overall_rating = models.IntegerField(blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
         verbose_name_plural = "Companies"


class Office(models.Model): 
    city = models.ForeignKey(City, related_name="location", blank=True)
    address = models.CharField(max_length=512, blank=True)
    phone = models.CharField(max_length=512, blank=True)

    def __unicode__(self):
        return self.address
