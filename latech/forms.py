from django.forms import ModelForm
from django import forms
from companies.models import *
from contacts.models import *
from location.models import *
from django.contrib.auth.models import User 

class SearchForm(forms.Form):
    query = forms.CharField(
        label=u'Enter a keyword to search for',
        widget=forms.TextInput(attrs={'size': 20})
    )

class CompanySearchForm(forms.Form):
    keywords = forms.CharField(
        label=u'Keywords',
        widget=forms.TextInput(attrs={'size': 20, 'placeholder': "For all the companies use *"} ),
                required = False
    )
    category_company = forms.ModelChoiceField(
        label=u'Categories',
        queryset=Category.objects.all(),
        required = False
    )
    country_company = forms.ModelChoiceField(
        label=u'Country',
        queryset=Country.objects.all(),
        required = False
    )

    industry_company = forms.CharField(
        label=u'Industries',
        widget=forms.TextInput(attrs={'size': 20}),
        required = False
    )
    technology_company = forms.CharField(
        label=u'Technologies',
        widget=forms.TextInput(attrs={'size': 20}),
        required = False
    )
    
class ContactSearchForm(forms.Form):
    terms = forms.CharField(
        label=u'Keywords',
        widget=forms.TextInput(attrs={'size': 20} ),
                required = False
    )
    overview = forms.CharField(
        label=u'Overview',
        widget=forms.TextInput(attrs={'size': 20} ),
                required = False
    )
    tags = forms.CharField(
        label=u'Tags',
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

class UserForm(forms.ModelForm):
    class Meta:
        model = User

        fields = ('username', 'password')
        action="login"

