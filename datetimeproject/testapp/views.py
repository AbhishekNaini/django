from django.shortcuts import render
import datetime
from django.http import HttpResponse
# Create your views here.
def date_time_info(request):
    date=datetime.datetime.now()
    h=int(date.strftime('%H'))
    msg='<h1>Hello Guest Very'
    if h<12:
        msg+='Good Mrng'
    elif h<16:
        msg+='Good Afternoon'
    elif h<21:
        msg+='Good evening'
    else:
        msg+='Good night'
    msg+='</h1><hr>'
    msg+='<h1>Now the server time is:'+str(date)+'</h1>'
    return HttpResponse(msg)