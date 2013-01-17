from companies.models import *
from django.forms import ModelForm

class CompanyForm(ModelForm):
    class Meta:
       model = Company
    #   exclude = ['slug']

class FundingForm(ModelForm):
	class Meta:
		model = Funding
	#	exclude = ['company']

class CompetitorsForm(ModelForm):
	class Meta:
		model = Competitors
	#	exclude = ['company']

class OfficeForm(ModelForm):
	class Meta:
		model = Office
	#	exclude = ['company'] 
