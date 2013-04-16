import datetime
from django.contrib.auth.models import User
from django.db import models
from django.template import defaultfilters

from companies.models import Company


class Event(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True)
    where = models.CharField(max_length=255)
    posted_by = models.ForeignKey(User)
    company = models.ForeignKey(Company, blank=True, null=True)
    datetime = models.DateTimeField()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.title)
        super(Event, self).save(*args, **kwargs)
