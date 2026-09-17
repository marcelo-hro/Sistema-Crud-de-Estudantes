from django.db import models

class Estudante(models.Model):
    nome=models.CharField(max_length=30)
    foto=models.ImageField(upload_to="fotos/estudantes",default="foto.png")
    email=models.EmailField(unique=True)
    senha=models.CharField(max_length=100)
    telefone=models.CharField(max_length=15)
    nascimento=models.DateField()

    def __str__(self):
           return self.nome