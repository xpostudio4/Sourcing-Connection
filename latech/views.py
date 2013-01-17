import operator
from django.utils import simplejson
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, Context
from django.shortcuts import render_to_response, get_object_or_404
from taxonomy.models import *
from companies.models import *
from contacts.models import *
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from latech.forms import SearchForm, AdvanceSearchForm
from django.db.models import Q

def tagit(request):
   tags = Tag.objects.all()
   result = []
   result = [x.name for x in tags]
   f = simplejson.dumps(result)
   return render_to_response("tagit.html", {'f':f},context_instance=RequestContext(request))

def base(request):
   return render_to_response("index.html",{'user': request.user}, 
context_instance=RequestContext(request))

#Used to obtain the list of tags as a Ajax request returns a Json Array
#def tagsplete(request):
#   tags = Tag.objects.filter(name__istartswith=request.REQUEST['term'])
#   results = []
#   for tag in tags:
#      tag_dict = {'id':tag.id, 'label':tag.name, 'value':tag.name}
#      results.append(tag_dict)
#   return HttpResponse(simplejson.dumps(results),mimetype='application/json')

def tagitt(request):
   tags = Tag.objects.all()
   result = []
   result = [x.name for x in tags]
   return HttpResponse(simplejson.dumps(result),mimetype='application/json')

def file_not_found_404(request):
    return render_to_response('404.html',context_instance=RequestContext(request))

def search_page(request):
    form = SearchForm()
    company_list = []
    contact_list = []    
    show_results = False
    if 'query' in request.GET:
       show_results = True
       query = request.GET['query'].strip()
       if query:
           keywords = query.split()
           # Splitting Keywords for companies searchs
           for keyword in keywords:
               company_list = Company.objects.filter(
                   Q(name__icontains=keyword)|
                   Q(description__icontains=keyword)|
                   Q(technologies__icontains=keyword)|
                   Q(industries__icontains=keyword))[:10]
           # Splitting Keywords for contacts searchs
           for keyword2 in keywords:
               contact_list = Contact.objects.filter(
                   Q(fr_name__icontains=keyword2)|
                   Q(ls_name__icontains=keyword2)|
                   Q(m_name__icontains=keyword2)|
                   Q(overview__icontains=keyword2))[:10]
           form = SearchForm({'query': query})
    variables = RequestContext(request, {
        'form':form,    
        'company_list': company_list,
        'contact_list': contact_list,        
        'show_results': show_results
    })
    
#    return render_to_response('company_list.html', variables)
#    else:
    return render_to_response('search.html', variables)

def advance_company_search(request):
    company_form = AdvanceSearchForm()
    company_list = []
    errors = []
    show_results = False
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        category = request.GET['category']
        industry = request.GET['industry']
        technology = request.GET['technology']
        if not (keywords or industry or technology or category):
            errors.append('Enter a search term.')
        else:
            show_results = True

            company_list = Company.objects.filter(
                name__icontains=keywords
            ).filter(
                industries__icontains=industry
            ).filter(
                categories__name__icontains=category
            ).filter(
                technologies__icontains=technology
            )
            query = "Field 1: %s, Field 2: %s, Field 3: %s Field 4: %s" % (keywords, technology, industry, category)

            company_form = AdvanceSearchForm({
               'query': query,
            })
    variables = RequestContext(request, {
            'company_form':company_form,    
            'company_list': company_list,
            'show_results': show_results
             })
   
    return render_to_response('index.html', variables)

def advance_contact_search(request):
    contact_form = AdvanceSearchForm()
    contact_list = []
    errors = []
    show_results = False
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        category = request.GET['category']
        industry = request.GET['industry']
        technology = request.GET['technology']
        if not (keywords or industry or technology or category):
            errors.append('Enter a search term.')
        else:
            show_results = True

            company_list = Company.objects.filter(
                name__icontains=keywords
            ).filter(
                industries__icontains=industry
            ).filter(
                categories__name__icontains=category
            ).filter(
                technologies__icontains=technology
            )
            query = "Field 1: %s, Field 2: %s, Field 3: %s Field 4: %s" % (keywords, technology, industry, category)

            company_form = AdvanceSearchForm({
               'query': query,
            })
    variables = RequestContext(request, {
            'company_form':company_form,    
            'company_list': company_list,
            'show_results': show_results
             })
    return render_to_response('index.html', variables)

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

