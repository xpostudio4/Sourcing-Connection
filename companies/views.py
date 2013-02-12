from django.template import RequestContext, Context
from django.shortcuts import render_to_response, get_object_or_404, render 
from companies.models import *
from companies.forms import *
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
        office_form = OfficeForm(request.POST, prefix="office")
        
        #the forms can be empty
        forms_array = []

        #last_id = company.objects.latest('id').id+1



        if company_form.is_valid():
            company = company_form.save()

            if funding_form.is_valid():

                sff = funding_form.save(commit=False)
                sff.company = company
                sff.save()
    

            

            if competitors_form.is_valid():
                scf = competitors_form.save(commit=False)
                scf.company = company
                scf.save()
                
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

        #pass the instance to the view
        return render(request, "company_form.html",{
            'company_form': company_form,
            'funding_form': funding_form,
            'competitors_form': competitors_form,
            'office_form': office_form
            })

def check_company_access(user):
    try:
        #Does the user has permission to modify this claim?
        permissions = AccessCompanyProfile.objects.get(contact=user.id)

        for i in permissions.company.all():
               if i.name == company.name:
                 edit['useful'] = True
                 return edit
    except AccessCompanyProfile.DoesNotExist:
        edit = {}
        return edit
    


def company_view(request, slug):
    try:
        company = Company.objects.get(slug=slug)

    except Company.DoesNotExist:
        return HttpResponse("This company does not Exist in our database")

    
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
                edit = check_company_access(request.user)
               
        except Contact.DoesNotExist:
            edit ={}
    else:
        edit = {}
    

    return render_to_response(
        "company_page.html",
        {'company':company, 'pictures':pictures, 'permission': edit},
        context_instance=RequestContext(request))

@login_required
def company_update(request, slug):

    #Does the user is from Globaltech or does not have access to modify the claim?
    user_id = request.user.id
    try:
            contact = Contact.objects.get(id = user_id)
            #If the user is not a latech employee
            if contact.latech_contact == False:
                #verify the person does not have access
                if not check_company_access.useful: 
                    return HttpResponseRedirect('/company/'+str(slug))
    except Contact.DoesNotExist:
        return HttpResponseRedirect('/company/'+str(slug))


    #obtain company with the slug and add 
    company = Company.objects.get(slug=slug)
    company_form = CompanyForm(instance=company)

    #obtain photos made against company models.
    pictures = Picture.objects.filter(company=company.id)

    return render_to_response(
        "company_form.html",
        {'form':company_form, 'pictures':pictures},
        context_instance=RequestContext(request))



class CompanyList(ListView):
    model = Company
    template_name = 'company_list.html'    

def company_page(request, slug):
    try:
       comp = Company.objects.get(slug=slug)
    except Company.DoesNotExist:
       raise Http404
    return render_to_response('company_page.html',{'comp':comp},context_instance=RequestContext(request)) 


