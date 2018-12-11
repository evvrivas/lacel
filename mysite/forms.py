#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mysite.datos_artetronica.models import *

from django.forms import ModelForm, Textarea

class UsuariosForm(ModelForm):
	class Meta:
		model= Usuarios		
		exclude=["fecha_ingreso","privilegio"]

privilegio=models.CharField(max_length=30,choices=PRIVILEGIOS,default="'DE_BAJA")
	      
########################  CEL  ##########################
class CentralForm(ModelForm):#usuario
	class Meta:			
		model=Central
		exclude=["fecha_ingreso"]
				    
class TransformadorForm(ModelForm):#tiendas
	class Meta:			
		model=Transformador
		exclude=["fecha_ingreso"]
		 
class MedicionForm(ModelForm):#productos
	class Meta:			
		model=Medicion
		exclude=["fecha_ingreso"]
    
#########################################################