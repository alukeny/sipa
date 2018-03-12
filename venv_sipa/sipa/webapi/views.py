# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import orgao, categoria, posto, servico
from .serializers import orgaoSerializer, categoriaSerializer, postoSerializer, servicoSerializer
from django.http import Http404
from rest_framework.decorators import api_view

# Area de criação de views

#Metodo que retorna a view home, para a página principal
def home(request):
    context = locals()
    template = 'home.html'
    return  render(request, template, context)


#View para listar orgãos
class orgaoLista(APIView):
    """
    Fornece a lista de todos os orgãos e da a possibilidade de criar um novo.
    """
    def get(self, request, format=None):
        dados = orgao.objects.all()
        serializer = orgaoSerializer(dados, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = orgaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#View para exibir o orgão em função do primary key e outras operações - update e delete.
class orgaoDetalhes(APIView):
    """
    Fornece opções de consultar por pk, actualizar e deletar.
    """
    def get_object(self, pk):
        try:
            return orgao.objects.get(pk=pk)
        except orgao.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dados = self.get_object(pk)
        serializer = orgaoSerializer(dados)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        dados = self.get_object(pk)
        serializer = orgaoSerializer(dados, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dados = self.get_object(pk)
        dados.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#View para listar categorias
class categoriaLista(APIView):

    def get(self, request, format=None):
        dados = categoria.objects.all()
        serializer = categoriaSerializer(dados, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = categoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#View para exibir a categoria em função do primary key e outras operações - update e delete.
class categoriaDetalhes(APIView):
    """
    Fornece opções de consultar por pk, actualizar e deletar.
    """
    def get_object(self, pk):
        try:
            return categoria.objects.get(pk=pk)
        except categoria.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dados = self.get_object(pk)
        serializer = categoriaSerializer(dados)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        dados = self.get_object(pk)
        serializer = categoriaSerializer(dados, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dados = self.get_object(pk)
        dados.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#View para listar postos
class postoLista(APIView):
    def get(self, request, format=None):
        dados = posto.objects.all()
        serializer = postoSerializer(dados, many=True)
        return  Response(serializer.data)

    def post(self, request, format=None):
        serializer = postoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#View para exibir o posto em função do primary key e outras operações - update e delete.
class postoDetalhes(APIView):
    """
    Fornece opções de consultar por pk, actualizar e deletar.
    """
    def get_object(self, pk):
        try:
            return posto.objects.get(pk=pk)
        except posto.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dados = self.get_object(pk)
        serializer = postoSerializer(dados)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        dados = self.get_object(pk)
        serializer = postoSerializer(dados, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dados = self.get_object(pk)
        dados.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# View para listar serviços
class servicoLista(APIView):

    def get(self, request, format=None):
        dados = servico.objects.all()
        serializer = servicoSerializer(dados, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = servicoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#View para exibir o serviço em função do primary key e outras operações - update e delete.
class servicoDetalhes(APIView):
    """
    Fornece opções de consultar por pk, actualizar e deletar.
    """
    def get_object(self, pk):
        try:
            return servico.objects.get(pk=pk)
        except servico.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dados = self.get_object(pk)
        serializer = servicoSerializer(dados)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        dados = self.get_object(pk)
        serializer = servicoSerializer(dados, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dados = self.get_object(pk)
        dados.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)