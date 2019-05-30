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
	
class GeneradoresForm(ModelForm):#tiendas
	class Meta:			
		model=Generadores
		exclude=["fecha_ingreso"]	


class MedicionesForm(ModelForm):#productos
	class Meta:			
		model=Mediciones
		widgets = {'comentario': Textarea(attrs={'cols': 40, 'rows': 3}),}
		exclude=["fecha_ingreso","codigo_usuario"]


class Mediciones_rapidasForm(ModelForm):#productos
	class Meta:			
		model=Mediciones_rapidas
		widgets = {'comentario': Textarea(attrs={'cols': 40, 'rows': 3}),}
		exclude=[""]
  
#########################################################

class Mediciones_DPForm(ModelForm):#productos
	class Meta:			
		model=Mediciones_DP
		widgets = {'comentario': Textarea(attrs={'cols': 40, 'rows': 3}),}
		exclude=["fecha_ingreso","codigo_usuario"]


class Sistema_termograficoForm(ModelForm):#productos
	class Meta:			
		model=Sistema_termografico
		widgets = {'justificacion': Textarea(attrs={'cols': 40, 'rows': 3}),}
		exclude=["fecha_ingreso"]

class TermografiasForm(ModelForm):#productos
	class Meta:			
		model=Termografias
		widgets = {'comentario_termografia_1': Textarea(attrs={'cols': 40, 'rows': 3}),'comentario_termografia_2': Textarea(attrs={'cols': 40, 'rows': 3}),}
		exclude=["fecha_ingreso","codigo_usuario"]

