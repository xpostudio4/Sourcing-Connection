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


class EcosystemForm(ModelForm):
    class Meta:
       model = Ecosystem
       exclude = ("company",)
