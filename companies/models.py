from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=80)
    logo = models.ImageField()
    description = models.CharField(max_length=144)
    value_proprosition = models.CharField(max_length=144)
    overview = models.CharField(max_length=512)
    management = models.ForeignKey("Contact")
    web_url = models.URLField()
    blog_url = models.URLField()
    twitter_username = models.CharField()
    main_phone = models.CharField()
    email = models.EmailField()
    industries = models.ForeignKey("Industry")
    tech_area = models.ForeignKey("Technology")
    category = models.ForeignKey("Category")
    application = models.ForeignKey("Application")
    tag = models.ForeignKey("Tag")
    #competitors = models.Foreignkey("")
    competitors = models.CharField()
    offices = models.ForeignKey("Office")
    others_people = models.ForeignKey("Contact")
    funding = models.CharField()
    acquisition = models.CharField()
    product = models.ForeignKey("Product")
    prod_ser_img = models.ManyToManyField("")
    certification = models.ForeignKey("Certification")
    customer = models.CharField()
    project = models.ManyToManyField("Project")
    links = models.ForeignKey("URLs")
    contact = models.CharField()
    # Visible for LATech members
    scalability_rating = models.IntegerField()
    expansion_rating = models.IntegerField()
    physical_plant_rating = models.IntegerField()
    profilatibily_rating = models.IntegerField()
    ret_talent_rating = models.IntegerField()
    financials_rating = models.IntegerField()
    rating_of_ownership = models.IntegerField()
    gtb_overall_rating = models.IntegerField()

    def __unicode__(self):
        return self.name

class Office(models.Model): 
    city = models.ForeignKey("City")
    address = models.CharField(max_length=255)
    phone = models.CharField()

    def __unicode__(self):
        return self.address
