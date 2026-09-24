from django.urls import path 
from estudantes import views 
urlpatterns = [
    path("",views.listarEstudantes, name="estudante_listar"),
    path("adicionar/",views.AdicionarEstudantes, name="estudante_criar"), 
    path("editar/<id>",views.EditarEstudantes, name="estudante_editar"),
    path("deletar/<id>",views.DeletarEstudantes, name="estudante_deletar"),
    path("visualizar/<id>",views.VisualizarEstudantes, name="estudante_visualizar"),
]