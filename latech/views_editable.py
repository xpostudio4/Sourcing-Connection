#Django core utils
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.views.decorators.http import require_POST, require_http_methods
from django.core.urlresolvers import resolve

#Aplication models

from companies.models import *
from companies.forms import CustomerForm, AwardForm, CertificationForm, FundingForm, AcquisitionForm, ManagementForm, CompetitorsForm, OfficeForm

# testing Bootstrap editable


@require_POST
def form_fields2(request, id, model, field):
    model = get_object_or_404(Company, id=id)
    model.value_proposition = request.POST['value']
#    model.description = request.POST['value']
    model.save()
    return HttpResponse("aja")

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
def form_validation2(request, slug, model):
    models_form = {
        "CompanyLink": CompanyLinkForm(request.POST),
    }



    company = get_object_or_404(Company, slug=slug)
    form = models_form[model]

    if form.is_valid():
        f = form.save(commit=False)
        f.company = company
        f.save()
     
        d = { 
            'id': f.id, 
            'model': model,
            'company': company.name
            }

        if f.name:
            d['name'] = f.name
        return json_response(d)

    return json_response({ "errors":dict(form.errors.items()) })
