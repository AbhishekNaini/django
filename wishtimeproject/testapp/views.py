from django.shortcuts import render
import datetime 
# Create your views here.
def wish(request):
    date=datetime.datetime.now()
    msg='hello Guest Very Very good'
    h=int(date.strftime('%H'))
    if h<=12:
        msg+='Good Morning'
    elif h<=16:
        msg+='Good Afternoon'
    elif h<=21:
        msg+='Good Evening'
    else:
        msg+='Good Night'
    my_dict={'inser_date':date,'insert_msg':msg}
    return render(request,'testapp/wish.html',my_dict)