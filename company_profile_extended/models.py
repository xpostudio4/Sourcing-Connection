#Python Libraries
import os
from datetime import datetime

#Django internal modules
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.template import defaultfilters

#Internal Apps
from companies.models import Company

#Third Parties
from storagess.backends.gs import GSBotoStorage

if os.getenv('HEROKU_ENV') == 'True':
    gs = GSBotoStorage()
else:
    gs = FileSystemStorage()


# Company Information
class AnnualRevenue(models.Model):
    company = models.ForeignKey(Company, related_name='Company Annual Revenue')
    revenue = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField(blank=True,null=True)

    def __unicode__(self):
        return ("%s: %.2f ") % (self.company, self.revenue)

class Milestone(models.Model):
    company = models.ForeignKey(Company, related_name='Company Milestones')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    from_date = models.DateField()
    to_date = models.DateField()

    def __unicode__(self):
        return ('%s: %s') % (self.company, self.title)

# Company Experience
class Project(models.Model):
    company = models.ForeignKey(Company, related_name='Company Projects')
    client = models.ForeignKey(Company, related_name='Company Clients')
    name = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()


    def __unicode__(self):
        return ('%s: %s - client: %s') % (self.company, self.name, self.client)


class SuccessStories(models.Model):
    company = models.ForeignKey(Company, related_name='Company Stories')
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.FileField(storage=gs, upload_to="companies/docs/", blank=True)

    class Meta:
        verbose_name_plural = "Success Stories"

    def __unicode__(self):
        return self.title

class Expertise(models.Model):
    company = models.ForeignKey(Company, related_name='Company Expertise')
    expertise = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.expertise)
        super(Expertise, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.expertise
    
class Vertical(models.Model):
    company = models.ForeignKey(Company, related_name='Company Verticals')
    vertical = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200)

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.vertical)
        #self.description_html = markdown(self.description)
        super(Vertical, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.vertical
    

# All Models separated:

class Partnership(models.Model):
    company = models.ForeignKey(Company, related_name='Company Partnerships')
    name = models.ForeignKey(Company, related_name='Company Partner')
    description = models.TextField(blank=True)

    def __unicode__(self):
        return ("%s") % (self.name)

class Alliance(models.Model):
    company = models.ForeignKey(Company, related_name='Company Alliances')
    name = models.ForeignKey(Company, related_name='Company Ally')
    description = models.TextField(blank=True)

    def __unicode__(self):
        return ("%s") % (self.name)


class TechnicalAssociation(models.Model):
    company = models.ForeignKey(Company, related_name='Company Technical Association')
    name = models.ForeignKey(Company, related_name='Company Associate')
    description = models.TextField(blank=True)

    def __unicode__(self):
        return ("%s") % (self.name)

class Competitor(models.Model):
    company = models.ForeignKey(Company, related_name="Company Competitors", blank=True)
    name = models.ForeignKey(Company, related_name='Company Competitor')
    description = models.TextField(blank=True)

    def __unicode__(self):
        return str(self.company) +":" + str(self.name)

    class Meta:
         verbose_name_plural = "Competitors"

class Product(models.Model):
    company = models.ForeignKey(Company, related_name="Company Products", blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
 
    def __unicode__(self):
        return (self.product)