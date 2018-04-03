from uuid import uuid4

from django.db import models
from PIL import Image

import os


# Create your models here.

def path_and_rename(instance, filename):
    upload_to = 'logos/'
    ext = filename.split('.')[-1]
    ext = 'jpg'
    # get filename
    if instance.pk:
        filename = 'logo_thumb_{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = 'logo_thumb_{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class Clube(models.Model):
    nome = models.CharField(u'Nome', max_length=3)
    apelido = models.CharField(u'Apelido', max_length=200)
    especie = models.CharField(u'Especie', max_length=100, null=True, blank=True)
    raca = models.CharField(u'Raça', max_length=100, null=True, blank=True)
    observacao = models.TextField(u'Observação', max_length=512, null=True, blank=True)
    adotado = models.BooleanField(u'Adotado', default=False)
    logo = models.ImageField(u'Logo', max_length=350, null=True, blank=True, upload_to=path_and_rename)

    def __str__(self):
        return self.nome