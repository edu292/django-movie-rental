from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, reverse, redirect

from django.views.decorators.http import require_http_methods, require_GET
from django_htmx.http import HttpResponseLocation

from .models import Filme, Pessoa, Genero, Aluguel

from django.http import HttpRequest as HttpRequestBase
from django_htmx.middleware import HtmxDetails


class HttpRequest(HttpRequestBase):
    htmx: HtmxDetails


@require_GET
def home(request):
    query = request.GET.get("q")
    if query:
        filmes = Filme.objects.filter(titulo__icontains=query)
    else:
        filmes = Filme.objects.all()[:3]
    return render(request, 'main/home.html', {'filmes': filmes})


@require_GET
def top5(request):
    filmes = Filme.objects.all()[:5]
    return render(request, 'main/top5.html', context={'filmes': filmes})


@require_GET
def biografias(request):
    query = request.GET.get('q')
    if query:
        pessoas = Pessoa.objects.filter(nome__icontains=query)
    else:
        pessoas = Pessoa.objects.all()[:8]
    context = {
        'pessoas': pessoas,
        'query': query,
    }
    return render(request, 'main/biografias.html', context)


@require_GET
def biografia(request, slug):
    pessoa = get_object_or_404(Pessoa, slug=slug)
    return render(request, "main/biografia.html", {"pessoa": pessoa})


@require_GET
def genero(request, slug):
    genero = get_object_or_404(Genero, slug=slug)
    return render(request, 'main/genero.html', {'genero': genero})


@require_GET
def generos(request):
    query = request.GET.get('q')
    if query:
        pessoas = Genero.objects.filter(nome__icontains=query)
    else:
        pessoas = Genero.objects.all()[:8]
    context = {
        'generos': pessoas,
        'query': query,
    }
    return render(request, 'main/generos.html', context)


@require_GET
def filme(request, slug):
    filme = get_object_or_404(Filme, slug=slug)
    return render(request, 'main/filme.html', {'filme': filme})


@require_http_methods(['POST', 'DELETE'])
@login_required
def aluguel(request, pk):
    if request.method == 'POST':
        filme = get_object_or_404(Filme, pk=pk)
        Aluguel.objects.create(usuario=request.user, filme=filme)
    else:
        aluguel = get_object_or_404(Aluguel, pk=pk, usuario=request.user)
        aluguel.delete()

    return HttpResponseLocation(reverse('main:perfil'))


@login_required
def perfil(request):
    alugueis = Aluguel.objects.filter(usuario=request.user)
    return render(request, 'main/perfil.html', {'alugueis': alugueis})