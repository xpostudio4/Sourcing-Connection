from django.db import models

# Create your models here.

#Country_Table

class Country(models.Model):
    name = models.CharField(max_length=30)
    flag = models.Imagefield()
    government_type = models.CharField(max_length=30)
    stability_rating = models.CharField(max_length=30)
    policy_favorability_Rating= models.CharField(max_length=30)
    url_wolfram= models.URLField()
    url_wiki= models.URLField()

    def __unicode__(self):
        return self.title

#Region_Table

class Region_Table(models.Model):
    country = models.CharField(max_length=30)
    region_Name = models.CharField(max_length=30)
    accesiblity_rating = models.CharField(max_length=30)
    transportations = models.CharField(max_length=30)
    url_wolfram= models.URLField()
    url_wiki= models.URLField()

    def __unicode__(self):
        return self.title

#City_Tablet

class City_Table(models.Model):
    country = models.CharField(max_length=30)
    region_name = models.CharField(max_length=30)
    city_name = models.CharField(max_length=30)
    universities = models.CharField(max_length=30)
    telecom_facilities = models.CharField(max_length=30)
    local_talent_pool_rating = models.CharField(max_length=30)
    url_wolfram= models.URLField()
    url_wiki= models.URLField()
    
    def __unicode__(self):
        return self.title
    
