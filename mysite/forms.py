#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mysite.datos_artetronica.models import *

from django.forms import ModelForm, Textarea

class UsuariosForm(ModelForm):
	class Meta:
		model= Usuarios		
		exclude=["codigoapk","plan_tienda_activo","fecha_inicio_plan","fecha_final_plan","fecha_ingreso"]


########################  CEL  ##########################
class CentralForm(ModelForm):
	class Meta:			
		model=Central
		exclude=[]
				    
class TransformadorForm(ModelForm):
	class Meta:			
		model=Transformador
		exclude=[]
		 
class MedicionForm(ModelForm):
	class Meta:			
		model=Medicion
		exclude=[]

#########################################################