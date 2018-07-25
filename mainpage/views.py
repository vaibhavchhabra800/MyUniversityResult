from .models import *
from django.http import HttpResponse, Http404
from django.template.response import TemplateResponse
from django.shortcuts import render_to_response,HttpResponseRedirect,render

def mainpage(request):
    return render(request,"mainpage.html",{})

def admincall(request):
    return render(request,"admin.html",{})

def user1(request):
    data=usermodelk1.objects.all()
    return TemplateResponse(request,"user1.html",{"data":data})


