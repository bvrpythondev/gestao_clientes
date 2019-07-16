from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import logout
import datetime
from django.utils.timezone import utc
from django.views.generic.base import  TemplateView
from django.views import View




def home(request):
    return render(request,'home_1.html')

def my_logout(request):
    logout(request)
    return redirect('home')

def time(request):

    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    now.strftime('%H:%M:%S')
    return render(request,'time1.html',{'myDate':now})



class HomePageView(TemplateView):
    template_name = 'home_3.html'

    def post(self,request,**kwargs):
        return HttpResponse('Post')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['minha_variavel'] = 'Hello Welcome to Django'
        return context


class MyView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'home_3.html')

    def post(self,request,*args,**kwargs):
        return HttpResponse('Post')


def litest(request):
    return render(request,'litest.html')