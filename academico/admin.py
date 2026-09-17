from django.contrib import admin

from academico.models import Curso, Disciplina, Professor, Turma

# Register your models here.
admin.site.register(Curso)
admin.site.register(Professor)
admin.site.register(Turma)
admin.site.register(Disciplina)