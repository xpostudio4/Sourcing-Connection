from django.conf.urls import patterns, include, url
#from latech.views import search_page, advance_company_search
#from latech.search import advance_contact_search, advance_company_search
from companies.views import CompanyUpdate, CompanyCreate, CompanyView, CompanyList
from django.views.generic import DetailView, ListView, UpdateView
from django.contrib.auth.decorators import login_required
from contacts.views import ProfileView, ProfileUpdate, ProfileCreate
#from companies.models import *

# Uncomment the next two lines to enable the admin:

from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
     # Company URLs

     url(r'^company/new/$', 'companies.views.CompanyCreate'),
#     url(r'^company/(\w+)/$', 'latech.views.company_page'),
     url(r'^company/(?P<slug>[\w-]+)/update/$', CompanyUpdate.as_view(), name='company_update'),
     url(r'^company/(?P<slug>[\w-]+)/$', CompanyView.as_view(), name='company_view'),
     url(r'^companies/$', CompanyList.as_view(), name='company_list'),

     # Profile
     url(r'^profile/(?P<pk>[\w-]+)/$', ProfileView.as_view(), name='profile_view'),
     url(r'^profile/(?P<pk>[\w-]+)/edit/$', ProfileUpdate.as_view(), name='profile_update'),

      # This is the Form to create a new Contact/Profile
#     url(r'^profile/(?P<pk>[\w-]+)/create/$', ProfileCreate.as_view(), name='profile_update'),
     url(r'^login/$', 'latech.views.authenticationView'),
     url(r'^logout/$', 'latech.views.logout_page'),

     # Search Urls
     url(r'^search/$', 'latech.search.search_page'),
     url(r'^$', "latech.search.advanced_search"),

#     url(r'^advance_search/', 'latech.views.advance_search'),
#     url(r'^$', "latech.search.advance_contact_search"),
#     url(r'^search/companies$', "latech.search.advance_company_search"),

     #This is the url for Ajax requests for taggit
     #url(r'^tags', "latech.views.tagitt"),
     url(r'^admin/', include(admin.site.urls)),

 
)


