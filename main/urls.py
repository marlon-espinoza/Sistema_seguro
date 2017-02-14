from django.conf.urls import include, url
import main.views

urlpatterns = [
   	url(r'^$', main.views.Index.as_view(),name="index"),
   	url(r'^administrador/$', main.views.Administrador.as_view(),name="administrador"),
   	url(r'^usuario/$', main.views.Usuario.as_view(),name="usuario"),
  	]