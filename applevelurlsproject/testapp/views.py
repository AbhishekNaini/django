from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def exam_view(request):
    return HttpResponse('<h1>exam view<h1>')
def fees_view(request):
    return HttpResponse('<h1>fees view<h1>')
def attendance_view(request):
    return HttpResponse('<h1>attendance view<h1>')
