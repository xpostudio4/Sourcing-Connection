from companies.models import *
from django import forms
from django.forms import ModelForm

class CompanyForm(ModelForm):
    class Meta:
       model = Company
       exclude = ("slug", "tags", "contact", "company_status")

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class CompanyLinkForm(ModelForm):
	class Meta:
		model = CompanyLink
		exclude = ('company')

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
			'contact',
			'title')
			
			
class ManagementPictureForm(ModelForm):
    class Meta:
       model = ManagementPicture
       exclude = ("manager","slug")
