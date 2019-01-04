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
	
	
	

class MedicionesForm(ModelForm):#productos
	class Meta:			
		model=Mediciones
		exclude=["fecha_ingreso"]


class Mediciones_rapidasForm(ModelForm):#productos
	class Meta:			
		model=Mediciones_rapidas
		exclude=[""]
	
   
#########################################################

