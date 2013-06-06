from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from company_profile_extended.views import *
#from company_profile_extended.models import *

urlpatterns = patterns('',


#     url(r'^(?P<slug>[\w-]+)/revenues/new/$','company_profile_extended.views.revenue_create'),
#     url(r'^(?P<slug>[\w-]+)/revenues/(?P<id>[\d]+)/update/$','company_profile_extended.views.revenue_update'),
     url(r'^(?P<slug>[\w-]+)/revenues/(?P<id>[\d]+)/delete/$','company_profile_extended.views.revenue_delete'),
#     url(r'^(?P<slug>[\w-]+)/revenues/(?P<id>[\d]+)/$','company_profile_extended.views.revenue_view'),


#     url(r'^(?P<slug>[\w-]+)/products/new/$','company_profile_extended.views.product_create'),
#     url(r'^(?P<slug>[\w-]+)/products/(?P<id>[\d]+)/update/$','company_profile_extended.views.product_update'),
     url(r'^(?P<slug>[\w-]+)/products/(?P<id>[\d]+)/delete/$','company_profile_extended.views.product_delete'),
#     url(r'^(?P<slug>[\w-]+)/products/(?P<id>[\d]+)/$','company_profile_extended.views.product_view'),

     #url(r'^(?P<slug>[\w-]+)/project/new/$','company_profile_extended.views.project_create'),
	 #url(r'^(?P<slug>[\w-]+)/project/(?P<id>[\d]+)/update/$','company_profile_extended.views.project_update'),
     url(r'^(?P<slug>[\w-]+)/projects/(?P<id>[\d]+)/delete/$','company_profile_extended.views.project_delete'),
     #url(r'^(?P<slug>[\w-]+)/project/(?P<id>[\d]+)/$','company_profile_extended.views.project_view'),

     #url(r'^(?P<slug>[\w-]+)/expertises/new/$','company_profile_extended.views.expertise_create'),
     #url(r'^(?P<slug>[\w-]+)/expertises/(?P<id>[\d]+)/update/$','company_profile_extended.views.expertise_update'),
     url(r'^(?P<slug>[\w-]+)/expertises/(?P<id>[\d]+)/delete/$','company_profile_extended.views.expertise_delete'),
     #url(r'^(?P<slug>[\w-]+)/expertises/(?P<id>[\d]+)/$','company_profile_extended.views.expertise_view'),

     #url(r'^(?P<slug>[\w-]+)/stories/new/$','company_profile_extended.views.story_create'),
     #url(r'^(?P<slug>[\w-]+)/stories/(?P<id>[\d]+)/update/$','company_profile_extended.views.story_update'),
     url(r'^(?P<slug>[\w-]+)/stories/(?P<id>[\d]+)/delete/$','company_profile_extended.views.story_delete'),
     #url(r'^(?P<slug>[\w-]+)/stories/(?P<id>[\d]+)/$','company_profile_extended.views.story_view'),

     #url(r'^(?P<slug>[\w-]+)/associations/new/$','company_profile_extended.views.association_create'),
     #url(r'^(?P<slug>[\w-]+)/associations/(?P<id>[\d]+)/update/$','company_profile_extended.views.association_update'),
     url(r'^(?P<slug>[\w-]+)/associations/(?P<id>[\d]+)/delete/$','company_profile_extended.views.association_delete'),
     #url(r'^(?P<slug>[\w-]+)/associations/(?P<id>[\d]+)/$','company_profile_extended.views.association_view'),

     #url(r'^(?P<slug>[\w-]+)/alliances/new/$','company_profile_extended.views.alliance_create'),
     #url(r'^(?P<slug>[\w-]+)/alliances/(?P<id>[\d]+)/update/$','company_profile_extended.views.alliance_update'),
     url(r'^(?P<slug>[\w-]+)/alliances/(?P<id>[\d]+)/delete/$','company_profile_extended.views.alliance_delete'),
     #url(r'^(?P<slug>[\w-]+)/alliances/(?P<id>[\d]+)/$','company_profile_extended.views.alliance_view'),


     #url(r'^(?P<slug>[\w-]+)/verticals/new/$','company_profile_extended.views.vertical_create'),
     #url(r'^(?P<slug>[\w-]+)/verticals/(?P<id>[\d]+)/update/$','company_profile_extended.views.vertical_update'),
     url(r'^(?P<slug>[\w-]+)/verticals/(?P<id>[\d]+)/delete/$','company_profile_extended.views.vertical_delete'),
     #url(r'^(?P<slug>[\w-]+)/verticals/(?P<id>[\d]+)/$','company_profile_extended.views.vertical_view'),


     #url(r'^(?P<slug>[\w-]+)/partnerships/new/$','company_profile_extended.views.partnership_create'),
     #url(r'^(?P<slug>[\w-]+)/partnerships/(?P<id>[\d]+)/update/$','company_profile_extended.views.partnership_update'),
     url(r'^(?P<slug>[\w-]+)/partnerships/(?P<id>[\d]+)/delete/$','company_profile_extended.views.partnership_delete'),
     #url(r'^(?P<slug>[\w-]+)/partnerships/(?P<id>[\d]+)/$','company_profile_extended.views.partnership_view'),


     #url(r'^(?P<slug>[\w-]+)/milestones/new/$','company_profile_extended.views.milestone_create'),
     #url(r'^(?P<slug>[\w-]+)/milestones/(?P<id>[\d]+)/update/$','company_profile_extended.views.milestone_update'),
     url(r'^(?P<slug>[\w-]+)/milestones/(?P<id>[\d]+)/delete/$','company_profile_extended.views.milestone_delete'),
     #url(r'^(?P<slug>[\w-]+)/milestones/(?P<id>[\d]+)/$','company_profile_extended.views.milestone_view'),


)
