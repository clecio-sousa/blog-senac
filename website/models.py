import os
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

def upload_path(instance, filename):
    return 'posts/{}'.format(filename)

# Create your models here.
class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=80)
    text = models.TextField()
    imagem = models.ImageField(upload_to=upload_path, null=True, blank=True, max_length=180)
    video = models.CharField(max_length=300, blank=True, null=True)

    STATUS = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado')
    )

    status = models.CharField(max_length=10,
                              choices=STATUS,
                              default='rascunho')

    CATEGORIAS = (
        ('programacao', 'Programação'),
        ('python', 'Python'),
        ('django', 'Django')
    )
    categorias = models.CharField(max_length=12,
                                  choices=CATEGORIAS,
                                  default='programacao')

    data_publicacao = models.DateTimeField(default=datetime.now(), blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True, blank=True)
    data_alteracao = models.DateTimeField(auto_now=True, blank=True)

    ativado = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.title


class Comentario(models.Model):
    SEXO = (
        ('M', 'Masculino'),
        ('F', 'Feminino')

    )

    aula = models.ForeignKey(Post, on_delete=models.CASCADE)
    nome_aluno = models.CharField(max_length=100)
    comentario = models.TextField()
    ativado = models.BooleanField(default=False)
    data_publicacao = models.DateTimeField(default=datetime.now(), blank=True)
    data_alteracao = models.DateTimeField(auto_now=True, blank=True)
    sexo = models.CharField(max_length=2, choices=SEXO, default='M')

    def __str__(self):
        return self.comentario
