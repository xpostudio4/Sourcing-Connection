from django.db import models
from django.contrib.auth.models import User
from django.template import defaultfilters
import datetime



# Create your models here.
class Post(models.Model):
    """This model holds the blog post that will appear on the homepage of the globaltech site."""
    name = models.CharField(max_length=520)
    slug = models.SlugField(max_length=80)
    created = models.DateTimeField(default=datetime.datetime.now, blank=True)
    url = models.URLField(blank=True)
    post = models.TextField(blank=True)
    user = models.ForeignKey(User, related_name="Blogger", null=True, blank=True)

    def save(self, *args, **kwargs):
    	''' On save, update timestamps '''
        if not self.user: 
            usr = User.objects.filter(username="xpostudio4")
            self.user = usr
        self.slug = defaultfilters.slugify(self.name)
        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name