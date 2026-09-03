from django import forms
from .models import Estudantes

class EstudantesForm(forms.ModelForm):
    class Meta:
        model = Estudantes
        fields = ['nome', 'foto', 'email', 'senha', 'telefone', 'data_nascimento']
         



def __init__(self, *args, **kwargs):
    super(EstudantesForm, self).__init__(*args, **kwargs)
    for visible in self.visible_fields():
        visible.field.widget.attrs['class'] = 'form-control'   
