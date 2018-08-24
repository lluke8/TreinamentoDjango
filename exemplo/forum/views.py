# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.utils.timezone import now
from forum import models
from django.views import generic
from forum import models
from forum import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

class Index(generic.ListView):
    template_name = 'index.html'
    model = models.Post
    context_object_name = 'posts'
    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['titulo'] = u'Forum bugado'
        return context

# class PostView(generic.DetailView):
#     template_name = 'ver_post.html'
#     model = models.Post
#     context_object_name = 'post'

#     def get_context_data(self, **kwargs):
#         context = super(PostView, self).get_context_data(**kwargs)
#         context['titulo'] = u'Forum bugado'
#         return context

#def index(request):
 #   return HttpResponse(render(request,
  #   'index.html',
   #   {'posts': models.Post.objects.all()}
    #  )
     # )

def ver_post(request,  pk):
   post = models.Post.objects.get(pk=pk)
   return render(
       request,
       'ver_post.html',
      {'post' : post, 'titulo': post.titulo}
   )

#def novo_post(request):

 #   if request.method == 'GET':
  #      form = forms.PostForm()
       
   # elif request.method == 'POST':
    #    form = forms.PostForm(request.POST)
     #   if form.is_valid():
      #      form.save()
       #     return redirect('index')
    #return render(request, 'form.html', {'form':form})

@login_required
def editar_post(request, pk = None):
    if pk:
        post = get_object_or_404(models.Post, pk=pk)
        if post.usuario != request.user:
            raise PermissionDenied
    else:
        post = None
    if request.method == 'POST':
        dados = request.POST
    else:
        dados = None

    form = forms.PostForm(dados, instance=post, initial={'usuario': request.user.id})           
    form.fields['usuario'].queryset = User.objects.filter(id=request.user.id)

    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'form.html', {'form':form})

@login_required
def comentar_post(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    
    if request.method == 'POST':
        dados = request.POST
    else:
        dados = None

    form = forms.CommentForm(dados, initial= {'post': post.id, 'usuario': request.user.id})
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'comentar.html', {'form':form})
