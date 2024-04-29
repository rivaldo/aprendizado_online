from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    instrutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cursos_ministrados')
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titulo
    
class Modulo(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='modulos')
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    order = models.IntegerField()
    
    def  __str__(self):
        return f'{self.titulo} (Order: {self.order})'
    
class Licao(models.Model):
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE, related_name='licoes')
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    order = models.IntegerField
    
    def __str__(self):
        return f'{self.titulo} (Order: {self.order})'