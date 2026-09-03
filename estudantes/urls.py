from django.urls import path 
from estudantes import views 
urlpatterns = [
    path("",views.listarEstudantes, name="listagem"),
    path("adicionar/",views.AdicionarEstudantes, name="adicionar"), 
    path("editar/<id>",views.EditarEstudantes, name="editar"),
    path("deletar/<id>",views.DeletarEstudantes, name="deletar"),
    path("visualizar/<id>",views.VisualizarEstudantes, name="visualizar"),
]