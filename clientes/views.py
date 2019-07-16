from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import Person
from vendas.models import Venda
from produtos.models import Produto
from .forms import PersonForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
from django.views import View
from django.utils.decorators import method_decorator




@login_required
def person_list(request):

    if request.user.has_perm('clientes.view_person') == True:

        termo_busca = request.GET.get('pesquisa' ,  None)

        usertemp = request.user

        if usertemp.is_staff == True:

            if termo_busca:
                persons = Person.objects.all()
                persons = persons.filter(first_name__icontains=termo_busca)
            else:
                persons = Person.objects.all()

            return render(request,'person.html',{"persons":persons})
        else:
            return render(request, "403.html")

    else:
        return render(request,"403.html")

@login_required
def person_new(request):

    if request.user.has_perm("clientes.add_person") == True:

        usertemp = request.user

        if usertemp.is_staff == True:

            form = PersonForm(request.POST or None,request.FILES or None)

            if form.is_valid():
                form.save()
                return redirect('person_list')

            return render(request,"person_form.html",{"form":form})
        else:
            return render(request,"403.html")
    else:
        return render(request, "403.html")

@login_required
def person_update(request,id):


    if request.user.has_perm("clientes.update_person") == True:

        usertemp = request.user

        if usertemp.is_staff == True:

            person   = get_object_or_404(Person,pk=id)
            form = PersonForm(request.POST or None, request.FILES or None,instance=person)

            if form.is_valid():
                form.save()
                return redirect('person_list')

            return render(request,"person_form.html",{"form":form})
        else:
            return render(request,"403.html")
    else:
        return render(request,"403.html")


@login_required
def person_delete(request,id):

    if request.user.has_perm("clientes.delete_person") == True:
        usertemp = request.user

        if usertemp.is_staff == True:
            person = get_object_or_404(Person, pk=id)

            if request.method == "POST":
                person.delete()
                return redirect('person_list')
            return render(request, "person_delete_confirm.html", {'person': person})

        else:
            return render(request,"403.html")
    else:
        return render(request,"403.html")




#Cbv Person


class PersonList(ListView):
    model = Person


    def  get_queryset(self):
        termo_busca = self.request.GET.get('pesquisa' , None)

        if termo_busca:
            persons = Person.objects.filter(first_name__icontains=termo_busca)
        else:
            persons = Person.objects.all().order_by('first_name')

        return persons




class PersonDetail(DetailView):
    model = Person




    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return Person.objects.select_related('doc').get(id=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vendas'] = Venda.objects.filter(
            pessoa_id=self.object.id
        )
        return context




class PersonCreate(CreateView):
    model = Person
    fields = ['first_name','last_name','age','salary','bio','photo','doc']

    def get_success_url(self):
        return  reverse_lazy('person_list_cbv')


class PersonUpdate(UpdateView):
    model = Person
    fields = ['first_name','last_name','age','salary','bio','photo','doc']
    #success_url = reverse_lazy('person_list_cbv')

    def get_success_url(self):
        return  reverse_lazy('person_list_cbv')

class PersonDelete(DeleteView):
    model = Person
    #success_url = reverse_lazy('person_list_cbv')

    def get_success_url(self):
        return  reverse_lazy('person_list_cbv')


class ProdutoBulk(View):

    def get(self,request):
        produtos = ['Banana','Maça','Limao','Laranja','Melancia']
        list_produtos = []

        for produto in produtos:
            p = Produto(descricao=produto,preco=10)
            list_produtos.append(p)

        #Produto.objects.bulk_create(list_produtos)

        return HttpResponse('Funcionou')





