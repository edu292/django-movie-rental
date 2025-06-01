from main.models import Ator, Diretor, Pessoa, Filme

# Migrate Diretores
for diretor in Diretor.objects.all():
    pessoa, _ = Pessoa.objects.get_or_create(nome=diretor.nome)
    for filme in diretor.filme_set.all():  # or the related name if you defined it
        filme.direcao.add(pessoa)

# Migrate Atores
for ator in Ator.objects.all():
    pessoa, _ = Pessoa.objects.get_or_create(nome=ator.nome)
    for filme in ator.filme_set.all():
        filme.elenco.add(pessoa)