from django.contrib import admin
from .models import Person
from .models import Documento


class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados pessoais',{'fields':('first_name','last_name','age','doc')}),
        ('Dados complemtares',{"fields":('salary','bio','photo')}),
    )
    autocomplete_fields = ['doc']
    list_filter = ('age','salary')

    #fields = ('first_name','last_name','age','salary','doc','bio','photo')
    list_display = ('first_name','last_name','age','salary','doc','bio','tem_photo')
    search_fields = ('id','first_name')

    def tem_photo(self,obj):
        if obj.photo:
            return 'Sim'
        else:
            return 'Nao'

    tem_photo.short_description = 'Possui foto'


class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('id','num_doc')
    search_fields = ['num_doc']

# Register your models here.
admin.site.register(Person,PersonAdmin)
admin.site.register(Documento,DocumentoAdmin)



