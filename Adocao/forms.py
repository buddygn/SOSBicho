# -*- coding: utf-8 -*-
from PIL import Image
from django.contrib.auth.models import User
from django.forms import ModelForm, FloatField, HiddenInput, Textarea
from django import forms

from Adocao.models import Animal


class AnimalForm(ModelForm):
    x = FloatField(widget=HiddenInput(), required=False)
    y = FloatField(widget=HiddenInput(), required=False)
    width = FloatField(widget=HiddenInput(), required=False)
    height = FloatField(widget=HiddenInput(), required=False)

    def __init__(self, request, *args, **kwargs):
        self.user = request.user
        super(AnimalForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Animal
        exclude = ['usuarioAlteracao']
        widgets = {
            'observacao': Textarea(attrs={'rows': 3}),
        }

    def save(self, commit=True):
        print('user',self.user)
        animal = super(AnimalForm, self).save(commit=False)
        animal.usuarioAlteracao = self.user
        animal = super(AnimalForm, self).save()

        if self.cleaned_data.get('x') is not None:

            x = int(self.cleaned_data.get('x'))
            y = int(self.cleaned_data.get('y'))
            w = int(self.cleaned_data.get('width'))
            h = int(self.cleaned_data.get('height'))

            image = Image.open(animal.foto)

            cropped_image = image.crop((x, y, w + x -1, h + y -1 ))
            resized_image = cropped_image.resize((300, 300), Image.ANTIALIAS)
            resized_image.save(animal.foto.path)
        return Animal


class AnimalForm(ModelForm):
    def __init__(self, request, *args, **kwargs):
        self.user = request.user
        super(AnimalForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Animal
        exclude = ['usuarioAlteracao']
        widgets = {
            'observacao': Textarea(attrs={'rows': 3}),
        }



class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email' ]
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

