from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)
    foto = models.ImageField(upload_to='foto', null=True, blank=True)

    def __str__(self):
        return self.nome


class Genero(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    capa = models.ImageField(upload_to='capa_filmes')
    sinopse = models.TextField()
    direcao = models.ManyToManyField(Pessoa, blank=True, related_name='direcao')
    elenco = models.ManyToManyField(Pessoa, blank=True, related_name='elenco')
    genero = models.ManyToManyField(Genero)

    def __str__(self):
        return self.titulo


class Aluguel(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    data_aluguel = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.filme.titulo