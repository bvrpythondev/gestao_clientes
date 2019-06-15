from django.forms import ModelForm
from .models import Person
from .models import Documento

class PersonForm(ModelForm):
    class Meta:
        model  = Person
        fields = ['first_name','last_name',"age","salary","bio","photo",'doc']


class DocumentForm(ModelForm):
    class Meta:
        model =Documento
        fields = ['num_doc']