from django.template import RequestContext, Context
from django.shortcuts import render_to_response, get_object_or_404
from contacts.models import *
from contacts.forms import *
from django.views.generic import DetailView, ListView, UpdateView, CreateView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from latech import settings

class ProfileCreate(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact_form.html'
    success_url = ('/') 
#    success_url = ('/contact/%s/' % str(slug.user)) 

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfileCreate, self).dispatch(*args, **kwargs)


@login_required
def profile_view(request, id):
    
    contact = get_object_or_404(Contact,id=id)

    if request.user :
        user_id = request.user.id 

    
    contacts = Contact.objects.filter(id=id)
    contacts_urls = Contact_Urls.objects.filter(latech_contact=contact)
   

    return render_to_response(
        "user_page.html",
        {'contacts':contacts, 'contacts_urls':contacts_urls},
        context_instance=RequestContext(request))


class ProfileView(DetailView):
    model = Contact
    template_name = 'user_page.html'

    def get(self, request, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['urls'] = Contact_Urls.objects.filter(latech_contact=self.object)
        return self.render_to_response(context)


class ProfileUpdate(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact_form.html'
    success_url = '/'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfileUpdate, self).dispatch(*args, **kwargs)


class ContactUrlUpdate(UpdateView):
    model = Contact_Urls
    form_class = ContactUrlForm
    template_name = 'contact_url_form.html'
    success_url = ('/') 


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ContactUrlUpdate, self).dispatch(*args, **kwargs)

