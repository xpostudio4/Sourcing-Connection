from django.conf.urls import patterns, include, url
from latech.views import search_page
from latech.views import ProfileView, ProfileUpdate, CompanyUpdate, CompanyCreate, CompanyView, SelfProfileView, search_page, CompanyList
from latech.views import search_page
from django.views.generic import DetailView, ListView, UpdateView
from django.contrib.auth.decorators import login_required
from companies.models import *

# Uncomment the next two lines to enable the admin:

from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:e
    # url(r'^$', 'latech.views.home', name='home'),
    # url(r'^latech/', include('latech.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^$', "latech.views.base"),
     #url(r'^tagit', "latech.views.tagit"),

#     url(r'^contact/new/$', 'latech.views.contact_form'), 
     
     # Company URLs
     url(r'^company/new/$', CompanyCreate.as_view(), name='company_create'),
#     url(r'^company/(\w+)/$', 'latech.views.company_page'),
     url(r'^company/(?P<slug>[\w-]+)/update/$', CompanyUpdate.as_view(), name='company_update'),
     url(r'^company/(?P<slug>[\w-]+)/$', CompanyView.as_view(), name='company_view'),
     url(r'^companies/$', CompanyList.as_view(), name='company_list'),


     # Profile
     url(r'^profile/(?P<pk>[\w-]+)/$', ProfileView.as_view(), name='profile_view'),
     url(r'^profile/self/$', login_required(SelfProfileView.as_view()), name='profile_self_view'),
#     url(r'^profile/(\w+)/$', 'latech.views.user_prof'),
#     url(r'^profile/(\w+)/edit/$', 'latech.views.contact_edit'),  
     url(r'^profile/(?P<pk>[\w-]+)/edit/$', ProfileUpdate.as_view(), name='profile_update'),
     url(r'^login/$', 'django.contrib.auth.views.login'),
     url(r'^logout/$', 'latech.views.logout_page'),

     # Search Urls
     url(r'^search/', 'latech.views.search_page'),

     #This is the url for Ajax requests for taggit
     #url(r'^tags', "latech.views.tagitt"),
     url(r'^admin/', include(admin.site.urls)),

 
)


