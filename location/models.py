from django.db import models
from smart_selects.db_fields import ChainedForeignKey 


# Create your models here.

#Country_Table

class Country(models.Model):
    class Meta:
         ordering = ['id']

    name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=2, blank=True)
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
    class Meta:
         ordering = ['id']

    country = models.ForeignKey(Country, related_name="countries",max_length=150)
    region_name = models.CharField(max_length=30, verbose_name=u'Region or State')
    accesiblity_rating = models.CharField(max_length=30,blank=True)
    transportations = models.CharField(max_length=30, blank=True)
    url_wolfram= models.URLField(blank=True)
    url_wiki= models.URLField(blank=True)

    def __unicode__(self):
        return self.region_name

#City_Tablet

class City(models.Model):
    class Meta:
         ordering = ['id']

    country = models.ForeignKey(Country, related_name="country")
    region_name = ChainedForeignKey(
        Region, 
        related_name="region",
        chained_field="country",
        chained_model_field="country", 
        show_all=False, 
        auto_choose=True
    )    
    #region_name = models.ForeignKey(Region, related_name="region") 
    city_name = models.CharField(max_length=150)
    universities = models.CharField(max_length=30,blank=True)
    telecom_facilities = models.CharField(max_length=30, blank=True)
    local_talent_pool_rating = models.CharField(max_length=30, blank=True)
    url_wolfram= models.URLField(blank=True)
    url_wiki= models.URLField(blank=True)
    
    def __unicode__(self):
        return self.city_name

    class Meta:
         verbose_name_plural = "Cities"
    
