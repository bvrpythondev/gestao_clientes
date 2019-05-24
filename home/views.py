from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import logout
import datetime
from django.utils.timezone import utc

def calcular(v1,v2):
    return v1 / v2

def home(request):
    value1 = 10
    value2 = 20
    res = calcular(value1,value2)
    return render(request,'home_1.html',{'result':res})

def my_logout(request):
    logout(request)
    return redirect('home')

def time(request):

    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    now.strftime('%H:%M:%S')
    return render(request,'time1.html',{'myDate':now})

def teste(request):
    return render(request,'images.html')
