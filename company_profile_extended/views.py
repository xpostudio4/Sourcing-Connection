#Django files
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Context
from django.utils.decorators import method_decorator

#Latech Apps
from companies.models import Company
from companies.functions import *
from company_profile_extended.models import *
from company_profile_extended.forms import *

@login_required
def revenue_delete(request, slug,id):
    """This view deletes the revenue info and redirects to the company page"""
    
    company =get_object_or_404(Company,slug=slug)
    edit = validate_user_company_access_or_redirect(request,company)

    if request.method == 'POST':
        return HttpResponseRedirect('/company/'+str(slug))
    else: 
        #verifies if the company exists if not returns a 404 page
        revenue_reference = get_object_or_404(AnnualRevenue, id=id,company=company)

        #deletes the view and redirects to the page.
        revenue_reference.delete()
        return HttpResponseRedirect('/company/'+str(slug))

@login_required
def milestone_delete(request, slug,id):
    """This view deletes the milestone info and redirects to the company page"""
    
    company =get_object_or_404(Company,slug=slug)
    edit = validate_user_company_access_or_redirect(request,company)

    if request.method == 'POST':
        return HttpResponseRedirect('/company/'+str(slug))
    else: 
        #verifies if the company exists if not returns a 404 page
        milestone_reference = get_object_or_404(Milestone, id=id,company=company)

        #deletes the view and redirects to the page.
        milestone_reference.delete()
        return HttpResponseRedirect('/company/'+str(slug))

@login_required
def vertical_delete(request, slug,id):
    """This view deletes the vertical info and redirects to the company page"""
    
    company =get_object_or_404(Company,slug=slug)
    edit = validate_user_company_access_or_redirect(request,company)

    if request.method == 'POST':
        return HttpResponseRedirect('/company/'+str(slug))
    else: 
        #verifies if the company exists if not returns a 404 page
        vertical_reference = get_object_or_404(Vertical, id=id,company=company)

        #deletes the view and redirects to the page.
        vertical_reference.delete()
        return HttpResponseRedirect('/company/'+str(slug))

@login_required
def partnership_delete(request, slug,id):
    """This view deletes the partnership info and redirects to the company page"""
    
    company =get_object_or_404(Company,slug=slug)
    edit = validate_user_company_access_or_redirect(request,company)

    if request.method == 'POST':
        return HttpResponseRedirect('/company/'+str(slug))
    else: 
        #verifies if the company exists if not returns a 404 page
        partnership_reference = get_object_or_404(Partnership, id=id,company=company)

        #deletes the view and redirects to the page.
        partnership_reference.delete()
        return HttpResponseRedirect('/company/'+str(slug))

def partnership_create(request, slug):
    """The purpose of this function is to create  new Partnership item associated with a created company"""
    #verifies if the company exists if not returns a 404 page
    company =get_object_or_404(Company,slug=slug)
    edit = validate_user_company_access_or_redirect(request,company)
    #if the request is GET presents empty form
    if request.method == 'GET':

        partnership_form = PartnershipForm()
        return render_to_response('award_form.html', {'form': partnership_form, 'company':company},
            context_instance=RequestContext(request))
     
    else:
        partnership_form = PartnershipForm(request.POST)
        #if is POST Validates the form is well filled and save it redirecting to the company page
        if partnership_form.is_valid():
            of = partnership_form.save(commit=False)
            of.company = company
            of.save()
            return HttpResponseRedirect('/company/'+str(slug))

        #if not well filled redirect to the original create and display error
        else:
            return render_to_response('certification_form.html', 
                {'form': partnership_form, 'form_errors': partnership_form.errors, 'company':company},
                context_instance=RequestContext(request))


@login_required
def association_delete(request, slug,id):
    """This view deletes the association info and redirects to the company page"""
    
    company =get_object_or_404(Company,slug=slug)
    edit = validate_user_company_access_or_redirect(request,company)

    if request.method == 'POST':
        return HttpResponseRedirect('/company/'+str(slug))
    else: 
        #verifies if the company exists if not returns a 404 page
        association_reference = get_object_or_404(TechnicalAssociation, id=id,company=company)

        #deletes the view and redirects to the page.
        association_reference.delete()
        return HttpResponseRedirect('/company/'+str(slug))

@login_required
def story_delete(request, slug,id):
    """This view deletes the Success Story info and redirects to the company page"""
    
    company =get_object_or_404(Company,slug=slug)
    edit = validate_user_company_access_or_redirect(request,company)

    if request.method == 'POST':
        return HttpResponseRedirect('/company/'+str(slug))
    else: 
        #verifies if the company exists if not returns a 404 page
        story_reference = get_object_or_404(SuccessStories, id=id,company=company)

        #deletes the view and redirects to the page.
        story_reference.delete()
        return HttpResponseRedirect('/company/'+str(slug))

@login_required
def expertise_delete(request, slug,id):
    """This view deletes the expertise info and redirects to the company page"""
    
    company =get_object_or_404(Company,slug=slug)
    edit = validate_user_company_access_or_redirect(request,company)

    if request.method == 'POST':
        return HttpResponseRedirect('/company/'+str(slug))
    else: 
        #verifies if the company exists if not returns a 404 page
        expertise_reference = get_object_or_404(Expertise, id=id,company=company)

        #deletes the view and redirects to the page.
        expertise_reference.delete()
        return HttpResponseRedirect('/company/'+str(slug))

@login_required
def project_delete(request, slug,id):
    """This view deletes the project info and redirects to the company page"""
    
    company =get_object_or_404(Company,slug=slug)
    edit = validate_user_company_access_or_redirect(request,company)

    if request.method == 'POST':
        return HttpResponseRedirect('/company/'+str(slug))
    else: 
        #verifies if the company exists if not returns a 404 page
        project_reference = get_object_or_404(Project, id=id,company=company)

        #deletes the view and redirects to the page.
        project_reference.delete()
        return HttpResponseRedirect('/company/'+str(slug))

@login_required
def product_delete(request, slug,id):
    """This view deletes the product info and redirects to the company page"""
    
    company =get_object_or_404(Company,slug=slug)
    edit = validate_user_company_access_or_redirect(request,company)

    if request.method == 'POST':
        return HttpResponseRedirect('/company/'+str(slug))
    else: 
        #verifies if the company exists if not returns a 404 page
        product_reference = get_object_or_404(Product, id=id,company=company)

        #deletes the view and redirects to the page.
        product_reference.delete()
        return HttpResponseRedirect('/company/'+str(slug))

@login_required
def alliance_delete(request, slug,id):
    """This view deletes the alliance info and redirects to the company page"""
    
    company =get_object_or_404(Company,slug=slug)
    edit = validate_user_company_access_or_redirect(request,company)

    if request.method == 'POST':
        return HttpResponseRedirect('/company/'+str(slug))
    else: 
        #verifies if the company exists if not returns a 404 page
        alliance_reference = get_object_or_404(Alliance, id=id,company=company)

        #deletes the view and redirects to the page.
        alliance_reference.delete()
        return HttpResponseRedirect('/company/'+str(slug))