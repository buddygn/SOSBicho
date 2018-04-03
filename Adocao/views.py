# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


@login_required(login_url='/SOSBicho/login/')
def index(request):
    return render(request, 'adocao/index.html')


@login_required(login_url='/SOSBicho/login/')
def newAnimal(request):
    return render(request, 'adocao/index.html')

def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'adocao/login.html', {"error": True})
    else:
        return render(request, 'adocao/login.html', None)



'''
@login_required(login_url='loginView')
def UserCreate(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            return HttpResponseRedirect(reverse('gpauser_list'))
        else:
            messages.error(request, "Error")
    else:
        form = UserForm()
    return render(request, 'core/gpauser_create.html', {'form': form})


@login_required(login_url='loginView')
def GpaUserUpdate(request, iduser):
    user = get_object_or_404(User, id=iduser)
    if request.method == 'POST':
        form = GpaUserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            return HttpResponseRedirect(reverse('gpauser_list'))
        else:
            messages.error(request, "Error")
    else:
        form = GpaUserForm(instance=user)

    return render(request, 'core/gpauser_create.html', {'user': user, 'form': form, })
'''