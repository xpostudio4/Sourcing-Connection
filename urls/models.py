from django.db import models

# Create your models here.
class Urls(models.Model):
	url_type = models.CharField()
	url  = models.UrlField()
	resource_id = models.IntegerField()
	comment = models.CharField()



	def __unicode__(self):
        return self.title