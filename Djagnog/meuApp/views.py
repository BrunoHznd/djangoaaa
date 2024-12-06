from django.shortcuts import render, redirect
from meuApp.models import Produto
# from . import forms
from meuApp.forms import FormProduto

# messagens
from django.contrib import messages

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProdutoSerializer

import requests

def index(request):
    p = Produto.objects.all()
    return render (request, 'index.html', {'produtos':p})

def cadastrar_produto(request):
    if request.method == 'POST':
        formP = FormProduto(request.POST, request.FILES)  # Include request.FILES for image upload

        if formP.is_valid():
            formP.save()  # Salva o produto
            messages.success(request, 'Produto adicionado com sucesso')
            return redirect('index')  # Redireciona para a página principal após sucesso
    else:
        formP = FormProduto()  # Cria uma instância vazia do formulário quando for um GET request

    return render(request, 'cadastrar-produto.html', {'form': formP})
    
# ctrl+P reiniciar servidor de linguagem


@api_view(['GET', 'POST'])
def getProdutos(request):
    if request.method == 'GET':
        produtos  = Produto.objects.all()
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)
    # ADICIONAR PRODUTO
    elif request.method =='POST':
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT','DELETE'])
def getProdutoID(request, id_produto):
    try:
        produto = Produto.objects.get(id=id_produto)
    except Produto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)
    
    # ATUALIZAR PRODUTO
    elif request.method =='PUT':
        serializer = ProdutoSerializer(produto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
def getAPI(request):
    dadosAPI = requests.get('https://jsonplaceholder.typicode.com/users').json()
    return render(request, 'api.html', {'dados':dadosAPI})


from matplotlib import pyplot as plt
import io
import base64
import urllib

# Garficos
def grafico(request):
    prod   = Produto.objects.all()
    nomes  = [prod.nome  for prod in prod]
    precos = [prod.preco for prod in prod] 
    
    fig, xy = plt.subplots()
    xy.bar(nomes, precos)
    xy.set_xlabel('Produto')
    xy.set_ylabel('Preço')
    xy.set_title('Preco dos Produtos')
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    
    string = base64.b64encode(buf.read())
    uri    = 'data:image/png;base64,' + urllib.parse.quote(string)
    
    context = {
        'data': uri
    }
    
    return render(request, 'grafico.html', context)





# LISTAR CURSO
def listar_produto(request):
    p = Produto.objects.all()
    return render(request, 'listar-produto.html', {'produtos': p})


# EDITAR CURSO
def editar_produto(request, id_produto):
    p = Produto.objects.get(id=id_produto)

    if request.method == 'POST':
        form = FormProduto(request.POST, request.FILES, instance=p)
        
        if form.is_valid():
            form.save()
            messages.success(request, f'Produto atualizado com sucesso!')
            return redirect('index')
    else:
        form = FormProduto(instance=p)
    
    context = {
        'form': form
    }
    
    return render(request, 'editar-produto.html', context)


# EXCLUIR CURSO
def excluir_produto(request, id_produto):
    p = Produto.objects.get(id=id_produto)
    p.delete()
    messages.success(request, f'Produto excluido com sucesso !')
    return redirect('index')

