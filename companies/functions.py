from companies.models import *
from contacts.models import Contact
from django.http import HttpResponse, HttpResponseRedirect

def update_completion(id_company):
    #Not needed due to the fact that the info is update in the function below. 
    pass

def percentage_completion(id_company): 
    """This function makes sure that the Profile Completion percentage is available for use """
    try:
        p = ProfileCompletion.objects.get(company_id = id_company)

        c = Company.objects.get(id=id_company)
        count = 0
        length = len(c.__dict__)

        for i in c.__dict__:
            if c.__dict__[i]:
                count += 1
        percentage = round(count/float(length),2)

        p.completion = percentage
        p.save()


        return {'percentage': int(p.completion*100) }
    except ProfileCompletion.DoesNotExist: 
        
        try:
            c = Company.objects.get(id=id_company)
            count = 0
            length = len(c.__dict__)

            for i in c.__dict__:
                if c.__dict__[i]:
                    count += 1
            percentage = round(count/float(length),2)

            p = ProfileCompletion(completion=percentage, company_id= id_company)
            p.save()

            return {'percentage': int(percentage*100)}
        except Company.DoesNotExist:
            return {'percentage':{'percentage':0 }}

def validate_user_company_access_or_redirect(request, company):
    """The purpose of this function is to validate the user has access to the page in place before 
    providing him accesss to the information at hand"""
    user_id = request.user.id
    try:
            contact = Contact.objects.get(id = user_id)
            #If the user is not a latech employee,
            #is the user an Admin?
            if request.user.is_staff or request.user.is_superuser or contact.latech_contact :
                return True

            else:

                #verify the person does not have access
                try:
                    #Does the user has permission to modify this claim?
                    permissions = AccessCompanyProfile.objects.get(contact=user_id)
                    edit = False

                    
                
                    for i in permissions.company.all(): 
                           if i.name == company.name:
                              edit = True
                    if edit == False: 
                        return HttpResponseRedirect('/company/'+str(company.slug))
                except AccessCompanyProfile.DoesNotExist:
                    return HttpResponseRedirect('/company/'+str(company.slug))

    except Contact.DoesNotExist:
        return HttpResponseRedirect('/company/'+str(company.slug))
