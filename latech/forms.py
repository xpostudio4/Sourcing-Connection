from django.forms import ModelForm
from django import forms
from companies.models import *
from location.models import *

class SearchForm(forms.Form):
    query = forms.CharField(
        label=u'Enter a keyword to search for',
        widget=forms.TextInput(attrs={'size': 20})
    )

class AdvanceSearchForm(forms.Form):
    keywords = forms.CharField(
        label=u'Keywords',
        widget=forms.TextInput(attrs={'size': 20})
    )
    category = forms.ModelChoiceField(
        label=u'Categories',
        queryset=Category.objects.all()
    )
    country = forms.ModelChoiceField(
        label=u'Country',
        queryset=Country.objects.all()
    )

    industry = forms.CharField(
        label=u'Industries',
        widget=forms.TextInput(attrs={'size': 20})
    )
    technology = forms.CharField(
        label=u'Technologies',
        widget=forms.TextInput(attrs={'size': 20})
    )
    


