from django.shortcuts import render
from testapp.models import *

def indexView(request):
    return render(request , 'index.html')

def hydJobsView(request):
    data = hydjobs.objects.all()
    job_list = {"title" : "Hydervad jobs",'jobs':data}
    return render(request , 'testapp/jobs.html' ,context=job_list)

def bloreJobsView(request):
    data = blorejobs.objects.all()
    job_list = {"title" : "Banglore jobs",'jobs':data}
    return render(request , 'testapp/jobs.html' ,context=job_list)

def chennaiJobsView(request):
    data = chennaijobs.objects.all()
    job_list = {"title" : "Chennai jobs",'jobs':data}
    return render(request , 'testapp/jobs.html' ,context=job_list)

def puneJobsView(request):
    data = punejobs.objects.all()
    job_list = {"title" : "Pune jobs",'jobs':data}
    return render(request , 'testapp/jobs.html' ,context=job_list)
