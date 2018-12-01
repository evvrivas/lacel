#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mysite.datos_artetronica.models import *

from django.forms import ModelForm, Textarea

class UsuariosForm(ModelForm):
	class Meta:
		model= Usuarios		
		exclude=["codigoapk","plan_tienda_activo","fecha_inicio_plan","fecha_final_plan","fecha_ingreso"]


########################  CEL  ##########################
class Central_generadoraForm(ModelForm):
	class Meta:			
		model=Central_generadora
		exclude=[]
				    
class TransformadorForm(ModelForm):
	class Meta:			
		model=Transformador
		exclude=[]
		 
class MedicionForm(ModelForm):
	class Meta:			
		model=Medicion
		exclude=[]

class Usuarios_celForm(ModelForm):
	class Meta:			
		model=Usuarios_cel
		exclude=[]	
#########################################################