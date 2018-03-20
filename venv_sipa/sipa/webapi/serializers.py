# -*- coding: utf-8 -*-
from rest_framework import  serializers
from .models import orgao, categoria, posto, servico, cidadao, agente, horario
from django.contrib.auth.models import User
from django.db import transaction

class orgaoSerializer(serializers.ModelSerializer):

    class Meta:
        model=orgao
        fields= ('cod_orgao','descricao','sigla','site')


class categoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model=categoria
        fields=('cod_categoria', 'descricao')

class servicoSerializer(serializers.ModelSerializer):

       class Meta:
        model = servico
        fields= ('cod_servico', 'descricao')

class postoSerializer(serializers.ModelSerializer):
    orgao = serializers.StringRelatedField(many=False)
    categoria = serializers.StringRelatedField(many=False)
    servicos = serializers.StringRelatedField(many=True)
    horarios = serializers.StringRelatedField(many=True)

    class Meta:
        model = posto
        fields = ('cod_posto','descricao','nif','tel','email','endereco', 'orgao', 'categoria', 'servicos', 'horarios')


class userSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username')


class cidadaoSerializer():
    utilizador = userSerializer(required=True)

    class Meta:
        model = cidadao
        fields = ('user','nome','sobrenome','email','tel','endereco')


class agenteSerializer():
    utilizador = userSerializer(required=True)
    posto = serializers.StringRelatedField(many=False)

    class Meta:
        model = agente
        fields = ('user','nome','sobrenome','email','tel','endereco', 'posto')


class horarioSerializer():

    class Meta:
        model = horario
        fields = ('dia', 'horainicio','horafinal')
