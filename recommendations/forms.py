from recommendations.models import Recommendation
from django import forms
from django.forms import ModelForm

class RecommendationForm(ModelForm):
    class Meta:
       model = Recommendation
       exclude = ("user",)
