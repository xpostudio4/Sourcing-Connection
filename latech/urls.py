from django.conf.urls import patterns, include, url
from companies.views import CompanyCreate,  CompanyList
from django.views.generic import DetailView, ListView, UpdateView
from django.contrib.auth.decorators import login_required
from contacts.views import ProfileView, ProfileUpdate, ProfileCreate
import settings
#from companies.models import *

# Uncomment the next two lines to enable the admin:

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     # Company URLs

     url(r'^company/new/$', 'companies.views.CompanyCreate'),
#     url(r'^company/(\w+)/$', 'latech.views.company_page'),
     url(r'^company/(?P<slug>[\w-]+)/update/$','companies.views.company_update'),
     url(r'^company/(?P<slug>[\w-]+)/$','companies.views.company_view'),
     url(r'^companies/$', CompanyList.as_view(), name='company_list'),
     #Loading Companies from the CSV file
     url(r'^companies/load/$', 'latech.views.load_company'),


     # Profile
     url(r'^profile/(?P<pk>[\w-]+)/$', ProfileView.as_view(), name='profile_view'),
     url(r'^profile/(?P<pk>[\w-]+)/edit/$', ProfileUpdate.as_view(), name='profile_update'),

      # This is the Form to create a new Contact/Profile
#     url(r'^profile/(?P<pk>[\w-]+)/create/$', ProfileCreate.as_view(), name='profile_update'),
     url(r'^login/$', 'latech.views.authentication_view'),
     url(r'^logout/$', 'latech.views.logout_page'),

     # Search Urls
     url(r'^search/$', 'latech.search.search_page'),
     url(r'^$', "latech.search.advanced_search"),

     #Tickets for site reports
     url(r'ticket/$','latech.views.ticket_create'),
     url(r'create/$','latech.views.asana_create'),

#     url(r'^advance_search/', 'latech.views.advance_search'),
#     url(r'^$', "latech.search.advance_contact_search"),
#     url(r'^search/companies$', "latech.search.advance_company_search"),

     #This is the url for Ajax requests for taggit
     #url(r'^tags', "latech.views.tagitt"),
     url(r'^admin/', include(admin.site.urls)),
 
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )
