from django.db import models
from django.contrib.auth.models import User
from taxonomy.models import *
from companies.models import Company
# Create your models here.

class Contact(User):

    #Special Information about contact
    overview = models.TextField(blank=True)

    m_name = models.CharField(max_length=255, blank=True)
    #photo = models.ImageField()
    phone = models.CharField(max_length=255, blank=True)

    #Comma separated list of Degrees
    degrees = models.CharField(max_length=255, blank=True)

    #Ptr to LinkedIn profile
    ld_url = models.URLField(blank=True)

    #Ptr to Twitter profile
    t_url = models.URLField(blank=True)

    #Ptr to person's blog
    blog_url = models.URLField(blank=True)

    #Ptr to other relevant links
    ext_url = models.URLField(blank=True)
    
    #LATech contact responsible for the entry
    lt_contact = models.CharField(max_length=255, blank=True)

    #List of Tags associated w/ contact
    tag = models.CharField(max_length=255, blank=True)

    #Pointer to  company from Company table
    company = models.ForeignKey(Company, related_name="company", blank=True)

    #Comma separated list of Companies
    financial_organization = models.CharField(max_length=255, blank=True)

    #Comma separated list of Companies
    government_organization = models.CharField(max_length=255, blank=True)

    #Current and past relevant Titles
    title = models.CharField(max_length=255, blank=True)

    #Pointer to Industry (industries) from Industry table
    industry = models.ManyToManyField(Industry, related_name="industries", blank=True)

    #Pointer to list of Technologies from Technology Table
    technology = models.ManyToManyField(Technology, related_name="technologies", blank=True) 

    #Pointer to list of Applications from Application Table
    application = models.ManyToManyField(Application, related_name="applications", blank=True)

    def __unicode__(self):
        return self.contact
