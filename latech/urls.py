from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
<<<<<<< HEAD
from django.contrib import admin
admin.autodiscover()
=======
# from django.contrib import admin
# admin.autodiscover()
>>>>>>> f79c379fecd923f54e3f45b1a3c20c86ae84105e

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'latech.views.home', name='home'),
    # url(r'^latech/', include('latech.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
<<<<<<< HEAD
     
     url(r'^admin/', include(admin.site.urls)),
=======
    # url(r'^admin/', include(admin.site.urls)),
>>>>>>> f79c379fecd923f54e3f45b1a3c20c86ae84105e
)
