from django.shortcuts import render, reverse
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.decorators.http import require_POST, require_http_methods
from django_htmx.http import HttpResponseClientRedirect


@require_http_methods(['GET', 'POST'])
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return HttpResponseClientRedirect(reverse('main:home'))
    form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return HttpResponseClientRedirect(reverse('main:home'))

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return HttpResponseClientRedirect(reverse('main:home'))
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', context={'form': form})


@require_POST
def logout(request):
    auth.logout(request)
    return HttpResponseClientRedirect('/')
