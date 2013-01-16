from django.template import RequestContext, Context
from django.shortcuts import render_to_response, get_object_or_404
from contacts.models import *
from contacts.forms import *
from django.views.generic import DetailView, ListView, UpdateView, CreateView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ProfileCreate(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact_form.html'
    success_url = ('/') 
#    success_url = ('/contact/%s/' % str(slug.user)) 

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfileCreate, self).dispatch(*args, **kwargs)

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


