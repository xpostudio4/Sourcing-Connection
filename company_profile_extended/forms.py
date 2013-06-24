from companies.models import Company
from company_profile_extended.models import *
from django import forms
from django.forms import ModelForm

class AnnualRevenueForm(ModelForm):
    class Meta:
       model = AnnualRevenue
       exclude = ("company",)

class MilestoneForm(ModelForm):
    class Meta:
       model = Milestone
       exclude = ("company",)

# Company Experience
class ProjectForm(ModelForm):
    class Meta:
       model = Project
       exclude = ("company",)

class SuccessStoriesForm(ModelForm):
    class Meta:
       model = SuccessStories
       exclude = ("company",)

class ExpertiseForm(ModelForm):
    class Meta:
       model = Expertise
       exclude = ("company","slug")

    
class VerticalForm(ModelForm):

    class Meta:
       model = Vertical
       exclude = ("company","slug")

class PartnershipForm(ModelForm):
#    def get_field(name, id):
#        name = forms.ModelChoiceField(queryset=Company.objects.all().exclude(id=id))
    class Meta:
       model = Partnership
       exclude = ("company",)

#    def __init__(self, company, *args, **kwargs):
#        super(PartnershipForm, self).__init__(*args, **kwargs)
#        self.fields['name'].queryset = Company.objects.all().exclude(id=company.id)

class AllianceForm(ModelForm):
    class Meta:
       model = Alliance
       exclude = ("company",)

class TechnicalAssociationForm(ModelForm):
    class Meta:
       model = TechnicalAssociation
       exclude = ("company",)

class ProductForm(ModelForm):
    class Meta:
       model = Product
       exclude = ("company",)

class ProductPictureForm(ModelForm):
    class Meta:
       model = Product
       fields = ("product_image",)
