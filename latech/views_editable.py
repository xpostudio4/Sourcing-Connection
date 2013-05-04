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
def form_fields(request, id, field, model, value):
    model = get_object_or_404(Company, id=id)
    value = request.POST.get('value', '')
    model.value_proposition = value
    model.save()
    return HttpResponse(value)



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
