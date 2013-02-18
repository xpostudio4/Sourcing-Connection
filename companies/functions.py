from models import *

def update_completion(id_company):
    #calculate info from the 
    pass

def percentage_completion(id_company): 
    """This function makes sure that the Profile Completion percentage is available for use """
    try:
        p = ProfileCompletion.objects.get(company_id = id_company)
        return {'percentage': p.completion}
    except ProfileCompletion.DoesNotExist: 
        
        try:
            c = Company.objects.get(id=id_company)
            count = 0
            length = len(c.__dict__)

            for i in c.__dict__:
                if c.__dict__[i]:
                    count += 1
            percentage = round(float(count/length),2)

            p = ProfileCompletion(completion=percentage, company_id= id_company)
            p.save()

            return {'percentage': percentage}
        except Company.DoesNotExist:
            return {'percentage':{'percentage':0 }}

