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
from django.views.generic import DetailView, ListView, UpdateView, CreateView, ListView
from forms import SearchForm

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


class CompanyCreate(CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'company_form.html'
    success_url = '/company/%(slug)s/'

class ProfileCreate(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact_form.html'
    success_url = ('/') 
#    success_url = ('/contact/%s/' % str(slug.user)) 


class ProfileView(DetailView):
    model = Contact
    template_name = 'user_page.html'


class ProfileUpdate(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact_form.html'
    success_url = '/'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfileUpdate, self).dispatch(*args, **kwargs)

def file_not_found_404(request):
    return render_to_response('404.html',context_instance=RequestContext(request))

def user_prof(request, pk):
    profile = Contact.objects.get(user=pk)
    uc = get_object_or_404(Contact)
    variables = RequestContext(request,{
        'contact':uc,
        })
    return render_to_response('user_page.html', variables) 

def company_page(request, slug):
    try:
       comp = Company.objects.get(slug=slug)
    except Company.DoesNotExist:
       raise Http404
    return render_to_response('company_page.html',{'comp':comp},context_instance=RequestContext(request)) 

class CompanyView(DetailView):
    queryset = Company.objects.all()
    template_name = 'company_page.html'
#    success_url = '/company/%(slug)s/'

class ProfileView(DetailView):
    model = Contact
    template_name = 'user_page.html'

#    def get_context_data(self, **kwargs)
#        context = super.(ProfileView, self).get_context_data(**kwargs)
#        return context

class SelfProfileView(ProfileView):
    def get_object(self):
        return self.request.user

class CompanyUpdate(UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'company_form.html'
    success_url = '/company/%(slug)s/'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CompanyUpdate, self).dispatch(*args, **kwargs)

class CompanyList(ListView):
    model = Company
    template_name = 'company_list.html'    


def search_page(request):
    form = SearchForm()
    company_list = []
    show_results = False
    if 'query' in request.GET:
       show_results = True
       query = request.GET['query'].strip()
       if query:
           form = SearchForm({'query': query})
           company_list = Company.objects.filter(name__icontains=query)[:10]
    variables = RequestContext(request, {
        'form':form,    
        'company_list': company_list,
        'show_results': show_results
    })
#    return render_to_response('company_list.html', variables)
#    else:
    return render_to_response('search.html', variables)

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

