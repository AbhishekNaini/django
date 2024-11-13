from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hyd_jobs_info(request):
    s='<h1>Hyderbad Jobs Information</h1>'
    return HttpResponse(s)
def bng_jobs_info(request):
    s='<h1>Bangalore Jobs Information</h1>'
    return HttpResponse(s)
def dubai_jobs_info(request):
    s='<h1>dubai Jobs Information</h1>'
    return HttpResponse(s)
def russia_jobs_info(request):
    s='<h1>russia Jobs Information</h1>'
    return HttpResponse(s)
def uk_jobs_info(request):
    s='<h1>uk Jobs Information</h1>'
    return HttpResponse(s)
def usa_jobs_info(request):
    s='<h1>usa Jobs Information</h1>'
    return HttpResponse(s)
