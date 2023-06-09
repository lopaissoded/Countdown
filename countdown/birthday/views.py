from django.shortcuts import render
import datetime

# Create your views here.

def index(request):
    now=datetime.datetime.now()
    d=now.day
    m=now.month

    if m > 6:
        month= 6 - m + 12
        if d<=30:
            day= 30 - d
        else:
            day= d-30

    elif m==6 :
        month = 0
        day= 30 - d
            
    else:
        month = 6 - m
        if d<=30:
            day= 30 - d
        else:
            day= d-30
    
    return render(request, "birthday/index.html",
    {
        "day": day, "month": month,
        "value": day==0 and month==0
    })