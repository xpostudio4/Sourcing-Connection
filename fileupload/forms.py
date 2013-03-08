from fileupload.models import *
from django.forms import ModelForm

class PictureForm(ModelForm):
    class Meta:
       model = Picture
       exclude = ("company","slug")
