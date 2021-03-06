#from django.conf.urls import patterns, include, url
#from django.contrib import admin

#from mysite.views import Index

##########################
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url,include

from django.contrib import admin


from django.conf import settings
import mysite.settings

from django.contrib.auth.views import login, logout

from django.conf.urls.static  import static 


from django.contrib import admin

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from mysite.views import *
#from histogram import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', login,{'template_name': 'login.html'}),
    url(r'^accounts/logout/$', logout),
    url(r'^informacion/$', informacion),
    url(r'^crear_usuario_cel/$',crear_ususario_cel),
    url(r'^ingresar_datos_trafo/([^/]+)/([^/]+)/$',ingresar_datos_trafo),
    url(r'^ingresar_datos_analisis_rapido/$',ingresar_datos_analisis_rapido),
    url(r'^ingreso_datos_dp/([^/]+)/([^/]+)/$',ingreso_datos_dp),
    url(r'^ingresar_termografias/([^/]+)/([^/]+)/$',ingresar_termografias),
    url(r'^ingresar_otros_analisis/([^/]+)/$',ingresar_otros_analisis),

      
    url(r'^$', principal),
   
    url(r'^tendencias/([^/]+)/([^/]+)/([^/]+)/$', tendencias),
    url(r'^grafico_tendencias/([^/]+)/([^/]+)/([^/]+)/$', grafico_tendencias),
    
    url(r'^grafico_gases_presentes/([^/]+)/([^/]+)/$', grafico_gases_presentes),
    url(r'^grafico_gases_presentes_rapido/([^/]+)/([^/]+)/$', grafico_gases_presentes_rapido),
    url(r'^grafico_tendencias_DP/([^/]+)/([^/]+)/$', grafico_tendencias_DP),
    
    url(r'^ver_graficas_mensuales/(\d+)/$',ver_graficas_mensuales),
  
    url(r'^informacion/$', informacion),
    url(r'^ver_registros/$', ver_registros),

    url(r'^listado_de_equipos/([^/]+)/$', listado_de_equipos),
    #url(r'^listado_de_mediciones/([^/]+)/([^/]+)/$', listado_de_mediciones),
    url(r'^analisis/([^/]+)/([^/]+)/$', analisis),
    url(r'^analisis_dp/([^/]+)/([^/]+)/$', analisis_dp),
   
    url(r'^analisis_termografico/([^/]+)/$', analisis_termografico),
    
    url(r'^datos_prueba_DP/$', datos_prueba_DP),
    url(r'^datos_prueba/$', datos_prueba),
  
    url(r'^manual_de_usuario/$',manual_de_usuario),

    url(r'^editar/(\d+)/([^/]+)/$', editar),
    url(r'^ver_validacion_AGDA/(\d+)/$', ver_validacion_AGDA),

    

       
       
]

    
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


