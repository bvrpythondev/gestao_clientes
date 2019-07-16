from django.urls import path
from .views import my_logout,HomePageView,time,home,MyView
from django.views.generic.base import  TemplateView
from .views import  litest

urlpatterns = [
    path('',home,name="home"),

    path('logout/',my_logout),

    path('time/',time,name='time'),

    #Home2 exemplo de usagem rapida somente para exibir o template direto!!
    path('home2/',TemplateView.as_view(template_name="home_2.html"),name='TemplateView'),

    #A home3 é um classed based view que nos a criamos e injetamos contexto no caso foi um texto simples
    path('home3/',HomePageView.as_view(template_name="home_3.html"),name='HomePageView'),


    #View simples para usos pequenos e simples
    path('view/',MyView.as_view()),

    path('litest/',litest,name='litest')



]
