from django.forms import ModelForm
from contacts.models import *
from django import forms

class ContactForm(ModelForm):
    class Meta:
       model = Contact
       exclude = ('user', 'slug', 'latech_contact')

class ContactUrlForm(ModelForm):
    class Meta:
       model = Contact_Urls
       exclude = ('latech_contact' )
