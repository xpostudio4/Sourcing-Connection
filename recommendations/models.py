from django.contrib.auth.models import User
from django.db import models

from companies.models import Company

class Recommendation(models.Model):
	user = models.OneToOneField(User)
	company = models.ForeignKey(Company)
	title = models.CharField(max_length=255)
	recommendation = models.TextField()

	def __unicode__(self):
		return ("%s recommends to %s") % (self.user, self.company)

