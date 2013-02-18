from models import *

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


