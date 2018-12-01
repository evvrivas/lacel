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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', login,{'template_name': 'login.html'}),
    url(r'^accounts/logout/$', logout),

    
    url(r'^$', pagina_principal),
  
            
       
]

    
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


