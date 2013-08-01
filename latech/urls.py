from django.conf.urls import patterns, include, url
#from companies.views import CompanyCreate, CompanyList, CompaniesCreate, CompaniesUpdate
from django.views.generic import DetailView, ListView, UpdateView
from django.contrib.auth.decorators import login_required
from contacts.views import ProfileView, ProfileUpdate, ProfileCreate, ContactUrlUpdate
from events.views import EventListView, EventNewView
import settings
#from companies.models import *

# Uncomment the next two lines to enable the admin:

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     # Company URLs

     url(r'^company/new/$', 'companies.views.CompanyCreate'),
     #url(r'company/new/$', CompaniesCreate.as_view(), name='company_create'),
#     url(r'^company/(\w+)/$', 'latech.views.company_page'),
     url(r'^company/(?P<slug>[\w-]+)/update/$','companies.views.company_update'),
#     url(r'^company/(?P<slug>[\w-]+)/update/$',CompaniesUpdate.as_view(), name='company_update'),
     url(r'^company/(?P<slug>[\w-]+)/$','companies.views.company_view'),
     url(r'^company/(?P<slug>[\w-]+)/edit/$','latech.views_editable.company_edit'),
     url(r'^company/(?P<slug>[\w-]+)/edit2/$','latech.views_editable.company_edit2'),
     url(r'^company/(?P<slug>[\w-]+)/logo/$','latech.views_editable.company_logo'),

#     url(r'^companies/$', CompanyList.as_view(), name='company_list'),
     #Loading Companies from the CSV file
#     url(r'^companies/load/$','latech.views.load_company'),

     #Loading Countries information from the CSV file
     #url(r'^country/load/$','latech.views.load_countries_info'),

     #forms generators
      url(r'^forms/(?P<model>[\w-]+)/$','latech.views.form_create'),
      url(r'^forms/(?P<slug>[\w-]+)/(?P<model>[\w-]+)/$','latech.views.form_validation'),
      url(r'^name_verify/$','latech.views_editable.company_name_verification'),
      url(r'^contact/$', 'latech.views_editable.webmaster_contact'),
      url(r'^user_msg/$', 'latech.views_editable.webmaster'),
      url(r'^companies/name/$','latech.views_editable.company_name_redirect'),

     # Using X-Editable for Editing In-place

      url(r'^formfields/(?P<model>[\w-]+)/(?P<id>[\d]+)/(?P<field>[\w-]+)/$','latech.views_editable.form_fields'),
      url(r'^userfields/(?P<model>[\w-]+)/(?P<id>[\d]+)/(?P<field>[\w-]+)/$','latech.views_editable.user_form_fields'),


# TESTING PRODUCT IMAGE FIELDS
      url(r'^imagefields/(?P<model>[\w-]+)/(?P<id>[\d]+)/(?P<field>[\w-]+)/$','latech.views_editable.product_image_fields'),


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

    # Certification urls
     url(r'^company/(?P<slug>[\w-]+)/certifications/new/$','companies.views.certification_create'),
     url(r'^company/(?P<slug>[\w-]+)/certifications/(?P<id>[\d]+)/update/$','companies.views.certification_update'),
     url(r'^company/(?P<slug>[\w-]+)/certifications/(?P<id>[\d]+)/delete/$','companies.views.certification_delete'),
     url(r'^company/(?P<slug>[\w-]+)/certifications/(?P<id>[\d]+)/$','companies.views.certification_view'),

    # Awards urls
     url(r'^company/(?P<slug>[\w-]+)/awards/new/$','companies.views.award_create'),
     url(r'^company/(?P<slug>[\w-]+)/awards/(?P<id>[\d]+)/update/$','companies.views.award_update'),
     url(r'^company/(?P<slug>[\w-]+)/awards/(?P<id>[\d]+)/delete/$','companies.views.award_delete'),
     url(r'^company/(?P<slug>[\w-]+)/awards/(?P<id>[\d]+)/$','companies.views.award_view'),

    # Fundings urls
     url(r'^company/(?P<slug>[\w-]+)/fundings/new/$','companies.views.funding_create'),
     url(r'^company/(?P<slug>[\w-]+)/fundings/(?P<id>[\d]+)/update/$','companies.views.funding_update'),
     url(r'^company/(?P<slug>[\w-]+)/fundings/(?P<id>[\d]+)/delete/$','companies.views.funding_delete'),
     url(r'^company/(?P<slug>[\w-]+)/fundings/(?P<id>[\d]+)/$','companies.views.funding_view'),

     # Picture urls
     url(r'^company/(?P<slug>[\w-]+)/pictures/new/$','fileupload.views.picture_create'),
     url(r'^company/(?P<slug>[\w-]+)/pictures/(?P<id>[\d]+)/update/$','fileupload.views.picture_update'),
     url(r'^company/(?P<slug>[\w-]+)/pictures/(?P<id>[\d]+)/delete/$','fileupload.views.picture_delete'),
     url(r'^company/(?P<slug>[\w-]+)/pictures/(?P<id>[\d]+)/$','fileupload.views.picture_view'),
     url(r'^company/(?P<slug>[\w-]+)/logo/update/$','latech.views_editable.logo_update'),
     url(r'^company/(?P<slug>[\w-]+)/product_image/(?P<id>[\d]+)/update/$','latech.views_editable.product_image_update'),
     url(r'^company/(?P<slug>[\w-]+)/product_img/(?P<id>[\d]+)/update/$','latech.views_editable.product_picture'),

     # ManagerPicture urls
     url(r'^company/(?P<slug>[\w-]+)/management/(?P<pk>[\w-]+)/pictures/new/$','fileupload.views.managerpicture_create'),
#     url(r'^company/(?P<slug>[\w-]+)/pictures/(?P<id>[\d]+)/update/$','fileupload.views.picture_update'),
#     url(r'^company/(?P<slug>[\w-]+)/pictures/(?P<id>[\d]+)/delete/$','fileupload.views.picture_delete'),
     url(r'^profile/(?P<pk>[\d]+)/pictures/(?P<id>[\d]+)$','fileupload.views.mpicture_view'),


    # Acquisitions urls
     url(r'^company/(?P<slug>[\w-]+)/acquisitions/new/$','companies.views.acquisition_create'),
     url(r'^company/(?P<slug>[\w-]+)/acquisitions/(?P<id>[\d]+)/update/$','companies.views.acquisition_update'),
     url(r'^company/(?P<slug>[\w-]+)/acquisitions/(?P<id>[\d]+)/delete/$','companies.views.acquisition_delete'),
     url(r'^company/(?P<slug>[\w-]+)/acquisitions/(?P<id>[\d]+)/$','companies.views.acquisition_view'),

     # Customer urls
     url(r'^company/(?P<slug>[\w-]+)/customers/new/$','companies.views.customer_create'),
     url(r'^company/(?P<slug>[\w-]+)/customers/(?P<id>[\d]+)/update/$','companies.views.customer_update'),
     url(r'^company/(?P<slug>[\w-]+)/customers/(?P<id>[\d]+)/delete/$','companies.views.customer_delete'),
     url(r'^company/(?P<slug>[\w-]+)/customers/(?P<id>[\d]+)/$','companies.views.customer_view'),

     # Competitors urls
     url(r'^company/(?P<slug>[\w-]+)/competitors/new/$','companies.views.competitors_create'),
     url(r'^company/(?P<slug>[\w-]+)/competitors/(?P<id>[\d]+)/update/$','companies.views.competitors_update'),
     url(r'^company/(?P<slug>[\w-]+)/competitors/(?P<id>[\d]+)/delete/$','companies.views.competitors_delete'),
     url(r'^company/(?P<slug>[\w-]+)/competitors/(?P<id>[\d]+)/$','companies.views.competitors_view'),

     url(r'^company/(?P<slug>[\w-]+)/links/update/$','companies.views.companylink_update'),
     
     url(r'^excel/export/$','latech.search.export'),

     # Profile
     # url(r'^profile/(?P<pk>[\w-]+)/$', ProfileView.as_view(), name='profile_view'),
     url(r'^profile/(?P<id>[\d]+)/$', 'contacts.views.profile_view'),
     url(r'^profile/(?P<pk>[\w-]+)/urls$', ContactUrlUpdate.as_view()),
     url(r'^profile/(?P<pk>[\w-]+)/edit/$', ProfileUpdate.as_view(), name='profile_update'),

      # This is the Form to create a new Contact/Profile

     # url(r'^profile/(?P<pk>[\w-]+)/create/$', ProfileCreate.as_view(), name='profile_update'),

     url(r'^login/$', 'latech.views.authentication_view'),
     url(r'^logout/$', 'latech.views.logout_page'),
     url(r'^password/change/$', 'django.contrib.auth.views.password_change',{'post_change_redirect': '/'}),

     # Search Urls
     url(r'^search/$', 'latech.search.search_page'),
     url(r'^$', "latech.search.advanced_search"),

     #Tickets for site reports
     url(r'ticket/$','latech.views.ticket_create'),
     url(r'create/$','latech.views.asana_create'),

     # Reset the ID sequences for companylinks
     url(r'reset/$','latech.views.reset'),
     
     #django comment frameworks
     url(r'^comments/', include('django.contrib.comments.urls')),

     #news related functions
     url(r'^news/new/$', 'news.views.news_create'),
     url(r'^news/(?P<id>[\d]+)/$', 'news.views.news_view'),
     url(r'^news/(?P<id>[\d]+)/update/$', 'news.views.news_update'),
     url(r'^news/(?P<id>[\d]+)/delete$', 'news.views.news_delete'),

     # Events related URLs
     url(r'events/$', EventListView.as_view()),
     url(r'events/new$', EventNewView.as_view()),


     # URLs for industries and verticals
     url(r'^industry/(?P<slug>[\w-]+)/$', 'latech.views.categories'),
     url(r'^vertical/(?P<slug>[\w-]+)/$', 'latech.views.verticals'),

     

#     url(r'^advance_search/', 'latech.views.advance_search'),
#     url(r'^$', "latech.search.advance_contact_search"),
#     url(r'^search/companies$', "latech.search.advance_company_search"),

     #This is the url for Ajax requests for taggit url(r'^tags',
     #"latech.views.tagitt"),

    # URLs from Company Profile Extended
     url(r'^company/', include('company_profile_extended.urls')),

     url(r'^chaining/', include('smart_selects.urls')),

     url(r'^admin/', include(admin.site.urls)),
)
