def nfe_emitida(modeladmin,request,queryset):
    queryset.update(nfe_emitida=True)

nfe_emitida.short_description = "NF-e emitida"

def nfe_nao_emitida(modeladmin,request,queryset):
    queryset.update(nfe_emitida=False)

nfe_nao_emitida.short_description = "NF-e nao emitida"