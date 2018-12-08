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
    url(r'^maquina_new/', maquina_new, name='maquina_new'),
    url(r'^chamado_new/', chamado_new, name='chamado_new'),
    url(r'^maquina_remove/(?P<pk>[0-9]+)', maquina_remove, name='maquina_remove'),
    url(r'^maquina_edit/(?P<pk>[0-9]+)', maquina_edit, name='maquina_edit'),
    url(r'^chamado_edit/(?P<pk>[0-9]+)', chamado_edit, name='chamado_edit')

]

