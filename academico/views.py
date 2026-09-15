from django.http import request
from django.shortcuts import render,redirect
from academico.models import Curso, Professor
from academico.forms import CursoForm, ProfessorForm

# Create your views here.
def listarCurso(request):
   curso = Curso.objects.all()
   dicionario = { 'registros': curso }

   return render(request, 'listagem_curso.html',context=dicionario)


def AdicionarCurso(request):
    dicionario={}
    form = CursoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/academico/listar/curso')

    dicionario['form'] = form
    return render(request, 'adicionar_curso.html',dicionario)

   
def EditarCurso(request, id=None):
    curso = Curso.objects.get(pk=id)
    form = CursoForm(request.POST or None, request.FILES or None, instance=curso)
    if form.is_valid():
        form.save()
        return redirect('/academico/listar/curso')

    dicionario ={'form': form}
    return render(request, 'editar_curso.html',dicionario)

def DeletarCurso(request, id=None):
    curso = Curso.objects.get(pk=id)
   # if request.method == 'POST':
    curso.delete()
    return redirect('/academico/listar/curso')
       # return render(request, 'deletar_curso.html')

def VisualizarCurso(request, id=None):
     dicionario = {}
     curso = Curso.objects.get(pk=id)
     dicionario['curso'] = curso
     return render(request, 'visualizar_curso.html', dicionario)
       

def listarProfessor(request):
   professor = Professor.objects.all()
   dicionario = { 'registros': professor }

   return render(request, 'listagem_professor.html',context=dicionario)

def AdicionarProfessor(request):
    dicionario={}
    form = ProfessorForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/academico/listar/professor')

    dicionario['form'] = form
    return render(request, 'adicionar_professor.html',dicionario)

def EditarProfessor(request, id=None):
    professor = Professor.objects.get(pk=id)
    form = ProfessorForm(request.POST or None, request.FILES or None, instance=professor)
    if form.is_valid():
        form.save()
        return redirect('/academico/listar/professor')

    dicionario ={'form': form}
    return render(request, 'editar_professor.html',dicionario)

def DeletarProfessor(request, id=None):
    professor = Professor.objects.get(pk=id)
   # if request.method == 'POST':
    professor.delete()
    return redirect('/academico/listar/professor')
       # return render(request, 'deletar_professor.html')


def VisualizarProfessor(request, id=None):
     dicionario = {}
     professor = Professor.objects.get(pk=id)
     dicionario['professor'] = professor
     return render(request, 'visualizar_professor.html', dicionario)
       

