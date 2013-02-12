import operator
from django.utils import simplejson
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, Context
from django.shortcuts import render_to_response, get_object_or_404
from taxonomy.models import *
from companies.models import *
from contacts.models import *
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from latech.forms import SearchForm, CompanySearchForm, ContactSearchForm
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q 
from latech.forms import TicketForm
from latech.asana import AsanaAPI, AsanaException
import requests
from bs4 import BeautifulSoup

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
  username = request.POST['username']
  password = request.POST['password']
  user = authenticate(username = username, password = password)
  if user is not None:
    if user.is_active:
      login(request,user)
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
      return render_to_response('ticket_form.html', { 'ticket_form':ticket_form, 'form_errors': ticket_form.errors},context_instance=RequestContext(request) )


  else: 
    return HttpResponseRedirect("/ticket")


  
  
  
  