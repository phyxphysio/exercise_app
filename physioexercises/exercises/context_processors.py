import datetime 
def current_year(request):
    return {'year':datetime.datetime.now().year}