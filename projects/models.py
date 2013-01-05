from django.db import models
from taxonomy.models import *
from companies.models import Company

# Create your models here.
class Project(models.Model):
	provider_company = models.ForeignKey(Company, related_name"provider")
	customer_name = models.ForeignKey(Company, related_name"customer")
	description = models.CharField(max_length=144)
	duration = models.IntegerField(blank=True)
	resource_use = models.IntegerField(blank=True)
	cost_rate = models.CharField(max_length=144, blank=True)
	#Image will taken in the view 
	#Urls pending
	contact = models.CharField(max_length=144, blank=True)
	industry = models.ManyToManyField(Industry, related_name="industries", blank=True)
	technology_areas = models.ManyToManyField(Technology, related_name="technology_areas", blank=True)
	categories = models.ManyToManyField(Category, related_name="categories", blank=True)
	application = models.ManyToManyField(Application, related_name="apps", blank=True)

	tag = models.ManyToManyField(Tag, related_name="tags", blank=True)
	rating_overview = models.CharField(max_length=144, blank=True)


	def __unicode__(self):
        return self.title




    
