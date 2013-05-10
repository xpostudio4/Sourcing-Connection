#Django core utils
import json
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.views.decorators.http import require_POST, require_http_methods
from django.core.urlresolvers import resolve
from django.template import RequestContext, Context


#Aplication models

from companies.models import *
from companies.forms import CustomerForm, AwardForm, CertificationForm, FundingForm, AcquisitionForm, ManagementForm, CompetitorsForm, OfficeForm
from contacts.models import *
# testing Bootstrap editable

def form_update(request, model, slug, id):
    company =get_object_or_404(Company,slug=slug)
    office_reference = get_object_or_404(Office, id=id,company=company)
#    office_form = OfficeForm(instance=office_reference)

    models ={
        "Office": OfficeForm(instance=office_reference),
    }
    return HttpResponse(models[model].as_p())

def sss(request):

    return render_to_response('test.html', context_instance=RequestContext(request) )

@require_POST
def ssss(request):
    if request.method == 'POST':
        if request.POST.get('name') != "" or " ": 
            value = request.POST.get('name')
            val = Company.objects.filter(name__iexact=value)
            if val:
                message = u'%s <div class="alert alert-error" >Exists in DB </div>\
                    <div class="btn btn-danger"></div>' % value
            else:
                message = u'%s <div class="alert alert-success" >Not Exists in DB </div>\
                    <div class="btn btn-success">' % value
        else:
            message = 'Waiting for an Input'
    else:
        message =""
    return HttpResponse(json.dumps(message), mimetype="application/json")

@require_POST
def company_create_modal(request):
    if request.method == 'POST':
        if request.POST.get('name') != "" or " ": 
            value = request.POST.get('name')
            val = Company.objects.filter(name__iexact=value)
            if val:
                message = u'%s <div class="alert alert-error" >Exists in DB </div>\
                    <div class="btn btn-danger"></div>' % value
            else:
                message = u'%s <div class="alert alert-success" >Not Exists in DB </div>\
                    <button class="btn btn-primary" type="button">Create Company</button>' % value
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
        elif field == "main_phone":
            o_model.main_phone = value
        elif field == "email":
            o_model.email = value
        elif field == "industries":
            o_model.industries = value
        elif field == "technologies":
            o_model.technologies = value
        elif field == "applications":
            o_model.applications = value
        elif field == "country":
            o_model.country = value
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
        o_model = get_object_or_404(Customer, id=id)
        
        if field == "name":
            o_model.name = value
        else: 
            o_model.date = value



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
