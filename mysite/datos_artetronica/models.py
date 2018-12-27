#!/usr/bin/python -tt
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.admin.widgets import AdminDateWidget 
from datetime import datetime 

from django.contrib.auth.models import User
#import Image

from PIL import Image as Img

from io import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile

from sorl.thumbnail import ImageField

class Centrales(models.Model):
	     
	     nombre=models.CharField(max_length=60,blank=True)
	     fecha_ingreso = models.DateField(default=datetime.now,editable = False)

	     def __str__(self):
		    		return  self.nombre
	     class Admin:
		    		list_display = ('nombre', 'fecha_ingreso')


PRIVILEGIOS=(
			('DE_ALTA', 'DE_ALTA'),
			('DE_BAJA', 'DE_BAJA'),
		     )


class Usuarios(models.Model):
	     codigo=models.IntegerField()
	     pasword=models.CharField(max_length=4)
	     email = models.EmailField(blank=True)
	     privilegio=models.CharField(max_length=30,choices=PRIVILEGIOS,default="'DE_BAJA")
	     fecha_ingreso = models.DateField(default=datetime.now,editable = False)

	     def __str__(self):
		    		return  self.codigo
	     class Admin:
		    		list_display = ('codigo',' privilegio')



class Transformadores(models.Model):

	     central=models.ForeignKey('Centrales')
	     codigo=models.CharField(max_length=60,blank=True)
	     marca=models.CharField(max_length=60,blank=True)
	     modelo=models.CharField(max_length=60,blank=True)
	     cararcteristicas=models.TextField(blank=True)
	     fecha_ingreso = models.DateField(default=datetime.now,editable = False)

	     def __str__(self):
		    		return  self.codigo
	     class Admin:
		    		list_display = ('codigo', 'marca', 'modelo','caracteristicas')

 
#from django.contrib.postgres.fields import ArrayField
class Mediciones(models.Model):
         central=models.ForeignKey('Centrales')
         transformador=models.ForeignKey('Transformadores')
         codigo_usuario=models.CharField(max_length=60,blank=True)
         Hidrogeno=models.FloatField(default=0,blank=True,null=True)
         Metano=models.FloatField(default=0,blank=True,null=True)
         Acetileno=models.FloatField(default=0,blank=True,null=True)
         Etileno=models.FloatField(default=0,blank=True,null=True)
         Etano=models.FloatField(default=0,blank=True,null=True)
         Monoxido_de_carbono=models.FloatField(default=0,blank=True,null=True)
         Oxigeno=models.FloatField(default=0,blank=True,null=True)
         Nitrogeno=models.FloatField(default=0,blank=True,null=True)
         Dioxido_de_carbono=models.FloatField(default=0,blank=True,null=True)
         fecha_del_analisis = models.DateField(default=datetime.now,null=False)
         fecha_ingreso = models.DateField(default=datetime.now,editable = True)
         def __str__(self):
         	return  self.codigo_usuario
         class Admin:
         	list_display = ('fecha','codigo_usuario','central','transformador')