#Django core utils
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core import serializers
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Context
from django.utils import simplejson
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST, require_http_methods

#Aplication models

from companies.models import *
from companies.forms import CustomerForm, AwardForm, CertificationForm, \
    FundingForm, AcquisitionForm, ManagementForm, CompetitorsForm, OfficeForm, ManagementPictureForm, CompanyLinkForm
from company_profile_extended.models import *
from company_profile_extended.forms import *
from contacts.models import *
from fileupload.forms import PictureForm
from latech.asana import AsanaAPI, AsanaException
from latech.forms import SearchForm, CompanySearchForm, ContactSearchForm, TicketForm
from taxonomy.models import *

#third party libraries
from bs4 import BeautifulSoup
import csv
import operator
import requests



def json_response(x):
    import json
    return HttpResponse(json.dumps(x, sort_keys=True, indent=2),
                        content_type='application/json; charset=UTF-8')

def form_create(request, model):
    models ={
        "Customer": CustomerForm(),
        "Award": AwardForm(),
        "Certification": CertificationForm(),
        "Funding": FundingForm(),
        "Acquisition": AcquisitionForm(),
        "Management":ManagementForm(),
        "ManagementPicture":ManagementPictureForm(),
        "Competitor": CompetitorsForm(),
        "Picture": PictureForm(),
        "Office": OfficeForm(),
        "CompanyLink": CompanyLinkForm(),
        # from company_profile_extended
        "Partnership":PartnershipForm(), 
        "Alliance":AllianceForm(),
        "TechnicalAssociation":TechnicalAssociationForm(),
        "Milestone":MilestoneForm(),
        "Project":ProjectForm(),
        "Product":ProductForm(),
        "SuccessStories":SuccessStoriesForm(),
        "Expertise":ExpertiseForm(),
        "Vertical":VerticalForm(),
        "AnnualRevenue":AnnualRevenueForm(),

    }
    return HttpResponse(models[model].as_p())


@require_POST
def form_validation(request, slug, model):
    models_form = {
        "Customer": CustomerForm(request.POST),
        "Award": AwardForm(request.POST),
        "Certification": CertificationForm(request.POST),
        "Funding": FundingForm(request.POST),
        "Acquisition": AcquisitionForm(request.POST),
        "Management":ManagementForm(request.POST),
        "ManagementPicture":ManagementPictureForm(request.POST, request.FILES),
        "Competitor": CompetitorsForm(request.POST),
        "Picture": PictureForm(request.POST, request.FILES),
        "Office": OfficeForm(request.POST),
        # From Company Extended Profile
        "Partnership":PartnershipForm(request.POST), 
        "Alliance":AllianceForm(request.POST),
        "TechnicalAssociation":TechnicalAssociationForm(request.POST),
        "Milestone":MilestoneForm(request.POST),
        "Project":ProjectForm(request.POST),
        "Product":ProductForm(request.POST),
        "SuccessStories":SuccessStoriesForm(request.POST),
        "Expertise":ExpertiseForm(request.POST),
        "Vertical":VerticalForm(request.POST),
        "AnnualRevenue":AnnualRevenueForm(request.POST),

    }


    company = get_object_or_404(Company, slug=slug)
    form = models_form[model]

    if form.is_valid():
        f = form.save(commit=False)
        f.company = company
        f.save()

        instance_models = {
            "Customer": Customer.objects.filter(id=f.id),
        }

        if model == "Acquisition":

            context = Acquisition.objects.get(id=f.id)
            
            template = """

                <div id="acquisitions-{{ acquisition.id }}"><a class="link-delete" data-type="acquisitions" data-id="{{ acquisition.id }}" id="{{ company.slug }}-acquisitions-{{ acquisition.id }}" href="/company/{{ company.slug }}/acquisitions/{{ acquisition.id }}/delete"><i class="icon-remove"></i></a>  <text data-type="text" data-model="Acquisition" data-url="/formfields/Acquisition/{{ acquisition.id }}/name/" data-pk="{{ acquisition.id }}" class="editable-value" data-title="Acquired Name">{{ acquisition.name }}</text> <i class="icon-pencil"></i></div>

            """

            template = template.replace("{{ company.slug }}", str(company.slug)).replace("{{ acquisition.id }}", str(context.id))
            template = template.replace("{{ acquisition.name }}", str(context.name))


        elif model == "Award":

            context = Award.objects.get(id=f.id)
            
            template = """
                <div id="awards-{{ award.id }}"><a class="link-delete" data-type="awards" data-id="{{ award.id }}" id="{{ company.slug }}-awards-{{ award.id }}"  href="/company/{{ company.slug }}/awards/{{ award.id }}/delete"><i class="icon-remove"></i></a>  <text data-type="text" data-model="Award" data-url="/formfields/Award/{{ award.id }}/name/" data-pk="{{ award.id }}" class="editable-value" data-title="Award Name">{{ award.name }}</text> <i class="icon-pencil"></i></div>
            """

            template = template.replace("{{ company.slug }}", str(company.slug)).replace("{{ award.id }}", str(context.id))
            template = template.replace("{{ award.name }}", str(context.name))

        elif model == "Certification":

            context = Certification.objects.get(id=f.id)
            
            template = """
                <div id="certifications-{{ certification.id }}"><a class="link-delete" data-type="certifications" data-id="{{ certification.id }}" 
                id="{{ company.slug }}-certifications-{{ certification.id }}"  href="/company/{{ company.slug }}/certifications/{{ certification.id }}/delete">
                <i class="icon-remove"></i></a>  <text data-type="text" data-model="Certification" data-url="/formfields/Certification/{{ certification.id }}/name/"
                data-pk="{{ certification.id }}"  data-title="Certification" class="editable-value" >{{ certification.name }}</text> <i class="icon-pencil"></i></div>

            """

            template = template.replace("{{ company.slug }}", str(company.slug)).replace("{{ certification.id }}", str(context.id))
            template = template.replace("{{ certification.name }}", str(context.name))


        elif model == "Competitor":

            context = Competitor.objects.get(id = f.id)

            template = """
                <li id="competitors-{{ competitor.id }}">
                    <a class="link-delete" data-type="competitors" data-id="{{ competitor.id }}" id="{{ company.slug }}-competitors-{{ competitor.id }}" href="/company/{{ company.slug }}/competitors/{{ competitor.id }}/delete"><i class="icon-remove"></i></a>  
                    <a href="/company/{{ company.slug }}/competitors/{{ competitor.id }}/update">{{ competitor.name }}</a>
                </li>

            """

            template = template.replace("{{ company.slug }}", str(company.slug)).replace("{{ competitor.id }}", str(context.id))
            template = template.replace("{{ competitor.name }}", str(context.name))

        elif   model == "Customer":
            """Here is created the Customer model template to be returned via http request"""

            context = Customer.objects.get(id=f.id)

            template = """
                <li id="customers-{{ customer.id }}">
                <a class="link-delete" data-type="customers" data-id="{{ customer.id }}"  id="{{ company.slug }}-customers-{{ customer.id }}" href="/company/{{ company.slug }}/customers/{{ customer.id }}/delete" ><i class="icon-remove"></i></a>  
                <a href="/company/{{ company.slug }}/customers/{{ customer.id }}/update">{{ customer.name }}</a>
                </li>

            """

            template = template.replace("{{ company.slug }}", str(company.slug)).replace("{{ customer.id }}", str(context.id))
            template = template.replace("{{ customer.name }}", str(context.name))
        
        elif model == "Funding":

            context = Funding.objects.get(id=f.id)

            template = """
                <li id="fundings-{{ funding.id }}">
                    <a class="link-delete" data-type="fundings" data-id="{{ funding.id }}" id="{{ company.slug }}-fundings-{{ funding.id }}"  href="/company/{{ company.slug }}/fundings/{{ funding.id }}/delete"><i class="icon-remove"></i></a>
                    <a href="/company/{{ company.slug }}/fundings/{{ funding.id }}/update">{{ funding.round }}</a> 
                 <p> US$ {{ funding.raised }}</p>
                 </li>

            """

            template = template.replace("{{ company.slug }}", str(company.slug)).replace("{{ certification.id }}", str(context.id))
            template = template.replace("{{ certification.name }}", str(context.name))

        elif model == "Alliance":

            context = Alliance.objects.get(id=f.id)

            template = """

                <div id="alliances-{{ alliance.id }}"><a class="link-delete" data-type="alliances" data-id="{{ alliance.id }}" id="{{ company.slug }}-alliances-{{ alliance.id }}"  href="/company/{{ company.slug }}/alliances/{{ alliance.id }}/delete"><i class="icon-remove"></i></a>  <text data-type="text" data-model="Alliance" data-url="/formfields/Alliance/{{ alliance.id }}/name/" data-pk="{{ alliance.id }}"  data-title="alliance" class="editable-value" >{{ alliance.name }}</text> <i class="icon-pencil"></i></div>
            """

            template = template.replace("{{ company.slug }}", str(company.slug)).replace("{{ alliance.id }}", str(context.id))
            template = template.replace("{{ alliance.name }}", str(context.name))

            
        elif model == "Management":

            context = Management.objects.get(id=f.id)
            
            template = """
                <ul id="management-{{ manager.id }}" class="nav nav-list pull-left">
                    <li>
                        <a class="link-delete" data-type="management" data-id="{{ manager.id }}" id="{{ company.slug }}-management-{{ manager.id }}" href="/company/{{ company.slug }}/management/{{ manager.id }}/delete">
                            <i class="icon-remove"></i>
                        </a>
                    </li>

            <h5 class="media-heading text-info"> <a href="/company/{{ company.slug }}/management/{{ manager.id }}/update">{{ manager.full_name }}</a></h5>
                <p> {{ manager.title }}</p>
            </ul>

            """

            template = template.replace("{{ company.slug }}", str(company.slug)).replace("{{ manager.id }}", str(context.id))
            template = template.replace("{{ manager.title }}", str(context.title)).replace("{{ manager.full_name }}", str(context.full_name))
        
        elif model == "Office":
            context = Office.objects.get(id=f.id)

            template="""
            <li  id="office-{{ office.object.id }}" >
                <a class="link-delete pull-left" data-type="office" data-id="{{ office.object.id }}" id="{{ company.slug }}-office-{{ office.object.id }}" href="/company/{{ company.slug }}/office/{{ office.object.id }}/delete"><i class="icon-remove"></i></a>
                <address>
                    <strong><a href="/company/{{ company.slug }}/office/{{ office.object.id }}/update">{{ office.object.country }}</a></strong><br>
                    {{ office.object.description }}<br>
                    {{ office.object.address_1 }}<br>
                    {{ office.object.address_2 }}<br>
                      <abbr title="Phone">P:</abbr> {{ office.object.phone }}<br>
                </address>
            </li>
            """

            template = template.replace("{{ company.slug }}", str(company.slug)).replace("{{ office.object.id }}", str(context.id))
            template = template.replace("{{ office.object.description }}", str(context.description))
            template = template.replace("{{ office.object.address_1 }}", str(context.address_1))
            template = template.replace("{{ office.object.address_2 }}", str(context.address_2))
            template = template.replace("{{ office.object.phone }}", str(context.phone))

        elif model == "Picture":

            context = Picture.objects.get(id = f.id)

            template = """
                <li id="pictures-{{ picture.id }}" class="span2"> 
                <a class="link-delete" data-type="pictures" data-id="{{ picture.id }}" id="{{ company.slug }}-pictures-{{ picture.id }}" onclick="{{ company.slug }}_pictures_{{ picture.id }}(); return false;" href="/company/{{ company.slug }}/pictures/{{ picture.id }}/delete"><i class="icon-remove"></i></a>  
                <a class="gallery" href="{{ MEDIA_URL }}{{ picture.file }}" > <img data-src="holder.js/160x120" src="{{ MEDIA_URL }}{{ picture.file }}" width="160" height="160"> </a>
                </li>
            """
            
            template = template.replace("{{ company.slug }}", str(company.slug)).replace("{{ picture.id }}", str(context.id))
            template = template.replace("{{ picture.file }}", context.file )

        elif model == "ManagementPicture":

            manager = get_object_or_404(Management, pk=pk)
            context = ManagementPicture.objects.get(id=f.id)

            template = """
                <li id="managerpictures-{{ managementpicture.id }}" class="span2"> 
                <a class="link-delete" data-type="managementpictures" data-id="{{ managementpicture.id }}" id="{{ company.slug }}-managementpictures-{{ managementpicture.id }}" onclick="{{ company.slug }}_managementpictures_{{ managementpicture.id }}(); return false;" href="/company/{{ company.slug }}/management/{{ manager.pk }}/pictures/{{ managementpicture.id }}/delete"><i class="icon-remove"></i></a>  
                <a class="gallery" href="{{ MEDIA_URL }}{{ picture.file }}" > <img  data-src="holder.js/160x120" src="{{ MEDIA_URL }}{{ picture.file }}" width="160" height="160"> </a>
                </li>
            """
            
            template = template.replace("{{ company.slug }}", str(company.slug)).replace("{{ picture.id }}", str(context.id))
            template = template.replace("{{ picture.file }}", context.file )

        # For Company extended Profile

        elif   model == "Vertical":
            """Here is created the Vertical model template to be returned via http request"""

            context = Vertical.objects.get(id=f.id)

            template = """
                <div id="verticals-{{ vertical.id }}"><a class="link-delete" data-type="verticals" data-id="{{ vertical.id }}" id="{{ company.slug }}-verticals-{{ vertical.id }}" href="/company/{{ company.slug }}/verticals/{{ vertical.id }}/delete"><i class="icon-remove"></i></a><text data-type="text" data-model="Vertical" data-url="/formfields/Vertical/{{ vertical.id }}/vertical/" data-pk="{{ vertical.id }}" class="editable-value" data-title="Vertical Name">{{ vertical.name }}</text> <i class="icon-pencil"></i></div>

            """

            template = template.replace("{{ company.slug }}", str(company.slug)).replace("{{ vertical.id }}", str(context.id))
            template = template.replace("{{ vertical.name }}", str(context.name))

        elif   model == "Expertise":
            """Here is created the expertise model template to be returned via http request"""

            context = Expertise.objects.get(id=f.id)

            template = """
                <div id="expertises-{{ expertise.id }}"><a class="link-delete" data-type="expertises" data-id="{{ expertise.id }}" 
                id="{{ company.slug }}-expertises-{{ expertise.id }}" href="/company/{{ company.slug }}/expertises/{{ expertise.id }}/delete">
                <i class="icon-remove"></i></a>  <text data-type="text" data-model="Expertise" data-url="/formfields/Expertise/{{ expertise.id }}/name/" 
                data-pk="{{ expertise.id }}" class="editable-value" data-title="Expertises">{{ expertise.name }}</text> <i class="icon-pencil"></i></div>

            """

            template = template.replace("{{ company.slug }}", str(company.slug)).replace("{{ expertise.id }}", str(context.id))
            template = template.replace("{{ expertise.name }}", str(context.name))

        elif   model == "Partnership":
            """Here is created the expertise model template to be returned via http request"""

            context = Partnership.objects.get(id=f.id)

            template = """
                <div id="partnerships-{{ partnership.id }}"><a class="link-delete" data-type="partnerships" data-id="{{ partnership.id }}" id="{{ company.slug }}-partnerships-{{ partnership.id }}"  href="/company/{{ company.slug }}/partnerships/{{ partnership.id }}/delete"><i class="icon-remove"></i></a>  <text data-type="text" data-model="Partnership" data-url="/formfields/Partnership/{{ partnership.id }}/name/" data-pk="{{ partnership.id }}"  data-title="partnership" class="editable-value" >{{ partnership.name }}</text> <i class="icon-pencil"></i></div>
                        
            """

            template = template.replace("{{ company.slug }}", str(company.slug)).replace("{{ expertise.id }}", str(context.id))
            template = template.replace("{{ partnership.name }}", str(context.name))


        elif   model == "TechnicalAssociation":
            """Here is created the Technical Associations model template to be returned via http request"""

            context = TechnicalAssociation.objects.get(id=f.id)

            template = """

                <div id="associations-{{ association.id }}"><a class="link-delete" data-type="associations" data-id="{{ association.id }}" id="{{ company.slug }}-associations-{{ association.id }}"  href="/company/{{ company.slug }}/associations/{{ association.id }}/delete"><i class="icon-remove"></i></a>  <text data-type="text" data-model="TechnicalAssociation" data-url="/formfields/TechnicalAssociation/{{ association.id }}/name/" data-pk="{{ association.id }}"  data-title="association" class="editable-value" >{{ association.name }}</text> <i class="icon-pencil"></i></div>
                        
            """

            template = template.replace("{{ company.slug }}", str(company.slug)).replace("{{ association.id }}", str(context.id))
            template = template.replace("{{ association.name }}", str(context.name))


        elif   model == "Product":
            """Here is created the Product model template to be returned via http request"""

            context = Product.objects.get(id=f.id)

            template = """
            
                <td id="products-{{ product.id }}" data-type="text" data-model="Product" data-url="/formfields/Product/{{ product.id }}/name/" data-pk="{{ product.id }}" class="editable-value" data-title="Product Name"><a class="link-delete" data-type="products" data-id="{{ product.id }}" id="{{ company.slug }}-products-{{ product.id }}" href="/company/{{ company.slug }}/products/{{ product.id }}/delete"><i class="icon-remove"></i></a>{{ product.name }}<i class="icon-pencil"></i></td>

                <td data-type="text" class="products-{{ product.id }} editable-value" data-model="Product" data-url="/formfields/Product/{{ product.id }}/price/" data-pk="{{ product.id }}" data-id="{{ product.id }}"   data-title="Product Price" >{{ product.price|floatformat:"2" }}<i class="icon-pencil"></i></td>

                {% if product.product_image %}
                    <td><img class="img-polaroid" data-src="holder.js/64x64" src="{{ MEDIA_URL }}{{ product.product_image }}" height="65" width="115"></td>
                {% else %}
                    <td><img class="img-polaroid" data-src="holder.js/64x64" src="{{ STATIC_URL }}images/no_logo.png" height="65" width="115"></td>
                {% endif %}

                        
            """

            template = template.replace("{{ company.slug }}", str(company.slug)).replace("{{ product.id }}", str(context.id))
            template = template.replace("{{ product.name }}", str(context.name))
            template = template.replace('{{ product.price|floatformat:"2" }}', str(context.price))
            template = template.replace("{{ product.product_image }}", str(context.product_image))


        elif   model == "Project":
            """Here is created the Project model template to be returned via http request"""

            context = Project.objects.get(id=f.id)

            template = """
            
                <div id="projects-{{ project.id }}"><a class="link-delete" data-type="projects" data-id="{{ project.id }}" id="{{ company.slug }}-projects-{{ project.id }}" href="/company/{{ company.slug }}/projects/{{ project.id }}/delete"><i class="icon-remove"></i></a>  <text data-type="text" data-model="Project" data-url="/formfields/Project/{{ project.id }}/name/" data-pk="{{ project.id }}" class="editable-value" data-title="Project Name">{{ project.name }}</text> <i class="icon-pencil"></i></div>
                        
            """

            template = template.replace("{{ company.slug }}", str(company.slug)).replace("{{ project.id }}", str(context.id))
            template = template.replace("{{ project.name }}", str(context.name))



        elif   model == "SuccessStories":
            """Here is created the story model template to be returned via http request"""

            context = SuccessStories.objects.get(id=f.id)

            template = """
                <li id="stories-{{ story.id }}">
                <a class="link-delete" data-type="SuccessStories" data-id="{{ story.id }}"  id="{{ company.slug }}-stories-{{ story.id }}" href="/company/{{ company.slug }}/stories/{{ story.id }}/delete" ><i class="icon-remove"></i></a>  
                <a href="/company/{{ company.slug }}/SuccessStories/{{ story.id }}/update">{{ story.story }}</a>
                </li>

            """

            template = template.replace("{{ company.slug }}", str(company.slug)).replace("{{ story.id }}", str(context.id))
            template = template.replace("{{ story.title }}", str(context.title))

        else:
            pass

        d = { 
            'id': f.id, 
            'model': model,
            'company': company.name,
            'template': template,
            }
        if f.name:
            d['name'] = f.name
        return json_response(d)

        #We must return the template for the item.
    return json_response({ "errors":dict(form.errors.items()) })

def tagit(request):
    tags = Tag.objects.all()
    result = []
    result = [x.name for x in tags]
    f = simplejson.dumps(result)
    return render_to_response("tagit.html", {'f':f},context_instance=RequestContext(request))

def base(request):
    return render_to_response("index.html",{'user': request.user}, 
    context_instance=RequestContext(request))

#Used to obtain the list of tags as a Ajax request returns a Json Array
#def tagsplete(request):
#   tags = Tag.objects.filter(name__istartswith=request.REQUEST['term'])
#   results = []
#   for tag in tags:
#      tag_dict = {'id':tag.id, 'label':tag.name, 'value':tag.name}
#      results.append(tag_dict)
#   return HttpResponse(simplejson.dumps(results),mimetype='application/json')

def tagitt(request):
    tags = Tag.objects.all()
    result = []
    result = [x.name for x in tags]
    return HttpResponse(simplejson.dumps(result),mimetype='application/json')

def file_not_found_404(request):
    """Creates a file error with the info to display the user"""

    return render_to_response('404.html',context_instance=RequestContext(request))


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

def authentication_view(request):
    if request.method =='POST':
        try: 
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username = username, password = password)
            if user is not None:
                if user.is_active:
                    login(request,user)
            else:
                return HttpResponseRedirect('/')
        except: 
          return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

  
    return HttpResponseRedirect('/')



def hacked_news():
    """Steals the info from Hacker News to use in our demo Homepage """
    r = requests.get("http://news.ycombinator.com/")
    webpage = BeautifulSoup(r.text)

    pub_table = webpage.find_all('table')[2]
    link_collection = pub_table.select('.title')

    users = pub_table.select('a[href^="user?id="]')
    for  i in range(0, len(users)):
        users[i] = users[i].contents[0]

    array_links = []

    for i in link_collection:
        if str(i.a) != 'None' :
           array_links.append({'url': str(i.a['href']), 'text': i.a.text})


    for i in range(0, len(users)):
        array_links[i]["user"] = users[i]

    for i in range(0, len(array_links)):
        array_links[i]["id"] = 1+i

    array_links.pop()
    return array_links
  
def load_company(request):
    reader = csv.reader(open("gltclients2.csv"), dialect='excel')
    for row in reader:
        company = Company(name=row[0], slug=row[1], industries=row[3], technologies=row[7], applications=row[9] )
        company.save()
    return HttpResponseRedirect('/')    

def ticket_create(request):
    """This view generates the view of the ticket form"""
    #create empty ticket
    ticket_form = TicketForm()
    return render_to_response('ticket_form.html', {'ticket_form': ticket_form},context_instance=RequestContext(request) )


def asana_create(request): 
  """ Creates a bugs report in asana Bugs Database for evaluation of the Team"""
  #Create form from POST part of the request
  if request.method =="POST":
    #Verify the form is completeley filled with information
    ticket_form = TicketForm(request.POST)
    
    #if not created return to the previous ticket page
    if ticket_form.is_valid():
      #Verifies the Workplace 'Stance Labs' exists or renames the last one
      asana_api = AsanaAPI('nnZRaTW.3iyzMjyjZ3rSsNbU9sKs7haf', debug=False)
      work_spaces = asana_api.list_workspaces()

      for space in work_spaces:

        if space['name'] == 'Stance Labs': 
          work_space = space
      #verify the variable was assigned, otherwise assign it arbitrarily
      try:
        space
      except NameError:
        asana_api.update_workspace(work_spaces[-1]['id'], 'Stance Labs')
        work_space = work_spaces[-2]

      #Verifies there's a 'Bugs' project in the asana Workplace or creates it
      projects_list = asana_api.list_projects(work_space['id'])

      for project in projects_list:
        if project['name'] == 'Bugs':
          bugs_project = project
      try:
        bugs_project
      except NameError:
        bugs_note="""Place to work with all the tickets generated with our sites"""
        bugs_project = asana_api.create_project('Bugs', work_space, notes=bugs_note, archived=False)
      
      #Then it Creates a new Task with a person assigned to it.
      task_note  = "URL of the Error: \n" + str(ticket_form.data['url'])+ "\n\n"
      task_note += "Error description:\n" + str(ticket_form.data['error'])+ "\n\n"
      task_note += "Expected: \n" + str(ticket_form.data['expectation']) +"\n\n"
      task_note += "Actual:\n" + str(ticket_form.data['actual'])+"\n\n"
      task_note += "Contact Email: \n"+ str(ticket_form.data['email']) + "\n\n"

      task = asana_api.create_task(str(ticket_form.data['name']),
        workspace=work_space['id'], 
        assignee='me',
        notes=task_note)
      #Assign the task to a project
      asana_api.add_project_task(task['id'], bugs_project['id'])
      return render_to_response('ticket_form.html', {'ticket_form': TicketForm(), 'ticket_confirmation': str(task['id'])},context_instance=RequestContext(request) )

    else:
      return render_to_response('ticket_form.html', { 'form_errors': ticket_form.errors, 'ticket_form':ticket_form},context_instance=RequestContext(request) )


  else: 
    return HttpResponseRedirect("/ticket")
