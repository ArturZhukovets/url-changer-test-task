from django.shortcuts import render, redirect
from django.contrib import messages
from uuid import uuid4
from django.contrib.auth import login, logout, authenticate
from .models import Url
from .forms import UrlForm, UserRegisterForm, UserLoginForm



def index(request):
    """Url is generated automatically. Using the function uuid4()
    The domain will be the address of the server
    If the user is registered, all short links will be displayed to him"""
    domain = 'localhost:8000/'   # enter your domain here
    all_links = Url.objects.all()
    url_id = str(uuid4())[:6]
    short_url = domain + url_id
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            new_url = Url(source_url=form.cleaned_data['source_url'], url_id=url_id)
            new_url.save()
            context = {'form': form,'url_id': url_id, 'short_url': short_url, 'links': all_links}
            return render(request, 'urlshorter/index.html', context)
    else:
        form = UrlForm()
    context = {'form':form, 'links': all_links, 'domain':domain}

    return render(request, 'urlshorter/index.html', context)


def generated_url(request, pk):
    """Gets the address of the full link and redirects to it"""
    origin_url = Url.objects.get(url_id=pk)
    return redirect(origin_url.source_url)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "You have successfully registered!")
            return redirect('index')
        else:
            messages.error(request, 'Registration error')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'urlshorter/register.html', context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)  # todo "data=" proverit' pochemu ne rabotaet bez dati
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, 'urlshorter/login.html', context={'form': form})


def user_logout(request):
    logout(request)
    return redirect('index')


