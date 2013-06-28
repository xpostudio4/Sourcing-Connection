from django.forms import ModelForm
from django import forms
from companies.models import *
from contacts.models import *
from location.models import *
from django.contrib.auth.models import User 

BROWSER = (
    ("Chrome","Chrome" ),
    ("Firefox","Firefox"),
    ("Safari","Safari"),
    ("Internet Explorer","Internet Explorer"),
    ("Opera","Opera"),
    )

class SearchForm(forms.Form):

    query = forms.CharField(
        label=u"",
        widget=forms.TextInput(attrs={'size': 20, 'placeholder':'Enter a keyword to search for',})
    )

class CompanyStatusForm(forms.Form):
    company_status = forms.TypedChoiceField(
        label=u'GTB Status',
        empty_value='Nada', 
        choices=Company.COMPANY_STATUS_CHOICES,
        required = False
    )

class CompanySearchForm(forms.Form):
    keywords = forms.CharField(
        label=u'Keywords',
        widget=forms.TextInput(attrs={'size': 20, 'placeholder': "For all the companies use *"} ),
                required = False
    )
    category_company = forms.ModelChoiceField(
        label=u'Industry',
        queryset=Category.objects.all(),
        empty_label = "Any",
        required = False
    )
    country_company = forms.ModelChoiceField(
        label=u'Country',
        queryset=Country.objects.all(),
        empty_label = "Any",
        required = False
    )

    vertical_company = forms.CharField(
        label=u'Verticals',
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


class TicketForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class':"input-xlarge",'size': 20})
        )
    name = forms.CharField(
        label=u'Brief description of the Bug:',
        widget=forms.TextInput(attrs={'class':"input-xlarge",'size': 20 })
        )
    browser = forms.TypedChoiceField(
        label=u'Which Browser where You using',
        choices=BROWSER,
        widget=forms.RadioSelect(attrs={'class':"input-xlarge",'size': 20 })
        )
    url = forms.URLField(
        label=u'Url where the error happened:',
        widget=forms.TextInput(attrs={'class':"input-xlarge",'size': 20 })
        )
    error = forms.CharField(
        label=u'What We need to do to reproduce the error',
        widget=forms.Textarea(attrs={'class':"input-xlarge",'size':20})
        )
    expectation = forms.CharField(
        label=u'What You were expecting when doing that action',
        widget=forms.Textarea(attrs={'class':"input-xlarge",'size':20})
        )
    actual = forms.CharField(
        label=u'What error presented the application',
        widget=forms.Textarea(attrs={'class':"input-xlarge",'size':20})
        )

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
