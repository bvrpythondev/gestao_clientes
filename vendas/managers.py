from django.db import models
from django.db.models import  Sum,F,FloatField,Max,Avg,Count,Min


class VendaManager(models.Manager):


    def media(self):
        return self.all().aggregate(Avg('valor'))['valor__avg']

    def media_desc(self):
        return self.all().aggregate(Avg('desconto'))['desconto__avg']

    def max_desc(self):
        return self.all().aggregate(Max('desconto'))['desconto__max']


    def min_desc(self):
        return self.all().aggregate(Min('desconto'))['desconto__min']

    def min(self):
        return self.all().aggregate(Min('valor'))['valor__min']


    def max(self):
        return self.all().aggregate(Max('valor'))['valor__max']

    def n_ped(self):
        return self.all().aggregate(Count("id"))['id__count']

    def n_ped_nfe(self):
        return  self.filter(
            nfe_emitida=True).aggregate(Count('id'))['id__count']



