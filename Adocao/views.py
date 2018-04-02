# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    if request.method == 'POST':
        nome = request.POST.get('name',u'nao tem nome')
        return HttpResponse(u'o nome é %s' %nome)
    else:
        formulario = '''
        <form action="." method="post">
            <input type="text" name="name" maxlength="100" />
            <button type="submit">Enviar</button>
        </form>
        '''
        return HttpResponse(formulario)
