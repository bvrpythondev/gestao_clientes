from django.urls import path
from .views import home
from .views import my_logout
from .views import time
from .views import teste

urlpatterns = [
    path('',home,name="home"),
    path('logout/',my_logout),
    path('time/',time,name='time'),
    path('teste/',teste,name='teste')

]
