from django.db import models

# Create your models here.
class Project(models.Model):
	provider_company = models.ForeignKey(Company)
	customer_name = models.ForeignKey(Company)
	description = models.CharField(max_length=144)
	duration = models.IntegerField()
	resource_use = models.IntegerField()
	cost_rate = models.CharField(max_length=144)
	#Image will taken in the view 
	#Urls pending
	contact = models.CharField()
	industry = models.CharField()
	technology_areas = models.CharField()
	category = models.CharField()
	application = models.CharField()
	tags = models.CharField()
	rating_overview = models.CharField()


	def __unicode__(self):
        return self.title




    