from django.shortcuts import render
from django.views import View
from django.db.models import  Sum,F,FloatField,Max,Avg,Count,Min
from .models import Venda

class DashboardView(View):

    def get(self,request):

        data = {'media': Venda.objects.all().aggregate(Avg('valor'))['valor__avg'],
                'media_desc': Venda.objects.all().aggregate(Avg('desconto'))['desconto__avg'],
                'min': Venda.objects.all().aggregate(Min('valor'))['valor__min'],
                'max': Venda.objects.all().aggregate(Max('valor'))['valor__max'],
                'n_ped': Venda.objects.all().aggregate(Count('id'))['id__count'],
                'n_ped_nfe': Venda.objects.filter(
                    nfe_emitida=True).aggregate(Count('id'))['id__count']

                }


        return render(request,'vendas/dashboard.html',{'data':data,})

