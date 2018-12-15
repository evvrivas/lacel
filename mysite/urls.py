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



    
    url(r'^$', principal),
    url(r'^grafico/([^/]+)$', grafico),
    url(r'^tendencias/([^/]+)/([^/]+)/(\d+)/$', tendencias),



    url(r'^total_gases_combustibles/$', total_gases_combustibles),
    url(r'^limite_concentracion/$', limite_concentracion),
    url(r'^gas_clave/$', gas_clave),

    url(r'^informacion/$', informacion),

    url(r'^listado_de_transformadores/([^/]+)/$', listado_de_transformadores),
    url(r'^listado_de_mediciones/([^/]+)/([^/]+)/$', listado_de_mediciones),
    url(r'^analisis/([^/]+)/([^/]+)/(\d+)/$', analisis),

    url(r'^datos_prueba/$', datos_prueba),
    
        
       
]

    
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


