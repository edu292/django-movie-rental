from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import os


def get_filename_generator(target_folder):
    def filename_generator(instance, filename):
        extension = os.path.splitext(filename)[1]
        new_filename = instance.slug+extension

        return os.path.join(target_folder, new_filename)

    return filename_generator


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    bio = models.TextField()
    foto = models.ImageField(upload_to=get_filename_generator('foto'))
    slug = models.CharField(max_length=150)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome


class Genero(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    slug = models.CharField(max_length=150)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Gênero'

    def __str__(self):
        return self.nome


class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    duracao = models.IntegerField(blank=True, null=True)
    capa = models.ImageField(upload_to=get_filename_generator('capa-filmes'))
    sinopse = models.TextField()
    direcao = models.ManyToManyField(Pessoa, related_name='filmes_dirigidos')
    elenco = models.ManyToManyField(Pessoa, related_name='filmes_atuados')
    genero = models.ManyToManyField(Genero)
    slug = models.CharField(max_length=150)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.titulo


class Aluguel(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    data_aluguel = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Alugueis'

    def __str__(self):
        return self.filme.titulo