from django.conf.urls import url
from django.views import generic 
from forum import views
urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^post/(?P<pk>\d+)/$', views.ver_post, name='ver_post'),
    url(r'^novo_post/$', views.editar_post, name ='novo_post'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.editar_post, name='editar_post'),
    url(r'^post/(?P<pk>\d+)/comentar/$', views.comentar_post, name='comentar_post'),
    url(r'^comentario/(?P<pk>\d+)/edit/$', views.editar_comentario, name='editar_comentario'),
]