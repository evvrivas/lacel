#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.views.generic import View
from django import get_version
from django.http import HttpResponse

class Index(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Running Django ' + str(get_version()) + " on OpenShift")


from django.template.loader import get_template
from django.template import Context

from django.template import RequestContext, loader

from django.http import HttpResponse
import datetime

#from books.models import Publisher
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
#from miPagina.books.models import Book
from mysite.settings import MEDIA_URL


from django.contrib import auth
from django.core.files.uploadedfile import SimpleUploadedFile 
from django.contrib.auth.decorators import login_required



from mysite.forms import *
from mysite.datos_artetronica.models import *



from django.contrib.auth.models import User  
from django.core.mail import send_mail
#from templates import *
from django.db.models import Q



from django.db import connection

from random import sample


   
def logout(request):
    auth.logout(request)
    
    return HttpResponseRedirect("/")




def info_pagina():
    cantidad_usuarios=Usuarios.objects.all().count()
    cantidad_tiendas=Tiendas.objects.all().count()
    cantidad_productos=Productos.objects.all().count()
    connection.close()
    return cantidad_usuarios, cantidad_tiendas, cantidad_productos


def crear_usuario(request): 
        #!/usr/bin/python
        # -*- coding: latin-1 -*-
        categoria=n_categorias()
        
        n_usuarios, n_tiendas, n_productos=info_pagina()
        mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)

        import os, sys
       
        if request.method == 'POST': # si el usuario est enviando el formulario con datos
               
              
                    form = UsuariosForm(request.POST,request.FILES)                      
                    
                    if form.is_valid() :                        
                            
                            whatsapp = form.cleaned_data['id_usuario']
                            contra = form.cleaned_data['clave'] 
                                            
                            user = User.objects.create_user(username=whatsapp, password=contra)
                                                       
                            usuario = form.save(commit=False)
                            # commit=False tells Django that "Don't send this to database yet.
                            # I have more things I want to do with it."
                            usuario.id_usuario = user.username # Set the user object here
                            usuario.save() # Now you can send it to DB
                            form.save() # Guardar los datos en la base de datos  print 
                            user.save()  
                            
                            fecha= datetime.datetime.now()
                            mensaje= str(fecha)+"  "+str(whatsapp) + "Acaba de registrarse "+"\n"
                            sender =str("xgangasx@gmail.com")
                            asunto="nuevo usuario"+" "+ str(whatsapp)
                            try:
                                 send_mail(asunto, mensaje,"xgangasx@gmail.com",(sender,), fail_silently=False)            
                            except:
                                  pass
                            #return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
                            connection.close()
                            return render(request,'confirmar_usuario.html',locals())                  
                

        else:            
                         
                         form=UsuariosForm()
        connection.close()                  
        return render(request,'formulario_crear_usuario.html',locals()) 

        

def editar_usuario(request,acid):   
       categoria=n_categorias()
       n_usuarios, n_tiendas, n_productos=info_pagina()
       mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
       a=eval(acid)-1

       acido=str(a)
       f = Usuarios.objects.get(pk=acido)           
       
       if request.method == 'POST':
            
            form = UsuariosForm(request.POST,request.FILES,instance=f)
       
            if form.is_valid():

                    contra = form.cleaned_data['clave'] 

                    user = User.objects.get(username=request.user.username)
                    user.set_password(contra)
                    user.save()

                    usu=form.save(commit=False)
                    usu.id_usuario = request.user.username
                    usu.save() # Guardar los datos en la base de datos 
                    #return render_to_response('confirmar.html',locals(),context_instance=RequestContext(request))
                    
                    whatsapp=request.user.username
                    fecha= datetime.datetime.now()
                    mensaje= str(fecha)+"  "+str(whatsapp) + "EDITO SU ESTADO "+"\n"
                    sender =str("xgangasx@gmail.com")
                    asunto="edita"+" "+ str(whatsapp)
                    try:
                        send_mail(asunto, mensaje,"xgangasx@gmail.com",(sender,), fail_silently=False) 
                    except:
                         pass        
                    connection.close()
                    return render(request,'confirmar.html',locals())             
            
       else:
            
            form = UsuariosForm(instance=f)
            

        

       connection.close()
       #return render_to_response('formulario.html', locals(),context_instance=RequestContext(request))
       return render(request,'formulario_editar_usuario.html',locals())   

@login_required
def crear_tienda(request):                

     #!/usr/bin/python
     # -*- coding: latin-1 -*-
     import os, sys
     categoria=n_categorias()
     n_usuarios, n_tiendas, n_productos=info_pagina()
     mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username) 
    
     if request.method == 'POST': # si el usuario est enviando el formulario con datos
            form=TiendasForm(request.user.username,request.POST,request.FILES)                   
                  
            if form.is_valid():
                          tiendecilla = form.save(commit=False)
                          # commit=False tells Django that "Don't send this to database yet.
                          # I have more things I want to do with it."
                          tiendecilla.id_usuario = request.user.username # Set the user object here             
                                           
                          tiendecilla.save() # Now you can send it to DB
                          form.save()  
                          connection.close()
                          #return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
                          
                          return render(request,'confirmar.html',locals())     
            else:


                                      formCcomercial=CcomercialForm(request.POST,request.FILES) 
                                      if formCcomercial.is_valid() :                           

                                              Ccomer = formCcomercial.save(commit=False)
                                              # commit=False tells Django that "Don't send this to database yet.
                                              # I have more things I want to do with it."
                                              Ccomer.id_usuario = request.user.username # Set the user object here
                                              
                                              Ccomer.save() # Now you can send it to DB
                                              formCcomercial.save() # Guardar los datos en la base de datos  print  
                                              connection.close() 
                                              return render(request,'formulario_ingreso.html',locals())                           
                                                                           
                                 
                                          
     else:
        formCcomercial=CcomercialForm()
        form=TiendasForm(request.user.username)


                                

     connection.close() 
     return render(request,'formulario_ingreso.html',locals())
        #return render_to_response('formulario.html', locals() ,context_instance=RequestContext(request))

def editar_tienda(request,acid):   
        categoria=n_categorias()
        n_usuarios, n_tiendas, n_productos=info_pagina()
        mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
        
        f = Tiendas.objects.get(pk=acid)           
       
        if request.method == 'POST':
            
            form = TiendasForm(request.user.username,request.POST,request.FILES,instance=f)
       
            if form.is_valid():
                   tiendecilla = form.save(commit=False)
                   # commit=False tells Django that "Don't send this to database yet.
                   # I have more things I want to do with it."
                   tiendecilla.ultima_fecha_edicion=datetime.datetime.now()             
                   tiendecilla.save() # Now you can send it to DB
                   form.save() 
                   connection.close()
                   return render(request,'confirmar.html',locals())             
                    
        else:
            
            form = TiendasForm(request.user.username,instance=f)
            

        
        connection.close()
        #return render_to_response('formulario.html', locals(),context_instance=RequestContext(request))
        return render(request,'formulario_ingreso.html',locals())   





def pagina_principal(request):   


                         n_usuarios, n_tiendas, n_productos=info_pagina()
                         categoria=n_categorias()
                         mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username) 
                         configurar=Configuracion_sistema.objects.all().first()
                         
                         configurar.n_visitas+=1         
                         configurar.save()

                         
                         try:
                             comercio,tiendas,productos=publicida_inteligencia(request)
                         except:
                             pass
                         nuevo_comercio=Ccomercial.objects.all().order_by("-id")[:6]
                         nuevas_tiendas=Tiendas.objects.all().order_by("-id")[:6]
                         nuevos_productos=Productos.objects.all().order_by("-id")[:6]
                         
                         try:
                            count = Tiendas.objects.all().count()
                            rand_ids = sample(range(1, count), 3)
                            aleatorias_tiendas=Tiendas.objects.filter(id__in=rand_ids)
                         except:
                             pass
                         try:                      
                            count = Productos.objects.all().count()
                            rand_ids = sample(range(1, count), 3)
                            aleatorias_productos=Productos.objects.filter(id__in=rand_ids)
                         except:
                             pass

                         try:                      
                            count = Ccomercial.objects.all().count()
                            rand_ids = sample(range(1, count), 3)
                            aleatorias_comercio=Ccomercial.objects.filter(id__in=rand_ids)
                         except:
                             pass

                         
                         

                         connection.close()                    
                         return render(request,'principal.html',locals())   



def informacion(request): 
  return render(request,'informacion.html',locals())   


def principal(request):
  return render(request,'principal.html',locals())  


def busqueda(request):     
    return render(request,'cel_principal.html',locals())   
          

def ver(request):
  return render(request,'cel_principal.html',locals()) 