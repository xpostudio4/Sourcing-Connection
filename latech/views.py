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
    if request.POST:
        company_form = CompanyForm(request.POST)
        if company_form.is_valid():
            company_form.save()
    else:
        company_form = CompanyForm()
    return render_to_response('company_form.html', {'company_form': company_form },context_instance=RequestContext(request)) 

@login_required
def contact_form(request, username):
    if request.POST:
        contact_form = ContactForm(request.POST, instance=User.objects.get(username=request.user))
        if contact_form.is_valid():
            contact_form.save()
    else:
        contact_form = ContactForm()
    return render_to_response('contact_form.html', {'contact_form': contact_form, 'username':username },context_instance=RequestContext(request)) 

@login_required
def contact_edit(request, username):
    if company_name == '':
        companysub = Company()
    else:
        companysub = Company.objects.get(name=company_name)
    if request.method == 'POST':
        company_form = CompanyForm(request.POST, instance=companysub)
        if company_form.is_valid():
            company_form.save()
            return HttpResponseRedirect('/company/'+company_name)
    else:
        company_form = CompanyForm(instance = companysub)
    return render_to_response('company_form.html', context_instance=RequestContext(request, {'company_form': company_form })) 
    return render_to_response('contact_form.html', {'contact_form': contact_form, 'username':username },context_instance=RequestContext(request)) 

def contact_edit(request, username):
    if request.POST:
        contact_form = ContactForm(request.POST, instance=User.objects.get(username=request.user))
        if contact_form.is_valid():
            contact_form.save()
    else:
        contact_form = ContactForm()
    return render_to_response('contact_form.html', {'contact_form': contact_form, 'username':username },context_instance=RequestContext(request)) 


def user_prof(request, username):
    user = User.objects.get(username=username)
    uc = get_object_or_404(Contact)
    variables = RequestContext(request,{
        'contact':uc,
        })
    return render_to_response('user_page.html', variables) 

def company_page(request, name):
    try:
       comp = Company.objects.get(name=name)
    except Company.DoesNotExist:
       raise Http404
    return render_to_response('company_page.html',{'comp':comp},context_instance=RequestContext(request)) 

@login_required
def company_edit(request, company_name):
    if company_name == '':
        companysub = Company()
    else:
        companysub = Company.objects.get(name=company_name)
    if request.method == 'POST':
        company_form = CompanyForm(request.POST, instance=companysub)
        if company_form.is_valid():
            company_form.save()
            return HttpResponseRedirect('/company/'+company_name)
    else:
        company_form = CompanyForm(instance = companysub)
    return render_to_response('company_form.html', context_instance=RequestContext(request, {'company_form': company_form })) 

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

