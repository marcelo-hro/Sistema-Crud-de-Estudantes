from django.http import request
from django.shortcuts import render,redirect
from estudantes.models import Estudante
from estudantes.forms import EstudanteForm


def listarEstudantes(request):
    estudantes = Estudante.objects.all()
    dicionario = { 'registros': estudantes }

    return render(request, 'listagem.html',context=dicionario)



def AdicionarEstudantes(request):
    dicionario={}
    form = EstudanteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')

    dicionario['form'] = form
    return render(request, 'adicionar.html',dicionario)


def EditarEstudantes(request, id=None):
    estudante = Estudante.objects.get(pk=id)
    form = EstudanteForm(request.POST or None, request.FILES or None, instance=estudante)
    if form.is_valid():
        form.save()
        return redirect('/')

    dicionario ={'form': form}
    return render(request, 'editar.html',dicionario)


def DeletarEstudantes(request, id=None):
    estudante = Estudante.objects.get(pk=id)
   # if request.method == 'POST':
    estudante.delete()
    return redirect('/')
       # return render(request, 'deletar.html')


def VisualizarEstudantes(request, id=None):
     dicionario = {}
     estudante = Estudante.objects.get(pk=id)
     dicionario['estudante'] = estudante
     return render(request, 'visualizar.html''', dicionario)

