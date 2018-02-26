# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import orgao, categoria, posto
from .serializers import orgaoSerializer, categoriaSerializer, postoSerializer
from django.http import Http404
from rest_framework.decorators import api_view

# Area de criação de views

#View para listar orgãos
class orgaoLista(APIView):
    """
    Fornece a lista de todos os orgãos e da a possibilidade de criar um novo.
    """
    def get(self, request, format=None):
        Orgao = orgao.objects.all()
        serializer = orgaoSerializer(Orgao, many=True)
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
        Orgao = self.get_object(pk)
        serializer = orgaoSerializer(Orgao)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Orgao = self.get_object(pk)
        serializer = orgaoSerializer(Orgao, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Orgao = self.get_object(pk)
        Orgao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#View para listar categorias
class categoriaLista(APIView):

    def get(self, request, format=None):
        Categoria = categoria.objects.all()
        serializer = categoriaSerializer(Categoria, many=True)
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
        Categoria = self.get_object(pk)
        serializer = categoriaSerializer(Categoria)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Categoria = self.get_object(pk)
        serializer = categoriaSerializer(Categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Categoria = self.get_object(pk)
        Categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#View para listar postos
class postoLista(APIView):
    def get(self, request, format=None):
        Posto = posto.objects.all()
        serializer = postoSerializer(Posto, many=True)
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
        Posto = self.get_object(pk)
        serializer = postoSerializer(Posto)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Posto = self.get_object(pk)
        serializer = postoSerializer(Posto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Posto = self.get_object(pk)
        Posto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)