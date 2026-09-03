from django.http import request
from django.shortcuts import render,redirect
from .models import User
from .forms import UserForm




def listarEstudantes(resquest):
    estudantes = Estudantes.objects.all()
    dicionario = { 'registros': estudantes }

    return render(request, 'listagem.html',context=dicionario)



def AdicionarEstudantes(request):
    dicionario={}
    form = EstudantesForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')

    dicionario['form'] = form
    return render(request, 'adicionar.html',dicionario)


def EditarEstudantes(request, id=None):
    estudante = Estudantes.objects.get(pk=id)
    form = EstudantesForm(request.POST or None, request.FILES or None, instance=estudante)
    if form.is_valid():
        form.save()
        return redirect('/')

    dicionario['form'] = form
    return render(request, 'editar.html',dicionario)


def DeletarEstudantes(request, eid=None):
    estudante = Estudantes.objects.get(pk=eid)
   if request.method == 'POST':
        estudante.delete()
        return redirect('/')
    return render(request, 'deletar.html')


def VisualizarEstudantes(request, eid=None):
     dicionario = {}
     estudante = Estudantes.objects.get(pk=eid)
     dicionario['estudante'] = estudante
     return render(request, 'visualizar.html''', dicionario)

