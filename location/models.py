from django.db import models

# Create your models here.

#Country_Table

class Country(models.Model):
    name = models.CharField(max_length=30)
    #flag = models.Imagefield()
    government_type = models.CharField(max_length=30)
    stability_rating = models.CharField(max_length=30)
    policy_favorability_Rating= models.CharField(max_length=30)
    url_wolfram= models.URLField(blank=True)
    url_wiki= models.URLField(blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
         verbose_name_plural = "Countries"

#Region_Table

class Region(models.Model):
    country = models.ForeignKey(Country, related_name="countries",max_length=30)
    region_name = models.CharField(max_length=30)
    accesiblity_rating = models.CharField(max_length=30)
    transportations = models.CharField(max_length=30)
    url_wolfram= models.URLField(blank=True)
    url_wiki= models.URLField(blank=True)

    def __unicode__(self):
        return self.title

#City_Tablet

class City(models.Model):
    country = models.ForeignKey(Country, related_name="country",max_length=50)
    region_name = models.ForeignKey(Region, related_name="region",max_length=50) 
    city_name = models.CharField(max_length=30)
    universities = models.CharField(max_length=30)
    telecom_facilities = models.CharField(max_length=30)
    local_talent_pool_rating = models.CharField(max_length=30)
    url_wolfram= models.URLField(blank=True)
    url_wiki= models.URLField(blank=True)
    
    def __unicode__(self):
        return self.title

    class Meta:
         verbose_name_plural = "Cities"
    
