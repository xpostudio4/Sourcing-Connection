from django.template import RequestContext, Context
from django.shortcuts import render_to_response, get_object_or_404, render 
from companies.models import *
from companies.forms import *
from fileupload.models import Picture
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView, UpdateView, CreateView, ListView
from django.http import HttpResponse

#class CompanyCreate(CreateView):
#    model = Company
#    form_class = CompanyForm
#    template_name = 'company_form.html'
#    success_url = '/company/%(slug)s/'
#
#    @method_decorator(login_required)
#    def dispatch(self, *args, **kwargs):
#        return super(CompanyCreate, self).dispatch(*args, **kwargs)


def CompanyCreate(request):
    if request.method == "POST":
        

        reference = "...."
        #process the form.
        company_form = CompanyForm(request.POST, prefix="company")
        funding_form = FundingForm(request.POST, prefix="funding")
        competitors_form = CompetitorsForm(request.POST, prefix = "competitors")
        office_form = OfficeForm(request.POST, prefix="office")
        
        #the forms can be empty
        forms_array = []

        #last_id = company.objects.latest('id').id+1



        if company_form.is_valid():
            company = company_form.save()

            if funding_form.is_valid():
                funding_form.company_id = company
                forms_array.append(funding_form)
            else: 


                return render_to_response('erros.html', {'form':funding_form})

            if competitors_form.is_valid():
                #competitors_form.company_id = company
                forms_array.append(competitors_form)


            if office_form.is_valid():
                #office_form.company_id = company
                forms_array.append(office_form)

            

            for i in range(1, len(forms_array)):
                forms_array[i].save()



            #validate and return value needed.

        #if company_form.is_valid() and ((funding_form.is_valid() or funding_form.has_changed()==False) and competitors_form.is_valid() and office_form.is_valid():
        #    reference += "Validation happened and You did not watched it"
        #    company_form = company_form.save()
        #    funding_form.company = company_form
        #    funding_form = funding_form.save()
        #    competitors_form.company = company_form
        #    competitors_form = competitors_form.save()
        #    office_form.company = company_form
        #    office_form = office_form.save()
        else: 
            
            pass

        return HttpResponse(reference)
    else:
        #generate the instances of the forms in the template
        company_form = CompanyForm(prefix = "company")
        funding_form = FundingForm(prefix = "funding")
        competitors_form = CompetitorsForm(prefix = "competitors")
        office_form = OfficeForm(prefix = "office")

        #pass the instance to the view
        return render(request, "company_form.html",{
            'company_form': company_form,
            'funding_form': funding_form,
            'competitors_form': competitors_form,
            'office_form': office_form
            })


    
class CompanyView(DetailView):
    queryset = Company.objects.all()
    template_name = 'company_page.html'
#    success_url = '/company/%(slug)s/'

def company_view(request, slug):
    company = Company.objects.get(slug=slug)
    
    #obtain photos made against company models.
    pictures = Picture.objects.filter(company_id=company.id)

    return render_to_response(
        "company_page.html",
        {'company':company, 'pictures':pictures},
        context_instance=RequestContext(request))


def company_update(request, slug):

    #obtain company with the slug and add 
    company = Company.objects.get(slug=slug)
    company_form = CompanyForm(instance=company)

    #obtain photos made against company models.
    pictures = Picture.objects.filter(company=company.id)

    return render_to_response(
        "company_page.html",
        {'form':company_form, 'pictures':pictures},
        context_instance=RequestContext(request))



class CompanyUpdate(UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'company_form.html'
    success_url = '/company/%(slug)s/'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CompanyUpdate, self).dispatch(*args, **kwargs)

class CompanyList(ListView):
    model = Company
    template_name = 'company_list.html'    

def company_page(request, slug):
    try:
       comp = Company.objects.get(slug=slug)
    except Company.DoesNotExist:
       raise Http404
    return render_to_response('company_page.html',{'comp':comp},context_instance=RequestContext(request)) 


