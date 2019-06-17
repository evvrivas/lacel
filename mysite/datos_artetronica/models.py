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
        codigo_usuario=models.CharField(max_length=7)
        fecha_ingreso = models.DateField(default=datetime.now,editable = False)
        def __str__(self):
            return  self.nombre
        class Admin:
            list_display = ('nombre', 'fecha_ingreso')


PRIVILEGIOS=(
			('DE_ALTA', 'DE_ALTA'),            
            ('DE_ALTA_INVITADO', 'DE_ALTA__INVITADO'),
			('DE_BAJA', 'DE_BAJA'),

		     )


class Usuarios(models.Model):
        central=models.ForeignKey('Centrales')
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
        codigo_usuario=models.CharField(max_length=7)
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
    codigo_usuario=models.CharField(max_length=7)
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


         PDI_C1_1=models.FloatField(default=0,blank=True,null=True)
         PDI_C1_2=models.FloatField(default=0,blank=True,null=True)

         PDI_C2_1=models.FloatField(default=0,blank=True,null=True)
         PDI_C2_2=models.FloatField(default=0,blank=True,null=True)

         PDI_C3_1=models.FloatField(default=0,blank=True,null=True)
         PDI_C3_2=models.FloatField(default=0,blank=True,null=True)

                 

         imagen_PRPDD_1 = ImageField(upload_to='tmp',blank=True)
         imagen_3D_1 = ImageField(upload_to='tmp',blank=True)
         imagen_PHD_1 = ImageField(upload_to='tmp',blank=True)

        
         PDI_C4_1=models.FloatField(default=0,blank=True,null=True)
         PDI_C4_2=models.FloatField(default=0,blank=True,null=True)

         PDI_C5_1=models.FloatField(default=0,blank=True,null=True)
         PDI_C5_2=models.FloatField(default=0,blank=True,null=True)

         PDI_C6_1=models.FloatField(default=0,blank=True,null=True)
         PDI_C6_2=models.FloatField(default=0,blank=True,null=True)

         imagen_PRPDD_2 = ImageField(upload_to='tmp',blank=True)
         imagen_3D_2 = ImageField(upload_to='tmp',blank=True)
         imagen_PHD_2 = ImageField(upload_to='tmp',blank=True)

         comentario = models.TextField(blank=True)
  
         def __str__(self):
            return  self.generador.codigo
            
         
         class Admin:
            list_display = ('generador.codigo', 'generador.codigo','generador.modelo')


class Sistema_termografico(models.Model):
        central=models.ForeignKey('Centrales')
        codigo_usuario=models.CharField(max_length=7)
        nombre=models.CharField(max_length=60,blank=True)
        justificacion=models.TextField(blank=True)
        imagen_de_analisis_1 = ImageField(upload_to='tmp',blank=True)        
        fecha_ingreso = models.DateField(default=datetime.now,editable = False)

        def __str__(self):
               return  self.nombre
        class Admin:
               list_display = ('nombre', 'codigo',)

class Termografias(models.Model):        
         central=models.ForeignKey('Centrales')
         sistema_termografico=models.ForeignKey('Sistema_termografico')
         codigo_usuario = models.CharField(max_length=60,blank=True)
         fecha_del_analisis = models.DateField(default=datetime.now,null=False)
         fecha_ingreso= models.DateField(default=datetime.now,null=False)          
          
         imagen_termografica_secuencia_1 = ImageField(upload_to='tmp',blank=True)
         comentario_termografia_1 = models.TextField(blank=True)

         imagen_termografica_secuencia_2 = ImageField(upload_to='tmp',blank=True)         
         comentario_termografia_2 = models.TextField(blank=True)
  
         def __str__(self):
            return  self.sistema_termografico.nombre
                     
         class Admin:
            list_display = ('sistema_termografico.nombre', 'sistema_termografico.nombre','generador.modelo')

