from django.db import models

# Create your models here.

class Industry(models.Model): 
     name = models.CharField(max_length=80)

     def __unicode__(self):
        return self.title


class Technology(models.Model):
	name = models.CharField(max_length=80)

	def __unicode__(self):
        return self.title


class Category(models.Model):
	name = models.CharField(max_length=80)

	def __unicode__(self):
        return self.title


class Application(models.Model):
	name = models.CharField(max_length=80)

	def __unicode__(self):
        return self.title


class Tag(models.Model):
	name = models.CharField(max_length=80)

	def __unicode__(self):
        return self.title


class RatingOverview(models.Model):
    rating_overview = models.CharField() 
     