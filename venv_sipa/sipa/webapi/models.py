# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Aréa de criação dos modelos
#Orgãos - Ex: Ministério do Comércio
class orgao(models.Model):
    cod_orgao=models.IntegerField(unique=True, verbose_name='Código')
    descricao=models.CharField(max_length=100,unique=True, verbose_name='Descrição')
    sigla=models.CharField(max_length=20, verbose_name='SIGLA')
    site=models.CharField(max_length=20,verbose_name='Site', default='www.sipa.co.ao')
    estado=models.BooleanField(default=True, verbose_name='Activado')
    data_registo=models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name='Orgão'

    def __unicode__(self): #unicode para aceittar o encondig: utf8 para os acentos do português.
        return self.descricao

# Categórias - Ex: Loja de Registo | Conservatória | Posto de Identificação
class categoria(models.Model):
    cod_categoria = models.IntegerField(unique=True, verbose_name='Código')
    descricao = models.CharField(max_length=100, unique=True, verbose_name='Descrição')
    estado = models.BooleanField(default=True, verbose_name='Activado')
    data_registo = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name='Catégoria'

    def __unicode__(self):
        return self.descricao

class servico(models.Model):
     cod_servico = models.IntegerField(unique=True, verbose_name='Código')
     descricao = models.CharField(max_length=100, unique=True, verbose_name='Descrição')
     estado = models.BooleanField(default=True, verbose_name='Activado')
     data_registo = models.DateTimeField(auto_now=True, null=True, blank=True)

     class Meta:
         verbose_name='Serviço'

     def __unicode__(self):
         return self.descricao

class horario(models.Model):
    DIA_CHOICES = (
             (u'segunda-feira', 'SEGUNDA-FEIRA'),
             (u'terça-feira', 'TERÇA-FEIRA'),
             (u'quarta-feira', 'QUARTA-FEIRA'),
             (u'quinta-feira', 'QUINTA-FEIRA'),
             (u'sexta-feira', 'SEXTA-FEIRA'),
         )
    dia = models.CharField(max_length=20, choices=DIA_CHOICES)
    horainicio = models.TimeField(u'Hora de Ínicio', help_text=u'Hora de Ínicio')
    horafinal = models.TimeField(u'Hora de Ínicio', help_text=u'Hora de Ínicio')

    class Meta:
        verbose_name = 'Horário'

    def __unicode__(self):
        return '%s: %s - %s' % (self.dia, self.horainicio, self.horafinal)


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
    servicos=models.ManyToManyField(servico)
    horarios=models.ManyToManyField(horario)

    class Meta:
        unique_together = ('orgao', 'descricao', 'categoria')
        ordering = ['descricao']

    def __unicode__(self):
        return '%s' % (self.descricao)


#Cidadao - Ex: Adilson Pedro
class cidadao(models.Model):
    nome=models.CharField(max_length=50, verbose_name='Nome')
    sobrenome=models.CharField(max_length=50, verbose_name='Sobrenome')
    tel=models.CharField(max_length=20, verbose_name='Telefone')
    email=models.EmailField(default='eu@exemplo.com', verbose_name='E-mail')
    endereco=models.CharField(max_length=50, verbose_name='Morada')
    estado=models.BooleanField(default=True, verbose_name='Activado')
    data_registo=models.DateTimeField(auto_now=True, null=True)
    utilizador = models.OneToOneField(User)

    class Meta:
        verbose_name='Cidadão'

    def __unicode__(self):
        return '%s, %s' % (self.nome, self.sobrenome)


class agente(models.Model):
    nome=models.CharField(max_length=50, verbose_name='Nome')
    sobrenome=models.CharField(max_length=50, verbose_name='Sobrenome')
    tel=models.CharField(max_length=20, verbose_name='Telefone')
    email=models.EmailField(default='eu@exemplo.com', verbose_name='E-mail')
    endereco=models.CharField(max_length=50, verbose_name='Morada')
    estado=models.BooleanField(default=True, verbose_name='Activado')
    data_registo=models.DateTimeField(auto_now=True, null=True)
    utilizador = models.OneToOneField(User)
    posto = models.ForeignKey(posto, related_name='posto', on_delete=models.CASCADE)

    class Meta:
        verbose_name='Agente'

    def __unicode__(self):
        return '%s, %s' % (self.nome, self.sobrenome)

