import operator
from django.utils import simplejson
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, Context
from django.shortcuts import render_to_response, get_object_or_404
from taxonomy.models import *
from companies.models import *
from contacts.models import *
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from latech.forms import SearchForm, CompanySearchForm, ContactSearchForm
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
import requests
from bs4 import BeautifulSoup

def tagit(request):
   tags = Tag.objects.all()
   result = []
   result = [x.name for x in tags]
   f = simplejson.dumps(result)
   return render_to_response("tagit.html", {'f':f},context_instance=RequestContext(request))

def base(request):
   return render_to_response("index.html",{'user': request.user}, 
context_instance=RequestContext(request))

#Used to obtain the list of tags as a Ajax request returns a Json Array
#def tagsplete(request):
#   tags = Tag.objects.filter(name__istartswith=request.REQUEST['term'])
#   results = []
#   for tag in tags:
#      tag_dict = {'id':tag.id, 'label':tag.name, 'value':tag.name}
#      results.append(tag_dict)
#   return HttpResponse(simplejson.dumps(results),mimetype='application/json')

def tagitt(request):
   tags = Tag.objects.all()
   result = []
   result = [x.name for x in tags]
   return HttpResponse(simplejson.dumps(result),mimetype='application/json')

def file_not_found_404(request):
    return render_to_response('404.html',context_instance=RequestContext(request))


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

def authenticationView(request):
  username = request.POST['username']
  password = request.POST['password']
  user = authenticate(username = username, password = password)
  if user is not None:
    if user.is_active:
      login(request,user)
  else:
    return HttpResponseRedirect('/')

  
  return HttpResponseRedirect('/')



def hacked_news():
  """Steals the info from Hacker News to use in our demo"""
  r = requests.get("http://news.ycombinator.com/")
  webpage = BeautifulSoup(r.text)

  pub_table = webpage.find_all('table')[2]
  link_collection = pub_table.select('.title')

  users = pub_table.select('a[href^="user?id="]')
  for  i in range(0, len(users)):
    users[i] = users[i].contents[0]

  array_links = []

  for i in link_collection:
    if str(i.a) != 'None' :
      array_links.append({'url': str(i.a['href']), 'text': i.a.text})


  for i in range(0, len(users)):
     array_links[i]["user"] = users[i]

  for i in range(0, len(array_links)):
     array_links[i]["id"] = 1+i

  array_links.pop()
  return array_links

