from django.contrib import admin

from estudantes.models import Estudante


class EstudanteAdmin(admin.ModelAdmin):
    list_display=('nome','foto','email','senha','telefone','nascimento')

admin.site.register(Estudante,EstudanteAdmin)