from companies.models import *
from django.forms import ModelForm

class CompanyForm(ModelForm):
    class Meta:
       model = Company
       exclude = ("slug")

class CompetitorsForm(ModelForm):
	class Meta:
		model = Competitors
		exclude = ('company')

class CertificationForm(ModelForm):
	class Meta:
		model = Certification
		exclude = ('company')

class AcquisitionForm(ModelForm):
	class Meta:
		model = Acquisition
		exclude = ('company')

class AwardForm(ModelForm):
	class Meta:
		model = Award
		exclude = ('company')

class CustomerForm(ModelForm):
	class Meta:
		model = Customer 
		exclude = ('company')

class FundingForm(ModelForm):
	class Meta:
		model = Funding
		fields = ('round', 'raised')

class CompanyRatingForm(ModelForm):
	class Meta:
		model = CompanyRating
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

class ManagementForm(ModelForm):
	class Meta:
		model = Management
		fields = (
			'full_name',
			'title')
			
			
