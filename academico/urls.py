from django.urls import path
from academico import views


urlpatterns = [
    path("listar/curso",views.listarCurso, name="listagem"),
    path("adicionar/curso/",views.AdicionarCurso, name="adicionar"),
    path("editar/curso/<id>",views.EditarCurso, name="editar"),
    path("deletar/curso/<id>",views.DeletarCurso, name="deletar"),
    path("visualizar/curso/<id>",views.VisualizarCurso, name="visualizar"),

    path("listar/professor/",views.listarProfessor, name="listagem_professor"),
    path("adicionar/professor/",views.AdicionarProfessor, name="adicionar_professor"),
    path("editar/professor/<id>/",views.EditarProfessor, name="editar_professor"),
    path("deletar/professor/<id>/",views.DeletarProfessor, name="deletar_professor"),
    path("visualizar/professor/<id>/",views.VisualizarProfessor, name="visualizar_professor"),

    path("listar/turma/",views.listarTurma, name="listagem_turma"),
    path("adicionar/turma/",views.AdicionarTurma, name="adicionar_turma"),
    path("editar/turma/<id>/",views.EditarTurma, name="editar_turma"),
    path("deletar/turma/<id>/",views.DeletarTurma, name="deletar_turma"),
    path("visualizar/turma/<id>/",views.VisualizarTurma, name="visualizar_turma"),

    path("listar/disciplina/",views.listarDisciplina, name="listagem_disciplina"),
    path("adicionar/disciplina/",views.adicionarDisciplina, name="adicionar_disciplina"),
    path("editar/disciplina/<id>/",views.editarDisciplina, name="editar_disciplina"),
    path("deletar/disciplina/<id>/",views.deletarDisciplina, name="deletar_disciplina"),
    path("visualizar/disciplina/<id>/",views.visualizarDisciplina, name="visualizar_disciplina"),

    path("listar/departamento/",views.listarDepartamento, name="listagem_departamento"),
    path("adicionar/departamento/",views.adicionarDepartamento, name="adicionar_departamento"),
    path("editar/departamento/<id>/",views.editarDepartamento, name="editar_departamento"),
    path("deletar/departamento/<id>/",views.deletarDepartamento, name="deletar_departamento"),
    path("visualizar/departamento/<id>/",views.visualizarDepartamento, name="visualizar_departamento"),



]



