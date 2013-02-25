from latech.forms import SearchForm, CompanySearchForm, ContactSearchForm, UserForm, CompanyStatusForm
from django.template import RequestContext, Context
from django.shortcuts import render_to_response, HttpResponse
from taxonomy.models import *
from companies.models import *
from companies.functions import percentage_completion
from contacts.models import *
from django.db.models import Q, F
from django.contrib.auth.forms import AuthenticationForm
from latech.views import hacked_news


def search_page(request):
    search_form = SearchForm()
    company_list = []
    contact_list = []    
    errors =[]
    show_results = False

    if request.user :
        user_id = request.user.id 

        try:
            contact = Contact.objects.get(id = user_id)
            if contact.latech_contact == True:
                latech= {'contact':True}
            else:
                latech = {}
        except Contact.DoesNotExist:
            latech ={}
    else:
        latech = {}

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
        'search_form':search_form,    
        'errors':errors,
        'company_list': company_list,
        'contact_list': contact_list,        
        'show_results': show_results,
        'latech': latech,
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
    company_status_form = CompanyStatusForm()
    user_form  = AuthenticationForm()
    contact_list = []
    company_list = []
#    company_list = Company.objects.all()
    errors = []
    count = 0
    show_results = False

    if request.user :
        user_id = request.user.id 

        try:
            contact = Contact.objects.get(id = user_id)
            if contact.latech_contact == True:
                latech= {'contact':True}
            else:
                latech = {}
               
        except Contact.DoesNotExist:
            latech ={}
    else:
        latech = {}
    
    if 'keywords' in request.GET:
        keywords = request.GET['keywords'].strip()
        category_company = request.GET['category_company']
        country_company = request.GET['country_company']
        industry_company = request.GET['industry_company'].strip()
        technology_company = request.GET['technology_company'].strip()

        if (keywords or category_company or country_company or industry_company or technology_company):

            show_results = True
            q = Q()
            # Country Search
            if country_company:
                q = q & Q(country__id__icontains=country_company)

            #Keywords Search    
            if keywords !="*":
                keys = keywords.split()
                
                #Splitting keywords      
                for key in keys:
                    q = q & (Q(name__icontains=key)|
                        Q(description__icontains=key)|
                        Q(overview__icontains=key))
            else:
                company_list = Company.objects.all()

            # Category Search
            if category_company:
                q = q & Q(categories__id__contains=category_company)

            #Splitting Industries
            industry_keys = industry_company.split()
            for ikey in industry_keys:
               q = q & (Q(industries__icontains=ikey))
            
            # Splitting Technologies
            technology_keys = technology_company.split()
            for tkey in technology_keys:
               q = q & (Q(technologies__icontains=tkey))

            company_form = CompanySearchForm({
                'keywords':keywords,
                'technology_company':technology_company, 
                'industry_company':industry_company, 
                'category_company':category_company, 
                'country_company':country_company,

            })
            company_list = Company.objects.filter(q)
        else:
            show_results = True
            company_list = Company.objects.all()

   # Company Status Search

    if 'company_status' in request.GET:
        company_status = request.GET['company_status']
        if company_status:
            show_results = True
            company_list = Company.objects.filter(company_status__exact=company_status)
          
            company_status_form = CompanyStatusForm({
                'company_status':company_status
            })

        elif company_status == 0 or None:
            show_results = True
            company_list = Company.objects.all()

    if 'maximum' in request.GET:
        maximum = request.GET['maximum']
        minimum = request.GET['minimum']
        if maximum or minimum:
            minimum = float(minimum)/100.0
            maximum = float(maximum)/100.0
            show_results = True
            company_list = Company.objects.filter(pk__in=ProfileCompletion.objects.filter(completion__range=(minimum, maximum)))

           
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
        'company_status_form':company_status_form,
        'company_list': company_list,
        'contact_list': contact_list,        
        'show_results': show_results,
        'errors':errors,
        'user_form': user_form,
        'hacked_news': hacked_news(),
        'latech': latech,
#        'search_page':search_page()
    })
    return render_to_response(
        'index.html', 
        variables,
        context_instance = RequestContext(request)
        )
    
