from django.conf.urls import patterns, include, url
from companies.views import CompanyCreate, CompanyList, CompaniesCreate, CompaniesUpdate
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

#     url(r'^company/new/$', 'companies.views.CompanyCreate'),
     url(r'company/new/$', CompaniesCreate.as_view(), name='company_create'),
#     url(r'^company/(\w+)/$', 'latech.views.company_page'),
#     url(r'^company/(?P<slug>[\w-]+)/update/$','companies.views.company_update'),
     url(r'^company/(?P<slug>[\w-]+)/update/$',CompaniesUpdate.as_view(), name='company_update'),
     url(r'^company/(?P<slug>[\w-]+)/$','companies.views.company_view'),
     url(r'^companies/$', CompanyList.as_view(), name='company_list'),
     #Loading Companies from the CSV file
#     url(r'^companies/load/$','latech.views.load_company'),

     #Management for the item
     url(r'^company/(?P<slug>[\w-]+)/management/new/$','companies.views.management_create'),
     url(r'^company/(?P<slug>[\w-]+)/management/(?P<id>[\d]+)/update/$','companies.views.management_update'),
     url(r'^company/(?P<slug>[\w-]+)/management/(?P<id>[\d]+)/delete/$','companies.views.management_delete'),
     url(r'^company/(?P<slug>[\w-]+)/management/(?P<id>[\d]+)/$','companies.views.management_view'),

    #Office urls
     url(r'^company/(?P<slug>[\w-]+)/office/new/$','companies.views.office_create'),
     url(r'^company/(?P<slug>[\w-]+)/office/(?P<id>[\d]+)/update/$','companies.views.office_update'),
     url(r'^company/(?P<slug>[\w-]+)/office/(?P<id>[\d]+)/delete/$','companies.views.office_delete'),
     url(r'^company/(?P<slug>[\w-]+)/office/(?P<id>[\d]+)/$','companies.views.office_view'),

     #competitors urls
     url(r'^company/(?P<slug>[\w-]+)/competitors/new/$','companies.views.competitors_create'),
     url(r'^company/(?P<slug>[\w-]+)/competitors/(?P<id>[\d]+)/update/$','companies.views.competitors_update'),
     url(r'^company/(?P<slug>[\w-]+)/competitors/(?P<id>[\d]+)/delete/$','companies.views.competitors_delete'),
     url(r'^company/(?P<slug>[\w-]+)/competitors/(?P<id>[\d]+)/$','companies.views.competitors_view'),

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

     #ckeditor configuration Url

     #news related functions
     url(r'^news/new$', 'news.views.news_create'),

#     url(r'^advance_search/', 'latech.views.advance_search'),
#     url(r'^$', "latech.search.advance_contact_search"),
#     url(r'^search/companies$', "latech.search.advance_company_search"),

     #This is the url for Ajax requests for taggit
     #url(r'^tags', "latech.views.tagitt"),
     url(r'^admin/', include(admin.site.urls)),
 
)

