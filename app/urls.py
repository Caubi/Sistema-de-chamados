from .views import *
from django.conf.urls import include, url



urlpatterns = [
    url(r'^maquina/listar/(?P<categoria>[\w\-]+)/$', listar_maquina, name='listar_maquina'),
    url(r'^maquina/listar/$', listar_maquina, name='listar_maquina'),
    url(r'^chamado/listar/$', listar_chamado, name='listar_chamado'),
    url(r'^maquina/perfil/(?P<pk>[0-9]+)', perfil_maquina, name='perfil_maquina'),
    url(r'^chamado/perfil/(?P<pk>[0-9]+)', perfil_chamado, name='perfil_chamado'),
    url(r'^logar/$', logar, name='logar'),
    url(r'^deslogar/$', deslogar, name='deslogar'),
    url(r'^maquina_new/', maquina_new, name='maquina_new'), # Envia para a nossa view a view=" maquina_new " com o nome maquina_new
    url(r'^maquina_remove/(?P<pk>[0-9]+)', maquina_remove, name='maquina_remove'),
    url(r'^maquina_edit/(?P<pk>[0-9]+)', maquina_edit, name='maquina_edit') # Definimos com parêntestes () para definir que o que está dentro é um parâmetro e dentro dessa variável "<pk>" vamos colocar dígitos "um" ou "mais" que isso é definido pelo símbolo de "+" de 0 á 9, podendo ser de 0 a n dígitos e isso será o id de nosso livro que será setado na variável "pk" e enviado para nosso "livro_edit" por fim definimos o nome da rota que será "livro_edit"

]