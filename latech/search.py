from latech.forms import SearchForm, CompanySearchForm, ContactSearchForm, UserForm
from django.template import RequestContext, Context
from django.shortcuts import render_to_response
from taxonomy.models import *
from companies.models import *
from contacts.models import *
from django.db.models import Q, F
from django.contrib.auth.forms import AuthenticationForm
from latech.views import hacked_news

def search_page(request):
    search_form = SearchForm()
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
           search_form = SearchForm({'query': query})
    variables = RequestContext(request, {
        'search_form':form,    
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
    contact_form, company_form, = empty_search_form()
    company_form = CompanySearchForm(request.GET or None)
    user_form  = AuthenticationForm()
    contact_list = []
    company_list = []
    errors = []
    show_results = False
    if 'keywords' in request.GET:
        keywords = request.GET['keywords'].strip()
        category_company = request.GET['category_company']
        country_company = request.GET['country_company']
        industry_company = request.GET['industry_company']
        technology_company = request.GET['technology_company']
        if (keywords !="*" or category_company or country_company or industry_company):
            show_results = True
            company_list = Company.objects.filter(
                Q(name__icontains=keywords)|Q(overview__icontains=keywords)
            ).filter(
                Q(industries__icontains=industry_company)
            ).filter(
                Q(categories__id__icontains=category_company)
            ).filter(
                Q(country__id__icontains=country_company)
            ).filter(
                Q(technologies__icontains=technology_company)
            )
            company_form = CompanySearchForm({
                'keywords':keywords,
                'technology_company':technology_company, 
                'industry_company':industry_company, 
                'category_company':category_company, 
                'country_company':country_company
            })
        else:
            show_results = True
            company_list = Company.objects.all()

    if 'terms' in request.GET:
        terms = request.GET['terms'].strip()
        tags = request.GET['tags']
        overview = request.GET['overview'].strip()
        technology = request.GET['technology'].strip()
        industry = request.GET['industry'].strip()

        if (terms or tags or overview or technology or industry):
            show_results = True
            contact_list = Contact.objects.filter(
                Q(fr_name__icontains=terms)|Q(overview__icontains=terms)|Q(ls_name__icontains=terms)|Q(m_name__icontains=terms)
                ).filter(Q(tags__contains=tags)
                ).filter(Q(technology__contains=technology)
                ).filter(Q(overview__icontains=overview)
                ).filter(Q(industry__contains=industry))
            query2 = "%s %s %s %s %s" % (terms, tags, overview, technology, industry)
            contact_form = CompanySearchForm({'query2': query2})
           
    variables = RequestContext(request, {
        'company_form': company_form,
        'contact_form': contact_form,
        'company_list': company_list,
        'contact_list': contact_list,        
        'show_results': show_results,
        'user_form': user_form,
        'hacked_news': hacked_news(),
#        'search_page':search_page()
    })
    return render_to_response(
        'index.html', 
        variables, 
        context_instance = RequestContext(request)
        )
    
