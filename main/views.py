from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import *
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.contrib.auth import logout
# Create your views here.

class Index(TemplateView):
	template_name = 'index.html'
	def get_context_data(self, **kwargs):
		context = super(Index, self).get_context_data(**kwargs)
		print "Entra aqui!!"
		return context

class Administradores(TemplateView):
	template_name = 'administrador.html'
	def get_context_data(self, **kwargs):
		print self.request.session
		if self.request.session.has_key('admin'):
			username = self.request.session['admin']
			try:
				admin = Administrador.objects.get(usuario=username)
				context = super(Administradores, self).get_context_data(**kwargs)
				return context
			except Exception as e:
				return HttpResponseForbidden()
		else:
			return HttpResponseForbidden()

class Usuarios(TemplateView):
	template_name = 'usuario.html'
	def get_context_data(self, **kwargs):
		print self.request.session
		if self.request.session.has_key('usuario'):
			username = self.request.session['usuario']
			try:
				usuario = Usuario.objects.get(usuario=username)
				context = super(Usuarios, self).get_context_data(**kwargs)
				print "Entra aqui!!"
				return context
			except Exception as e:
				return HttpResponseForbidden()
		else:
			return HttpResponseForbidden()
		


def logout(request):
	for key in request.session.keys():
		del request.session[key]
	
	return redirect('index')


def loginUsuario(request):
	if request.method == 'POST':
		try:
			username = request.POST.get("username")
			password = request.POST.get("password")
			usuario = Usuario.objects.get(usuario=username,password=password)
			print usuario
			request.session['usuario'] = username
			return HttpResponse(1)
		except Exception as e:
			print e
			return HttpResponse(0)
def loginAdmin(request):
	if request.method == 'POST':
		try:
			username = request.POST.get("username")
			password = request.POST.get("password")
			usuario = Administrador.objects.get(usuario=username,password=password)
			print usuario
			request.session['admin'] = username
			return HttpResponse(1)
		except Exception as e:
			print e
			return HttpResponse(0)

def registrarUsuario(request):
	if request.method == 'POST':
		try:
			usuario = request.POST.get("username")
			nombre = request.POST.get("nombre")
			apellido = request.POST.get("apellido")
			password = request.POST.get("password")
			password2 = request.POST.get("confirm-password")
			if password==password2:
				usuario = Usuario(usuario=usuario,nombre=nombre,apellido=apellido,password=password)
				usuario.save()
				return HttpResponse(1)
			else: 
				return HttpResponse("Password no coincide")
		except Exception as e:
			print e
			return HttpResponse(0)