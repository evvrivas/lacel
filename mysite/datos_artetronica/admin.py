
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
    list_display = ['central__nombre','codigo_usuario', 'nombres','apellidos','fecha_ingreso',]
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
    list_display = ['central__nombre','codigo', 'marca','modelo',]
admin.site.register(Transformadores,TransformadoresAdmin)

##############################################


##############################################
class RulesAdmin(admin.ModelAdmin):
    form = GeneradoresForm
class GeneradoresAdmin(admin.ModelAdmin):
    model = Generadores
    list_display = ['central__nombre','codigo', 'marca','modelo',]
admin.site.register(Generadores,GeneradoresAdmin)
##############################################


##############################################
class RulesAdmin(admin.ModelAdmin):
    form = MedicionesForm
class MedicionesAdmin(admin.ModelAdmin):
    model = Mediciones
    list_display = ['central__nombre','transformador__codigo', 'transformador__marca','transformador__modelo','fecha_del_analisis',]
admin.site.register(Mediciones,MedicionesAdmin)
##############################################


##############################################
class RulesAdmin(admin.ModelAdmin):
    form = Mediciones_DPForm
class Mediciones_DPAdmin(admin.ModelAdmin):
    model = Mediciones_DP
    list_display = ['central__nombre','generador__codigo', 'generador__marca','generador__modelo','fecha_del_analisis',]    
admin.site.register(Mediciones_DP,Mediciones_DPAdmin)  
##############################################

 		 