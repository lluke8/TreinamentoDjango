# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.forms import HiddenInput
# Register your models here.
from forum import models

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_criacao', 'usuario')
   # list_filter = ('usuario', )
    search_fields = ('titulo', 'conteudo')
    date_hierarchy = ('data_criacao')

    def get_form(self, request, *args, **kwargs):
        form = super(PostAdmin, self).get_form(request, *args, **kwargs)
        qs = form.base_fields['usuario'].queryset
        form.base_fields['usuario'].queryset = qs.filter(id=request.user.id)
        form.base_fields['usuario'].widget = HiddenInput()
        return form

    def get_changeform_initial_data(self, request):
        return {
            'usuario': request.user
        }

    def has_change_permission(self, request, post=None):
        perm = super(PostAdmin, self).has_change_permission(request, post)
        if post:
            return perm and post.usuario == request.user
        return perm

    def has_delete_permission(self, request, post=None):
        perm = super(PostAdmin, self).has_change_permission(request, post)
        if post:
            return perm and post.usuario == request.user
        return perm

    def get_actions(self, request):
        return []

    def get_list_filter(self, request):
        if request.user.is_superuser:
            return ['usuario']
        return []

    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        if(request.user.is_superuser):
            return qs 
        return qs.filter(usuario=request.user.id)