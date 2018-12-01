
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
admin.site.register(Central_generadora)
class RulesAdmin(admin.ModelAdmin):
    form = Central_generadora

admin.site.register(Transformador)
class RulesAdmin(admin.ModelAdmin):
    form = Transformador

admin.site.register(Medicion)
class RulesAdmin(admin.ModelAdmin):
    form = Medicion

admin.site.register(Usuarios_cel)
class RulesAdmin(admin.ModelAdmin):
    form = Usuarios_cel  
  
 ########################################  
