from django.db import models
from django.contrib.auth.models import User
from taxonomy.models import *
from companies.models import Company
from django.forms import ModelForm

class Contact(models.Model):
    user = models.OneToOneField(User)
    fr_name = models.CharField(max_length=255, blank=True, verbose_name="First Name")
    ls_name = models.CharField(max_length=255, blank=True, verbose_name="Last Name")
    m_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    #Special Information about contact
    overview = models.TextField(blank=True)
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
    tags = models.CharField(max_length=255, blank=True)

    #Pointer to  company from Company table
    company = models.ForeignKey(Company, related_name="company", blank=True, null=True, on_delete=models.SET_NULL)

    #Comma separated list of Companies
    financial_organization = models.CharField(max_length=255, blank=True)

    #Comma separated list of Companies
    government_organization = models.CharField(max_length=255, blank=True)

    #Current and past relevant Titles
    title = models.CharField(max_length=255, blank=True)

    #Pointer to Industry (industries) from Industry table
    industry = models.CharField(max_length=255, blank=True)

    #Pointer to list of Technologies from Technology Table
    technology = models.CharField(max_length=255, blank=True)

    #Pointer to list of Applications from Application Table
    application = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return str(self.fr_name +" "+ self.ls_name)

    @models.permalink
    def get_absolute_url(self):
          return ("/profile/%s/" % self.user)


class ContactForm(ModelForm):
    class Meta:
       model = Contact
       exclude = ('user', 'slug', )
       

