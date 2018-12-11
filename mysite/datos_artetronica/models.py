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

class Central(models.Model):
	     
	     nombre=models.CharField(max_length=60,blank=True)   
	     cararcteristicas=models.TextField(blank=True)        
	     fecha_ingreso = models.DateField(default=datetime.now,editable = False)	     

	     def __str__(self):
		    		return  self.codigo
	     class Admin:
		    		list_display = ('codigo', 'marca', 'modelo','caracteristicas')


PRIVILEGIOS=(
			('DE_ALTA', 'DE_ALTA'),
			('DE_BAJA', 'DE_BAJA'),
		     )


class Usuarios(models.Model):
	     codigo=models.IntegerField()
	     nombre=models.CharField(max_length=30)
	     apellidos=models.CharField(max_length=30)
	     pasword=models.CharField(max_length=4)
	     email = models.EmailField(blank=True)
	     privilegio=models.CharField(max_length=30,choices=PRIVILEGIOS,default="'DE_BAJA")
	     fecha_ingreso = models.DateField(default=datetime.now,editable = False)	    
	     
	     def __str__(self):
		    		return  self.codigo
	     class Admin:
		    		list_display = ('id_usuario')



class Transformador(models.Model):

	     central=models.ForeignKey('Central')
	     codigo=models.CharField(max_length=60,blank=True)
	     marca=models.CharField(max_length=60,blank=True)
	     modelo=models.CharField(max_length=60,blank=True)
	     cararcteristicas=models.TextField(blank=True)  	     
	     #imagen1      = models.ImageField(upload_to='tmp')	  
	     imagen1 = ImageField(upload_to='tmp',blank=True)	    
	     #nombre_recurso=models.CharField(max_length=40,blank=True)
	     #recurso=models.URLField(blank=True)	     
	     fecha_ingreso = models.DateField(default=datetime.now,editable = False)	     

	     def __str__(self):
		    		return  self.codigo
	     class Admin:
		    		list_display = ('codigo', 'marca', 'modelo','caracteristicas')



#from django.contrib.postgres.fields import ArrayField


class Medicion(models.Model):

	     equipo=models.ForeignKey('Transformador')  	
	     usuario=models.ForeignKey('Usuarios')

	     Hidrogeno=models.FloatField(default=0,blank=True,null=True)
	     Oxigeno=models.FloatField(default=0,blank=True,null=True)
	     Nitrogeno=models.FloatField(default=0,blank=True,null=True)
	     Metano=models.FloatField(default=0,blank=True,null=True)
	     Monoxido_de_carbono=models.FloatField(default=0,blank=True,null=True)
	     Etano=models.FloatField(default=0,blank=True,null=True)
	     Dioxido_de_carbono=models.FloatField(default=0,blank=True,null=True)
	     Etileno=models.FloatField(default=0,blank=True,null=True)
	     Acetileno=models.FloatField(default=0,blank=True,null=True)
	     Propileno=models.FloatField(default=0,blank=True,null=True)
	     Propano=models.FloatField(default=0,blank=True,null=True)
	     Butano=models.FloatField(default=0,blank=True,null=True)
	     
	     fecha_ingreso = models.DateField(default=datetime.now,editable = False) 	     
	     def __str__(self):
		    		return  self.equipo
	     class Admin:
		    		list_display = ('equipo', 'fecha')