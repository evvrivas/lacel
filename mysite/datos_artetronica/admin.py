
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.

from mysite.datos_artetronica.models import *

#admin.site.unregister(User)
from mysite.forms import *

admin.site.register(Usuarios)
class RulesAdmin(admin.ModelAdmin):
    form = UsuariosForm

###################  cel #####################
admin.site.register(Centrales)
class RulesAdmin(admin.ModelAdmin):
    form = CentralesForm

admin.site.register(Transformadores)
class RulesAdmin(admin.ModelAdmin):
    form = TransformadoresForm

admin.site.register(Generadores)
class RulesAdmin(admin.ModelAdmin):
    form = GeneradoresForm

admin.site.register(Mediciones)
class RulesAdmin(admin.ModelAdmin):
    form = MedicionesForm

admin.site.register(Mediciones_DP)
class RulesAdmin(admin.ModelAdmin):
    form = Mediciones_DPForm
  
 ##########################
