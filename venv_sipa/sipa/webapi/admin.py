# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import  orgao, categoria, posto, servico, cidadao, agente, horario
# Area de registo dos modelos

admin.site.register(orgao)
admin.site.register(categoria)
admin.site.register(posto)
admin.site.register(servico)
admin.site.register(cidadao)
admin.site.register(agente)
admin.site.register(horario)