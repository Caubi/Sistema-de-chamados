from django.contrib import admin
from .models import *

# Register your models here.

admin.site.site_url = '/chamado/listar/'
admin.site.register(Tecnico)
admin.site.register(Maquina)
admin.site.register(Chamado)




