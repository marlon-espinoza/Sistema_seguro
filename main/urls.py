from django.conf.urls import include, url
import main.views

urlpatterns = [
   	url(r'^$', main.views.Index.as_view(),name="index"),
   	url(r'^administrador/$', main.views.Administradores.as_view(),name="administrador"),
   	url(r'^usuario/$', main.views.Usuarios.as_view(),name="usuario"),
   	url(r'^login_usuario/$', main.views.loginUsuario,name="login_usuario"),
   	url(r'^login_admin/$', main.views.loginAdmin,name="login_admin"),
  	]