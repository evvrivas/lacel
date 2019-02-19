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
	     codigo_usuario=models.CharField(max_length=7)
	     pasword=models.CharField(max_length=4)
	     nombres=models.CharField(max_length=30)
	     apellidos=models.CharField(max_length=30)
	     email = models.EmailField(blank=True)
	     privilegio=models.CharField(max_length=30,choices=PRIVILEGIOS,default="DE_BAJA")
	     fecha_ingreso = models.DateField(default=datetime.now,editable = False)

	     def __str__(self):
		    		return  self.codigo_usuario
	     class Admin:
		    		list_display = ('codigo_usuario',' privilegio')

class Generadores(models.Model):

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
         comentario = models.TextField(blank=True)
         fecha_del_analisis = models.DateField(default=datetime.now,null=False)
         fecha_ingreso = models.DateField(default=datetime.now,editable = True)
         def __str__(self):
         	return  self.codigo_usuario
         class Admin:
         	list_display = ('fecha','codigo_usuario','central','transformador')

  
#from django.contrib.postgres.fields import ArrayField
class Mediciones_rapidas(models.Model):
         central=models.CharField(max_length=60,blank=True)
         transformador=models.CharField(max_length=60,blank=True)         
         Hidrogeno=models.FloatField(default=0,blank=True,null=True)
         Metano=models.FloatField(default=0,blank=True,null=True)
         Acetileno=models.FloatField(default=0,blank=True,null=True)
         Etileno=models.FloatField(default=0,blank=True,null=True)
         Etano=models.FloatField(default=0,blank=True,null=True)
         Monoxido_de_carbono=models.FloatField(default=0,blank=True,null=True)
         Oxigeno=models.FloatField(default=0,blank=True,null=True)
         Nitrogeno=models.FloatField(default=0,blank=True,null=True)
         Dioxido_de_carbono=models.FloatField(default=0,blank=True,null=True)
         comentario = models.TextField(blank=True)
         fecha_del_analisis = models.DateField(default=datetime.now,null=False)
         
         def __str__(self):
         	return  self.central
         class Admin:
         	list_display = ('')


CAG_SI_NO=(
         ('SI', 'SI'),
         ('NO', 'NO'),
           )

class Mediciones_DP(models.Model):
         central=models.ForeignKey('Centrales')
         generador=models.ForeignKey('Generadores')
         codigo_usuario = models.CharField(max_length=60,blank=True)
         
         fecha_del_analisis = models.DateField(default=datetime.now,null=False)
         fecha_ingreso= models.DateField(default=datetime.now,null=False)
              
         frecuencia=models.FloatField(default=0,blank=True,null=True)
         potencia_activa=models.FloatField(default=0,blank=True,null=True)
         potencia_reactiva=models.FloatField(default=0,blank=True,null=True)
         temperatura_promedio=models.FloatField(default=0,blank=True,null=True)
         temperatura_calent=models.FloatField(default=0,blank=True,null=True)
         humedad_relativa=models.FloatField(default=0,blank=True,null=True)
         CAG=models.CharField(max_length=30,choices=CAG_SI_NO,default="SI")

         
         NQNC1posA1=models.FloatField(default=0,blank=True,null=True)
         NQNC2posA1=models.FloatField(default=0,blank=True,null=True)        
         NQNC1negA1=models.FloatField(default=0,blank=True,null=True)
         NQNC2negA1=models.FloatField(default=0,blank=True,null=True)
         
         QMAXC1posA1=models.FloatField(default=0,blank=True,null=True)
         QMAXC2posA1=models.FloatField(default=0,blank=True,null=True)         
         QMAXC1negA1=models.FloatField(default=0,blank=True,null=True)
         QMAXC2negA1=models.FloatField(default=0,blank=True,null=True)

         NQNC1posB1=models.FloatField(default=0,blank=True,null=True)
         NQNC2posB1=models.FloatField(default=0,blank=True,null=True)        
         NQNC1negB1=models.FloatField(default=0,blank=True,null=True)
         NQNC2negB1=models.FloatField(default=0,blank=True,null=True)
         
         QMAXC1posB1=models.FloatField(default=0,blank=True,null=True)
         QMAXC2posB1=models.FloatField(default=0,blank=True,null=True)         
         QMAXC1negB1=models.FloatField(default=0,blank=True,null=True)
         QMAXC2negB1=models.FloatField(default=0,blank=True,null=True)

         NQNC1posC1=models.FloatField(default=0,blank=True,null=True)
         NQNC2posC1=models.FloatField(default=0,blank=True,null=True)        
         NQNC1negC1=models.FloatField(default=0,blank=True,null=True)
         NQNC2negC1=models.FloatField(default=0,blank=True,null=True)
         
         QMAXC1posC1=models.FloatField(default=0,blank=True,null=True)
         QMAXC2posC1=models.FloatField(default=0,blank=True,null=True)         
         QMAXC1negC1=models.FloatField(default=0,blank=True,null=True)
         QMAXC2negC1=models.FloatField(default=0,blank=True,null=True)

         imagen_PRPDD_1 = ImageField(upload_to='tmp',blank=True)
         imagen_3D_1 = ImageField(upload_to='tmp',blank=True)
         imagen_PHD_1 = ImageField(upload_to='tmp',blank=True)

         NQNC3posA2=models.FloatField(default=0,blank=True,null=True)
         NQNC4posA2=models.FloatField(default=0,blank=True,null=True)        
         NQNC3negA2=models.FloatField(default=0,blank=True,null=True)
         NQNC4negA2=models.FloatField(default=0,blank=True,null=True)
         
         QMAXC3posA2=models.FloatField(default=0,blank=True,null=True)
         QMAXC4posA2=models.FloatField(default=0,blank=True,null=True)         
         QMAXC3negA2=models.FloatField(default=0,blank=True,null=True)
         QMAXC4negA2=models.FloatField(default=0,blank=True,null=True)

         NQNC3posB2=models.FloatField(default=0,blank=True,null=True)
         NQNC4posB2=models.FloatField(default=0,blank=True,null=True)        
         NQNC3negB2=models.FloatField(default=0,blank=True,null=True)
         NQNC4negB2=models.FloatField(default=0,blank=True,null=True)
         
         QMAXC3posB2=models.FloatField(default=0,blank=True,null=True)
         QMAXC4posB2=models.FloatField(default=0,blank=True,null=True)         
         QMAXC3negB2=models.FloatField(default=0,blank=True,null=True)
         QMAXC4negB2=models.FloatField(default=0,blank=True,null=True)

         NQNC3posC2=models.FloatField(default=0,blank=True,null=True)
         NQNC4posC2=models.FloatField(default=0,blank=True,null=True)        
         NQNC3negC2=models.FloatField(default=0,blank=True,null=True)
         NQNC4negC2=models.FloatField(default=0,blank=True,null=True)
         
         QMAXC3posC2=models.FloatField(default=0,blank=True,null=True)
         QMAXC4posC2=models.FloatField(default=0,blank=True,null=True)         
         QMAXC3negC2=models.FloatField(default=0,blank=True,null=True)
         QMAXC4negC2=models.FloatField(default=0,blank=True,null=True)

         imagen_PRPDD_2 = ImageField(upload_to='tmp',blank=True)
         imagen_3D_2 = ImageField(upload_to='tmp',blank=True)
         imagen_PHD_2 = ImageField(upload_to='tmp',blank=True)

         comentario = models.TextField(blank=True)
  
         def __str__(self):
            return  self.central
         
         class Admin:
            list_display = ('')


