# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import  orgao, categoria, posto
# Area de registo dos modelos

admin.site.register(orgao)
admin.site.register(categoria)
admin.site.register(posto)
#admin.site.register(servico)