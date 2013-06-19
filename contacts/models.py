import os
from PIL import Image
from os.path import join
from django.db import models
from django.contrib.auth.models import User
from taxonomy.models import *
from location.models import Country, City
from companies.models import Company
from django.forms import ModelForm
from django.core.files.base import ContentFile
from django.db.models.signals import post_save, pre_save
from django.dispatch import dispatcher
from django.dispatch import receiver

#from storages.backends.gs import GSBotoStorage
from django.core.files.storage import FileSystemStorage
from storagess.backends.gs import GSBotoStorage


# Detecting Heroku Deployment
if os.getenv('HEROKU_ENV') == 'True':
    gs = GSBotoStorage()
else:
    gs = FileSystemStorage()
    
class Contact(models.Model):
    user = models.OneToOneField(User)
    fr_name = models.CharField(max_length=255, blank=True, verbose_name="First Name")
    ls_name = models.CharField(max_length=255, blank=True, verbose_name="Last Name")
    m_name = models.CharField(max_length=255, blank=True, verbose_name="Middle Name")
    email = models.EmailField(blank=True)
    #Special Information about contact
    overview = models.TextField(blank=True)
    #photo = models.ImageField()
    photo_profile = models.ImageField(blank=True, null=True, storage=gs, upload_to="images/profile_img/")
    
    phone = models.CharField(max_length=255, blank=True)
    # Contact Country
    country = models.ForeignKey(Country, related_name="Country", null=True, blank=True)
    city = models.ForeignKey(City, related_name="City", null=True, blank=True)
    #Comma separated list of Degrees
    degrees = models.CharField(max_length=255, blank=True)
    #LATech contact responsible for the entry

    lt_contact = models.CharField(max_length=255, blank=True, verbose_name="Latech Contact" )

    #List of Tags associated w/ contact
    tags = models.CharField(max_length=255, blank=True)

    #Pointer to  company from Company table
    company = models.ForeignKey(Company, related_name="company", blank=True, null=True, on_delete=models.SET_NULL)

    latech_contact = models.BooleanField(default=False)
   
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
        if self.fr_name and self.ls_name:
            return str(self.fr_name +" "+ self.ls_name)

        elif not self.fr_name and not self.ls_name and self.user.first_name and self.user.last_name:
            return str(self.user.first_name +" "+ self.user.last_name)

        else:
            return str(self.user)

    def __init__(self, *args, **kwargs):
        """
        Overwritting of __init__ to take some initial values from User's models needed in this application
        """

        super(Contact, self).__init__(*args, **kwargs)
        if not self.fr_name:
            self.fr_name = self.user.first_name

        if not self.ls_name:
            self.ls_name = self.user.last_name

        if not self.email:
            self.email = self.user.email
        
        


    def save(self,*args, **kwargs):
        if not self.user.first_name:
            self.user.first_name =self.fr_name
        
        if not self.user.last_name:
            self.user.last_name = self.ls_name

        if not self.user.email:
            self.user.email = self.email


        super(Contact, self).save(*args, **kwargs)
        contact_url = Contact_Urls(latech_contact=self)
        if not contact_url:
            contact_url.save()

    @models.permalink
    def get_absolute_url(self):
          return ("/profile/%s/" % self.user)
    

class Contact_Urls(models.Model):
    latech_contact = models.OneToOneField(Contact)
   #Ptr to LinkedIn profile
    ld_url = models.URLField(blank=True, null=True, verbose_name="LinkedIn Url")

    #Ptr to Twitter profile
    t_url = models.URLField(blank=True, verbose_name="Twitter Url")

    #Ptr to person's blog
    blog_url = models.URLField(blank=True, verbose_name="Blog Url")

    #Ptr to other relevant links
    ext_url = models.URLField(blank=True, verbose_name="External Urls")
    
    def __unicode__(self):
        return str(self.latech_contact.fr_name +" "+ self.latech_contact.ls_name + " Urls")
    
    class Meta:
        verbose_name_plural="Contact Urls"
    

@receiver(post_save, sender=User)
def create_contact(sender, instance, created, **kwargs):
    if created:
        
        contact = Contact.objects.create(user=instance)
 