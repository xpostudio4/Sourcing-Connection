import operator
from django.utils import simplejson
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, Context
from django.shortcuts import render_to_response, get_object_or_404
from taxonomy.models import *
from companies.models import *
from contacts.models import *
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from latech.forms import SearchForm, CompanySearchForm, ContactSearchForm
from django.db.models import Q

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

