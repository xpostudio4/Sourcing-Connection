#Python Libraries
from datetime import datetime

#Django internal modules
from django.db import models
from django.template import defaultfilters

#Internal Apps
from companies.models import Company

#Third Parties


# Company Information
class AnnualRevenue(models.Model):
    company = models.ForeignKey(Company, related_name='Company Annual Revenue')
    revenue = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField(blank=True,null=True)

    def __unicode__(self):
        return ("%s: %.2f ") % (self.company, self.revenue)

class Milestone(models.Model):
    company = models.ForeignKey(Company, related_name='Company Milestones')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    from_date = models.DateField()
    to_date = models.DateField()

    def __unicode__(self):
        return ('%s: %s') % (self.company, self.title)

# Company Experience
class Project(models.Model):
    company = models.ForeignKey(Company, related_name='Company Projects')
    name = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    client = models.ForeignKey(Company, related_name='Company Clients')

    def __unicode__(self):
        return ('%s: %s - client: %s') % (self.company, self.name, self.client)


class SuccessStories(models.Model):
    company = models.ForeignKey(Company, related_name='Company Stories')
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = "Success Stories"

    def __unicode__(self):
        return self.title

class Expertise(models.Model):
    company = models.ForeignKey(Company, related_name='Company Expertise')
    expertise = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.expertise)
        super(Expertise, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.expertise
    
class Vertical(models.Model):
    company = models.ForeignKey(Company, related_name='Company Verticals')
    vertical = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200)

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.vertical)
        #self.description_html = markdown(self.description)
        super(Vertical, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.vertical
    

#Ecosystem
# All-in-one model with choices


class Ecosystem(models.Model):
    ECOSYSTEM_CHOICES = (
        (1, "Partnership"),
        (2, "Alliance"),
        (3, "Technical Association"),
        (4, "Competitor")
    )
    company = models.ForeignKey(Company, related_name='Internal Company')
    competence = models.ForeignKey(Company, related_name='Company Ecosystem', verbose_name='Company')
    relationship = models.PositiveIntegerField(choices=ECOSYSTEM_CHOICES)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return ("%s: %s with %s") % (self.company, self.get_relationship_display(), self.competence)


# All Models separated:

#class Partnership(models.Model):
#    company = models.ForeignKey(Company, related_name='+')
#    partner = models.ForeignKey(Company, related_name='Company Partner')
#    description = models.TextField(blank=True)

#class Alliance(models.Model):
#    company = models.ForeignKey(Company, related_name='+')
#    ally = models.ForeignKey(Company, related_name='+')
#    description = models.TextField(blank=True)

#class TechnicalAssociation(models.Model):
#    company = models.ForeignKey(Company, related_name='+')
#    ally = models.ForeignKey(Company, related_name='+')
#    description = models.TextField(blank=True)

#class Competitors(models.Model):
#    company = models.ForeignKey(Company, related_name="Source Company", blank=True)
#    name = models.CharField(max_length=255)

#    def __unicode__(self):
#        return str(self.company) +":" + str(self.name)

#    class Meta:
#         verbose_name_plural = "Competitors"
