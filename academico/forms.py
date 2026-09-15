from django import forms 
from .models import Curso, Professor

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
