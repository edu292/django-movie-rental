from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    bio = models.TextField()
    foto = models.ImageField(upload_to='foto')

    def __str__(self):
        return self.nome


class Genero(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    duracao = models.IntegerField(blank=True, null=True)
    capa = models.ImageField(upload_to='capa_filmes')
    sinopse = models.TextField()
    direcao = models.ManyToManyField(Pessoa, related_name='filmes_dirigidos')
    elenco = models.ManyToManyField(Pessoa, related_name='filmes_atuados')
    genero = models.ManyToManyField(Genero)

    def __str__(self):
        return self.titulo


class Aluguel(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    data_aluguel = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.filme.titulo