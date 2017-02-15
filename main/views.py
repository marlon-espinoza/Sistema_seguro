from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import *
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
		context = super(Administradores, self).get_context_data(**kwargs)
		print "Entra aqui!!"
		return context

class Usuarios(TemplateView):
	template_name = 'usuario.html'
	def get_context_data(self, **kwargs):
		context = super(Usuarios, self).get_context_data(**kwargs)
		print "Entra aqui!!"
		return context

def loginUsuario(request):
	if request.method == 'POST':
		try:
			usuario = request.POST.get("username")
			print usuario
			password = request.POST.get("password")
			print password
			usuario = Usuario.objects.get(usuario=usuario,password=password)
			print usuario
			return HttpResponse(1)
		except Exception as e:
			print e
			return HttpResponse(0)
def loginAdmin(request):
	if request.method == 'POST':
		try:
			usuario = request.POST.get("username")
			print usuario
			password = request.POST.get("password")
			print password
			usuario = Administrador.objects.get(usuario=usuario,password=password)
			print usuario
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