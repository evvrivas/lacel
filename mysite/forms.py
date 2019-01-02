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
	
	def __init__(self, nombre_central,*args, **kwargs):
		super(TransformadoresForm, self).__init__(*args, **kwargs)
		self.fields['central'].queryset=Centrales.objects.filter(nombre=nombre_transformador)
		#self.fields['ccomercial'].queryset=Ccomercial.objects.filter(id_usuario=user)
	

class MedicionesForm(ModelForm):#productos
	class Meta:			
		model=Mediciones
		exclude=["fecha_ingreso"]

	def __init__(self, codigo_transformador,*args, **kwargs):
		super(MedicionesForm, self).__init__(*args, **kwargs)		
		self.fields['transformador'].queryset=Tranformador.objects.filter(codigo=nombre_transformador)

    
#########################################################

class ProductosForm(ModelForm):

	class Meta:
		model= Productos
		widgets = {'descripcion': Textarea(attrs={'cols': 40, 'rows': 3}),}
		exclude=["id_usuario","puntuacion","fecha_ingreso","ultima_fecha_edicion"]
	
	def __init__(self, user,nombre_tienda,*args, **kwargs):
		super(ProductosForm, self).__init__(*args, **kwargs)		
		self.fields['categoria'].queryset=Categoria.objects.filter(id_usuario=user,tienda=nombre_tienda)


class TiendasForm(ModelForm):
	class Meta:
		model= Tiendas	
		widgets = {'descripcion': Textarea(attrs={'cols': 50, 'rows': 8}),}	
		exclude=["codigoapk","id_usuario","fecha_ingreso","n_visitas","ultimo_comentario","ultima_fecha_edicion"]
	def __init__(self, user,*args, **kwargs):
		super(TiendasForm, self).__init__(*args, **kwargs)
		self.fields['ccomercial'].queryset=Ccomercial.objects.all()
		#self.fields['ccomercial'].queryset=Ccomercial.objects.filter(id_usuario=user)