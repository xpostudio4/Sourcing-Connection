from django.db import models
from django.contrib.auth.models import User
import datetime



# Create your models here.
class Post(models.Model):
    """This model holds the blog post that will appear on the homepage of the globaltech site."""
    name = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80)
    created = models.DateTimeField()
    url = models.URLField(blank=True)
    post = models.TextField(blank=True)
    user = models.ForeignKey(User, related_name="Blogger", null=True, blank=True)

    #def save(self, *args, **kwargs):
    #	''' On save, update timestamps '''
    #    if not self.id:
    #        self.created = datetime.datetime.today()
    #    super(Post, self).save(*args, **kwargs)