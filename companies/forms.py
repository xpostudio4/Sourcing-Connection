from companies.models import *
from django.forms import ModelForm

class CompanyForm(ModelForm):
    class Meta:
       model = Company
       exclude = ("slug")

class FundingForm(ModelForm):
	class Meta:
		model = Funding
		fields = ('round', 'raised')

class CompetitorsForm(ModelForm):
	class Meta:
		model = Competitors
		exclude = ('company')

class OfficeForm(ModelForm):
	class Meta:
		model = Office
		fields = (
			"description",
			"address_1",
			"address_2",
			"city",
			"phone",
			"zip_code",
			"country")
