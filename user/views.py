from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('main:home'))
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})