import os
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .utils import make_tree


def index(request):
    return render(request, 'gallery/index.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                next_url = request.POST.get('next')
                return HttpResponseRedirect(next_url or reverse('index'))
            else:
                return render(request, 'gallery/login.html',
                              {'error': 'Your account is inactive'})
        else:
            return render(request, 'gallery/login.html',
                          {'error': 'Invalid login'})
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'gallery/login.html', {})


@login_required
def gallery(request):
    tree = make_tree(settings.MEDIA_ROOT)
    return render(request, 'gallery/gallery.html', {'tree': tree})
