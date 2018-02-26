# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Aréa de criação dos modelos
#Orgãos - Ex: Ministério do Comércio
class orgao(models.Model):
    cod_orgao=models.IntegerField(unique=True, verbose_name='Código')
    descricao=models.CharField(max_length=100,unique=True, verbose_name='Descrição')
    sigla=models.CharField(max_length=20, verbose_name='SIGLA')
    site=models.CharField(max_length=20,verbose_name='Site', default='www.sipa.co.ao')
    estado=models.BooleanField(default=True, verbose_name='Activado')
    data_registo=models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.descricao

# Categórias - Ex: Loja de Registo | Conservatória | Posto de Identificação
class categoria(models.Model):
    cod_categoria = models.IntegerField(unique=True, verbose_name='Código')
    descricao = models.CharField(max_length=100, unique=True, verbose_name='Descrição')
    estado = models.BooleanField(default=True, verbose_name='Activado')
    data_registo = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.descricao

#Postos - Ex: Posto de Identificação do Rangel
class posto(models.Model):
    cod_posto=models.IntegerField(unique=True, verbose_name='Código')
    descricao=models.CharField(max_length=100, unique=True, verbose_name='Descrição')
    nif=models.CharField(max_length=15, unique=True, verbose_name='Número de Idenficação Fiscal')
    tel=models.CharField(max_length=20, verbose_name='Telefone')
    email=models.EmailField(default='info@sipa.co.ao', verbose_name='E-mail')
    endereco=models.CharField(max_length=50, verbose_name='Endereço')
    estado=models.BooleanField(default=True, verbose_name='Activado')
    data_registo=models.DateTimeField(auto_now=True, null=True, blank=True)
    orgao=models.ForeignKey(orgao, related_name='orgao', on_delete=models.CASCADE)
    categoria=models.ForeignKey(categoria, related_name='categoria', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('orgao', 'descricao', 'categoria')
        ordering = ['descricao']

    def __unicode__(self):
        return '%s: %s' ', %s' % (self.orgao, self.descricao, self.categoria)


"""
class servico(models.Model):
    cod_servico=models.IntegerField(unique=True, verbose_name='Código')
    descricao=models.CharField(max_length=100, unique=True, verbose_name='Descrição')
    estado=models.BooleanField(default=True, verbose_name='Activado')
    data_registo=models.DateTimeField(auto_now=True, null=True, blank=True)
    posto=models.ForeignKey(posto, related_name='posto', on_delete=models.CASCADE)

    def __str__(self):
        return  self.descricao

"""