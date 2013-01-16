from django.db import models

# Create your models here.

class Industry(models.Model): 
     name = models.CharField(max_length=80)

     def __unicode__(self):
        return self.name

     class Meta:
         verbose_name_plural = "Industries"


class Technology(models.Model):
    name = models.CharField(max_length=80)

    def __unicode__(self):
        return self.name
    class Meta:
         verbose_name_plural = "Technologies"

class Category(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
          return ("/categories/%s/" % self.slug)

    class Meta:
         verbose_name_plural = "Categories"


class Application(models.Model):
    name = models.CharField(max_length=80)

    def __unicode__(self):
        return self.name

# The tags models is now provided by the Django-taggit app

class Tag(models.Model):
    name = models.CharField(max_length=80)

    def __unicode__(self):
        return self.name


# This class is on the Project's table 

#class RatingOverview(models.Model):
#    rating_overview = models.CharField(max_length=100) 
     
