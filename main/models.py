from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager,BaseUserManager

# Create your models here.
class Administrador(AbstractBaseUser):
	usuario = models.CharField(max_length=15,unique=True)
	nombre = models.CharField(max_length=30,blank=True,null=True)
	apellido = models.CharField(max_length=30,blank=True,null=True)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=True)
	USERNAME_FIELD = 'usuario'
	objects = UserManager()

	def __unicode__(self):
		return self.usuario

class Usuario(AbstractBaseUser):
	usuario = models.CharField(max_length=15,unique=True)
	nombre = models.CharField(max_length=30,blank=True,null=True)
	apellido = models.CharField(max_length=30,blank=True,null=True)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=True)
	USERNAME_FIELD = 'usuario'
	objects = UserManager()

	def __unicode__(self):
		return self.usuario

class Pelicula(models.Model):
	nombre = models.CharField(max_length=15)
	descripcion = models.CharField(max_length=30)
	estrella = models.DecimalField(max_digits=5,decimal_places=0)
	url = models.CharField(max_length=125)
	imagen = models.CharField(max_length=125)
	vistas = models.DecimalField(max_digits=20,decimal_places=0)
	usuario = models.ForeignKey(Usuario)

	def __unicode__(self):
		return self.nombre
