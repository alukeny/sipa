# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-20 13:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0007_auto_20180320_1300'),
    ]

    operations = [
        migrations.CreateModel(
            name='agente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=50, verbose_name='Sobrenome')),
                ('tel', models.CharField(max_length=20, verbose_name='Telefone')),
                ('email', models.EmailField(default='eu@exemplo.com', max_length=254, verbose_name='E-mail')),
                ('endereco', models.CharField(max_length=50, verbose_name='Morada')),
                ('estado', models.BooleanField(default=True, verbose_name='Activado')),
                ('data_registo', models.DateTimeField(auto_now=True, null=True)),
                ('posto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posto', to='webapi.posto')),
            ],
            options={
                'verbose_name': 'Agente',
            },
        ),
    ]
