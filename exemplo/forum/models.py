# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=1024, verbose_name=u'Título')
    conteudo = models.TextField(verbose_name=u'conteúdo')
    usuario = models.ForeignKey('auth.User', null=True, on_delete=models.SET_NULL, verbose_name=u'Usuário')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name= u'Data de criação')

    def __unicode__(self):
        return u'{} - {}'.format(self.titulo, self.data_criacao)



class Comment(models.Model):
    comentario = models.TextField(verbose_name = u'Comentário')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name= u'Data de criação')
    usuario = models.ForeignKey('auth.User', null=True, on_delete=models.SET_NULL, verbose_name=u'Usuário')

    def __unicode__(self):
        return u'{}'.format(self.comentario)
