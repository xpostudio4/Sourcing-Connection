from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(User):
    m_name = models.CharField(max_length=255)
    photo = models.ImageField()
    phone = models.charField()
    degrees = models.CharField()
    ld_url = models.URLField()
    t_url = models.URLField()
    blog_url = models.URLField()
    ext_url = models.URLField()
    lt_contact = models.CharField()
    tag = models.ForeignKey("Tag")
    company = models.ForeignKey("Company")
    financial_organization = models.CharField()
    government_organization = models.CharField()
    title = models.CharField()
    industry = models.CharField()
    technology = models.CharField()
    application = models.ForeignKey("Application")
    overview = models.CharField()

    def __unicode__(self):
        return self.contact
