from django import forms
from estudantes.models import Estudante

class EstudanteForm(forms.ModelForm):
    class Meta:
        model = Estudante
     #  fields = ['nome', 'foto', 'email', 'senha', 'telefone', 'data_nascimento']
        fields = '__all__'
         



    def __init__(self, *args, **kwargs):
        super(EstudanteForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'   
