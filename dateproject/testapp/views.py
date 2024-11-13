from django.shortcuts import render
import datetime
def wish(request):
    date=datetime.datetime.now()
    name='sunny'
    rollno=101
    marks=98
    my_dict={'insert_date':date,'insert_name':name,'rollno':rollno,'marks':marks}
    return render(request,'testapp/wish.html',my_dict)
