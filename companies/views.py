from django.template import RequestContext, Context
from django.shortcuts import render_to_response, get_object_or_404
from companies.models import *
from companies.forms import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView, UpdateView, CreateView, ListView

class CompanyCreate(CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'company_form.html'
    success_url = '/company/%(slug)s/'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CompanyCreate, self).dispatch(*args, **kwargs)
    
class CompanyView(DetailView):
    queryset = Company.objects.all()
    template_name = 'company_page.html'
#    success_url = '/company/%(slug)s/'

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

def company_page(request, slug):
    try:
       comp = Company.objects.get(slug=slug)
    except Company.DoesNotExist:
       raise Http404
    return render_to_response('company_page.html',{'comp':comp},context_instance=RequestContext(request)) 


