from latech.forms import SearchForm, CompanySearchForm, ContactSearchForm
from django.template import RequestContext, Context
from django.shortcuts import render_to_response
from taxonomy.models import *
from companies.models import *
from contacts.models import *
from django.db.models import Q

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

def empty_search_form():
    contact_form = ContactSearchForm()
    company_form = CompanySearchForm()
    return contact_form, company_form

def advanced_search(request):
    contact_form, company_form = empty_search_form()
    contact_list = []
    company_list = []
    errors = []
    show_results = False
    if 'keywords' in request.GET:
        keywords = request.GET['keywords'].strip()
        category = request.GET['category']
        if keywords or category:
            show_results = True
            company_list = Company.objects.filter(
                Q(name__icontains=keywords))
            query1 = "Field 1: %s" % (keywords)
            company_form = CompanySearchForm({'query1': query1})

    if 'keywords' in request.GET:
        keywords = request.GET['keywords'].strip()
        if keywords:
            show_results = True
            contact_list = Contact.objects.filter(
                Q(fr_name__icontains=keywords))
            query2 = "Field 1: %s" % (keywords)
            contact_form = CompanySearchForm({'query2': query2})
           
    variables = RequestContext(request, {
        'company_form': company_form,
        'contact_form': contact_form,
        'company_list': company_list,
        'contact_list': contact_list,        
        'show_results': show_results
    })
    return render_to_response('index.html', variables)
            
def advance_contact_search(request):
    contact_form = ContactSearchForm()
    contact_list = []
    errors = []
    show_results = False
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        tags = request.GET['tags']
        industry = request.GET['industry']
        technology = request.GET['technology']
        if not (keywords or industry or technology or tags):
            errors.append('Enter a search term.')
        else:
            show_results = True
            contact_list = Contact.objects.filter(
                Q(fr_name__icontains=keywords)|Q(ls_name__icontains=keywords)|Q(m_name__icontains=keywords)
                |Q(overview__icontains=keywords)
            ).filter(
                industry__icontains=industry
            ).filter(
                tags__icontains=tags
            ).filter(
                technology__icontains=technology
            )
            query = "Field 1: %s, Field 2: %s, Field 3: %s Field 4: %s" % (keywords, technology, industry, tags)

            contact_form = ContactSearchForm({
               'query': query,
            })
    variables = RequestContext(request, {
            'contact_form':contact_form,    
            'contact_list': contact_list,
            'show_results': show_results
             })
   
    return render_to_response('index.html', variables)

def advance_company_search(request):
    company_form = CompanySearchForm()
    company_list = []
    errors = []

    show_results = False
    if 'keywords' in request.GET:
        keywords = request.GET['keywords'].strip()
        category = request.GET['category']
        industry = request.GET['industry'].strip()
        technology = request.GET['technology'].strip()
        if not (keywords or industry or technology or category):
            errors.append('Enter a search term.')
        else:
            
            show_results = True
            
            company_list = Company.objects.filter(
                name__icontains=keywords
            ).filter(
                industries__icontains=industry
            ).filter(
                categories__id__icontains=category
            ).filter(
                technologies__icontains=technology
            )
            query = "Field 1: %s, Field 2: %s, Field 3: %s Field 4: %s" % (keywords, technology, industry, category)
            company_form = CompanySearchForm({
               'query': query,
            })
    variables = RequestContext(request, {
            'company_form':company_form,    
            'company_list': company_list,
            'show_results': show_results
             })
    return render_to_response('search_company.html', variables)


