import tablib
from latech.forms import SearchForm, CompanySearchForm, ContactSearchForm, UserForm, CompanyStatusForm
from django.template import RequestContext, Context
from django.shortcuts import render_to_response, HttpResponse, redirect
from taxonomy.models import *
from companies.models import *
from company_profile_extended.models import Vertical
from companies.functions import percentage_completion
from contacts.models import *
from django.db.models import Q, F
from django.contrib.auth.forms import AuthenticationForm
from latech.views import hacked_news
from news.functions import news


def empty_search_form():
    contact_form = ContactSearchForm()
    company_form = CompanySearchForm()
    return contact_form, company_form

def search_function(request):
    contact_form, company_form = empty_search_form()
    company_status_form = CompanyStatusForm()
    contact_list = []
    maximum = 100
    minimum = 0
    company_list = Company.objects.all()
    q = Q()

    show_results = False

    if 'keywords' in request.GET:
        keywords = request.GET['keywords'].strip()
        category_company = request.GET['category_company']
        country_company = request.GET['country_company']
        industry_company = request.GET['industry_company'].strip()
        technology_company = request.GET['technology_company'].strip()
        vertical_company = request.GET['vertical_company'].strip() 

        if (keywords or category_company or country_company or industry_company or technology_company or vertical_company):

            show_results = True
        
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
            else:
                company_list = Company.objects.all()

            #Splitting Industries
            if industry_company:

                industry_keys = industry_company.split()
                for ikey in industry_keys:
                   q = q & (Q(industries__icontains=ikey))

            else:
                company_list = Company.objects.all()

            
            # Splitting Technologies
            if technology_company:
                technology_keys = technology_company.split()
                for tkey in technology_keys:
                   q = q & (Q(technologies__icontains=tkey))
            else:
                company_list = Company.objects.all()

            #Splitting Verticals
            if vertical_company:

                company_ids =[]
                vertical_keys = vertical_company
                verticals = Vertical.objects.filter(name__icontains=vertical_keys)
                for vkey in verticals:
                    company_ids.append(vkey.company.id)
                    q = q & (Q(id__in=company_ids))

            else:
                company_list = Company.objects.all()

            company_form = CompanySearchForm({
                'keywords':keywords,
                'technology_company':technology_company, 
                'industry_company':industry_company, 
                'category_company':category_company, 
                'country_company':country_company,
                'vertical_company':vertical_company,

            })
    
#            company_list = Company.objects.filter(q)
        
   # Company Status Search

    if 'company_status' in request.GET:
        company_status = request.GET['company_status']
        if company_status:

            show_results = True

            q = q &Q(company_status__exact=company_status)
          
            company_status_form = CompanyStatusForm({
                'company_status':company_status
            })

        else:

            company_list = Company.objects.all()


    if 'maximum' in request.GET:
        maximum = request.GET['maximum']
        minimum = request.GET['minimum']
        if maximum or minimum:
            minimum = float(minimum)/100.0
            maximum = float(maximum)/100.0

#            q = q &Q(id__in=ProfileCompletion.objects.filter(completion__range=(minimum, maximum)))
    else:
        company_list = Company.objects.all()

    company_list = Company.objects.filter(q)
           
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
            contact_form = ContactSearchForm({'query2': query2})
        else:
            show_results = True
            contact_list = Contact.objects.all()


    return contact_form, company_form, company_status_form, show_results, company_list,contact_list

def advanced_search(request):
    user_form  = AuthenticationForm()
    
#    company_list = Company.objects.all()
    errors = []
    count = 0
    

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
    
    contact_form, company_form, company_status_form, show_results, company_list,contact_list = search_function(request)
    

    variables = RequestContext(request, {
        'company_form': company_form,
        'contact_form': contact_form,
        'company_status_form':company_status_form,
        'company_list': company_list,
        'contact_list': contact_list,        
        'show_results': show_results,
        'errors':errors,
        'user_form': user_form,
        #'hacked_news': hacked_news(),
        'blog_news': news(page=1, qty=20),
        'latech': latech,
#        'search_page':search_page()
    })
    return render_to_response(
        'index.html', 
        variables,
        context_instance = RequestContext(request)
        )
    
def export(request, filename='export', format="xlsx"):
    contact_form, company_form, company_status_form, show_results, company_list,contact_list = search_function(request)

    dataset = tablib.Dataset(title="Company Data")

    for co in company_list:
        dataset.append([
            co.name,
            co.email,
            co.main_phone,
            co.industries, 
            co.categories,
            co.value_proposition,
            co.description,
            co.company_status,
            co.employee_quantity,
            co.industries,
            co.technologies,
        ])

    dataset.headers = [
            "Company Name",
            "Email",
            "Phone",
            "Industries", 
            "Category",
            "Value Proposition",
            "Description",
            "GB Status",
            "Employee Quantity Range",
            "Industries",
            "Technologies",
    ]


    filename = '%s.%s' % (filename, format)
    response = HttpResponse(
        getattr(dataset, format),
        mimetype=(format, 'application/octet-stream')
        )
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response


def search_page(request):
    if 'q' in request.GET:
       query = request.GET['q']#.strip()
#        if query:
#           keywords = query.split()
    return redirect(("/?keywords=%s&category_company=&country_company=&industry_company=&vertical_company=&technology_company=&company_status=&minimum=0&maximum=100") % (query))
