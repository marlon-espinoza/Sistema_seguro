from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class Index(TemplateView):
	template_name = 'index.html'
	def get_context_data(self, **kwargs):
		context = super(Index, self).get_context_data(**kwargs)
		print "Entra aqui!!"
		return context

class Administrador(TemplateView):
	template_name = 'administrador.html'
	def get_context_data(self, **kwargs):
		context = super(Administrador, self).get_context_data(**kwargs)
		print "Entra aqui!!"
		return context

class Usuario(TemplateView):
	template_name = 'usuario.html'
	def get_context_data(self, **kwargs):
		context = super(Usuario, self).get_context_data(**kwargs)
		print "Entra aqui!!"
		return context