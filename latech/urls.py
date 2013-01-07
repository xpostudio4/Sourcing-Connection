from django.conf.urls import patterns, include, url

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
     url(r'^company/new/$', 'latech.views.company_form'),
     url(r'^profile/(\w+)/$', 'latech.views.user_prof'),
     url(r'^login/$', 'django.contrib.auth.views.login'),
     url(r'^logout/$', 'latech.views.logout_page'),

     #url(r'^profile/<user>/edit$', 'latech.views.company_form'),
     #url(r'^profile/new/$', 'latech.views.company_form'),
     url(r'^tags', "latech.views.tagitt"),
     url(r'^admin/', include(admin.site.urls)),
 
)
