#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mysite.datos_artetronica.models import *

from django.forms import ModelForm, Textarea

class UsuariosForm(ModelForm):
	class Meta:
		model= Usuarios		
		exclude=["fecha_ingreso","privilegio"]

      
########################  CEL  ##########################
class CentralesForm(ModelForm):#usuario
	class Meta:			
		model=Centrales
		exclude=["fecha_ingreso"]
				    
class TransformadoresForm(ModelForm):#tiendas
	class Meta:			
		model=Transformadores
		exclude=["fecha_ingreso"]
	
	def __init__(self, *args, **kwargs):
		super(TransformadoresForm, self).__init__(*args, **kwargs)
		self.fields['central'].queryset=Centrales.objects.all()
		#self.fields['ccomercial'].queryset=Ccomercial.objects.filter(id_usuario=user)
	

class MedicionesForm(ModelForm):#productos
	class Meta:			
		model=Mediciones
		exclude=["fecha_ingreso"]

	def __init__(self, *args, **kwargs):
		super(MedicionesForm, self).__init__(*args, **kwargs)		
		self.fields['transformador'].queryset=Tranformador.objects.all()

    
#########################################################

