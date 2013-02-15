from django.db import models
from companies.models import Company
from django.core.files.storage import FileSystemStorage
from storagess.backends.gs import GSBotoStorage


# Detecting Heroku Deployment
if os.getenv('HEROKU_ENV') == 'True':
    gs = GSBotoStorage()
else:
    gs = FileSystemStorage()

class Picture(models.Model):

    # This is a small demo using just two fields. The slug field is really not
    # necessary, but makes the code simpler. ImageField depends on PIL or
    # pillow (where Pillow is easily installable in a virtualenv. If you have
    # problems installing pillow, use a more generic FileField instead.

    #file = models.FileField(upload_to="pictures")
    file = models.ImageField(storage=gs, upload_to="images/companies_imgs/")
    slug = models.SlugField(max_length=50, blank=True)
    company = models.ForeignKey(Company, related_name="Company Images")

    def __unicode__(self):
        return self.slug

    @models.permalink
    def get_absolute_url(self):
        return ('upload-new', )

    def save(self, *args, **kwargs):
        self.slug = self.file.name
        super(Picture, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.file.delete(False)
        super(Picture, self).delete(*args, **kwargs)
