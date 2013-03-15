from django.template import RequestContext, Context
from django.shortcuts import render_to_response, get_object_or_404, render 
from companies.models import *
from companies.forms import *
from fileupload.forms import *
from companies.functions import percentage_completion, update_completion, validate_user_company_access_or_redirect
from contacts.models import Contact
from fileupload.models import Picture
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView, UpdateView, CreateView, ListView
from django.http import HttpResponse, HttpResponseRedirect

class CompaniesCreate(CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'company_form.html'
    success_url = '/company/%(slug)s/'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CompaniesCreate, self).dispatch(*args, **kwargs)

class CompaniesUpdate(UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'company_form.html'
    success_url = '/company/%(slug)s/'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CompaniesUpdate, self).dispatch(*args, **kwargs)


def CompanyCreate(request):
    if request.method == "POST":
      
        #process the form.
        company_form = CompanyForm(request.POST, prefix="company")

        #the forms can be empty
        forms_array = []

        #last_id = company.objects.latest('id').id+1

        if company_form.is_valid():
            company = company_form.save()

            #create a company completion element for this company
            #Create company percentage object in that table.
            c = Company.objects.get(id=company.id)
            count = 0 
            length = len(c.__dict__)

            for i in c.__dict__:
                if c.__dict__[i]:
                    count += 1

            percentage = round(count/float(length),2)

            p = ProfileCompletion(completion=percentage, company_id= company.id)
            p.save()

            #create a new reference for the company in the company profile of LAtech
            #must create a reference for the user in company access
            #verify if the user has an access model if not 
            try: 
                access = AccessCompanyProfile.objects.get(contact=request.user)
            
            except AccessCompanyProfile.DoesNotExist:
                access = AccessCompanyProfile.objects.create(contact=request.user)
                access.save()

            #independent of the user provided the access will be created.            
            access.company.add(company)
            access.save()

            #Else used to detect errors in the process
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

#        return HttpResponseRedirect("company Duplicated")
        return render_to_response('company_form.html', 
            {'form': company_form, 'form_errors': company_form.errors},
            context_instance=RequestContext(request))

    else:
        #generate the instances of the forms in the template
        company_form = CompanyForm(prefix = "company")
        #pass the instance to the view
        return render(request, "company_form.html",{
            'company_form': company_form,
            })


def company_view(request, slug):
    
    company = get_object_or_404(Company,slug=slug)

    

    #This variable keeps the percentage of completion of the profile. 
    percentage_profile = percentage_completion(company.id)
    
    #obtain photos made against company models.
#    pictures = Picture.objects.filter(company_id=company.id)

    #If the user is a globaltech employee does not have to  check for the company
    #All globaltech employees have access to modify all the Companies.

    if request.user :
        user_id = request.user.id 


        try:
            contact = Contact.objects.get(user=user_id)
            if contact.latech_contact or request.user.is_staff or request.user.is_superuser  == True:
                edit= True

            else:
                
                #verify the person does not have access
                try:
                    #Does the user has permission to modify this claim?
                    permissions = AccessCompanyProfile.objects.get(contact=request.user)
                    
                    if permissions.company.all().filter(name__icontains=company.name) :
                              edit = True
                    else: 
                            edit = False
                except AccessCompanyProfile.DoesNotExist:

                    edit = False
        except Contact.DoesNotExist:
            edit =False
    else:
        edit = False
    
    management = Management.objects.filter(company= company)
    competitors = Competitors.objects.filter(company=company)
    certifications = Certification.objects.filter(company=company)
    customers = Customer.objects.filter(company=company)
    awards = Award.objects.filter(company=company)
    offices = Office.objects.filter(company=company)
    acquisitions = Acquisition.objects.filter(company=company)
    pictures = Picture.objects.filter(company=company)
    companylinks = CompanyLink.objects.filter(company=company)
    office_list = []
    count = 0
    
    for i in offices:
        count += 1
        if (count)%3==0:
            office_list.append({"object":i, "ul":True})
        else:
            office_list.append({"object":i})


    return render_to_response(
        "company_page.html",
        {'company':company, 'companylinks':companylinks,'pictures':pictures, 'permission': edit, "percentage_profile": percentage_profile,
        'management': management,'offices':office_list, 'competitors': competitors,"certifications":certifications,
        "customers":customers, "awards":awards, "pictures":pictures},
        context_instance=RequestContext(request))

@login_required
def company_update(request, slug):
    #obtain company with the slug and add 
    company = get_object_or_404(Company, slug=slug)

    #Does the user is from Globaltech or does not have access to modify the claim?
    company =get_object_or_404(Company,slug=slug)
    edit = validate_user_company_access_or_redirect(request,company)

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
    company = get_object_or_404(Company,slug=slug)
    return render_to_response('company_page.html',{'comp':company},context_instance=RequestContext(request)) 

##################################################################################################################
################################################ Company Link Views ################################################
##################################################################################################################

@login_required
def companylink_update(request, slug):
    """The purpose of this view is to update the links for companies"""

    #verifies if the company exists if not returns a 404 page
    company =get_object_or_404(Company,slug=slug)
    companylink_reference = get_object_or_404(CompanyLink, company=company)
    companylink_form = CompanyLinkForm(instance=companylink_reference)

    #verifies the person has access to the company or is an incubator employee
    edit = validate_user_company_access_or_redirect(request,company)

    #if the request is GET presents info, 
    if request.method == 'GET':
        return render_to_response('companylink_form.html',{'form':companylink_form, 'info': companylink_reference},context_instance=RequestContext(request))
    else:
        companylink_form = CompanyLinkForm(request.POST, instance=companylink_reference)
        #if is POST Validates the form is well filled and save it redirecting to the company page 
        if companylink_form.is_valid():
            companylink_form.save()

            return HttpResponseRedirect('/company/'+str(slug))
        #if not well filled redirect to the original update page and display error
        else:
            return render_to_response('companylink_form.html', 
                {'form': companylink_form, 'form_errors': companylink_form.errors, 'info': companylink_reference},
                context_instance=RequestContext(request))

##################################################################################################################
################################################ Management Views ################################################
##################################################################################################################

@login_required
def management_create(request, slug):
    """The purpose of this function is to create  new management item associated with a created company"""
    #verifies if the company exists if not returns a 404 page
    company =get_object_or_404(Company,slug=slug)

    #verifies the person has access to the company or is an incubator employee
    edit = validate_user_company_access_or_redirect(request,company)

    #if the request is GET presents empty form
    if request.method == 'GET':

        management_form = ManagementForm()
        return render_to_response('management_form.html', {'form': management_form, 'company':company},
            context_instance=RequestContext(request))
     
    else:
        management_form = ManagementForm(request.POST)
        #if is POST Validates the form is well filled and save it redirecting to the company page
        if management_form.is_valid():
            mf = management_form.save(commit=False)
            mf.company = company
            mf.save()
            return HttpResponseRedirect('/company/'+str(slug))

        #if not well filled redirect to the original create and display error
        else:
            return render_to_response('management_form.html', 
                {'form': management_form, 'form_errors': management_form.errors, 'company':company},
                context_instance=RequestContext(request))

@login_required
def management_update(request, slug, id):
    """The purpose of this view is to update the info of the management page"""
    #verifies if the company exists if not returns a 404 page
    company =get_object_or_404(Company,slug=slug)
    management_reference = get_object_or_404(Management, id=id,company=company)
    management_form = ManagementForm(instance=management_reference)

    #verifies the person has access to the company or is an incubator employee
    edit = validate_user_company_access_or_redirect(request,company)

    #if the request is GET presents info, 
    if request.method == 'GET':
        return render_to_response('management_form.html',{'form':management_form, 'info': management_reference},context_instance=RequestContext(request))
    else:
        management_form = ManagementForm(request.POST, instance=management_reference)
        #if is POST Validates the form is well filled and save it redirecting to the company page 
        if management_form.is_valid():
            management_form.save()

            return HttpResponseRedirect('/company/'+str(slug))
        #if not well filled redirect to the original update page and display error
        else:
            return render_to_response('management_form.html', 
                {'form': management_form, 'form_errors': management_form.errors, 'info': management_reference},
                context_instance=RequestContext(request))

@login_required
def management_delete(request, slug,id):
    """This view deletes the management info and redirects to the company page"""
    
    company =get_object_or_404(Company,slug=slug)
    edit = validate_user_company_access_or_redirect(request,company)

    if request.method == 'POST':
        return HttpResponseRedirect('/company/'+str(slug))
    else: 
        #verifies if the company exists if not returns a 404 page
        management_reference = get_object_or_404(Management, id=id,company=company)

        #deletes the view and redirects to the page.
        management_reference.delete()
        return HttpResponseRedirect('/company/'+str(slug))



@login_required
def management_view(request, slug, id):
    """This view makes possible to display a management item alone"""
    company =get_object_or_404(Company,slug=slug)
    edit = validate_user_company_access_or_redirect(request,company)
    management_reference = get_object_or_404(Management, id=id,company=company)

    return render_to_response('management_form.html', 
                {'details': management_reference,'info':management_reference},
                context_instance=RequestContext(request))

##################################################################################################################
############################################### Competitors Views ################################################
##################################################################################################################


@login_required
def competitors_create(request, slug):
    """The purpose of this function is to create  new management item associated with a created company"""
    #verifies if the company exists if not returns a 404 page
    company =get_object_or_404(Company,slug=slug)

    #verifies the person has access to the company or is an incubator employee
    edit = validate_user_company_access_or_redirect(request,company)

    #if the request is GET presents empty form
    if request.method == 'GET':

        competitors_form = CompetitorsForm()
        return render_to_response('competitors_form.html', {'form': competitors_form, 'company':company},
            context_instance=RequestContext(request))
     
    else:
        competitors_form = CompetitorsForm(request.POST)
        #if is POST Validates the form is well filled and save it redirecting to the company page
        if competitors_form.is_valid():
            cf = competitors_form.save(commit=False)

            #verify if other companies with the same info exists anywhere
            try: 
                comparison = Competitors.objects.get(name=cf.name,company= company)
                
                if str(comparison.name) != str(cf.name):
                    cf.company = company
                    cf.save()
                    
                else:
                    form_errors = {"Name - The competitor " + str(comparison.name).capitalize() + " has been already created for "+ str(company.name).capitalize() + "."}
                    return render_to_response('competitors_form.html', 
                    {'form': competitors_form, 'form_errors': form_errors, 'company':company},
                    context_instance=RequestContext(request))

            except Competitors.DoesNotExist :
                cf.company = company
                cf.save()


            
            return HttpResponseRedirect('/company/'+str(slug))

        #if not well filled redirect to the original create and display error
        else:
            return render_to_response('competitors_form.html', 
                {'form': competitors_form, 'form_errors': competitors_form.errors, 'company':company},
                context_instance=RequestContext(request))


@login_required
def competitors_update(request, slug,id):
    """The purpose of this view is to update the info of the competitors page"""
    #verifies if the company exists if not returns a 404 page
    company =get_object_or_404(Company,slug=slug)
    competitors_reference = get_object_or_404(Competitors, id=id,company=company)
    competitors_form = CompetitorsForm(instance=competitors_reference)

    #verifies the person has access to the company or is an incubator employee
    edit = validate_user_company_access_or_redirect(request,company)

    #if the request is GET presents info, 
    if request.method == 'GET':
        return render_to_response('competitors_form.html',{'form':competitors_form, 'info': competitors_reference},context_instance=RequestContext(request))
    else:
        competitors_form = CompetitorsForm(request.POST)
        #if is POST Validates the form is well filled and save it redirecting to the company page 
        if competitors_form.is_valid():
            cf= competitors_form.save(commit = False)
            #verify the item is not the same as the company page
            if str(company.name) == str(cf.name):
                
                form_errors = {"Name - You can't be a competitor of Your own company. "}
                return render_to_response('competitors_form.html', 
                {'form': competitors_form, 'form_errors': form_errors, 'info': competitors_reference},
                context_instance=RequestContext(request))
            #verify if other companies with the same info exists anywhere
            try: 
                comparison = Competitors.objects.get(name=cf.name,company= company)

                if competitors_reference.id == comparison.id:
                    competitors_reference.name = cf.name
                    competitors_reference.save()
                else:
                    form_errors = {"Name - The company " + str(cf.name).capitalize() + " already exists as a competitor of " +str(company.name).capitalize() +"."  }
                    return render_to_response('competitors_form.html', 
                    {'form': competitors_form, 'form_errors': form_errors, 'info': competitors_reference},
                    context_instance=RequestContext(request))

            except:
                competitors_reference.name = cf.name
                competitors_reference.save()


            return HttpResponseRedirect('/company/'+str(slug))
        #if not well filled redirect to the original update page and display error
        else:
            return render_to_response('competitors_form.html', 
                {'form': competitors_form, 'form_errors': competitors_form.errors, 'info': competitors_reference},
                context_instance=RequestContext(request))

@login_required
def competitors_delete(request, slug,id):
    """This view deletes the competitors info and redirects to the company page"""
    company =get_object_or_404(Company,slug=slug)
    edit = validate_user_company_access_or_redirect(request,company)

    if request.method == 'POST':
        return HttpResponseRedirect('/company/'+str(slug))
    else: 
        #verifies if the company exists if not returns a 404 page
        competitors_reference = get_object_or_404(Competitors, id=id,company=company)

        #deletes the view and redirects to the page.
        competitors_reference.delete()
        return HttpResponseRedirect('/company/'+str(slug))

@login_required
def competitors_view(request, slug, id):
    """This view makes possible to display a competitor item alone"""
    company =get_object_or_404(Company,slug=slug)
    edit = validate_user_company_access_or_redirect(request,company)
    competitors_reference = get_object_or_404(Competitors, id=id,company=company)

    return render_to_response('competitors_form.html', 
                {'details': competitors_reference,'info':competitors_reference},
                context_instance=RequestContext(request))

##################################################################################################################
################################################ Office Views ####################################################
##################################################################################################################

def office_create(request, slug):
    """The purpose of this function is to create  new office item associated with a created company"""
    #verifies if the company exists if not returns a 404 page
    company =get_object_or_404(Company,slug=slug)
    edit = validate_user_company_access_or_redirect(request,company)
    #if the request is GET presents empty form
    if request.method == 'GET':

        office_form = OfficeForm()
        return render_to_response('office_form.html', {'form': office_form, 'company':company},
            context_instance=RequestContext(request))
     
    else:
        office_form = OfficeForm(request.POST)
        #if is POST Validates the form is well filled and save it redirecting to the company page
        if office_form.is_valid():
            of = office_form.save(commit=False)
            of.company = company
            of.save()
            return HttpResponseRedirect('/company/'+str(slug))

        #if not well filled redirect to the original create and display error
        else:
            return render_to_response('office_form.html', 
                {'form': office_form, 'form_errors': office_form.errors, 'company':company},
                context_instance=RequestContext(request))


def office_update(request, slug, id):
    """The purpose of this view is to update the info of the office page"""
    #verifies if the company exists if not returns a 404 page
    company =get_object_or_404(Company,slug=slug)
    office_reference = get_object_or_404(Office, id=id,company=company)
    office_form = OfficeForm(instance=office_reference)

    #verifies the person has access to the company or is an incubator employee
    edit = validate_user_company_access_or_redirect(request,company)

    #if the request is GET presents info, 
    if request.method == 'GET':
        return render_to_response('office_form.html',{'form':office_form, 'info': office_reference},context_instance=RequestContext(request))
    else:
        office_form = OfficeForm(request.POST, instance=office_reference)
        #if is POST Validates the form is well filled and save it redirecting to the company page 
        if office_form.is_valid():
            office_form.save(commit = False)

            return HttpResponseRedirect('/company/'+str(slug))
        #if not well filled redirect to the original update page and display error
        else:
            return render_to_response('office_form.html', 
                {'form': office_form, 'form_errors': office_form.errors, 'info': office_reference},
                context_instance=RequestContext(request))

@login_required
def office_delete(request, slug,id):
    """This view deletes the office info and redirects to the company page"""
    
    company =get_object_or_404(Company,slug=slug)
    edit = validate_user_company_access_or_redirect(request,company)

    if request.method == 'POST':
        return HttpResponseRedirect('/company/'+str(slug))
    else: 
        #verifies if the company exists if not returns a 404 page
        office_reference = get_object_or_404(Office, id=id,company=company)

        #deletes the view and redirects to the page.
        office_reference.delete()
        return HttpResponseRedirect('/company/'+str(slug))



@login_required
def office_view(request, slug, id):
    """This view makes possible to display a office item alone"""
    company =get_object_or_404(Company,slug=slug)
    edit = validate_user_company_access_or_redirect(request,company)
    office_reference = get_object_or_404(Office, id=id,company=company)

    return render_to_response('office_form.html', 
                {'details': office_reference,'info':office_reference},
                context_instance=RequestContext(request))


##################################################################################################################
################################################ Certification Views #############################################
##################################################################################################################

def certification_create(request, slug):
    """The purpose of this function is to create  new certification item associated with a created company"""
    #verifies if the company exists if not returns a 404 page
    company =get_object_or_404(Company,slug=slug)
    edit = validate_user_company_access_or_redirect(request,company)
    #if the request is GET presents empty form
    if request.method == 'GET':

        certification_form = CertificationForm()
        return render_to_response('certification_form.html', {'form': certification_form, 'company':company},
            context_instance=RequestContext(request))
     
    else:
        certification_form = CertificationForm(request.POST)
        #if is POST Validates the form is well filled and save it redirecting to the company page
        if certification_form.is_valid():
            of = certification_form.save(commit=False)
            of.company = company
            of.save()
            return HttpResponseRedirect('/company/'+str(slug))

        #if not well filled redirect to the original create and display error
        else:
            return render_to_response('certification_form.html', 
                {'form': certification_form, 'form_errors': certification_form.errors, 'company':company},
                context_instance=RequestContext(request))


def certification_update(request, slug, id):
    """The purpose of this view is to update the info of the certification page"""
    #verifies if the company exists if not returns a 404 page
    company =get_object_or_404(Company,slug=slug)
    certification_reference = get_object_or_404(Certification, id=id,company=company)
    certification_form = CertificationForm(instance=certification_reference)

    #verifies the person has access to the company or is an incubator employee
    edit = validate_user_company_access_or_redirect(request,company)

    #if the request is GET presents info, 
    if request.method == 'GET':
        return render_to_response('certification_form.html',{'form':certification_form, 'info': certification_reference},context_instance=RequestContext(request))
    else:
        certification_form = CertificationForm(request.POST, instance=certification_reference)
        #if is POST Validates the form is well filled and save it redirecting to the company page 
        if certification_form.is_valid():
            certification_form.save()

            return HttpResponseRedirect('/company/'+str(slug))
        #if not well filled redirect to the original update page and display error
        else:
            return render_to_response('certification_form.html', 
                {'form': certification_form, 'form_errors': certification_form.errors, 'info': certification_reference},
                context_instance=RequestContext(request))

@login_required
def certification_delete(request, slug,id):
    """This view deletes the certification info and redirects to the company page"""
    
    company =get_object_or_404(Company,slug=slug)
    edit = validate_user_company_access_or_redirect(request,company)

    if request.method == 'POST':
        return HttpResponseRedirect('/company/'+str(slug))
    else: 
        #verifies if the company exists if not returns a 404 page
        certification_reference = get_object_or_404(Certification, id=id,company=company)

        #deletes the view and redirects to the page.
        certification_reference.delete()
        return HttpResponseRedirect('/company/'+str(slug))



@login_required
def certification_view(request, slug, id):
    """This view makes possible to display a certification item alone"""
    company =get_object_or_404(Company,slug=slug)
    edit = validate_user_company_access_or_redirect(request,company)
    certification_reference = get_object_or_404(Certification, id=id,company=company)

    return render_to_response('certification_form.html', 
                {'details': certification_reference,'info':certification_reference},
                context_instance=RequestContext(request))


##################################################################################################################
################################################ Award Views #############################################
##################################################################################################################

def award_create(request, slug):
    """The purpose of this function is to create  new awards item associated with a created company"""
    #verifies if the company exists if not returns a 404 page
    company =get_object_or_404(Company,slug=slug)
    edit = validate_user_company_access_or_redirect(request,company)
    #if the request is GET presents empty form
    if request.method == 'GET':

        award_form = AwardForm()
        return render_to_response('award_form.html', {'form': award_form, 'company':company},
            context_instance=RequestContext(request))
     
    else:
        award_form = AwardForm(request.POST)
        #if is POST Validates the form is well filled and save it redirecting to the company page
        if award_form.is_valid():
            af = award_form.save(commit=False)
            af.company = company
            af.save()
            return HttpResponseRedirect('/company/'+str(slug))

        #if not well filled redirect to the original create and display error
        else:
            return render_to_response('award_form.html', 
                {'form': award_form, 'form_errors': award_form.errors, 'company':company},
                context_instance=RequestContext(request))

@login_required
def award_update(request, slug,id):
    """The purpose of this view is to update the info of the awards page"""
    #verifies if the company exists if not returns a 404 page
    company =get_object_or_404(Company,slug=slug)
    award_reference = get_object_or_404(Award, id=id,company=company)
    award_form = AwardForm(instance=award_reference)

    #verifies the person has access to the company or is an incubator employee
    edit = validate_user_company_access_or_redirect(request,company)

    #if the request is GET presents info, 
    if request.method == 'GET':
        return render_to_response('award_form.html',{'form':award_form, 'info': award_reference},context_instance=RequestContext(request))
    else:
        award_form = AwardForm(request.POST, instance=award_reference)
        if award_form.is_valid():
            award_form.save()
 
            return HttpResponseRedirect('/company/'+str(slug))
        #if not well filled redirect to the original update page and display error
        else:
            return render_to_response('award_form.html', 
                {'form': award_form, 'form_errors': award_form.errors, 'info': award_reference},
                context_instance=RequestContext(request))


@login_required
def award_delete(request, slug,id):
    """This view deletes the award info and redirects to the company page"""
    
    company =get_object_or_404(Company,slug=slug)
    edit = validate_user_company_access_or_redirect(request,company)

    if request.method == 'POST':
        return HttpResponseRedirect('/company/'+str(slug))
    else: 
        #verifies if the company exists if not returns a 404 page
        award_reference = get_object_or_404(Award, id=id,company=company)

        #deletes the view and redirects to the page.
        award_reference.delete()
        return HttpResponseRedirect('/company/'+str(slug))



@login_required
def award_view(request, slug, id):
    """This view makes possible to display a award item alone"""
    company =get_object_or_404(Company,slug=slug)
    edit = validate_user_company_access_or_redirect(request,company)
    award_reference = get_object_or_404(Award, id=id,company=company)

    return render_to_response('award_form.html', 
                {'details': award_reference,'info':award_reference},
                context_instance=RequestContext(request))


##################################################################################################################
################################################ Customer Views #############################################
##################################################################################################################

def customer_create(request, slug):
    """The purpose of this function is to create  new customers item associated with a created company"""
    #verifies if the company exists if not returns a 404 page
    company =get_object_or_404(Company,slug=slug)
    edit = validate_user_company_access_or_redirect(request,company)
    #if the request is GET presents empty form
    if request.method == 'GET':

        customer_form = CustomerForm()
        return render_to_response('customer_form.html', {'form': customer_form, 'company':company},
            context_instance=RequestContext(request))
     
    else:
        customer_form = CustomerForm(request.POST)
        #if is POST Validates the form is well filled and save it redirecting to the company page
        if customer_form.is_valid():
            of = customer_form.save(commit=False)
            of.company = company
            of.save()
            return HttpResponseRedirect('/company/'+str(slug))

        #if not well filled redirect to the original create and display error
        else:
            return render_to_response('customer_form.html', 
                {'form': customer_form, 'form_errors': customer_form.errors, 'company':company},
                context_instance=RequestContext(request))


def customer_update(request, slug, id):
    """The purpose of this view is to update the info of the customer page"""
    #verifies if the company exists if not returns a 404 page
    company =get_object_or_404(Company,slug=slug)
    customer_reference = get_object_or_404(Customer, id=id,company=company)
    customer_form = CustomerForm(instance=customer_reference)

    #verifies the person has access to the company or is an incubator employee
    edit = validate_user_company_access_or_redirect(request,company)

    #if the request is GET presents info, 
    if request.method == 'GET':
        return render_to_response('customer_form.html',{'form':customer_form, 'info': customer_reference},context_instance=RequestContext(request))
    else:
        customer_form = CustomerForm(request.POST, instance=customer_reference)
        #if is POST Validates the form is well filled and save it redirecting to the company page 
        if customer_form.is_valid():
            customer_form.save()

            return HttpResponseRedirect('/company/'+str(slug))
        #if not well filled redirect to the original update page and display error
        else:
            return render_to_response('customer_form.html', 
                {'form': customer_form, 'form_errors': customer_form.errors, 'info': customer_reference},
                context_instance=RequestContext(request))

@login_required
def customer_delete(request, slug,id):
    """This view deletes the award info and redirects to the company page"""
    
    company =get_object_or_404(Company,slug=slug)
    edit = validate_user_company_access_or_redirect(request,company)

    if request.method == 'POST':
        return HttpResponseRedirect('/company/'+str(slug))
    else: 
        #verifies if the company exists if not returns a 404 page
        customer_reference = get_object_or_404(Customer, id=id,company=company)

        #deletes the view and redirects to the page.
        customer_reference.delete()
        return HttpResponseRedirect('/company/'+str(slug))



@login_required
def customer_view(request, slug, id):
    """This view makes possible to display a award item alone"""
    company =get_object_or_404(Company,slug=slug)
    edit = validate_user_company_access_or_redirect(request,company)
    customer_reference = get_object_or_404(Customer, id=id,company=company)

    return render_to_response('customer_form.html', 
                {'details': customer_reference,'info':customer_reference},
                context_instance=RequestContext(request))


##################################################################################################################
################################################ Acquisitions Views #############################################
##################################################################################################################

def acquisition_create(request, slug):
    """The purpose of this function is to create  new acquisition item associated with a created company"""
    #verifies if the company exists if not returns a 404 page
    company =get_object_or_404(Company,slug=slug)
    edit = validate_user_company_access_or_redirect(request,company)
    #if the request is GET presents empty form
    if request.method == 'GET':

        acquisition_form = AcquisitionForm()
        return render_to_response('acquisition_form.html', {'form': acquisition_form, 'company':company},
            context_instance=RequestContext(request))
     
    else:
        acquisition_form = AcquisitionForm(request.POST)
        #if is POST Validates the form is well filled and save it redirecting to the company page
        if acquisition_form.is_valid():
            aqf = acquisition_form.save(commit=False)
            aqf.company = company
            aqf.save()
            return HttpResponseRedirect('/company/'+str(slug))

        #if not well filled redirect to the original create and display error
        else:
            return render_to_response('acquisition_form.html', 
                {'form': acquisition_form, 'form_errors': acquisition_form.errors, 'company':company},
                context_instance=RequestContext(request))


def acquisition_update(request, slug, id):
    """The purpose of this view is to update the info of the acquisition page"""
    #verifies if the company exists if not returns a 404 page
    company =get_object_or_404(Company,slug=slug)
    acquisition_reference = get_object_or_404(Acquisition, id=id,company=company)
    acquisition_form = AcquisitionForm(instance=acquisition_reference)

    #verifies the person has access to the company or is an incubator employee
    edit = validate_user_company_access_or_redirect(request,company)

    #if the request is GET presents info, 
    if request.method == 'GET':
        return render_to_response('acquisition_form.html',{'form':acquisition_form, 'info': acquisition_reference},context_instance=RequestContext(request))
    else:
        acquisition_form = AcquisitionForm(request.POST, instance=acqusition_reference)
        #if is POST Validates the form is well filled and save it redirecting to the company page 
        if acquisition_form.is_valid():
            acquisition_form.save()

            return HttpResponseRedirect('/company/'+str(slug))
        #if not well filled redirect to the original update page and display error
        else:
            return render_to_response('acquisition_form.html', 
                {'form': acquisition_form, 'form_errors': acquisition_form.errors, 'info': acquisition_reference},
                context_instance=RequestContext(request))

@login_required
def acquisition_delete(request, slug,id):
    """This view deletes the acquisition info and redirects to the company page"""
    
    company =get_object_or_404(Company,slug=slug)
    edit = validate_user_company_access_or_redirect(request,company)

    if request.method == 'POST':
        return HttpResponseRedirect('/company/'+str(slug))
    else: 
        #verifies if the company exists if not returns a 404 page
        acquisition_reference = get_object_or_404(Acquisition, id=id,company=company)

        #deletes the view and redirects to the page.
        acquisition_reference.delete()
        return HttpResponseRedirect('/company/'+str(slug))



@login_required
def acquisition_view(request, slug, id):
    """This view makes possible to display a acquisition item alone"""
    company =get_object_or_404(Company,slug=slug)
    edit = validate_user_company_access_or_redirect(request,company)
    acquisition_reference = get_object_or_404(Acquisition, id=id,company=company)

    return render_to_response('acquisition_form.html', 
                {'details': acquisition_reference,'info':acquisition_reference},
                context_instance=RequestContext(request))


