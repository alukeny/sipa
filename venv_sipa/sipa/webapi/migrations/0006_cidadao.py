# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-09 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0005_auto_20180228_2105'),
    ]

    operations = [
        migrations.CreateModel(
            name='cidadao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_cidadao', models.IntegerField(unique=True, verbose_name='C\xf3digo')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=50, verbose_name='Sobrenome')),
                ('tel', models.CharField(max_length=20, verbose_name='Telefone')),
                ('email', models.EmailField(default='eu@exemplo.com', max_length=254, verbose_name='E-mail')),
                ('endereco', models.CharField(max_length=50, verbose_name='Morada')),
                ('estado', models.BooleanField(default=True, verbose_name='Activado')),
                ('data_registo', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Cidad\xe3o',
            },
        ),
    ]
