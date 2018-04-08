# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from Adocao.forms import AnimalForm, UserForm
from Adocao.models import Animal


# CRUD ANIMAL
@login_required(login_url='loginView')
def index(request):
    animais = Animal.objects.all()
    print(animais.values('nome', 'usuarioAlteracao'))
    return render(request, 'adocao/index.html', {'animais': animais})


@login_required(login_url='loginView')
def newAnimal(request):
    if request.method == 'POST':
        form = AnimalForm(request, request.POST, request.FILES)
        if form.is_valid():
            animal = form.save(commit=False)
            animal.usuarioAlteracao = request.user
            animal.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = AnimalForm(request)

    return render(request, 'adocao/newAnimal.html', {'form': form})


@login_required(login_url='loginView')
def editAnimal(request, idAnimal):
    animal = get_object_or_404(Animal, pk=idAnimal)
    if request.method == 'POST':
        form = AnimalForm(request, request.POST, request.FILES, instance=animal)
        if form.is_valid():
            animal.usuarioAlteracao = request.user
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = AnimalForm(request, instance=animal)

    return render(request, 'adocao/newAnimal.html', {'animal': animal, 'form': form, })


@login_required(login_url='loginView')
def takeAnimal(request, idAnimal):
    animal = get_object_or_404(Animal, pk=idAnimal)
    if request.method == 'POST':
        form = AnimalForm(request, request.POST, request.FILES, instance=animal)
        if form.is_valid():
            animal.usuarioAdotou = request.user
            animal.adotado = True
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = AnimalForm(request, instance=animal)

    return render(request, 'adocao/takeAnimal.html', {'animal': animal, 'form': form, })


@login_required(login_url='loginView')
def delAnimal(request, idAnimal):
    animal = get_object_or_404(Animal, pk=idAnimal)
    animal.delete()
    index(request)


#--Controle de Usuarios
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



def newUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserForm()
    return render(request, 'adocao/newUser.html', {'form': form})

'''
@login_required(login_url='loginView')
def GpaUserUpdate(request, iduser):
    user = get_object_or_404(User, id=iduser)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserForm(instance=user)

    return render(request, 'core/gpauser_create.html', {'user': user, 'form': form, })
'''