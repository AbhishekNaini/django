from django.shortcuts import render
import datetime
# Create your views here.
def info_views(request):
    time=datetime.datetime.now()
    name='Django'
    prerequisite='Python'
    my_dict={'time':time,'name':name,'prerequisite':prerequisite}
    return render(request,'testapp/result.html',my_dict)
