from django.db import models

# Create your models here.

#Country_Table

class Country(models.Model):
    name = models.CharField(max_length=100)
    #flag = models.Imagefield()
    government_type = models.CharField(max_length=80, blank=True)
    stability_rating = models.CharField(max_length=30, blank=True)
    policy_favorability_Rating= models.CharField(max_length=30, blank=True)
    url_wolfram= models.URLField(blank=True)
    url_wiki= models.URLField(blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
         verbose_name_plural = "Countries"

#Region_Table

class Region(models.Model):
    country = models.ForeignKey(Country, related_name="countries",max_length=30)
    region_name = models.CharField(max_length=30)
    accesiblity_rating = models.CharField(max_length=30,blank=True)
    transportations = models.CharField(max_length=30, blank=True)
    url_wolfram= models.URLField(blank=True)
    url_wiki= models.URLField(blank=True)

    def __unicode__(self):
        return self.region_name

#City_Tablet

class City(models.Model):
    country = models.ForeignKey(Country, related_name="country",max_length=50)
    region_name = models.ForeignKey(Region, related_name="region",max_length=50) 
    city_name = models.CharField(max_length=30)
    universities = models.CharField(max_length=30,blank=True)
    telecom_facilities = models.CharField(max_length=30, blank=True)
    local_talent_pool_rating = models.CharField(max_length=30, blank=True)
    url_wolfram= models.URLField(blank=True)
    url_wiki= models.URLField(blank=True)
    
    def __unicode__(self):
        return self.city_name

    class Meta:
         verbose_name_plural = "Cities"
    
