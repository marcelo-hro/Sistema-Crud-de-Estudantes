from django.db import models

# Create your models here.
class Professor(models.Model):
    matricula = models.CharField(max_length=12)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    cpf = models.CharField(max_length=14)
    
class Curso(models.Model):
    codigo = models.IntegerField(max_length=2, primary_key=True)
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos/cursos')
    duracao = models.DecimalField(max_digits=3, decimal_places=2)
    data_inicio = models.DateField(blank=True, )
    cargaHoraria = models.IntegerField()

class Turma(models.Model):
    codigo = models.CharField(max_length=15)
    anoIngresso = models.IntegerField(max_length=4)
    periodo = models.IntegerField(max_length=1)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    
class Disciplina(models.Model):
    codigo = models.IntegerField(max_length=3)
    nome = models.CharField(max_length=150)
    cargaHoraria = models.IntegerField()
    turno = models.CharField(max_length=10)
    turma = models.ForeignKey(Turma,on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)   
    

    