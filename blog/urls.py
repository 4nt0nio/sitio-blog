from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.lista_posts),
    url (r'^post/(?P<pk>[0-9]+)/$', views.detalle_post),
    url(r'^post/nuevo/$', views.nuevo_post, name='nuevo_post'),
    url(r'^post/(?P<pk>[0-9]+)/editar/$', views.editar_post, name='editar_post'),
]