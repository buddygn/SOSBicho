from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models
from PIL import Image

import os


# Create your models here.

def path_and_rename(instance, filename):
    upload_to = 'animal/'
    ext = filename.split('.')[-1]
    ext = 'jpg'
    # get filename
    if instance.pk:
        filename = 'animal_thumb_{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random strinpyhtg
        filename = 'animal_thumb_{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class Animal(models.Model):
    nome = models.CharField(u'Nome', max_length=100)
    apelido = models.CharField(u'Apelido', max_length=200)
    especie = models.CharField(u'Especie', max_length=100, null=True, blank=True)
    raca = models.CharField(u'Raça', max_length=100, null=True, blank=True)
    nascimento =  models.DateField(u'Nascimento', null=True, blank=True)
    observacao = models.TextField(u'Observação', max_length=512, null=True, blank=True)
    adotado = models.BooleanField(u'Adotado', default=False)
    usuarioAdotou = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='usuarioAdotou')
    foto = models.ImageField(u'Logo', max_length=350, null=True, blank=True, upload_to=path_and_rename)
    usuarioAlteracao = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuarioAlteracao')

    def __str__(self):
        return self.nome