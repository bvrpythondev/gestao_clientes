from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from clientes.models import Person
from produtos.models import Produto
from django.db.models import Sum, F, FloatField, Max



class Venda(models.Model):

    numero = models.CharField(max_length=7)
    valor = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    desconto = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    impostos = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    pessoa = models.ForeignKey(Person,null=True,blank=True,on_delete=models.PROTECT)
    nfe_emitida = models.BooleanField(default=False)

    def get_total(self):
        tot = self.itemdopedido_set.all().aggregate(
            tot_ped=Sum( (F('quantidade') * F('produto__preco')) - F('desconto'),output_field=FloatField())
        )['tot_ped'] or 0


        tot = tot - float(self.impostos) - float(self.desconto)


        self.valor = tot
        Venda.objects.filter(id=self.id).update(valor=tot)

        return self.valor




    def __str__(self):
        return self.numero


class ItemDoPedido(models.Model):
    venda = models.ForeignKey(Venda,on_delete=models.PROTECT)
    produto = models.ForeignKey(Produto,on_delete=models.PROTECT)
    quantidade = models.FloatField()
    desconto = models.DecimalField(max_digits=5 ,decimal_places=2)


    def __str__(self):
        return self.venda.numero + ' - ' + self.produto.descricao


@receiver(post_save,sender=ItemDoPedido)
def update_vendas_total(sender,instance,**kwargs):
    instance.venda.get_total()

@receiver(post_save,sender=Venda)
def update_vendas_total2(sender,instance,**kwargs):
    instance.get_total()
