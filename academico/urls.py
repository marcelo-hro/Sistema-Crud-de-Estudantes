from django.urls import path
from academico import views


urlpatterns = [
    path ('',views.dashboard,name='dashboard'),
    path("/listar/curso",views.listarCurso, name="curso_listar"),
    path("/adicionar/curso/",views.AdicionarCurso, name="curso_criar"),
    path("/editar/curso/<id>",views.EditarCurso, name="curso_editar"),
    path("/deletar/curso/<id>",views.DeletarCurso, name="curso_deletar"),
    path("/visualizar/curso/<id>",views.VisualizarCurso, name="curso_visualizar"),

    path("/listar/professor/",views.listarProfessor, name="professor_listar"),
    path("/adicionar/professor/",views.AdicionarProfessor, name="professor_criar"),
    path("/editar/professor/<id>/",views.EditarProfessor, name="professor_editar"),
    path("/deletar/professor/<id>/",views.DeletarProfessor, name="professor_editar"),
    path("/visualizar/professor/<id>/",views.VisualizarProfessor, name="professor_visualizar"),

    path("/listar/turma/",views.listarTurma, name="turma_listar"),
    path("/adicionar/turma/",views.AdicionarTurma, name="turma_criar"),
    path("/editar/turma/<id>/",views.EditarTurma, name="turma_editar"),
    path("/deletar/turma/<id>/",views.DeletarTurma, name="turma_deletar"),
    path("/visualizar/turma/<id>/",views.VisualizarTurma, name="turma_visualizar"),

    path("/listar/disciplina/",views.listarDisciplina, name="disciplina_listar"),
    path("/adicionar/disciplina/",views.adicionarDisciplina, name="disciplina_criar"),
    path("/editar/disciplina/<id>/",views.editarDisciplina, name="disciplina_editar"),
    path("/deletar/disciplina/<id>/",views.deletarDisciplina, name="disciplina_deletar"),
    path("/visualizar/disciplina/<id>/",views.visualizarDisciplina, name="disciplina_visualizar"),

    path("/listar/departamento/",views.listarDepartamento, name="departamento_listar"),
    path("/adicionar/departamento/",views.adicionarDepartamento, name="departamento_criar"),
    path("/editar/departamento/<id>/",views.editarDepartamento, name="departamento_editar"),
    path("/deletar/departamento/<id>/",views.deletarDepartamento, name="departamento_deletar"),
    path("/visualizar/departamento/<id>/",views.visualizarDepartamento, name="departamento_visualizar"),



]



