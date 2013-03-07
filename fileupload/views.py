from fileupload.models import Picture
from fileupload.forms import PictureForm
from companies.functions import *
from companies.models import Company
from django.views.generic import CreateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404, render 
from django.template import RequestContext, Context

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils import simplejson
from django.core.urlresolvers import reverse

from django.conf import settings

def response_mimetype(request):
    if "application/json" in request.META['HTTP_ACCEPT']:
        return "application/json"
    else:
        return "text/plain"

class PictureCreateView(CreateView):
    model = Picture

    def form_valid(self, form):
        self.object = form.save()
        f = self.request.FILES.get('file')
        data = [{'name': f.name, 'url': settings.MEDIA_URL + "pictures/" + f.name.replace(" ", "_"), 'thumbnail_url': settings.MEDIA_URL + "pictures/" + f.name.replace(" ", "_"), 'delete_url': reverse('upload-delete', args=[self.object.id]), 'delete_type': "DELETE"}]
        response = JSONResponse(data, {}, response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response


class PictureDeleteView(DeleteView):
    model = Picture

    def delete(self, request, *args, **kwargs):
        """
        This does not actually delete the file, only the database record.  But
        that is easy to implement.
        """
        self.object = self.get_object()
        self.object.delete()
        if request.is_ajax():
            response = JSONResponse(True, {}, response_mimetype(self.request))
            response['Content-Disposition'] = 'inline; filename=files.json'
            return response
        else:
            return HttpResponseRedirect('/upload/new')

class JSONResponse(HttpResponse):
    """JSON response class."""
    def __init__(self,obj='',json_opts={},mimetype="application/json",*args,**kwargs):
        content = simplejson.dumps(obj,**json_opts)
        super(JSONResponse,self).__init__(content,mimetype,*args,**kwargs)



##################################################################################################################
################################################ Customer Views #############################################
##################################################################################################################

def picture_create(request, slug):
    """The purpose of this function is to create  new customers item associated with a created company"""
    #verifies if the company exists if not returns a 404 page
    company =get_object_or_404(Company,slug=slug)
    edit = validate_user_company_access_or_redirect(request,company)
    #if the request is GET presents empty form
    if request.method == 'GET':

        picture_form = PictureForm()
        return render_to_response('picture_form.html', {'form': picture_form, 'company':company},
            context_instance=RequestContext(request))
     
    else:
        picture_form = PictureForm(request.POST, request.FILES)
        #if is POST Validates the form is well filled and save it redirecting to the company page
        if picture_form.is_valid():
            pf = picture_form.save(commit=False)
            pf.company = company
            pf.save()
            return HttpResponseRedirect('/company/'+str(slug))

        #if not well filled redirect to the original create and display error
        else:
            return render_to_response('picture_form.html', 
                {'form': picture_form, 'form_errors': picture_form.errors, 'company':company},
                context_instance=RequestContext(request))


def picture_update(request, slug, id):
    """The purpose of this view is to update the info of the customer page"""
    #verifies if the company exists if not returns a 404 page
    company =get_object_or_404(Company,slug=slug)
    picture_reference = get_object_or_404(Picture, id=id,company=company)
    picture_form = PictureForm(instance=picture_reference)

    #verifies the person has access to the company or is an incubator employee
    edit = validate_user_company_access_or_redirect(request,company)

    #if the request is GET presents info, 
    if request.method == 'GET':
        return render_to_response('picture_form.html',{'form':picture_form, 'info': picture_reference},context_instance=RequestContext(request))
    else:
        picture_form = PictureForm(request.POST)
        #if is POST Validates the form is well filled and save it redirecting to the company page 
        if picture_form.is_valid():
            pf = picture_form.save(commit = False)
            pf.company = company
            pf.save()

            return HttpResponseRedirect('/company/'+str(slug))
        #if not well filled redirect to the original update page and display error
        else:
            return render_to_response('picture_form.html', 
                {'form': picture_form, 'form_errors': picture_form.errors, 'info': picture_reference},
                context_instance=RequestContext(request))

@login_required
def picture_delete(request, slug,id):
    """This view deletes the award info and redirects to the company page"""
    
    company =get_object_or_404(Company,slug=slug)
    edit = validate_user_company_access_or_redirect(request,company)

    if request.method == 'POST':
        return HttpResponseRedirect('/company/'+str(slug))
    else: 
        #verifies if the company exists if not returns a 404 page
        picture_reference = get_object_or_404(Picture, id=id,company=company)

        #deletes the view and redirects to the page.
        picture_reference.delete()
        return HttpResponseRedirect('/company/'+str(slug))



@login_required
def picture_view(request, slug, id):
    """This view makes possible to display a award item alone"""
    company =get_object_or_404(Company,slug=slug)
    edit = validate_user_company_access_or_redirect(request,company)
    picture_reference = get_object_or_404(Picture, id=id,company=company)

    return render_to_response('picture_form.html', 
                {'details': picture_reference,'info':picture_reference},
                context_instance=RequestContext(request))
