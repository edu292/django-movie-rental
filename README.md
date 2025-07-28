# Projeto: Plataforma de Aluguel de Filmes com Django e HTMX

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2-darkgreen.svg)](https://www.djangoproject.com/)
[![Status](https://img.shields.io/badge/deploy-ativo-brightgreen)](URL_DO_SEU_SITE_AQUI)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Acesse a aplicação em produção:** [**django-movie-rental-production.up.railway.app**](https://django-movie-rental-production.up.railway.app)

![Preview](https://github.com/user-attachments/assets/6131c9a8-4b3c-4469-8853-f887f038896a)

---

## 📝 Descrição do Projeto

Este projeto é uma aplicação web full-stack para aluguel de filmes, desenvolvida para demonstrar a implementação de uma arquitetura moderna e performática com *Django*. O foco principal foi construir uma interface de usuário dinâmica utilizando **HTMX** para chamadas assíncronas, combinando a experiência de uma Single-Page Application (SPA) com a robustez e simplicidade do rendering tradicional do lado do servidor.

A aplicação abrange desde a modelagem de dados e autenticação de usuários até otimizações de produção e o deploy contínuo na plataforma *Railway*.

---

## ✨ Funcionalidades Principais

### Para Usuários:
* **Cadastro e Autenticação:** Sistema completo de registro e login de usuários.
* **Catálogo Navegável:** Explore listas de Filmes, Gêneros e Pessoas (Atores/Diretores).
* **Busca Inteligente:** Pesquise por nome em qualquer uma das categorias.
* **Páginas de Detalhes:** Veja informações aprofundadas sobre cada filme, incluindo elenco, direção e sinopse, com URLs amigáveis (ex: `/filme/pulp-fiction/`).
* **Sistema de Aluguel:** Usuários logados podem alugar filmes com um clique.
* **Perfil de Usuário:** Seção pessoal para visualizar os filmes alugados atualmente.

### Destaques Técnicos:
* **Navegação Rápida com HTMX:** A transição entre páginas é feita de forma assíncrona, carregando apenas o conteúdo necessário e reduzindo o tempo de carregamento.
* **Progressive Enhancement:** O site é 100% funcional mesmo com o JavaScript desabilitado, garantindo acessibilidade e robustez.
* **Otimização para Produção:**
    * Entrega de assets estáticos otimizada com **Whitenoise**.
    * CSS **minificado** para reduzir o tamanho dos arquivos.
    * **Middleware de Compressão** (Zstandard/Brotli/Gzip) para diminuir o tráfego de dados.
    * Comunicação segura via **HTTPS/TLS** gerenciado pelo Railway.

---

## 🧠 Decisões de Design e Arquitetura

A arquitetura deste projeto foi uma escolha deliberada para unir o melhor de dois mundos: a produtividade do Django e a experiência de usuário de aplicações modernas.

1.  **Por que HTMX em vez de React/Vue?**
    A escolha do **HTMX** foi estratégica para evitar a complexidade de um framework JavaScript completo. Com HTMX, mantemos toda a lógica de renderização e de negócio no backend (Python/Django), onde o Django brilha. Isso resulta em:
    * **Menos código duplicado:** Sem a necessidade de reescrever lógicas de validação e modelos no frontend.
    * **Desenvolvimento mais rápido:** A curva de aprendizado é menor e a produtividade, maior.
    * **Performance:** Enviamos HTML puro pela rede, que é leve e rapidamente interpretado pelo navegador, em vez de grandes bundles de JavaScript.

2.  **Progressive Enhancement como Prioridade**
    A aplicação foi construída para funcionar perfeitamente sem JavaScript. O HTMX apenas *aprimora* a experiência, não é um requisito. Isso demonstra um foco em boas práticas de engenharia web, como acessibilidade e resiliência, garantindo que a aplicação seja utilizável em qualquer navegador ou condição de rede.

3.  **URLs Amigáveis e Estruturadas**
    Cada recurso principal (filme, pessoa, etc.) possui uma URL única e legível (slug). Essa prática, além de melhorar a experiência de navegação, é um pilar fundamental para a indexação por mecanismos de busca (SEO) e para a criação de APIs RESTful, caso o projeto fosse expandido.

---

## 🛠️ Tecnologias Utilizadas

* **Backend:** Django, Python
* **Frontend:** HTMX, HTML5, CSS3
* **Banco de Dados:** PostgreSQL (padrão do Railway, compatível com SQLite para dev local)
* **Servidor de Produção:** Gunicorn
* **Deploy:** Railway, Whitenoise

---

## 🚀 Como Executar o Projeto Localmente

Siga os passos abaixo para ter uma cópia do projeto rodando em sua máquina.


### 1. Clone o repositório
```bash
git clone https://github.com/edu292/django-movie-rental
cd NOME_DO_REPOSITORIO
```

### 2. Crie e ative um ambiente virtual (recomendado)
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instale as dependências
```bash
pip install requirements.txt
```

### 4. Crie um arquivo .env na raiz do projeto
Adicione as seguintes variáveis de ambiente:
```bash
DATABASE_URL=sqlite:///db.sqlite3  (para desenvolvimento local)
SECRET_KEY=sua_secret_key_super_segura  
ALLOWED_HOSTS='*'
DEBUG=True
USE_X_FORWARDED_HOST=False
SECURE_SSL_REDIRECT=False
SESSION_COOKIE_SECURE=False
CSRF_COOKIE_SECURE=False 
```

### 5. Aplique as migrações do banco de dados
```bash
python manage.py migrate
```

### 6. Crie um superusuário para acessar o Django Admin
```bash
python manage.py createsuperuser
```

### 7. Inicie o servidor de desenvolvimento
```bash
python manage.py runserver
```
