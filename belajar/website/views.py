from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse

def index(request):
    print("user=", request.user)
    user = request.user
    context_data = {
        'title': 'website',
        'user': user,
    }
    return render(request, 'websites/index.html', context_data)

def register_view(request):
    form = RegistrationForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect(reverse('websites:login'))

    context_data = {
        'title': 'website',
        'form': form,
    }
    return render(request, 'websites/register.html', context_data)

def login_view(request):
    form = LoginForm(data=request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            print(username, password, user)
            if user is not None:
                login(request, user)
                return redirect(reverse('websites:index'))

    context_data = {
        'title': 'website',
        'form': form,
    }
    return render(request, 'websites/login.html', context_data)

def logout_view(request):
    logout(request)
    return redirect(reverse('websites:index'))