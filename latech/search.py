from latech.forms import SearchForm, CompanySearchForm, ContactSearchForm, UserForm
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
        category = request.GET['category_company']
        country = request.GET['country_company']
        industry = request.GET['industry_company'].strip()
        technology = request.GET['technology_company'].strip()
        if (keywords or category or industry or country or technology):
            show_results = True
            company_list = Company.objects.filter(
                Q(name__icontains=keywords)|Q(overview__icontains=keywords)
            ).filter(
                industries__icontains=industry
            ).filter(
                categories__id__icontains=category
            ).filter(
                country__id__icontains=country
            ).filter(
                technologies__icontains=technology
            )
            query1 = ("%s %s %s %s %s") % (keywords, technology, industry, category, country)
            company_form = CompanySearchForm({'query1': query1})

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
        'show_results': show_results
    })
    return render_to_response('index.html', variables)
    
