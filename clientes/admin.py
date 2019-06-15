from django.contrib import admin
from .models import Person
from .models import Produto
from .models import Documento,Venda

class PersonAdmin(admin.ModelAdmin):
    fields = ('first_name','last_name','age','salary','doc','bio','photo')
    list_display = ('first_name','last_name','age','salary','doc','bio','photo')

# Register your models here.
admin.site.register(Person,PersonAdmin)
admin.site.register(Documento)
admin.site.register(Venda)
admin.site.register(Produto)
