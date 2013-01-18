from django.forms import ModelForm
from django import forms
from companies.models import *
from contacts.models import *
from location.models import *

class SearchForm(forms.Form):
    query = forms.CharField(
        label=u'Enter a keyword to search for',
        widget=forms.TextInput(attrs={'size': 20})
    )

class CompanySearchForm(forms.Form):
    keywords = forms.CharField(
        label=u'Keywords',
        widget=forms.TextInput(attrs={'size': 20} ),
                required = False
    )
    category = forms.ModelChoiceField(
        label=u'Categories',
        queryset=Category.objects.all(),
        required = False
    )
    country = forms.ModelChoiceField(
        label=u'Country',
        queryset=Country.objects.all(),
        required = False
    )

    industry = forms.CharField(
        label=u'Industries',
        widget=forms.TextInput(attrs={'size': 20}),
        required = False
    )
    technology = forms.CharField(
        label=u'Technologies',
        widget=forms.TextInput(attrs={'size': 20}),
        required = False
    )
    
class ContactSearchForm(forms.Form):
    keywords = forms.CharField(
        label=u'Keywords',
        widget=forms.TextInput(attrs={'size': 20} ),
                required = False
    )
    overview = forms.CharField(
        label=u'Keywords',
        widget=forms.TextInput(attrs={'size': 20} ),
                required = False
    )
    tags = forms.CharField(
        label=u'Keywords',
        widget=forms.TextInput(attrs={'size': 20} ),
                required = False
    )

    industry = forms.CharField(
        label=u'Industries',
        widget=forms.TextInput(attrs={'size': 20}),
        required = False
    )
    technology = forms.CharField(
        label=u'Technologies',
        widget=forms.TextInput(attrs={'size': 20}),
        required = False
    )


