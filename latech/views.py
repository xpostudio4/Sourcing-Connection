from django.utils import simplejson
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, Context
from django.shortcuts import render_to_response, get_object_or_404
from taxonomy.models import *
from companies.models import *
from contacts.models import *
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

#def index(request):
def tagit(request):
   tags = Tag.objects.all()
   result = []
   result = [x.name for x in tags]
   f = simplejson.dumps(result)
   return render_to_response("tagit.html", {'f':f},context_instance=RequestContext(request))

def base(request):
   
   return render_to_response("index.html",{'user': request.user}, 
context_instance=RequestContext(request))
 
#def tag_array(request):
#def tagit(request):
def nana(request):
   tags = Tag.objects.all()
   f = "["
   for tag  in tags:
     f+= "'"+tag.name+"',"
   f = f[:-1]
   f = f+"]"
   return render_to_response("tagit.html", {'f':f},context_instance=RequestContext(request))

#def tagsplete(request):
## Vieja
#    out = ["hola", "mundo", "adios", "universo"]
#    return HttpResponse(simplejson.dumps(out))
#    result = []
#    if 'q' in request.GET:
#        tags = Tag.objects.filter(name__istartswith=request.GET['q'])[:10]
#        result = [name for x in tags ]
##        return HttpResponse(u'\n'.join(tag.name for tag in tags))
#    tags = Tag.objects.all()
#    result = [x.name for x in tags]
#    json = simplejson.dumps(result)
#    return HttpResponse(json, mimetype="application/json")
#def venue_lookup(request):
def tagsplete(request):
   tags = Tag.objects.filter(name__istartswith=request.REQUEST['term'])
   results = []
   for tag in tags:
      tag_dict = {'id':tag.id, 'label':tag.name, 'value':tag.name}
      results.append(tag_dict)
   return HttpResponse(simplejson.dumps(results),mimetype='application/json')

def tagitt(request):
   tags = Tag.objects.all()
   result = []
   result = [x.name for x in tags]
   return HttpResponse(simplejson.dumps(result),mimetype='application/json')

def company_form(request):
#    f_a = {}
    if request.POST:
        cf = CompanyForm(request.POST)
        if cf.is_valid():
            cf.save()
    else:
        cf = CompanyForm()
 #      f_a['data'] = request.POST
#       if cf.is_valid():
#          cfs = cf.save(commit=True)
#
#    cf = CompanyForm(**f_a)
#    if cf.is_valid():
#       cfs = cf.save(commit=True)
    return render_to_response('company_form.html', {'cf': cf },context_instance=RequestContext(request)) 

@login_required
def contact_form(request, username):
    if request.POST:
        cof = ContactForm(request.POST, instance=User.objects.get(username=request.user))
        if cof.is_valid():
            cof.save()
    else:
        cof = ContactForm()
    return render_to_response('contact_form.html', {'cof': cof, 'username':username },context_instance=RequestContext(request)) 

def user_prof(request, username):
    user = User.objects.get(username=username)
    uc = get_object_or_404(Contact)
    variables = RequestContext(request,{
        'contact':uc,
        })
    return render_to_response('user_page.html', variables) 
 

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

