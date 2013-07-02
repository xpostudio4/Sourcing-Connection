#Django core utils
import json
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404, render
from django.views.decorators.http import require_POST, require_http_methods
from django.core.urlresolvers import resolve
from django.template import RequestContext, Context 
from django.template.defaultfilters import slugify


#Aplication models

from companies.models import *
from companies.forms import CustomerForm, AwardForm, CertificationForm, FundingForm, AcquisitionForm, ManagementForm,\
 CompetitorsForm, OfficeForm, CompanyLinkForm
from companies.functions import *
from company_profile_extended.models import *
from company_profile_extended.forms import *
from recommendations.models import Recommendation
from latech.forms import ContactForm, CompanyLogoForm, ProductImageForm
from contacts.models import *
from fileupload.models import *
from location.models import Country

# testing Bootstrap editable

def form_update(request, model, slug, id):
    company =get_object_or_404(Company,slug=slug)
    office_reference = get_object_or_404(Office, id=id,company=company)
#    office_form = OfficeForm(instance=office_reference)

    models ={
        "Office": OfficeForm(instance=office_reference),
    }
    return HttpResponse(models[model].as_p())


@require_POST
def company_create_modal(request):
    if request.method == 'POST':
        if request.POST.get('name') != "" or " ": 
            value = request.POST.get('name')
            val = Company.objects.filter(name__iexact=value)
            if val:
                message = u'%s <div id="alerts" class="alert alert-error" >Exists in DB </div>\
                    <div class="btn btn-danger"></div>' % value
            else:
                message = u'%s <div id="alerts" class="alert alert-success" >Not Exists in DB </div>\
                    <div class="btn btn-success">' % value
        else:
            message = 'Waiting for an Input'
    else:
        message =""
    return HttpResponse(json.dumps(message), mimetype="application/json")

@require_POST
def feature_names_modal(request):
    if request.method == 'POST':
        if request.POST.get('name') != "" or " ": 
            value = request.POST.get('name')
            val = Company.objects.filter(name__iexact=value)
            if val:
                message = u'%s <div id="alerts" class="alert alert-error" >Exists in DB </div>\
                    <div class="btn btn-danger"></div>' % value
            else:
                message = u'%s <div id="alerts" class="alert alert-success" >Not Exists in DB </div>\
                    <div class="btn btn-success">' % value
        else:
            message = 'Waiting for an Input'
    else:
        message =""
    return HttpResponse(json.dumps(message), mimetype="application/json")


def webmaster_contact(request):
    if request.method == 'POST': # If the form has been submitted...
        webmaster_contact_form = ContactForm(request.POST) # A form bound to the POST data
        if webmaster_contact_form.is_valid(): # All validation rules pass
            subject = ("%s sents the next message: %s") % (request.user,webmaster_contact_form.cleaned_data['subject'])
            message = webmaster_contact_form.cleaned_data['message']
            sender = request.user.email
            #cc_myself = webmaster_contact_form.cleaned_data['cc_myself']

            recipients = ['jalcantara@stancelabs.com', 'jeasoft@gmail.com']
#            if cc_myself:
#                recipients.append(sender)

            from django.core.mail import send_mail
            send_mail(subject, message, sender, recipients)

            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        webmaster_contact_form = ContactForm() # An unbound form


    return render(request, 'webmaster_form.html', {
        'form': webmaster_contact_form,
    })


@require_POST
def webmaster(request):

    if request.method == 'POST':
        subject = ("%s: %s") % (request.user.get_full_name(), request.REQUEST["msg_subject"])
        message = request.REQUEST["msg_content"]

        sender = request.user.email
        recipients = ['jalcantara@stancelabs.com', 'samuel@globaltechbridge.com']
        from django.core.mail import send_mail
        send_mail(subject, message, sender, recipients)

    return HttpResponse("")

@require_POST
def product_picture(request, id, slug):

    if request.method == 'POST':
        request.REQUEST["product-image"]
        product
    return HttpResponse("")



def company_edit(request, slug, **kwargs):

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
    fundings = Funding.objects.filter(company=company)
    pictures = Picture.objects.filter(company=company)
    companylinks = CompanyLink.objects.filter(company=company)

    # From Company Extended Profile
    partnerships = Partnership.objects.filter(company=company) 
    alliances = Alliance.objects.filter(company=company) 
    associations = TechnicalAssociation.objects.filter(company=company) 
    expertises = Expertise.objects.filter(company=company)
    verticals = Vertical.objects.filter(company=company)
    stories = SuccessStories.objects.filter(company=company)
    revenues = AnnualRevenue.objects.filter(company=company)
    milestones = Milestone.objects.filter(company=company)
    projects = Project.objects.filter(company=company)
    products = Product.objects.filter(company=company)
    #Recommendations
    recommendations = Recommendation.objects.filter(company=company)
    countries = Country.objects.all().order_by('id')
    industries = Category.objects.all().order_by('id')

    # Product Picture Form
#    product_reference = get_object_or_404(Product, id=request.GET["product_id"], company=company)
    company_logo_form = CompanyLogoForm(request.POST, request.FILES, instance=company)
#    image_reference = get_object_or_404(Product, id=id,company=company)
#    product_picture_form = ProductPictureForm(request.POST, request.FILES)#, instance=company.company_products__id)
    
    if request.method == 'POST':

#        if product_picture_form.is_valid():
#            product_picture_form.save()
    
        if company_logo_form.is_valid():
            company_logo_form.save()


    office_list = []
    count = 0
    
    for i in offices:
        count += 1
        if (count)%3==0:
            office_list.append({"object":i, "ul":True})
        else:
            office_list.append({"object":i})



    return render_to_response(
        "company_edit.html",
        {'company':company, 'companylinks':companylinks,'pictures':pictures, 'permission': edit, "percentage_profile": percentage_profile,
        'management': management,'offices':office_list, 'competitors': competitors,"certifications":certifications,
        "customers":customers, "awards":awards,"acquisitions":acquisitions, "fundings":fundings,  "pictures":pictures,
        # From Company Extended Profile
        "expertises":expertises, "verticals":verticals,"stories":stories,"revenues":revenues, "milestones":milestones,
        "projects":projects, "partnerships":partnerships, "alliances":alliances, "associations":associations,"products":products,
        # Recommendations
        "recommendations":recommendations,
        # Calling All objects from these models to update them in place
        "countries":countries,"industries":industries,
        #Picture Form
        #"product_picture_form":product_picture_form,#'product_reference':product_reference,
        "company_logo_form":company_logo_form,
         },
        context_instance=RequestContext(request))


def company_edit2(request, slug):


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
    #offices = Office.objects.filter(company=company)
    offices = company.office_set.all()


    acquisitions = Acquisition.objects.filter(company=company)
    fundings = Funding.objects.filter(company=company)
    pictures = Picture.objects.filter(company=company)
    companylinks = CompanyLink.objects.filter(company=company)
    # From Company Extended Profile
    partnerships = Partnership.objects.filter(company=company) 
    alliances = Alliance.objects.filter(company=company) 
    associations = TechnicalAssociation.objects.filter(company=company) 
    expertises = Expertise.objects.filter(company=company)
    verticals = Vertical.objects.filter(company=company)
    stories = SuccessStories.objects.filter(company=company)
    revenues = AnnualRevenue.objects.filter(company=company)
    milestones = Milestone.objects.filter(company=company)
    projects = Project.objects.filter(company=company)
    products = Product.objects.filter(company=company)
    #Recommendations
    recommendations = Recommendation.objects.filter(company=company)
    categories = Category.objects.all()


    office_list = []
    count = 0
    
    for i in offices:
        count += 1
        if (count)%3==0:
            office_list.append({"object":i, "ul":True})
        else:
            office_list.append({"object":i})



    return render_to_response(
        "company_edit2.html",
        {'company':company, 'companylinks':companylinks,'pictures':pictures, 'permission': edit, "percentage_profile": percentage_profile,
        'management': management,'offices':office_list, 'competitors': competitors,"certifications":certifications,
        "customers":customers, "awards":awards,"acquisitions":acquisitions, "fundings":fundings,  "pictures":pictures,
        # From Company Extended Profile
        "expertises":expertises, "verticals":verticals,"stories":stories,"revenues":revenues, "milestones":milestones,
        "projects":projects, "partnerships":partnerships, "alliances":alliances, "associations":associations,"products":products,
        # Recommendations
        "recommendations":recommendations,
         },
        context_instance=RequestContext(request))


@require_POST
def company_name_redirect(request):
    if request.method == 'POST':
        if request.POST.get('name') != "" or " ": 
            value = request.POST.get('name')
            company = Company.objects.create(name=value, slug=slugify(value), created_by=request.user)
            return HttpResponseRedirect('/company/%s' % company.slug)

@require_POST
def company_logo(request, slug):
    if request.method == 'POST':
        if request.FILES.get('file'): 
            file = request.FILES.get['file']
            company = get_object_or_404(Company, slug=slug, logo= file)
            company.save()
        return HttpResponse("")

            #return HttpResponseRedirect('/company/%s' % company.slug)


@require_POST
def company_name_verification(request):
    if request.method == 'POST':
        if request.POST.get('name') != "" or " ": 
            value = request.POST.get('name').strip()
            val = Company.objects.filter(name__iexact=value)
            if val:
                message = u'''<div class="alert alert-error"> <strong>%s</strong> Exists in DB
                    </div>''' % value
            else:

                message = u'<div class="alert alert-success" > <strong>%s</strong> Not Exists in DB </div>' % value
        else:
            message = 'Waiting for an Input'
    else:
        message =""
    return HttpResponse(json.dumps(message), mimetype="application/json")


@require_POST
def form_fields(request, id, model, field):

    value = request.POST['value']

    if model == "Company":

        o_model = get_object_or_404(Company, id=id)

        if field == "overview":
            o_model.overview = value
        elif field == "value_proposition":
            o_model.value_proposition = value
        elif field == "description":
            o_model.description = value
        elif field == "company_status":
            o_model.company_status = value 
        elif field == "employee_quantity":
            o_model.employee_quantity = value
        elif field == "founding_date":
            o_model.founding_date = value
        elif field == "main_phone":
            o_model.main_phone = value
        elif field == "logo":
            o_model.logo = value
        elif field == "email":
            o_model.email = value
        elif field == "industries":
            o_model.industries = value
        elif field == "technologies":
            o_model.technologies = value
        elif field == "applications":
            o_model.applications = value
        elif field == "tags":
            o_model.tags = value
        elif field == "country":
            country = Country.objects.get(id=value)
            o_model.country = country
        elif field == "categories":
            categories = Category.objects.get(id=value)
            o_model.categories = categories

#            country = Country.objects.get()
 #           Country.objects.get(country=value)
        else:
            o_model.contact = value

    if model =="CompanyLink":

        o_model = get_object_or_404(CompanyLink, id=id)


        if field == "web_url":
            o_model.web_url = value
        elif  field == "linkedin_url":
            o_model.linkedin_url = value
        elif field == "blog_url":
            o_model.blog_url  = value
        elif field == "twitter_url":
            o_model.twitter_url  = value
        else:
            o_model.facebook_link = value

    if model =="Management":

        o_model = get_object_or_404(Management, id=id)

        if field == "full_name":
            o_model.full_name = value
        else:
            o_model.title = value

    if model == "Funding":

        o_model = get_object_or_404(Funding, id=id)

        if field == "round":
            o_model.round = value
        else:
            o_model.raised = value

    if model == "Acquisition":

        o_model = get_object_or_404(Acquisition, id=id)

        if field == "name":
            o_model.name = value
        elif field == "price":
            o_model.price = value
        elif field == "acquired_date":
            o_model.acquired_date = value
        else:
            o_model.terms = value

    if model == "Competitors":
        o_model = get_object_or_404(Competitors, id=id)
        o_model.name = value


    if model == "Certification":
        o_model = get_object_or_404(Certification, id=id)
        o_model.name = value

    if model == "Customer":
        o_model = get_object_or_404(Customer, id=id)
        o_model.name = value

    if model == "Award":
        o_model = get_object_or_404(Award, id=id)
        
        if field == "name":
            o_model.name = value
        else: 
            o_model.date = value

     # From Company Extended Profile
    if model == "Expertise":
        o_model = get_object_or_404(Expertise, id=id)
        o_model.name = value

    if model == "Vertical":
        o_model = get_object_or_404(Vertical, id=id)
        o_model.name = value
        o_model.slug = slugify(value)

    if model == "Partnership":
        o_model = get_object_or_404(Partnership, id=id)
        o_model.name = value

    if model == "TechnicalAssociation":
        o_model = get_object_or_404(TechnicalAssociation, id=id)
        o_model.name = value

    if model == "Alliance":
        o_model = get_object_or_404(Alliance, id=id)
        o_model.name = value

    if model == "SuccessStories":
        o_model = get_object_or_404(SuccessStories, id=id)
        o_model.title = value


    if model == "Product":
        o_model = get_object_or_404(Product, id=id)
        if field == "name":
            o_model.name = value
        elif field == "price":
            o_model.price = value
        elif field == "product_image":
            o_model.product_image = value


#    if model == "Vertical":
#        o_model = get_object_or_404(Vertical, id=id)
#        o_model.vertical = value

    o_model.save()

    return HttpResponse("")



@require_POST
def user_form_fields(request, id, model, field):

    value = request.POST['value']

    if model == "Contact":

        o_model = get_object_or_404(Contact, id=id)

        if field == "fr_name":
            o_model.fr_name = value

        elif field == "ls_name":
            o_model.ls_name  = value
        elif field == "email":
            o_model.email  = value
        elif field == "overview":
            o_model.overview  = value
        elif field == "phone":
            o_model.phone  = value
        elif field == "country":
            o_model.country  = value
        elif field == "city":
            o_model.city  = value
        elif field == "degrees":
            o_model.degrees  = value
        elif field == "tags":
            o_model.tags  = value
        elif field == "company":
            o_model.company  = value
        elif field == "financial_organization":
            o_model.financial_organization  = value
        elif field == "government_organization":
            o_model.government_organization  = value
        elif field == "title":
            o_model.title  = value
        elif field == "industry":
            o_model.industry  = value
        elif field == "technology":
            o_model.technology  = value
        elif field == "application":
            o_model.application  = value

    if model == "Contact_Urls":
        o_model = get_object_or_404(Contact_Urls, id=id)

        if field == "ld_url":
            o_model.ld_url = value

        elif field == "t_url":
            o_model.t_url  = value
        elif field == "blog_url":
            o_model.blog_url  = value
        elif field == "ext_url":
            o_model.ext_url  = value

    o_model.save()

    return HttpResponse("")

def logo_update(request, slug):
    """The purpose of this view is to update the info of the management page"""
    #verifies if the company exists if not returns a 404 page
    company =get_object_or_404(Company,slug=slug)
    logo_form = CompanyLogoForm(instance=company)

    #verifies the person has access to the company or is an incubator employee
    edit = validate_user_company_access_or_redirect(request,company)

    #if the request is GET presents info, 
    if request.method == 'GET':
        return render_to_response('pictures.html',{'form':logo_form },context_instance=RequestContext(request))
    else:
        logo_form = CompanyLogoForm(request.POST, request.FILES, instance=company)
        #if is POST Validates the form is well filled and save it redirecting to the company page 
        if logo_form.is_valid():
            logo_form.save()


            # To FIX
            return HttpResponseRedirect('/company/%s/edit/' % str(slug))
        #if not well filled redirect to the original update page and display error
        else:
            return render_to_response('pictures.html', 
                {'form': logo_form, 'form_errors': logo_form.errors},
                context_instance=RequestContext(request))


def product_image_update(request, slug, id):
    """The purpose of this view is to update the info of the management page"""
    #verifies if the company exists if not returns a 404 page
    company =get_object_or_404(Company,slug=slug)
    image_reference = get_object_or_404(Product, id=id,company=company)
    product_image_form = ProductImageForm(instance=image_reference)

    #verifies the person has access to the company or is an incubator employee
    edit = validate_user_company_access_or_redirect(request,company)

    #if the request is GET presents info, 
    if request.method == 'GET':
        return render_to_response('pictures.html',{'form':product_image_form },context_instance=RequestContext(request))
    else:
        product_image_form = ProductImageForm(request.POST, request.FILES, instance=image_reference)
        #if is POST Validates the form is well filled and save it redirecting to the company page 
        if product_image_form.is_valid():
            product_image_form.save()


            # To FIX
            return HttpResponseRedirect('/company/%s/edit/' % str(slug))
        #if not well filled redirect to the original update page and display error
        else:
            return render_to_response('pictures.html', 
                {'form': product_image_form, 'form_errors': product_image_update.errors},
                context_instance=RequestContext(request))
