from django.utils import simplejson
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, Context
from django.shortcuts import render_to_response
from taxonomy.models import Tag
from companies.models import *
from django.contrib.auth.models import User
from django.contrib.auth import logout

#def index(request):
def tagit(request):
   tags = Tag.objects.all()
   result = []
   result = [x.name for x in tags]
   f = simplejson.dumps(result)
   return render_to_response("tagit.html", {'f':f},context_instance=RequestContext(request))

def base(request):
   return render_to_response("index.html",context_instance=RequestContext(request))
 
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
    f_a = {}
    if request.POST:
       f_a['data'] = request.POST
       if cf.is_valid():
          cfs = cf.save(commit=True)

    cf = CompanyForm(**f_a)
    if cf.is_valid():
       cfs = cf.save(commit=True)
    return render_to_response('company_form.html', {'cf': cf },context_instance=RequestContext(request)) 

def user_prof(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404(u'Requested user not found.')
 #   bookmarks = user.bookmark_set.all()
    variables = Context({
        'username': username,
#        'bookmarks': bookmarks
        })
    return render_to_response('user_page.html', {'username': username,  },context_instance=RequestContext(request)) 

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

