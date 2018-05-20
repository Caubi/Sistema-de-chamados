from django.shortcuts import get_object_or_404
from .models import *
from django.forms import ModelForm
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def listar_maquina(request, template_name="maquinas_list.html"):

    query = request.GET.get("busca", '')# Armazena na variável query onde vamos obter os dados do parâmetro busca que está em 'maquina_lit.html' se não tiver nada ele retorna vazio ''
    page = request.GET.get('page', '')
    #ordenar = request.GET.get("ordenar", '')

    if query: # Se encontrar alguma coisa nessa query, no caso se tiver algum valor significa que precisamos buscar a máquina por um determinado modelo
        maquina = Maquina.objects.filter(num_serie__icontains=query) # Buscar as máquinas de acordo com seu modelo que contém o modelo que enviamos lá no parâmetro busca do noso template. o i de icontains é pra definir que a busca é case insensitive e o contains é que não precisamos digitar o nome completo
    else:
        try:# Senão se agente não tem nenhum valor na variável query significa que não estamos fazendo nenhuma busca
            maquina = Maquina.objects.all() # Com isso ele retorna todas os objetos ou seja todas as  máquinas
            maquina = Paginator(maquina, 6)
            maquina = maquina.page(page)
        except PageNotAnInteger:
            maquina = maquina.page(1)
        except EmptyPage:
            maquina = paginator.page(paginator.num_pages)
    maquinas = {
        'lista': maquina}  # Armazenamos todas as máquinas em uma variável dentro de uma lista apelidamos a variável de 'máquinas'
    return render(request, template_name, maquinas) # Renderizar as informações para o nosso template




    # Senao se cliclar somente no botão de buscar ele vai exibir todos os registros
    # Vai mostrar 3 maquinas por pagina, e vai chamar a paginação


    #else:
    #    try:
    #       if categoria != "Todos":
    #           if ordenar:
    #               maquina = Maquina.objects.filter(tipo=categoria).order_by(ordenar)
    #               else:
    #               maquina = Maquina.objects.filter(tipo=categoria)
#           else:
#if ordenar:
                    #maquina = Maquina.objects.all().order_by(ordenar)
                    #            else:
    #               maquina = Maquina.objects.all()
                    #           maquina = Paginator(maquina, 3)
#          maquina = maquina.page(page)
#       # Excessão caso a página não for um inteiro ela volta pra página inicial um
 #       except PageNotAnInteger:
#           maquina = maquina.page(1)
        # Excessão caso a página seja nulo vazia ela retorna o número de páginas disponíveis pra utilização
#       except EmptyPage:
#           maquina = paginator.page(paginator.num_pages)
#   maquinas = {'lista': maquina}
#return render(request, template_name, maquinas)

def listar_chamado(request, template_name="chamados_list.html"):
    query = request.GET.get("busca",'')
    ordenar = request.GET.get("ordenar",'')
    if query:
        chamado = Chamado.objects.filter(num_chamado__icontains=query)
    else:
        if ordenar:
            chamado = Chamado.objects.all().order_by(ordenar)
        else:
            chamado = Chamado.objects.all()
    chamados = {'lista': chamado}
    return render(request, template_name, chamados)

def perfil_maquina(request, pk, template_name="perfil_maquina.html"):
    maquina = get_object_or_404(Maquina, pk=pk)
    return render(request, template_name, {'maquina': maquina})

def perfil_chamado(request, pk, template_name="perfil_chamado.html"):
    chamado = get_object_or_404(Maquina, pk=pk)
    return render(request, template_name, {'chamado': chamado})

def voltar(request):
    return render(request, 'maquinas_list.html');

def back(request):
    return render(request, 'login.html');

def logar(request, template_name='login.html'): # Recebe uma request com o template 'login.html'
    next = request.GET.get('next', '/maquina/listar/') # Na variável 'next' pega o parâmetro que passamos no 'login.html' a última página que o cara tentou acessar
    if request.method == 'POST': # Se existir alguma coisa ele recupera, senão o padrão será '/listar_usuario/' que é a próxima página depois que ele faz o login
        username = request.POST['usuario'] # Se o método for post ele recupera o usuário que digitamos no formulário
        password = request.POST['senha'] # Se o método for post ele recupera a senha  que digitamos no formulário
        user = authenticate(username=username, password=password) # Tenta autenticar esse cara passamos os parâmetros do usuario e senha  e salvamos na variável 'user'
        if user is not None: # Se existir o usuário e se não for vazio
            login(request, user) # Ele irá utilizar o método login pra logar e autenticar esse cara
            return HttpResponseRedirect(next) # Depois ele retorna pra rota 'next' que obtivemos lá na linha 33, que acessa ou a última página que o cara tentou acessar ou retorna para a página padrão '/listar_usuario/'

        else:
            messages.error(request, 'Usuário ou senha incorretos.')
            return HttpResponseRedirect(settings.LOGIN_URL) # Senao autenticar esse usuário ele retorna para o LOGIN_URL definido lá em 'settings.py'

    return render(request, template_name, {'redirect_to': next}) # Renderiza com request e o template e a última página que o cara tentou acessar que é o 'next'

def deslogar(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)

class MaquinaForm(ModelForm): # Nossos atributos do Livro armazenados do banco de dados
    class Meta:
        model = Maquina
        fields = ['modelo', 'estado', 'patrimonio', 'num_serie', 'ID_chamado', 'tecnico'] # Tem que ser igual na view

def maquina_new(request, template_name='maquina_form.html'):
    form = MaquinaForm(request.POST or None)# Guardar o tipo de formulário na variável form, e ela vai ser uma request do tipo POST
    if form.is_valid(): # Verifica se este formulário é válido
        form.save() # Salva no banco de dados
        return redirect('listar_maquina') # Redireciona para a nossa tela de listagem de livros que é a nossa view definida nas url´s
    return render(request, template_name, {'form': form}) #Retorna renderizando passando o request o nosso template_name e a nossa variável form

def maquina_remove(request, pk): # Vai passar a request e um pimary key, e essa pk faremos uma consulta no nosso banco pra pegar esse maquina
    maquina = Maquina.objects.get(pk=pk)  # Recuperamos a máquina do nosso banco de dados e guardamos na variável maquina
    if request.method == "POST": # Se o método passado é POST....
        maquina.delete() #... Se sim deletamos a máquina
        return redirect('listar_maquina') # Retornamos para nossa listagem de livros para validarmos se foi excluido
    return render(request, 'maquina_delete.html', {'maquina': maquina}) # Retorna renderizando o request a nossa template, e passamos a nossa maquina pra que nessa nosso template possamos imprimir algumas informações dele pra que o usuário tenha certeza que é essa maquina que está removendo

def maquina_edit(request, pk, template_name='maquina_form.html'): # Passa a request, depois passa a primary key, e nosso template
    maquina = get_object_or_404(Maquina, pk=pk) # Aki faz a captura do livro, o "get_object_or_404" Ou ela pega o livro corretamente o ela dispara o erro 404
    if request.method == "POST": # Se o request for POST....
        form = MaquinaForm(request.POST, instance=maquina) #..... Ele vai salvar no nosso form o nosso LivroForm, passando a requisição do tipo POST, e pegando a nossa instância do livro
        if form.is_valid(): # Testa se o formulário é válido....
            maquina = form.save() #... Se for ele vai salvar o formulário
            return redirect('listar_maquina') #.. E redirecionar para nossa listagem de livros
    else:
        form = MaquinaForm(instance=maquina)
    return render(request, template_name, {'form': form}) # Ele renderizar passando uma request o nosso template name, e nossa variável form


