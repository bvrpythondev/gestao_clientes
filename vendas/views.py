from django.shortcuts import render
from django.views import View
from .models import Venda

class DashboardView(View):

    def get(self,request):
        data = {'media': Venda.objects.media(),
                'media_desc': Venda.objects.media_desc(),
                'max_desc':Venda.objects.max_desc(),
                'min_desc':Venda.objects.min_desc(),
                'min': Venda.objects.min(),
                'max': Venda.objects.max(),
                'n_ped': Venda.objects.n_ped(),
                'n_ped_nfe': Venda.objects.n_ped_nfe(),
        }



        return render(request,'vendas/dashboard.html',{'my_data':data,})

