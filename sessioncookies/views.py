from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def set_session(request):
    #setting data as a setting 
    request.session['username']='john_row'
    request.session['is_logged_in']=True
    return HttpResponse("session data set")
    

def get_session(request):
    username=request.session.get('username','Guest')   # defalt vale is not set 
    is_logged_in=request.session.get('is_logged_in',False)
    return HttpResponse(f"'Username':{username},'Logged In':{is_logged_in}")


def  delete_session(request):
    # deletting data from the session 
    try:
        del request.session['username']
        del request.session['is_logged_in']
        return HttpResponse("session data deleted")
    except:
        HttpResponse('no session data to deleted')