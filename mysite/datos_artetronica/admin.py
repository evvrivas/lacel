
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.

from mysite.datos_artetronica.models import *

#admin.site.unregister(User)
from mysite.forms import *

##############################################
class RulesAdmin(admin.ModelAdmin):
    form = UsuariosForm
class UsuariosAdmin(admin.ModelAdmin):
    model = Usuarios
    list_display = ['central_nombre','codigo_usuario', 'nombres','apellidos','fecha_ingreso',]
    def central_nombre(self,instance):
    	return instance.central.nombre
admin.site.register(Usuarios,UsuariosAdmin)
##############################################


##############################################
class RulesAdmin(admin.ModelAdmin):
    form = CentralesForm
class CentralesAdmin(admin.ModelAdmin):
    model = Centrales
    list_display = ['nombre','fecha_ingreso', ]
admin.site.register(Centrales,CentralesAdmin)
##############################################


##############################################
class RulesAdmin(admin.ModelAdmin):
    form = TransformadoresForm
class TransformadoresAdmin(admin.ModelAdmin):
    model = Transformadores
    list_display = ['central_nombre','codigo', 'marca','modelo',]
    def central_nombre(self,instance):
    	return instance.central.nombre
admin.site.register(Transformadores,TransformadoresAdmin)

##############################################


##############################################
class RulesAdmin(admin.ModelAdmin):
    form = GeneradoresForm
class GeneradoresAdmin(admin.ModelAdmin):
    model = Generadores
    list_display = ['central_nombre','codigo', 'marca','modelo',]
    def central_nombre(self,instance):
    	return instance.central.nombre
admin.site.register(Generadores,GeneradoresAdmin)
##############################################


##############################################
class RulesAdmin(admin.ModelAdmin):
    form = MedicionesForm
class MedicionesAdmin(admin.ModelAdmin):
    model = Mediciones
    list_display = ['central_nombre','transformador_marca', 'fecha_del_analisis',]
    def central_nombre(self,instance):
    	return instance.central.nombre
    def transformador_marca(self,instance):
    	return instance.transformador.marca
admin.site.register(Mediciones,MedicionesAdmin)
##############################################


##############################################
class RulesAdmin(admin.ModelAdmin):
    form = Mediciones_DPForm
class Mediciones_DPAdmin(admin.ModelAdmin):
    model = Mediciones_DP
    list_display = ['central_nombre', 'generador__marca','fecha_del_analisis',]
    def central_nombre(self,instance):
    	return instance.central.nombre
    def generador_marca(self,instance):
    	return instance.generador.marca
admin.site.register(Mediciones_DP,Mediciones_DPAdmin)  
##############################################

 		 