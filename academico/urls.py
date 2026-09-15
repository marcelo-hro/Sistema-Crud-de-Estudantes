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

]



