from django.contrib import admin
from .models import ItemDoPedido
from .models import  Venda
from .actions import nfe_emitida,nfe_nao_emitida

class ItemPedidoInline(admin.TabularInline):
    model = ItemDoPedido
    extra =  1

class VendaAdmin(admin.ModelAdmin):
    readonly_fields = ('valor',)
    autocomplete_fields = ('client',)
    list_filter = ('client__doc',)
    search_fields = ("id",'client__first_name','client__doc__num_doc')
    list_display = ('client','id','nfe_emitida')
    actions = [nfe_emitida,nfe_nao_emitida]
    inlines = [ItemPedidoInline]

    def total(self,obj):
        return obj.calcular_total()

    total.short_description = 'Total'


admin.site.register(ItemDoPedido)
admin.site.register(Venda,VendaAdmin)

