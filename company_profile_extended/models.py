#Python Librariess
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
    company = models.ForeignKey(Company, related_name='annual_revenues')
    revenue = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField(blank=True,null=True)

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return ("%s: %.2f ") % (self.company, self.revenue)

class Milestone(models.Model):
    company = models.ForeignKey(Company, related_name='milestones')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return ('%s: %s') % (self.company, self.title)

# Company Experience
class Project(models.Model):
    company = models.ForeignKey(Company, related_name='projects')
    client = models.ForeignKey(Company, related_name='clients')
    name = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()

    class Meta:
        ordering = ['id']


    def __unicode__(self):
        return ('%s: %s - client: %s') % (self.company, self.name, self.client)


class SuccessStories(models.Model):
    company = models.ForeignKey(Company, related_name='success_stories')
    title = models.CharField(max_length=200)
    description = models.TextField()
    story_image = models.ImageField(blank=True, null=True, storage=gs, upload_to="images/companies_imgs/")
    link = models.FileField(storage=gs, upload_to="companies/docs/", blank=True)

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Success Stories"

    def __unicode__(self):
        return self.title

class Expertise(models.Model):
    company = models.ForeignKey(Company, related_name='expertises')
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    class Meta:
        ordering = ['id']


    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.name)
        super(Expertise, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
    
class Vertical(models.Model):
#    company = models.ForeignKey(Company, related_name='Verticals')
    company = models.ForeignKey(Company, related_name='verticals')
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200)

    class Meta:
        ordering = ['id']

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.name)
        #self.description_html = markdown(self.description)
        super(Vertical, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
    

# All Models separated:

class Partnership(models.Model):
    company = models.ForeignKey(Company, related_name='partnerships')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return ("%s") % (self.name)

class Alliance(models.Model):
    company = models.ForeignKey(Company, related_name='alliances')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return ("%s") % (self.name)


class TechnicalAssociation(models.Model):
    company = models.ForeignKey(Company, related_name='technical_association')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return ("%s") % (self.name)

class Competitor(models.Model):
    company = models.ForeignKey(Company, related_name="company_competitors", blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Competitors"

    def __unicode__(self):
        return str(self.company) +":" + str(self.name)


class Product(models.Model):
    company = models.ForeignKey(Company, related_name="company_products", blank=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    product_image = models.ImageField(blank=True, null=True, storage=gs, upload_to="images/companies_imgs/products/")

    class Meta:
        ordering = ['id']
 
    def __unicode__(self):
        return (self.name)