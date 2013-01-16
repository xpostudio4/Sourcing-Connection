from django.forms import ModelForm
from contacts.models import *

class ContactForm(ModelForm):
    class Meta:
       model = Contact
       exclude = ('user', 'slug', )

