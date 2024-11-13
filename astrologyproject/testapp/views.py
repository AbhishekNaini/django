from django.shortcuts import render
import datetime,random
def result_view(request):
    msg_list = [
    'The golden days a head',
    'Better to sleep more time even in class',
    'Tomorrow will be the best day of your life',
    'Tomorrow is the perfect day to propose ur GF',
    'Very soon you will get the job'
    ]
    names_list = ['sunny','radhika','lilly','katrina','kareena','deepika','samantha']
    time = datetime.datetime.now()
    h = int(time.strftime('%H'))
    if h < 12:
        s = 'Good Morning'
    elif h < 16:
        s = 'Good Afternoon'
    elif h < 21:
        s = 'Good Evening'
    else:
        s = 'Good Night'
    name = random.choice(names_list)
    msg = random.choice(msg_list)
    my_dict = {'time':time,'name':name,'msg':msg,'wish':s}
    return render(request,'testapp/astrology.html',my_dict)