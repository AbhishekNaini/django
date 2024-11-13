from django.shortcuts import render

# Create your views here.
def news_info(request):
    return render(request,'testapp/index.html')
def movies_view(request):
    head_msg='movies information'
    sub_msg1='kalki is a future movie'
    sub_msg2='waiting for pushpa 2'
    sub_msg3='devara movie is too god'
    type= 'movies'
    my_dict={"head_msg":head_msg,"sub_msg1":sub_msg1,"sub_msg2":sub_msg2,"sub_msg3":sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)

def sports_view(request):
    head_msg='sports information'
    sub_msg1='india won t20 worldcup'
    sub_msg2='nxt odi worldcup is also likely to india'
    sub_msg3='virat kohli is king of cricket'
    type = 'sports'
    my_dict={"head_msg":head_msg,"sub_msg1":sub_msg1,"sub_msg2":sub_msg2,"sub_msg3":sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)

def politics_view(request):
    head_msg='politics information'
    sub_msg1='present deputy cm of AP is PAWANKALYAN'
    sub_msg2='prime minister of india is MODI JI'
    sub_msg3='telangana best IT minister KTR'
    type = 'politics'
    my_dict={"head_msg":head_msg,"sub_msg1":sub_msg1,"sub_msg2":sub_msg2,"sub_msg3":sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)