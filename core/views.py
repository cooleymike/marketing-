from django.http import HttpResponse
from django.template.response import TemplateResponse

def homepage(request):
   title = "homepage"
   return TemplateResponse(request, "home.html", {"title": "homepage"})

def signin(request):
    title = "signin"
    return TemplateResponse(request, 'signin.html', {"title": "signin"})


def bookeeping(request):
    return TemplateResponse(request,'bookeeping.html', {"title": "bookeeping"}) 

def managing(request):
    return TemplateResponse(request,'managing.html', {"title": "managing"})

def confirm(request):
    return TemplateResponse(request,'confirm.html', {"title": "confirm"})

def signup(request):
    return TemplateResponse(request,'signup.html', {"title": "signup"})

def upload(request):
   return TemplateResponse(request, "upload.html", {"title": "upload"})