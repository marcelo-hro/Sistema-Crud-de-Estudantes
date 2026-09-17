from django import forms 
from .models import Curso, Professor, Turma, Disciplina

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
         



    def __init__(self, *args, **kwargs):
        super(CursoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'        



class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'
         



    def __init__(self, *args, **kwargs):
        super(ProfessorForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'   


class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = '__all__'

         
    def __init__(self, *args, **kwargs):
        super(TurmaForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'               


class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = '__all__'
         



    def __init__(self, *args, **kwargs):
        super(DisciplinaForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'   