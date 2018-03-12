# -*- coding: utf-8 -*-
from rest_framework import  serializers
from .models import orgao, categoria, posto, servico
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

    class Meta:
        model = posto
        fields = ('cod_posto','descricao','nif','tel','email','endereco', 'orgao', 'categoria', 'servicos')
