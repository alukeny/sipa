"""sipa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from webapi import  views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^orgao/$', views.orgaoLista.as_view()),
    url(r'^orgao/(?P<pk>[0-9]+)$', views.orgaoDetalhes.as_view()),
    url(r'^categoria/$', views.categoriaLista.as_view()),
    url(r'^categoria/(?P<pk>[0-9]+)$', views.categoriaDetalhes.as_view()),
    url(r'^posto/$', views.postoLista.as_view()),
    url(r'^posto/(?P<pk>[0-9]+)$', views.postoDetalhes.as_view()),
    url(r'^servico/$', views.servicoLista.as_view()),
    url(r'^servico/(?P<pk>[0-9]+)$', views.servicoDetalhes.as_view()),
    url(r'^cidadao/$', views.cidadaoLista.as_view()),
    url(r'^cidadao/(?P<pk>[0-9]+)$', views.cidadaoDetalhes.as_view()),
    url(r'^agente/$', views.agenteLista.as_view()),
    url(r'^agente/(?P<pk>[0-9]+)$', views.agenteDetalhes.as_view()),
    url(r'^horario/$', views.horarioLista.as_view()),
    url(r'^horario/(?P<pk>[0-9]+)$', views.horarioDetalhes.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)