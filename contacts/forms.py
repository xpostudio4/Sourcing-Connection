from django.forms import ModelForm
from contacts.models import *
from django import forms

class ContactForm(ModelForm):
    class Meta:
       model = Contact
       exclude = ('user', 'slug', )

