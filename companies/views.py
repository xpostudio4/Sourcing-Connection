from django.template import RequestContext, Context
from django.shortcuts import render_to_response, get_object_or_404, render 
from companies.models import *
from companies.forms import *
from companies.functions import percentage_completion, update_completion
from contacts.models import Contact
from fileupload.models import Picture
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView, UpdateView, CreateView, ListView
from django.http import HttpResponse, HttpResponseRedirect

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
        company_rating_form = CompanyRatingForm(request.POST, prefix="company_ratings")

        office_form = OfficeForm(request.POST, prefix="office")
        
        #the forms can be empty
        forms_array = []

        #last_id = company.objects.latest('id').id+1



        if company_form.is_valid():
            company = company_form.save()

            #create a company completion element for this company
            company_rating = CompanyRating()
            company_rating.company = company
            company_rating.save()


            if funding_form.is_valid():

                sff = funding_form.save(commit=False)
                sff.company = company
                sff.save()

    
            if competitors_form.is_valid():
                scf = competitors_form.save(commit=False)
                scf.company = company
                scf.save()
            

            if company_rating_form.is_valid():
                srf = company_rating_form.save(commit=False)
                srf.company = company
                srf.save()
                
                #forms_array.append(competitors_form)#


            if office_form.is_valid():
                sof = office_form.save(commit=False)
                sof.company = company
                sof.save()
                
            #Else used to detect errrors in the process
            #else: 

               # return render_to_response('erros.html', {'form':funding_form})

                #forms_array.append(office_form)
            c = Company.objects.latest('id')
            return HttpResponseRedirect("/company/" + c.slug)
            

            #for i in range(1, len(forms_array)):
                #forms_array[i].save()



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

        return HttpResponseRedirect("company Duplicated")
    else:
        #generate the instances of the forms in the template
        company_form = CompanyForm(prefix = "company")
        funding_form = FundingForm(prefix = "funding")
        competitors_form = CompetitorsForm(prefix = "competitors")
        office_form = OfficeForm(prefix = "office")
        company_rating_form = CompanyRatingForm(prefix="company_ratings")

        #pass the instance to the view
        return render(request, "company_form.html",{
            'company_form': company_form,
            'funding_form': funding_form,
            'competitors_form': competitors_form,
            'office_form': office_form,
            'company_rating_form':company_rating_form
            })


def company_view(request, slug):
    
    company = get_object_or_404(Company,slug=slug)

    

    #This variable keeps the percentage of completion of the profile. 
    percentage_profile = percentage_completion(company.id)
    
    #obtain photos made against company models.
    pictures = Picture.objects.filter(company_id=company.id)

    #If the user is a globaltech employee does not have to  check for the company
    #All globaltech employees have access to modify all the Companies.

    if request.user :
        user_id = request.user.id 

        try:
            contact = Contact.objects.get(id = user_id)
            if contact.latech_contact == True:
                edit= {'useful':True}
            else:
                #verify the person does not have access
                try:
                    #Does the user has permission to modify this claim?
                    permissions = AccessCompanyProfile.objects.get(contact=user_id)
                    edit = {}
                    for i in permissions.company.all():
                           if i.name == company.name:
                              edit = {'useful':True}
                    
                        
                except AccessCompanyProfile.DoesNotExist:
                    edit = {}
        except Contact.DoesNotExist:
            edit ={}
    else:
        edit = {}
    

    return render_to_response(
        "company_page.html",
        {'company':company, 'pictures':pictures, 'permission': edit, "percentage_profile": percentage_profile},
        context_instance=RequestContext(request))

@login_required
def company_update(request, slug):
    #obtain company with the slug and add 
    company = get_object_or_404(Company, slug=slug)

    #Does the user is from Globaltech or does not have access to modify the claim?
    user_id = request.user.id
    try:
            contact = Contact.objects.get(id = user_id)
            #If the user is not a latech employee
            if contact.latech_contact == False:
                #verify the person does not have access
                try:
                    #Does the user has permission to modify this claim?
                    permissions = AccessCompanyProfile.objects.get(contact=user_id)
                    edit = False

                    for i in permissions.company.all():
                           if i.name == company.name:
                              edit = True
                    if edit == False: 
                        return HttpResponseRedirect('/company/'+str(slug))
                except AccessCompanyProfile.DoesNotExist:
                    return HttpResponseRedirect('/company/'+str(slug))
    except Contact.DoesNotExist:
        return HttpResponseRedirect('/company/'+str(slug))

    #obtain photos made against company models.
    pictures = Picture.objects.filter(company=company.id)

    if request.method == 'GET':
    
            company_form = CompanyForm(instance=company, prefix="company")

            

            return render_to_response(
                "company_form.html",
                {'form':company_form, 'pictures':pictures},
                context_instance=RequestContext(request))

    else: 
        #obtain the data of the form for manipulation
        company_form = CompanyForm(request.POST, prefix="company", instance=company)

        if company_form.is_valid():
            #if the form is ok, save and redirect to the original page. 
            company_form.save()
            return HttpResponseRedirect('/company/'+str(slug))
        else: 
            
            return render_to_response(
                'company_form.html', 
                {'form': company_form, 'form_errors':company_form.errors,'pictures':pictures},
                context_instance=RequestContext(request))



class CompanyList(ListView):
    model = Company
    template_name = 'company_list.html'    

def company_page(request, slug):
    try:
       comp = Company.objects.get(slug=slug)
    except Company.DoesNotExist:
       return HttpResponse('The page You are looking does not exist <a href="/"> click here</a> to return home')
       #A 404 page must be rised when needed.
       #raise Http404
    return render_to_response('company_page.html',{'comp':comp},context_instance=RequestContext(request)) 


