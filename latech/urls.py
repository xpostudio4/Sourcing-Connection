from django.conf.urls import patterns, include, url, handler404
from latech.views import file_not_found_404, CompanyUpdate, CompanyCreate
from django.views.generic import DetailView, ListView, UpdateView

# Uncomment the next two lines to enable the admin:

from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'latech.views.home', name='home'),
    # url(r'^latech/', include('latech.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^$', "latech.views.base"),
     url(r'^tagit', "latech.views.tagit"),

     url(r'^contact/new/$', 'latech.views.contact_form'), 
     
     #Company URLs
     url(r'^company/new/$', CompanyCreate.as_view(), name='company_create'),
     url(r'^company/(\w+)/$', 'latech.views.company_page'),
#     url(r'^company/(\w+)/edit/$', 'latech.views.company_edit'),
     url('^company/(?P<slug>[\w-]+)/update/$', CompanyUpdate.as_view(), name='company_update'),


     url(r'^profile/(\w+)/$', 'latech.views.user_prof'),
     url(r'^profile/(\w+)/edit/$', 'latech.views.contact_edit'),  
     url(r'^login/$', 'django.contrib.auth.views.login'),
     url(r'^logout/$', 'latech.views.logout_page'),

     #url(r'^profile/<user>/edit$', 'latech.views.company_form'),
     #url(r'^profile/new/$', 'latech.views.company_form'),
     url(r'^tags', "latech.views.tagitt"),
     url(r'^admin/', include(admin.site.urls)),
 
)

handler404 = 'latech.views.file_not_found_404'


