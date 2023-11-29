from django.template.response import TemplateResponse


from django.http import HttpResponse

def homepage(request):
   return TemplateResponse(request, "home.html")

def welcome(request):
    return HttpResponse(request,'welcome.html')

def bookeeping(request):
    return HttpResponse(request,'bookeeping.html')

def managing(request):
    return HttpResponse(request,'managing.html')

def confirm(request):
    return HttpResponse(request,'confirm.html')

def signup(request):
    return HttpResponse(request,'signup.html')

def upload(request):
    return HttpResponse(request,'upload.html')


