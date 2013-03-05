from news.models import Post
from django.forms import ModelForm
from django import forms


class PostForm(ModelForm):

	class Meta:
		model = Post
		fields= ("name", "url", "post") 
