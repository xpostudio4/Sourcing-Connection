# Create your views here.
from news.forms import PostForm
from news.models import Post
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext, Context

def news_create(request):

		if request.method == 'GET':
			post_form = PostForm()

			return render_to_response('news_form.html', {'form': post_form,}, context_instance=RequestContext(request))


