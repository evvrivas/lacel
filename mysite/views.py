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


#from mysite.views_datos import *
   
def logout(request):
    auth.logout(request)
    
    return HttpResponseRedirect("/")

def informacion(request):
  centrales=Centrales.objects.all()
  try:
        usuario_comun=Usuarios.objects.get(codigo_usuario=request.user.username)
  except:
        pass
  return render(request,'informacion.html',locals())


def crear_ususario_cel(request):
        import os, sys
        if request.method == 'POST': # si el usuario est enviando el formulario con datos
                             
                    form = UsuariosForm(request.POST,request.FILES)                      
                    
                    if form.is_valid() :
                           
                            temp = form.save(commit=False)
                            temp.fecha_ingreso=datetime.datetime.now()  
                            temp.save() #  

                            usuariocel = form.cleaned_data['codigo_usuario']
                            contracel = form.cleaned_data['pasword']
                            correo=form.cleaned_data['email']
                            nom=form.cleaned_data['nombres']
                            apell=form.cleaned_data['apellidos']                     
                            

                            user = User.objects.create_user(username=usuariocel, password=contracel,email=correo,first_name=nom,last_name=apell)
                            user.save() 

                            form.save() # Guardar los datos en la base de datos  print 
                            #return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
                            connection.close()
                            return render(request,'confirmar.html',locals())                  
                

        else:            
                         
            form=UsuariosForm()

        connection.close()                  
        return render(request,'ingreso_de_datos.html',locals()) 
    
    


def ingresar_datos_trafo(request):
        #!/usr/bin/python
        # -*- coding: latin-1 -*-        
        import os, sys
        if request.method == 'POST': # si el usuario est enviando el formulario con datos
                             
                    form = MedicionesForm(request.POST,request.FILES)                      
                    
                    if form.is_valid() :
                           
                            temp = form.save(commit=False)
                            # commit=False tells Django that "Don't send this to database yet.
                            # I have more things I want to do with it."
                            
                            temp.fecha_ingreso=datetime.datetime.now()  
                            temp.codigo_usuario=request.user.username # Set the user object here    
                            temp.save() #  

                            form.save() # Guardar los datos en la base de datos  print 
                            #return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
                            connection.close()
                            return render(request,'confirmar.html',locals())                  
                

        else:            
                         
                         form=MedicionesForm()

        connection.close()                  
        return render(request,'ingreso_de_datos.html',locals()) 

def ingresar_datos_analisis_rapido(request):
        #!/usr/bin/python
        # -*- coding: latin-1 -*-        
        import os, sys
        if request.method == 'POST': # si el usuario est enviando el formulario con datos
                             
                    form = Mediciones_rapidasForm(request.POST,request.FILES)                      
                    
                    if form.is_valid() :
                            #SIMBOLO_GAS=["H2","CH4","C2H2","C2H4","C2H6","CO","O2","N2","CO2"]
                            Mediciones_rapidas.objects.all().delete()  
                            cent=form.cleaned_data['central']
                            trafo= form.cleaned_data['transformador']                                                                                             

                            form.save() # Guardar los datos en la base de datos  print 
                            #return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
                            connection.close()
                            central_x=cent
                            transformador_x=trafo

                            #analisis_rapido(request,cent,trafo)

                            VALOR_DEL_GAS= datos_de_analisis_rapido(central_x, transformador_x)
   
                            VALOR_GAS_LIMITES=[]
                            LIMITES_GAS=["100","120","2--35","50","65","350","-","-","-"]    
                            for i in range(len(VALOR_DEL_GAS)):   
                                a=[VALOR_DEL_GAS[i][0],VALOR_DEL_GAS[i][1],LIMITES_GAS[i]]
                                VALOR_GAS_LIMITES.append(a)
                                
                            central=central_x
                            transformador=transformador_x
                            segun_gas_clave=gas_clave(VALOR_DEL_GAS)#valor
                            concentraciones_limite=limite_concentracion(VALOR_DEL_GAS)#vector
                            gases_combustibles= total_gases_combustibles(VALOR_DEL_GAS)#vector    
                            Triangulo_duval=duval( VALOR_DEL_GAS)    
                            segun_donenberg=donenberg(VALOR_DEL_GAS)
                            segun_roger=roger(VALOR_DEL_GAS)     
                            segun_IEC_60599=IEC_60599(VALOR_DEL_GAS)    
                            segun_analitico_CO2_CO=analitico_CO2_CO(VALOR_DEL_GAS)
                            segun_analitico_C2H2_H2=analitico_C2H2_H2(VALOR_DEL_GAS)

                            return render(request,'analisis_rapido.html',locals())                  
                

        else:            
                         
                         form=Mediciones_rapidasForm()

        connection.close()                  
        return render(request,'ingreso_de_datos.html',locals()) 


def ingresar_termografias(request):
        #!/usr/bin/python
        # -*- coding: latin-1 -*-        
        import os, sys
        if request.method == 'POST': # si el usuario est enviando el formulario con datos
                             
                    form = TermografiasForm(request.POST,request.FILES)                      
                    
                    if form.is_valid() :
                           
                            temp = form.save(commit=False)
                            # commit=False tells Django that "Don't send this to database yet.
                            # I have more things I want to do with it."
                            
                            temp.fecha_ingreso=datetime.datetime.now()  
                            temp.codigo_usuario=request.user.username # Set the user object here    
                            temp.save() #  

                            form.save() # Guardar los datos en la base de datos  print 
                            #return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
                            connection.close()
                            return render(request,'confirmar.html',locals())                  
                

        else:            
                         
                         form=TermografiasForm()

        connection.close()                  
        return render(request,'ingreso_de_datos.html',locals()) 


def datos_prueba(request):

    date=datetime.datetime.now()


    p1=Centrales(nombre="CH 5 NOVIEMBRE",fecha_ingreso=date)   
    p1.save() 


    p21=Transformadores(central=p1,codigo="C0848A",marca="EFACEC",modelo="NA",cararcteristicas="U1",fecha_ingreso=date)
    p21.save()
      
    #EFACET U1
    #2014
    date=datetime.datetime(2014,6,30)
    p31=Mediciones(central=p1,transformador=p21,codigo_usuario="7807004",Hidrogeno=3,Oxigeno=0,Nitrogeno=0,Metano=1,Monoxido_de_carbono=4,Etano=1,Dioxido_de_carbono=203.41,Etileno=0.17,Acetileno=0.7,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p31.save()
    #2015
    date=datetime.datetime(2015,6,30)
    p32=Mediciones(central=p1,transformador=p21,codigo_usuario="7807004",Hidrogeno=5.38,Oxigeno=29.92,Nitrogeno=36320,Metano=8.8,Monoxido_de_carbono=4.97,Etano=2.1,Dioxido_de_carbono=926,Etileno=0.68,Acetileno=1.2,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p32.save()
    #2016
    date=datetime.datetime(2016,6,30)
    p33=Mediciones(central=p1,transformador=p21,codigo_usuario="7807004",Hidrogeno=2,Oxigeno=0,Nitrogeno=0,Metano=50,Monoxido_de_carbono=137,Etano=67,Dioxido_de_carbono=2010,Etileno=5,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p33.save()
    #2017
    date=datetime.datetime(2017,6,30)
    p34=Mediciones(central=p1,transformador=p21,codigo_usuario="7807004",Hidrogeno=5,Oxigeno=0,Nitrogeno=0,Metano=57,Monoxido_de_carbono=155,Etano=79,Dioxido_de_carbono=2037,Etileno=10,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p34.save()
    #2018
    date=datetime.datetime(2018,6,30)
    p35=Mediciones(central=p1,transformador=p21,codigo_usuario="7807004",Hidrogeno=15,Oxigeno=0,Nitrogeno=0,Metano=89,Monoxido_de_carbono=159,Etano=134,Dioxido_de_carbono=2308,Etileno=12,Acetileno=3,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p35.save()





    p22=Transformadores(central=p1,codigo="33562",marca="TUBOS TRRANS ELECTRIC",modelo="NA",cararcteristicas="U2",fecha_ingreso=date)
    p22.save()
    #2010
    date=datetime.datetime(2010,6,30)
    p31=Mediciones(central=p1,transformador=p22,codigo_usuario="7807004",Hidrogeno=5,Oxigeno=0,Nitrogeno=0,Metano=4,Monoxido_de_carbono=132,Etano=12,Dioxido_de_carbono=2027,Etileno=25,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p31.save()
    #2012
    date=datetime.datetime(2012,6,30)
    p32=Mediciones(central=p1,transformador=p22,codigo_usuario="7807004",Hidrogeno=24,Oxigeno=0,Nitrogeno=0,Metano=7,Monoxido_de_carbono=352,Etano=10,Dioxido_de_carbono=3641,Etileno=34,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p32.save()
    #2013
    date=datetime.datetime(2013,6,30)
    p33=Mediciones(central=p1,transformador=p22,codigo_usuario="7807004",Hidrogeno=17,Oxigeno=0,Nitrogeno=87500,Metano=9,Monoxido_de_carbono=463,Etano=11,Dioxido_de_carbono=4140,Etileno=40,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p33.save()
    #2014
    date=datetime.datetime(2014,6,30)
    p34=Mediciones(central=p1,transformador=p22,codigo_usuario="7807004",Hidrogeno=16,Oxigeno=0,Nitrogeno=0,Metano=4,Monoxido_de_carbono=42,Etano=7,Dioxido_de_carbono=680,Etileno=11,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p34.save()
    #2015
    date=datetime.datetime(2015,6,30)
    p35=Mediciones(central=p1,transformador=p22,codigo_usuario="7807004",Hidrogeno=12,Oxigeno=0,Nitrogeno=0,Metano=11,Monoxido_de_carbono=228,Etano=3,Dioxido_de_carbono=2226,Etileno=5,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p35.save()

    #2016
    date=datetime.datetime(2016,6,30)
    p35=Mediciones(central=p1,transformador=p22,codigo_usuario="7807004",Hidrogeno=15,Oxigeno=0,Nitrogeno=0,Metano=9,Monoxido_de_carbono=247,Etano=9,Dioxido_de_carbono=2381,Etileno=14,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p35.save()





    p23=Transformadores(central=p1,codigo="L252373",marca="GENERAL ELECTRIC",modelo="NA",cararcteristicas="U3",fecha_ingreso=date)
    p23.save()

     #2012
    date=datetime.datetime(2012,6,30)
    p31=Mediciones(central=p1,transformador=p23,codigo_usuario="7807004",Hidrogeno=106,Oxigeno=0,Nitrogeno=0,Metano=17,Monoxido_de_carbono=552,Etano=8,Dioxido_de_carbono=6920,Etileno=34,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p31.save()
    #2013
    date=datetime.datetime(2013,6,30)
    p32=Mediciones(central=p1,transformador=p23,codigo_usuario="7807004",Hidrogeno=74,Oxigeno=0,Nitrogeno=0,Metano=14,Monoxido_de_carbono=553,Etano=6,Dioxido_de_carbono=6798,Etileno=32,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p32.save()
    #2014
    date=datetime.datetime(2014,6,30)
    p33=Mediciones(central=p1,transformador=p23,codigo_usuario="7807004",Hidrogeno=74,Oxigeno=727,Nitrogeno=65942,Metano=12,Monoxido_de_carbono=427,Etano=3,Dioxido_de_carbono=4351,Etileno=17,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p33.save()
    #2015
    date=datetime.datetime(2015,6,30)
    p34=Mediciones(central=p1,transformador=p23,codigo_usuario="7807004",Hidrogeno=43,Oxigeno=0,Nitrogeno=0,Metano=8,Monoxido_de_carbono=334,Etano=8,Dioxido_de_carbono=4162,Etileno=18,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p34.save()
    #2016
    date=datetime.datetime(2016,6,30)
    p35=Mediciones(central=p1,transformador=p23,codigo_usuario="7807004",Hidrogeno=46,Oxigeno=0,Nitrogeno=0,Metano=9,Monoxido_de_carbono=330,Etano=8,Dioxido_de_carbono=4320,Etileno=17,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p35.save()
    #2017
    date=datetime.datetime(2017,6,30)
    p35=Mediciones(central=p1,transformador=p23,codigo_usuario="7807004",Hidrogeno=5,Oxigeno=0,Nitrogeno=0,Metano=1,Monoxido_de_carbono=9,Etano=2,Dioxido_de_carbono=151,Etileno=0,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p35.save()
     #2018
    date=datetime.datetime(2018,6,30)
    p35=Mediciones(central=p1,transformador=p23,codigo_usuario="7807004",Hidrogeno=11,Oxigeno=0,Nitrogeno=0,Metano=4,Monoxido_de_carbono=177,Etano=5,Dioxido_de_carbono=1896,Etileno=5,Acetileno=3,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p35.save()


    p24=Transformadores(central=p1,codigo="89115",marca="TADEO CZERWENY",modelo="NA",cararcteristicas="U4",fecha_ingreso=date)
    p24.save()

     #2012
    date=datetime.datetime(2012,6,30)
    p31=Mediciones(central=p1,transformador=p24,codigo_usuario="7807004",Hidrogeno=36,Oxigeno=0,Nitrogeno=0,Metano=22,Monoxido_de_carbono=522,Etano=6,Dioxido_de_carbono=1953,Etileno=9,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p31.save()
    #2013
    date=datetime.datetime(2013,6,30)
    p32=Mediciones(central=p1,transformador=p24,codigo_usuario="7807004",Hidrogeno=24,Oxigeno=0,Nitrogeno=0,Metano=29,Monoxido_de_carbono=708,Etano=7,Dioxido_de_carbono=2512,Etileno=8,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p32.save()
    #2014
    date=datetime.datetime(2014,6,30)
    p33=Mediciones(central=p1,transformador=p24,codigo_usuario="7807004",Hidrogeno=34,Oxigeno=0,Nitrogeno=0,Metano=29,Monoxido_de_carbono=771,Etano=3,Dioxido_de_carbono=2633,Etileno=10,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p33.save()
    #2015
    date=datetime.datetime(2015,6,30)
    p34=Mediciones(central=p1,transformador=p24,codigo_usuario="7807004",Hidrogeno=36,Oxigeno=0,Nitrogeno=0,Metano=32,Monoxido_de_carbono=785,Etano=3,Dioxido_de_carbono=2745,Etileno=8,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p34.save()
    #2016
    date=datetime.datetime(2016,6,30)
    p35=Mediciones(central=p1,transformador=p24,codigo_usuario="7807004",Hidrogeno=26,Oxigeno=0,Nitrogeno=0,Metano=33,Monoxido_de_carbono=916,Etano=8,Dioxido_de_carbono=2978,Etileno=12,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p35.save()
    #2017
    date=datetime.datetime(2017,6,30)
    p35=Mediciones(central=p1,transformador=p24,codigo_usuario="7807004",Hidrogeno=0,Oxigeno=0,Nitrogeno=0,Metano=30,Monoxido_de_carbono=1006,Etano=7,Dioxido_de_carbono=3281,Etileno=8,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p35.save()


    p25=Transformadores(central=p1,codigo="E-74470689",marca="DELTA STAR",modelo="NA",cararcteristicas="U5",fecha_ingreso=date)
    p25.save()

    #2012
    date=datetime.datetime(2012,6,30)
    p31=Mediciones(central=p1,transformador=p25,codigo_usuario="7807004",Hidrogeno=30,Oxigeno=0,Nitrogeno=0,Metano=11,Monoxido_de_carbono=328,Etano=23,Dioxido_de_carbono=15922,Etileno=14,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p31.save()
    #2013
    date=datetime.datetime(2013,6,30)
    p32=Mediciones(central=p1,transformador=p25,codigo_usuario="7807004",Hidrogeno=21,Oxigeno=0,Nitrogeno=0,Metano=13,Monoxido_de_carbono=308,Etano=20,Dioxido_de_carbono=15521,Etileno=10,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p32.save()
    #2014
    date=datetime.datetime(2014,6,30)
    p33=Mediciones(central=p1,transformador=p25,codigo_usuario="7807004",Hidrogeno=18,Oxigeno=0,Nitrogeno=0,Metano=9,Monoxido_de_carbono=194,Etano=15,Dioxido_de_carbono=4940,Etileno=8,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p33.save()
    #2015
    date=datetime.datetime(2015,6,30)
    p34=Mediciones(central=p1,transformador=p25,codigo_usuario="7807004",Hidrogeno=10,Oxigeno=0,Nitrogeno=112000,Metano=7,Monoxido_de_carbono=219,Etano=3,Dioxido_de_carbono=8150,Etileno=3,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p34.save()
    #2016
    date=datetime.datetime(2016,6,30)
    p35=Mediciones(central=p1,transformador=p25,codigo_usuario="7807004",Hidrogeno=16,Oxigeno=0,Nitrogeno=0,Metano=1,Monoxido_de_carbono=234,Etano=35,Dioxido_de_carbono=8630,Etileno=10,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p35.save()











    p26=Transformadores(central=p1,codigo="A15051",marca="TOSHIBA",modelo="NA",cararcteristicas="U6",fecha_ingreso=date)
    p26.save()

     #2016
    date=datetime.datetime(2016,6,30)
    p31=Mediciones(central=p1,transformador=p26,codigo_usuario="7807004",Hidrogeno=10,Oxigeno=7760,Nitrogeno=26500,Metano=5,Monoxido_de_carbono=212,Etano=2,Dioxido_de_carbono=677,Etileno=2,Acetileno=2,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p31.save()
    #2018
    date=datetime.datetime(2018,6,30)
    p32=Mediciones(central=p1,transformador=p26,codigo_usuario="7807004",Hidrogeno=18,Oxigeno=0,Nitrogeno=0,Metano=29,Monoxido_de_carbono=785,Etano=3,Dioxido_de_carbono=4062,Etileno=6,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p32.save()







    p27=Transformadores(central=p1,codigo="A15052",marca="TOSHIBA",modelo="NA",cararcteristicas="U7",fecha_ingreso=date)
    p27.save()

    #2016
    date=datetime.datetime(2016,6,30)
    p31=Mediciones(central=p1,transformador=p27,codigo_usuario="7807004",Hidrogeno=10,Oxigeno=7760,Nitrogeno=26500,Metano=5,Monoxido_de_carbono=212,Etano=2,Dioxido_de_carbono=677,Etileno=2,Acetileno=2,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p31.save()
    #2018
    date=datetime.datetime(2018,6,30)
    p32=Mediciones(central=p1,transformador=p27,codigo_usuario="7807004",Hidrogeno=21,Oxigeno=0,Nitrogeno=0,Metano=32,Monoxido_de_carbono=887,Etano=6,Dioxido_de_carbono=4395,Etileno=8,Acetileno=3,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p32.save()






    p28=Transformadores(central=p1,codigo="544328",marca="MITSUBICHI",modelo="NA",cararcteristicas="RESERVA",fecha_ingreso=date)
    p28.save()

    #2012
    date=datetime.datetime(2012,6,30)
    p31=Mediciones(central=p1,transformador=p28,codigo_usuario="7807004",Hidrogeno=48,Oxigeno=0,Nitrogeno=0,Metano=2,Monoxido_de_carbono=12,Etano=61,Dioxido_de_carbono=4166,Etileno=19,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p31.save()
    #2013
    date=datetime.datetime(2013,6,30)
    p32=Mediciones(central=p1,transformador=p28,codigo_usuario="7807004",Hidrogeno=33,Oxigeno=0,Nitrogeno=0,Metano=3,Monoxido_de_carbono=11,Etano=60,Dioxido_de_carbono=3999,Etileno=6,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p32.save()
    #2014
    date=datetime.datetime(2014,6,30)
    p33=Mediciones(central=p1,transformador=p28,codigo_usuario="7807004",Hidrogeno=8,Oxigeno=250,Nitrogeno=82.065,Metano=8,Monoxido_de_carbono=14,Etano=53,Dioxido_de_carbono=4781,Etileno=0,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p33.save()
    #2015
    date=datetime.datetime(2015,6,30)
    p34=Mediciones(central=p1,transformador=p28,codigo_usuario="7807004",Hidrogeno=30,Oxigeno=0,Nitrogeno=89.8,Metano=4.9,Monoxido_de_carbono=4.9,Etano=44,Dioxido_de_carbono=4900,Etileno=1.9,Acetileno=1.9,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p34.save()


    u1=User.objects.create_user(username="7807004", password="4690",email="evvaldez@cel.gob.sv",first_name="Ernesto Vladimir",last_name="Valdez Rivas")
    u1.save()
    u1=Usuarios(central=p1,codigo_usuario="7807004", pasword="4690",email="evvaldez@cel.gob.sv",nombres="Ernesto Vladimir",apellidos="Valdez Rivas",privilegio="DE_ALTA",fecha_ingreso=date)
    u1.save()



    p1=Centrales(nombre="Guajoyo",fecha_ingreso=date)   
    p1.save() 


    p21=Transformadores(central=p1,codigo="00001111",marca="GUAJOYOX",modelo="NA",cararcteristicas="U1",fecha_ingreso=date)
    p21.save()
      
    #EFACET U1
    #2014
    date=datetime.datetime(2014,6,30)
    p31=Mediciones(central=p1,transformador=p21,codigo_usuario="7807004",Hidrogeno=3,Oxigeno=0,Nitrogeno=0,Metano=1,Monoxido_de_carbono=4,Etano=1,Dioxido_de_carbono=203.41,Etileno=0.17,Acetileno=0.7,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p31.save()
    #2015
    date=datetime.datetime(2015,6,30)
    p32=Mediciones(central=p1,transformador=p21,codigo_usuario="7807004",Hidrogeno=5.38,Oxigeno=29.92,Nitrogeno=36320,Metano=8.8,Monoxido_de_carbono=4.97,Etano=2.1,Dioxido_de_carbono=926,Etileno=0.68,Acetileno=1.2,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p32.save()
    #2016
    date=datetime.datetime(2016,6,30)
    p33=Mediciones(central=p1,transformador=p21,codigo_usuario="7807004",Hidrogeno=2,Oxigeno=0,Nitrogeno=0,Metano=50,Monoxido_de_carbono=137,Etano=67,Dioxido_de_carbono=2010,Etileno=5,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p33.save()
    #2017
    date=datetime.datetime(2017,6,30)
    p34=Mediciones(central=p1,transformador=p21,codigo_usuario="7807004",Hidrogeno=5,Oxigeno=0,Nitrogeno=0,Metano=57,Monoxido_de_carbono=155,Etano=79,Dioxido_de_carbono=2037,Etileno=10,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p34.save()
    #2018
    date=datetime.datetime(2018,6,30)
    p35=Mediciones(central=p1,transformador=p21,codigo_usuario="7807004",Hidrogeno=15,Oxigeno=0,Nitrogeno=0,Metano=89,Monoxido_de_carbono=159,Etano=134,Dioxido_de_carbono=2308,Etileno=12,Acetileno=3,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p35.save()





    p22=Transformadores(central=p1,codigo="222222",marca="Guajoyos23",modelo="NA",cararcteristicas="U2",fecha_ingreso=date)
    p22.save()
    #2010
    date=datetime.datetime(2010,6,30)
    p31=Mediciones(central=p1,transformador=p22,codigo_usuario="7807004",Hidrogeno=5,Oxigeno=0,Nitrogeno=0,Metano=4,Monoxido_de_carbono=132,Etano=12,Dioxido_de_carbono=2027,Etileno=25,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p31.save()
    #2012
    date=datetime.datetime(2012,6,30)
    p32=Mediciones(central=p1,transformador=p22,codigo_usuario="7807004",Hidrogeno=24,Oxigeno=0,Nitrogeno=0,Metano=7,Monoxido_de_carbono=352,Etano=10,Dioxido_de_carbono=3641,Etileno=34,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p32.save()
    #2013
    date=datetime.datetime(2013,6,30)
    p33=Mediciones(central=p1,transformador=p22,codigo_usuario="7807004",Hidrogeno=17,Oxigeno=0,Nitrogeno=87500,Metano=9,Monoxido_de_carbono=463,Etano=11,Dioxido_de_carbono=4140,Etileno=40,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p33.save()
    #2014
    date=datetime.datetime(2014,6,30)
    p34=Mediciones(central=p1,transformador=p22,codigo_usuario="7807004",Hidrogeno=16,Oxigeno=0,Nitrogeno=0,Metano=4,Monoxido_de_carbono=42,Etano=7,Dioxido_de_carbono=680,Etileno=11,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p34.save()
    #2015
    date=datetime.datetime(2015,6,30)
    p35=Mediciones(central=p1,transformador=p22,codigo_usuario="7807004",Hidrogeno=12,Oxigeno=0,Nitrogeno=0,Metano=11,Monoxido_de_carbono=228,Etano=3,Dioxido_de_carbono=2226,Etileno=5,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p35.save()

    #2016
    date=datetime.datetime(2016,6,30)
    p35=Mediciones(central=p1,transformador=p22,codigo_usuario="7807004",Hidrogeno=15,Oxigeno=0,Nitrogeno=0,Metano=9,Monoxido_de_carbono=247,Etano=9,Dioxido_de_carbono=2381,Etileno=14,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date,comentario="Sin comentario")
    p35.save()



    return render(request,'principal.html',locals())



################################################################################


def datos_de_analisis_rapido(central_x, transformador_x):

    x=Mediciones_rapidas.objects.filter(central=central_x).first()
    SIMBOLO_GAS=["H2","CH4","C2H2","C2H4","C2H6","CO","O2","N2","CO2"]
    NG=["Hidrogeno","Metano","Acetileno","Etileno","Etano","Monoxido_de_carbono","Oxigeno","Nitrogeno","Dioxido_de_carbono"]
    
    gas_analisis=[ (NG[0],x.Hidrogeno),(NG[1],x.Metano),(NG[2],x.Acetileno),(NG[3],x.Etileno),(NG[4],x.Etano),(NG[5],x.Monoxido_de_carbono),(NG[6],x.Oxigeno),(NG[7],x.Nitrogeno),(NG[8],x.Dioxido_de_carbono) ]
              
    return gas_analisis

################################################################################
def datos_de_analisis(central_x, transformador_x):

    MedicionesF=Mediciones.objects.filter(Q(central__nombre__icontains=central_x) &  Q(transformador__codigo__icontains=transformador_x)).order_by("fecha_del_analisis")
       
    SIMBOLO_GAS=["H2","CH4","C2H2","C2H4","C2H6","CO","O2","N2","CO2"]
    NOMBRE_GAS_PRUEBA=["Hidrogeno","Metano","Acetileno","Etileno","Etano","Monoxido_de_carbono","Oxigeno","Nitrogeno","Dioxido_de_carbono"]
   
    gas_analisis=[]
    valor=[]
    
    for i in NOMBRE_GAS_PRUEBA:
        datos=MedicionesF.values_list(i, flat=True) 
        
        for y in datos: 
            if y!=0 and y!="":
                valor.append(y)

        gas_analisis.append((i,valor[-1])) 

    return gas_analisis


################################################################################

################################################################################

def gas_clave( VALOR_DEL_GAS):
        
        #VALOR_DEL_GAS= datos_de_analisis(central_x, transformador_x)     

        SIMBOLO_GAS=["H2","CH4","C2H2","C2H4","C2H6","CO","O2","N2","CO2"]
        NOMBRE_GAS_PRUEBA=["Hidrogeno","Metano","Acetileno","Etileno","Etano","Monoxido_de_carbono","Oxigeno","Nitrogeno","Dioxido_de_carbono"]

        SIMBOLO_GAS_COMBUSTIBLE=["H2","CH4","C2H2","C2H4","C2H6","CO"]
        NOMBRE_GAS_COMBUSTIBLE=["Hidrogeno","Metano","Acetileno","Etileno","Etano","Monoxido_de_carbono"]

        SUMTDG=0
        for i in range(len (SIMBOLO_GAS_COMBUSTIBLE)):
            SUMTDG+=VALOR_DEL_GAS[i][1]

        PORCENTAJES=[]
        for i in range(len (SIMBOLO_GAS_COMBUSTIBLE)):
            valor=100*VALOR_DEL_GAS[i][1]/SUMTDG
            PORCENTAJES.append(valor)

        Vmaximo=max( PORCENTAJES)
        indice_Vmaximo= PORCENTAJES.index(Vmaximo)

        if indice_Vmaximo==0:#hidrogeno H2
                    estado_trafo="SE DETECTO EFECTO CORONA"              
                       
        elif indice_Vmaximo==2:# acetileno C2H2
                        estado_trafo="SE DETECTO ARCO INTERNO"

        elif indice_Vmaximo==3:#etileno C2H4            
                        estado_trafo="SE DETECTO ACEITE SOBRE CALENTADO"

        elif indice_Vmaximo==5:#monoxido de carbono CO
                        estado_trafo="SE DETECTO PAPEL SOBRECALENTADO"

        else:
                    estado_trafo="NO APLICA"


        return estado_trafo

################################################################################

################################################################################
def limite_concentracion(VALOR_DEL_GAS):
        #Segun IEEE c57.104-1991
        #SIMBOLO_GAS=["H2","CH4","C2H2","C2H4","C2H6","CO","O2","N2","CO2"]
        #NOMBRE_GAS_PRUEBA=["Hidrogeno","Metano","Acetileno","Etileno","Etano","Monoxido_de_carbono","Oxigeno","Nitrogeno","Dioxido_de_carbono"]
        #VALOR_DEL_GAS= datos_de_analisis(central_x, transformador_x)  

        SIMBOLO_GAS=["H2","CH4","C2H2","C2H4","C2H6","CO"]
        NOMBRE_GAS_PRUEBA=["Hidrogeno","Metano","Acetileno","Etileno","Etano","Monoxido_de_carbono"]

        LIMITE_1=[100,120,2,50,65,350]
        LIMITE_2=[700,400,5,100,100,570]
       
        SUMTDGC=0
        for i in range(len (LIMITE_1)):
            SUMTDGC+=VALOR_DEL_GAS[i][1]

        if SUMTDGC<700:
            estado_trafo="EL TRANSFORMADOR ESTA OPERANDO NORMALMENTE"
        elif SUMTDGC>=700 and SUMTDGC <1900 :
            estado_trafo="PRECAUCION !! EL TRANSFORMADOR REQUIERE ATENCION"
        else:
            estado_trafo="EL TRANSFORMADOR TIENE UN PROBLEMA GRAVE (INTERVENCION O CAMBIO)" 
        #return estado_trafo
                
        
        ESTADO_DE_GASES=[]
        for i in range(len(LIMITE_1)):
            if VALOR_DEL_GAS[i][1]<LIMITE_1[i]:
                estado = "NORMAL"
            elif VALOR_DEL_GAS[i][1]>=LIMITE_1[i] and VALOR_DEL_GAS[i][1]<LIMITE_2[i]:
                estado = "PRECAUCION"
            else:
                estado = "ADVERTENCIA"
            
            vector=[NOMBRE_GAS_PRUEBA[i], SIMBOLO_GAS[i],VALOR_DEL_GAS[i][1],estado]
            ESTADO_DE_GASES.append(vector)
        
        respuesta= [estado_trafo,ESTADO_DE_GASES]
        return respuesta

        #return render(request,'analisis.html',locals())

################################################################################
################################################################################
def total_gases_combustibles(VALOR_DEL_GAS):
        #SIMBOLO_GAS=["H2","CH4","C2H2","C2H4","C2H6","CO","O2","N2","CO2"]
        #NOMBRE_GAS_PRUEBA=["Hidrogeno","Metano","Acetileno","Etileno","Etano","Monoxido_de_carbono","Oxigeno","Nitrogeno","Dioxido_de_carbono"]
        #VALOR_DEL_GAS= datos_de_analisis(central_x, transformador_x)  

        SIMBOLO_GAS=["H2","CH4","C2H2","C2H4","C2H6","CO"]
        NOMBRE_GAS_PRUEBA=["Hidrogeno","Metano","Acetileno","Etileno","Etano","Monoxido_de_carbono"]

        LIMITE_1=[100,120,35,50,65,350]
        LIMITE_2=[700,400,50,100,100,570]
        LIMITE_3=[1800,1000,80,200,150,1400]


        SUMTDGC=0
        for i in range(len (LIMITE_1)):
            SUMTDGC+=VALOR_DEL_GAS[i][1]

        if SUMTDGC<720:
            estado_trafo="EL TRANSFORMADOR ESTA OPERANDO SATISFACTORIAMENTE"
        elif SUMTDGC>=720 and SUMTDGC <1920 :
            estado_trafo="EL TRANSFORMADOR PRESENTA NIVEL DE GASES MAS ALTO QUE LO NORMAL,\n INVESTIGAR LOS LIMITES PARA CADA GAS"
        elif SUMTDGC>=1920 and SUMTDGC <4630 :
            estado_trafo="EL TRANSFORMADOR PRESENTA UN ALTO GRADO DE DESCOMPOSICION DE\n CELULOSA Y/O ACEITE, INVESTIGAR LOS LIMITES PARA CADA GAS"
        else:
            estado_trafo="EL TRANSFORMADOR PRESENTA UN ALTO GRADO DE DESCOMPOSICION DE\n CELULOSA Y/O ACEITE, LA OPERACION CONTINUA DEL TTRANSFORMADOR \nPUEDE RESULTAR EN FALLA DEL MISMO"
        

        ESTADO_DE_GASES=[]
    
        for i in range(len(LIMITE_1)):
            if VALOR_DEL_GAS[i][1]<LIMITE_1[i]:
                estado = "NORMAL"
            elif VALOR_DEL_GAS[i][1]>=LIMITE_1[i] and VALOR_DEL_GAS[i][1]<LIMITE_2[i]:
                estado = "ANORMAL MODERDADO"

            elif VALOR_DEL_GAS[i][1]>=LIMITE_2[i] and VALOR_DEL_GAS[i][1]<LIMITE_3[i]:
                estado = "ANORMAL EXESIVO"
            else:
                estado = "MUY ANORMAL"

            vector=[NOMBRE_GAS_PRUEBA[i], SIMBOLO_GAS[i],VALOR_DEL_GAS[i][1],estado]
            ESTADO_DE_GASES.append(vector)         
        
        
        respuesta= [estado_trafo,ESTADO_DE_GASES]

        return respuesta
        
        #return render(request,'analisis.html',locals())

################################################################################

################################################################################

def roger(VALOR_DEL_GAS):
        
        #VALOR_DEL_GAS= datos_de_analisis(central_x, transformador_x)     

        #SIMBOLO_GAS=["H2","CH4","C2H2","C2H4","C2H6","CO","O2","N2","CO2"]
        #NOMBRE_GAS_PRUEBA=["Hidrogeno","Metano","Acetileno","Etileno","Etano","Monoxido_de_carbono","Oxigeno","Nitrogeno","Dioxido_de_carbono"]

        #SIMBOLO_GAS_COMBUSTIBLE=["H2","CH4","C2H2","C2H4","C2H6","CO"]
        #NOMBRE_GAS_COMBUSTIBLE=["Hidrogeno","Metano","Acetileno","Etileno","Etano","Monoxido_de_carbono"]

        R1=VALOR_DEL_GAS[2][1]/VALOR_DEL_GAS[3][1]#C2H2/C2H4
        R2=VALOR_DEL_GAS[1][1]/VALOR_DEL_GAS[0][1]#CH4/H2
        R3=VALOR_DEL_GAS[3][1]/VALOR_DEL_GAS[4][1]#C2H4/C2H6

        R1=round(R1,2)
        R2=round(R2,2)
        R3=round(R3,2)

        
        if R1<0.1 and R2>0.1 and R2<1 and R3<1 :
            estado_trafo=" Estado Normal"

        if R1<0.1 and R2<0.1 and R3<1 :
            estado_trafo=" Descarga parcial (corona)\n Arco de baja dencidad de energia"

        if R1>0.1 and R1<3 and R2>0.1 and R2<1 and R3>3 :
            estado_trafo=" Arco\n Descarga de alta energia"

        if R1<0.1 and R2>0.1 and R2<1 and R3>1 and R3<3  :
            estado_trafo=" Sobrecalentamiento termico a baja temperatura" 
        
        if R1<0.1 and R2>0.1 and R3>1 and R3<3  :
            estado_trafo=" Calentamiento de alta temperatura menor de 700 grados celcius"

        if R1<0.1 and R2>0.1 and R3>3  :
            estado_trafo=" Calentamiento de alta temperatura mayor de 700 grados celcius"
        
        else:
            estado_trafo=" No aplica diagnostico con este metodo" 
        
        estado_trafo2 = "C2H2/C2H4=" + str(R1) + "  CH4/H2="+str(R2) + "  C2H4/C2H6="+str(R3) + estado_trafo
        
        return estado_trafo2
        #return render(request,'analisis.html',locals())

################################################################################

def donenberg(VALOR_DEL_GAS):
        
        #VALOR_DEL_GAS= datos_de_analisis(central_x, transformador_x)     

        #SIMBOLO_GAS=["H2","CH4","C2H2","C2H4","C2H6","CO","O2","N2","CO2"]
        #NOMBRE_GAS_PRUEBA=["Hidrogeno","Metano","Acetileno","Etileno","Etano","Monoxido_de_carbono","Oxigeno","Nitrogeno","Dioxido_de_carbono"]

        #SIMBOLO_GAS_COMBUSTIBLE=["H2","CH4","C2H2","C2H4","C2H6","CO"]
        #NOMBRE_GAS_COMBUSTIBLE=["Hidrogeno","Metano","Acetileno","Etileno","Etano","Monoxido_de_carbono"]
        
        R1=VALOR_DEL_GAS[1][1]/VALOR_DEL_GAS[0][1]#CH4/H2

        R2=VALOR_DEL_GAS[2][1]/VALOR_DEL_GAS[3][1]#C2H2/C2H4
        R1=round(R1,2)
        R2=round(R2,2)
        

        if R1>0.87 and R1<=100 and R2>=0.01 and R2<=0.87  :
            estado_trafo=" Se detecto un problema termico"

        if R1>=0.087 and R1<=0.87 and R2>0.1 and R2<=110 :
            estado_trafo=" Se detecto un problema de Arco"

        if R1>=0 and R1<=0.087 and R2>0.087 and R2<100 :
            estado_trafo=" Se detecto un problema de efecto Corona"       
        
        else:
            estado_trafo=" No aplica diagnostico con este metodo" 
        
        estado_trafo2 = "CH4/H2=" + str(R1) + "  C2H2/C2H4="+str(R2)  + estado_trafo
        return estado_trafo2
        #return render(request,'analisis.html',locals())
################################################################################

def duval( VALOR_DEL_GAS):
        
        #VALOR_DEL_GAS= datos_de_analisis(central_x, transformador_x)     

        #SIMBOLO_GAS=["H2","CH4","C2H2","C2H4","C2H6","CO","O2","N2","CO2"]
        #NOMBRE_GAS_PRUEBA=["Hidrogeno","Metano","Acetileno","Etileno","Etano","Monoxido_de_carbono","Oxigeno","Nitrogeno","Dioxido_de_carbono"]

        #SIMBOLO_GAS_COMBUSTIBLE=["H2","CH4","C2H2","C2H4","C2H6","CO"]
        #NOMBRE_GAS_COMBUSTIBLE=["Hidrogeno","Metano","Acetileno","Etileno","Etano","Monoxido_de_carbono"]
        SUMAGASES=VALOR_DEL_GAS[1][1]+VALOR_DEL_GAS[2][1]+VALOR_DEL_GAS[3][1]

        PCH4=VALOR_DEL_GAS[1][1]/SUMAGASES
        PC2H2=VALOR_DEL_GAS[2][1]/SUMAGASES
        PC2H4=VALOR_DEL_GAS[3][1]/SUMAGASES 

        PCH4=round(PCH4,2)
        PC2H2=round(PC2H2,2)
        PC2H4=round(PC2H4,2)

        respuesta=[PCH4,PC2H2,PC2H4]
        return respuesta 
        #return render(request,'analisis.html',locals())

################################################################################

def IEC_60599(VALOR_DEL_GAS):
    #SIMBOLO_GAS=["H2","CH4","C2H2","C2H4","C2H6","CO","O2","N2","CO2"]
    #NOMBRE_GAS_PRUEBA=["Hidrogeno","Metano","Acetileno","Etileno","Etano","Monoxido_de_carbono","Oxigeno","Nitrogeno","Dioxido_de_carbono"]
    
    X1=VALOR_DEL_GAS[2][1]/VALOR_DEL_GAS[3][1]
    X2=VALOR_DEL_GAS[1][1]/VALOR_DEL_GAS[0][1]
    X3=VALOR_DEL_GAS[2][1]/VALOR_DEL_GAS[4][1]

    X1=round(X1,2)
    X2=round(X2,2)
    X3=round(X3,2)

    if X2<0.1 and X3<0.2:
        estado_trafo="DP: Descargas parciales"

    elif X1>1 and X2>=0.1 and X2<=0.5 and X3>1:
        estado_trafo="D1: Descargas de BAJA energia"

    elif X1>=0.6 and X1<=2.5 and X2>=0.1 and X2<=1 and X3>2:
        estado_trafo="D2: Descargas de ALTA energia"

    elif X3<1:
        estado_trafo="T1: Descargas de baja energia"

    elif X1<0.1 and X2>1 and X3>1 and X3>=1 and X3<=4:
        estado_trafo="T2: Defecto termico 300 oC < T < 700 oC"

    elif X1<0.2 and X2>1 and X3>4:
        estado_trafo="T3: Defecto termico T > 700 oC"
    else:  
        estado_trafo="No aplica diagnostico con este metodo"
    
    SIMBOLO_GAS=["H2","CH4","C2H2","C2H4","C2H6","CO","O2","N2","CO2"]
    NOMBRE_GAS_PRUEBA=["Hidrogeno","Metano","Acetileno","Etileno","Etano","Monoxido_de_carbono","Oxigeno","Nitrogeno","Dioxido_de_carbono"]
    
    LIMITE_1=[ 60, 40, 3, 60,50,540,0,0,5100]
    LIMITE_2=[150,110,50,280,90,900,0,0,13000]
     
           
    ESTADO_DE_GASES=[]
    for i in range(len(LIMITE_1)):
        
        if i!=6 and i!=7:
            if VALOR_DEL_GAS[i][1]>=LIMITE_1[i] and VALOR_DEL_GAS[i][1]<LIMITE_2[i]:
                estado = "En valor tipico"
            else:
                estado = "Fuera del rango tipico"
        else:
                estado = "No aplica"

        vector=[NOMBRE_GAS_PRUEBA[i], SIMBOLO_GAS[i],VALOR_DEL_GAS[i][1],estado]
        ESTADO_DE_GASES.append(vector)
        
    respuesta= [estado_trafo,ESTADO_DE_GASES]
    return respuesta
   



def analitico_CO2_CO(VALOR_DEL_GAS):
    #SIMBOLO_GAS=["H2","CH4","C2H2","C2H4","C2H6","CO","O2","N2","CO2"]
    #NOMBRE_GAS_PRUEBA=["Hidrogeno","Metano","Acetileno","Etileno","Etano","Monoxido_de_carbono","Oxigeno","Nitrogeno","Dioxido_de_carbono"]
    R1=VALOR_DEL_GAS[8][1]/VALOR_DEL_GAS[5][1]
    R1=round(R1,2)

    if R1<3:
        respuesta="Degradacion excesiva del papel, con algun grado de carbonizacion CO2/CO="+str(R1) 
    
    elif R1>=3 and R1<6.5:
        respuesta="la relacion  CO2/CO="+str(R1) + ", Esta es mayor a 3 y menor a 6.5, 7 es una relacion normal"
    
    elif R1>=6.5 and R1<=7.5:
        respuesta="la relacion  CO2/CO es"+ str(R1)+ ", Lo normal es un valor proximo a 7"

    else:
        respuesta="Altas concentraciones de de CO2 y bajas de CO indican \n un sobrecalentamiento general CO2/CO="+str(R1)
     
    return respuesta

def analitico_C2H2_H2(VALOR_DEL_GAS):
    #SIMBOLO_GAS=["H2","CH4","C2H2","C2H4","C2H6","CO","O2","N2","CO2"]
    #NOMBRE_GAS_PRUEBA=["Hidrogeno","Metano","Acetileno","Etileno","Etano","Monoxido_de_carbono","Oxigeno","Nitrogeno","Dioxido_de_carbono"]
    R1=VALOR_DEL_GAS[2][1]/VALOR_DEL_GAS[0][1]
    R1=round(R1,2)

    if R1>3:
        respuesta="C2H2/H2="+ str(R1) + ", Indica contaminacion del aceite del tanque principal \n por aceite del cambiador de derivacion bajo carga \n en transformador con respiradero abierto" 
    else:
        respuesta="C2H2/H2="+ str(R1) + ",No aplica diagnostico con este metodo" 

    return respuesta

def analitico_O2_N2(lista_mediciones):
    #SIMBOLO_GAS=["H2","CH4","C2H2","C2H4","C2H6","CO","O2","N2","CO2"]
    #NOMBRE_GAS_PRUEBA=["Hidrogeno","Metano","Acetileno","Etileno","Etano","Monoxido_de_carbono","Oxigeno","Nitrogeno","Dioxido_de_carbono"]
    O2_N2=[]
    for i in lista_mediciones:        
        try:
            R=i[6]/i[7]
            R=round(R,2)
            O2_N2.append(R)
        except:
            R="--"
            O2_N2.append(R)
    
    respuesta=["O2/N2 a la baja indica exesivo calentamiento",O2_N2]

    return respuesta








from django.shortcuts import render
from matplotlib import pylab
from pylab import *
import PIL
import PIL.Image
import io
from io import *

##########################
import numpy as np
import matplotlib.pyplot as plt
#################################
import pylab as pl


def grafico_tendencias(request,central_x,transformador_x,gas_analizar):

    limites=[("Hidrogeno",150),("Oxigeno",16),("Nitrogeno",8.6),("Metano",110),("Monoxido_de_carbono",900),("Etano",90),("Dioxido_de_carbono",2500),("Etileno",280),("Acetileno",3)]
    for i in limites:
        if gas_analizar==i[0]:
            limite=i[1]
            break    
    
    
    MedicionesF=Mediciones.objects.filter(Q(central__nombre__icontains=central_x) &  Q(transformador__codigo__icontains=transformador_x)).order_by("fecha_del_analisis")
    
    datos=MedicionesF.values_list(gas_analizar, flat=True) 
    fecha=MedicionesF.values_list("fecha_del_analisis", flat=True)     
    anios=[]
    limitemax=[]

    for i in  fecha:
        an=i.strftime('%d%m%Y') 
        anios.append(an)
        limitemax.append(limite)    
        

    X= np.arange(len(fecha))
    Y1 = np.asarray(datos) 
   

    f=plt.figure()
    #barh(pos,datos,align = 'center')
    plt.plot(anios,limitemax, 'r')
    plt.plot(anios,datos,'b*-')

    plt.grid()


    z=0 
    for x, y in zip(X, Y1):
            plt.text(x, y ,str(y), ha='center', va= 'bottom')
            z=z+1


    plt.yticks(limitemax,color="r")
    #plt.yticks(datos,color="b")    
    #plt.xticks(anios,size="small",color="b",rotation=45)
    plt.xticks(rotation='vertical',size="small")

    plt.xlabel('Fecha de la prueba ')
    plt.ylabel('CONCENTRACIONES ppm')
    titulo="Tendencia del gas "+gas_analizar +" disuelto en aceite"
    plt.title(titulo)
    
    #subplots_adjust(left=0.21)

    buffer = io.BytesIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
   
    graphIMG = PIL.Image.fromstring('RGB', canvas.get_width_height(), canvas.tostring_rgb())
    graphIMG.save(buffer, "PNG")
    pylab.close()   
    f.clear()

    return HttpResponse (buffer.getvalue(), content_type="Image/png")
##############################
##########################################


def informacion(request):
  centrales=Centrales.objects.all()
  try:
        usuario_comun=Usuarios.objects.get(codigo_usuario=request.user.username)
  except:
        pass
  return render(request,'informacion.html',locals())

def principal(request):
    centrales=Centrales.objects.all()
    try:
        usuario_comun=Usuarios.objects.get(codigo_usuario=request.user.username)
    except:
        pass

    return render(request,'principal.html',locals())

def listado_de_equipos(request,central_x):
    centrales=Centrales.objects.all()
    try:
        usuario_comun=Usuarios.objects.get(codigo_usuario=request.user.username)
    except:
        pass   

    lista_generadores=Generadores.objects.filter(central__nombre__icontains=central_x)
    lista_transformadores=Transformadores.objects.filter(central__nombre__icontains=central_x)
    lista_sistemas_termograficos=Sistema_termografico.objects.filter(central__nombre__icontains=central_x)
    return render(request,'lista_de_equipos.html',locals())

#def (request,central_x,transformador_x):
#    centralelistado_de_medicioness=Centrales.objects.all()
                                       
 #   lista_mediciones=Mediciones.objects.filter(Q(central__nombre__icontains=central_x) &  Q(transformador__codigo__icontains=transformador_x)).order_by("fecha_del_analisis")
 #   identificador=lista_mediciones.first()
    
 #   VALOR_DEL_GAS= datos_de_analisis(central_x, transformador_x) 

        
  #  return render(request,'lista_de_mediciones.html',locals())

def tendencias(request,central_x,transformador_x,gas_x):
    gas=gas_x
    central=central_x
    transformador=transformador_x


    return render(request,'tendencias.html',locals()) 

def analisis_rapido(request,central_x,transformador_x):

    VALOR_DEL_GAS= datos_de_analisis_rapido(central_x, transformador_x)
   
    VALOR_GAS_LIMITES=[]
    LIMITES_GAS=["100","120","2--35","50","65","350","-","-","-"]    
    for i in range(len(VALOR_DEL_GAS)):   
        a=[VALOR_DEL_GAS[i][0],VALOR_DEL_GAS[i][1],LIMITES_GAS[i]]
        VALOR_GAS_LIMITES.append(a)
        
    central=central_x
    transformador=transformador_x
    segun_gas_clave=gas_clave(VALOR_DEL_GAS)#valor
    concentraciones_limite=limite_concentracion(VALOR_DEL_GAS)#vector
    gases_combustibles= total_gases_combustibles(VALOR_DEL_GAS)#vector    
    Triangulo_duval=duval( VALOR_DEL_GAS)    
    segun_donenberg=donenberg(VALOR_DEL_GAS)
    segun_roger=roger(VALOR_DEL_GAS)     
    segun_IEC_60599=IEC_60599(VALOR_DEL_GAS)    
    segun_analitico_CO2_CO=analitico_CO2_CO(VALOR_DEL_GAS)
    segun_analitico_C2H2_H2=analitico_C2H2_H2(VALOR_DEL_GAS)      

    return render(request,'analisis_rapido.html',locals())

def analisis(request,central_x,transformador_x):

    VALOR_DEL_GAS= datos_de_analisis(central_x, transformador_x)
    
    VALOR_GAS_LIMITES=[]
    LIMITES_GAS=["100","120","2--35","50","65","350","-","-","-"]    
    for i in range(len(VALOR_DEL_GAS)):   
        a=[VALOR_DEL_GAS[i][0],VALOR_DEL_GAS[i][1],LIMITES_GAS[i]]
        VALOR_GAS_LIMITES.append(a)
        
    centrales=Centrales.objects.all()
    central=central_x
    transformador=transformador_x

    segun_gas_clave=gas_clave(VALOR_DEL_GAS)#valor
    
    concentraciones_limite=limite_concentracion(VALOR_DEL_GAS)#vector
    gases_combustibles= total_gases_combustibles(VALOR_DEL_GAS)#vector    
    
    Triangulo_duval=duval( VALOR_DEL_GAS)    
    segun_donenberg=donenberg(VALOR_DEL_GAS)
    segun_roger=roger(VALOR_DEL_GAS)     
   
    lista_mediciones=Mediciones.objects.filter(Q(central__nombre__icontains=central_x) &  Q(transformador__codigo__icontains=transformador_x)).order_by("fecha_del_analisis")
    identificador=lista_mediciones.first()
    
    segun_IEC_60599=IEC_60599(VALOR_DEL_GAS)    
    segun_analitico_CO2_CO=analitico_CO2_CO(VALOR_DEL_GAS)
    segun_analitico_C2H2_H2=analitico_C2H2_H2(VALOR_DEL_GAS)
    segun_analitico_O2_N2=analitico_O2_N2(lista_mediciones)    

    return render(request,'analisis.html',locals())

##############################ejemplito
#class Make(models.Model):
#    name = models.CharField(max_length=200)

#class MakeContent(models.Model):
#    make = models.ForeignKey(Make, related_name='makecontent')
#    published = models.BooleanField()

#Make.objects.filter(makecontent__published=True)


def grafico_gases_presentes(request,central_x, transformador_x):  
       
        VALOR_DEL_GAS= datos_de_analisis(central_x, transformador_x)
        LIMITE_1=[100,120,35,50,65,350,0,0,2500]             

        nombre_gases=[]
        valor_gases=[]


        for i in VALOR_DEL_GAS:
            nombre_gases.append(i[0])
            valor_gases.append(i[1])

        X= np.arange(len(nombre_gases))
        
        Y1 = np.asarray(valor_gases)  
        Y2 = np.asarray(LIMITE_1)
     
                   
               
        f=plt.figure()
       
        plt.gca().set_yscale('log')

        bar_width = 0.02
        plt.bar(X-0.25, Y2, bar_width, color='r')
        bar_width = 0.45
        plt.bar(X, Y1, bar_width, color='b')

        

        SIMBOLO_GAS=["H2","CH4","C2H2","C2H4","C2H6","CO","O2","N2","CO2"]
      
        z=0 
        for x, y in zip(X, Y1):
            plt.text(x, y+1 ,str(y)+ "\n"+SIMBOLO_GAS[z], ha='center', va= 'bottom')
            z=z+1
 
      
        plt.xlabel('\nGases combustibles (H2,CH4,C2H2,C2H4,C2H6) +CO +O2 +N2 +CO2 ')
        plt.ylabel('Concentraciones de gas (ppm) ')
        titulo=""
        plt.title(titulo)
        plt.xticks(())

        subplots_adjust(left=0.21)
      

        buffer = io.BytesIO()
        canvas = pylab.get_current_fig_manager().canvas
        canvas.draw()        
        graphIMG = PIL.Image.fromstring('RGB', canvas.get_width_height(), canvas.tostring_rgb())
        graphIMG.save(buffer, "PNG")
        pylab.close()  

        f.clear()
        
        return HttpResponse (buffer.getvalue(), content_type="Image/png")

 # Store image in a string buffer
    
 
def grafico_gases_presentes_rapido(request,central_x, transformador_x):  
       
        VALOR_DEL_GAS= datos_de_analisis_rapido(central_x, transformador_x)
        LIMITE_1=[100,120,35,50,65,350,0,0,2500]             

        nombre_gases=[]
        valor_gases=[]


        for i in VALOR_DEL_GAS:
            nombre_gases.append(i[0])
            valor_gases.append(i[1])

        X= np.arange(len(nombre_gases))
        
        Y1 = np.asarray(valor_gases)  
        Y2 = np.asarray(LIMITE_1)
     
                   
               
        f=plt.figure()
       
        plt.gca().set_yscale('log')

        bar_width = 0.02
        plt.bar(X-0.25, Y2, bar_width, color='r')
        bar_width = 0.45
        plt.bar(X, Y1, bar_width, color='b')

        

        SIMBOLO_GAS=["H2","CH4","C2H2","C2H4","C2H6","CO","O2","N2","CO2"]
      
        z=0 
        for x, y in zip(X, Y1):
            plt.text(x, y+1 ,str(y)+ "\n"+SIMBOLO_GAS[z], ha='center', va= 'bottom')
            z=z+1
 
      
        plt.xlabel('\nGases combustibles (H2,CH4,C2H2,C2H4,C2H6) +CO +O2 +N2 +CO2 ')
        plt.ylabel('Concentraciones de gas (ppm) ')
        titulo=""
        plt.title(titulo)
        plt.xticks(())

        subplots_adjust(left=0.21)
      

        buffer = io.BytesIO()
        canvas = pylab.get_current_fig_manager().canvas
        canvas.draw()        
        graphIMG = PIL.Image.fromstring('RGB', canvas.get_width_height(), canvas.tostring_rgb())
        graphIMG.save(buffer, "PNG")
        pylab.close()  

        f.clear()
        
        return HttpResponse (buffer.getvalue(), content_type="Image/png")

#

def ingreso_datos_dp(request):
     #!/usr/bin/python
        # -*- coding: latin-1 -*-        
        import os, sys
        if request.method == 'POST': # si el usuario est enviando el formulario con datos
                             
                    form = Mediciones_DPForm(request.POST,request.FILES)                      
                    
                    if form.is_valid() :
                           
                            temp = form.save(commit=False)
                            # commit=False tells Django that "Don't send this to database yet.
                            # I have more things I want to do with it."
                            
                            temp.fecha_ingreso=datetime.datetime.now()  
                            temp.codigo_usuario=request.user.username # Set the user object here    
                            temp.save() #  

                            form.save() # Guardar los datos en la base de datos  print 
                            #return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
                            connection.close()
                            return render(request,'confirmar.html',locals())                  
                

        else:            
                         
                         form=Mediciones_DPForm()

        connection.close()                  
        
        return render(request,'ingreso_datos_dp.html',locals())




def analisis_dp(request,central_x,generador_x):        
    
    centrales=Centrales.objects.all()
    try:
        usuario_comun=Usuarios.objects.get(codigo_usuario=request.user.username)
    except:
        pass
     
    lista_mediciones=Mediciones_DP.objects.filter(Q(central__nombre__icontains=central_x) &  Q(generador__codigo__icontains=generador_x)).order_by("fecha_del_analisis")
    identificador=lista_mediciones.first()  


   
    return render(request,'analisis_descargas_parciales.html',locals())


def grafico_tendencias_DP(request,central_x, generador_x):
        centrales=Centrales.objects.all()
        try:
            usuario_comun=Usuarios.objects.get(codigo_usuario=request.user.username)
        except:
            pass

        datos=Mediciones_DP.objects.filter(Q(central__nombre__icontains=central_x) &  Q(generador__codigo__icontains=generador_x)).order_by("fecha_del_analisis")
        
        fecha=datos.values_list("fecha_del_analisis", flat=True)     
        anios=[]
      
        for i in  fecha:
            an=i.strftime('%m%Y') 
            anios.append(an)


      
        X= np.arange(len(fecha))
       

        f=plt.figure()    
        f.set_size_inches(8,16)     


        PDI_C1_1=models.FloatField(default=0,blank=True,null=True)
        PDI_C1_2=models.FloatField(default=0,blank=True,null=True)

        PDI_C2_1=models.FloatField(default=0,blank=True,null=True)
        PDI_C2_2=models.FloatField(default=0,blank=True,null=True)

        PDI_C3_1=models.FloatField(default=0,blank=True,null=True)
        PDI_C3_2=models.FloatField(default=0,blank=True,null=True)


        PDI_C1_1=datos.values_list("PDI_C1_1", flat=True)
        PDI_C1_2=datos.values_list("PDI_C1_2", flat=True)
        PDI_C2_1=datos.values_list("PDI_C2_1", flat=True)
        PDI_C2_2=datos.values_list("PDI_C2_2", flat=True)
        PDI_C3_1=datos.values_list("PDI_C3_1", flat=True)
        PDI_C3_2=datos.values_list("PDI_C3_2", flat=True)         
                
        
        Y1 = np.asarray(PDI_C1_1)
        Y2 = np.asarray(PDI_C1_2)

        Y3 = np.asarray(PDI_C2_1)       
        Y4 = np.asarray(PDI_C2_2)

        Y5 = np.asarray(PDI_C3_1)       
        Y6 = np.asarray(PDI_C3_2)


        plt.subplot(7,1,1)
        titulo="PDI_C1_1 azul, PDI_C1_2 verde,  PDI_C2_1 rojo, \n PDI_C2_2 aqua, PDI_C3_1 morado, PDI_C3_2 negro \n en mW"
        plt.title(titulo)    

        plt.plot(anios,Y1,'bo-') 
        plt.plot(anios,Y2,'go-')
        plt.plot(anios,Y3,'ro-')
        plt.plot(anios,Y4,'co-')
        plt.plot(anios,Y5,'mo-')
        plt.plot(anios,Y6,'ko-')

        plt.xticks(())

        plt.grid() 
     

        frecuencia=datos.values_list("frecuencia", flat=True) 
        temperatura_promedio=datos.values_list("temperatura_promedio", flat=True) 
        
        plt.subplot(7,1,3)
        titulo="Tendencia frecuencia(HZ) verde, temperatura(`C) rojo"
        plt.title(titulo)    
        plt.plot(anios,frecuencia,'go-')
        plt.plot(anios,temperatura_promedio,'ro-')

        plt.xticks(())
        plt.grid()



        potencia_activa=datos.values_list("potencia_activa", flat=True) 
        potencia_reactiva=datos.values_list("potencia_reactiva", flat=True) 
        
        plt.subplot(7,1,5)
        titulo="Tendencia Pot Activa(MW) morado, Pot Reactiva (VAR) negro"
        plt.title(titulo)    
        plt.plot(anios,potencia_activa,'mo-')
        plt.plot(anios,potencia_reactiva,'ko-')

        plt.xticks(())
        plt.grid()
   

        PDI_C4_1=models.FloatField(default=0,blank=True,null=True)
        PDI_C4_2=models.FloatField(default=0,blank=True,null=True)

        PDI_C5_1=models.FloatField(default=0,blank=True,null=True)
        PDI_C5_2=models.FloatField(default=0,blank=True,null=True)

        PDI_C6_1=models.FloatField(default=0,blank=True,null=True)
        PDI_C6_2=models.FloatField(default=0,blank=True,null=True)


        PDI_C4_1=datos.values_list("PDI_C1_1", flat=True)
        PDI_C4_2=datos.values_list("PDI_C1_2", flat=True)
        PDI_C5_1=datos.values_list("PDI_C2_1", flat=True)
        PDI_C5_2=datos.values_list("PDI_C2_2", flat=True)
        PDI_C6_1=datos.values_list("PDI_C3_1", flat=True)
        PDI_C6_2=datos.values_list("PDI_C3_2", flat=True)         
       
                
        Y1 = np.asarray(PDI_C4_1)
        Y2 = np.asarray(PDI_C4_2)

        Y3 = np.asarray(PDI_C5_1)       
        Y4 = np.asarray(PDI_C5_2)

        Y5 = np.asarray(PDI_C6_1)       
        Y6 = np.asarray(PDI_C6_2)


        plt.subplot(7,1,7)
        titulo="PDI_C4_1 azul, PDI_C4_2 verde,  PDI_C5_1 rojo,\n PDI_C5_2 aqua, PDI_C6_1 morado, PDI_C6_2 negro \n en mW"
        plt.title(titulo)    

        plt.plot(anios,Y1,'bo-') 
        plt.plot(anios,Y2,'go-')
        plt.plot(anios,Y3,'ro-')
        plt.plot(anios,Y4,'co-')
        plt.plot(anios,Y5,'mo-')
        plt.plot(anios,Y6,'ko-')

        plt.xticks(())
        plt.grid()



        #plt.xticks(rotation='vertical',)
        plt.xticks(rotation='vertical',size="small")

      
        #titulo="Tendencia del las preferencias\n"+" fml "+str(fml)+ "%    "+  "gan "+str(gan)+ "%    "+"vamo "+str(vamo)+ "%    "+"alian "+str(aaa)+ "%" +  "NS+NR "+str(ns_nr)+ "%"
                             
        #subplots_adjust(left=0.21)      

        buffer = io.BytesIO()
        canvas = pylab.get_current_fig_manager().canvas
        canvas.draw()        
        graphIMG = PIL.Image.fromstring('RGB', canvas.get_width_height(), canvas.tostring_rgb())
        graphIMG.save(buffer, "PNG")
        pylab.close()  

        f.clear()
        
        return HttpResponse (buffer.getvalue(), content_type="Image/png")



def  ver_graficas_mensuales(request,id_imagen):
    centrales=Centrales.objects.all()
    try:
        usuario_comun=Usuarios.objects.get(codigo_usuario=request.user.username)
    except:
        pass
    datos_DP=Mediciones_DP.objects.filter(id=id_imagen).first()
    identificador=datos_DP

    return render(request,'graficas_del_mes.html',locals())


def analisis_termografico(request,sistema_x):
    centrales=Centrales.objects.all()  
    try:
        usuario_comun=Usuarios.objects.get(codigo_usuario=request.user.username)
    except:
        pass  
    termografias_x=Termografias.objects.filter(sistema_termografico__nombre__icontains=sistema_x).order_by("fecha_del_analisis").first()
    termografias=Termografias.objects.filter(sistema_termografico__nombre__icontains=sistema_x).order_by("fecha_del_analisis")
          
    return render(request,'analisis_termografico.html',locals())


def datos_prueba_DP(request):
    p1=Centrales.objects.get(nombre="CH 5 NOVIEMBRE")  

    date=datetime.datetime(2018,1,1,16,58) 
    p21=Generadores(central=p1,codigo="U1-CH5N-ELIM",marca="ELIM",modelo="C0848A",cararcteristicas="GENERADOR DE 20MW ",fecha_ingreso=date)
    p21.save()
      
    #ELIM U1
    #2018

    date=datetime.datetime(2018,1,11,16,58)
    p31=Mediciones_DP(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60 ,  potencia_activa=16.11, potencia_reactiva=2.0, temperatura_promedio=59.3, temperatura_calent=35, humedad_relativa=61, CAG="SI",
         PDI_C1_1=14.5,
         PDI_C1_2=0,
         PDI_C2_1=0,
         PDI_C2_2=0.1,
         PDI_C3_1=0,
         PDI_C3_2=0.1,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,          
         
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()
    

    date=datetime.datetime(2018,2,12,14,15)
    p31=Mediciones_DP(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60 ,  potencia_activa=15.9, potencia_reactiva=4.7, temperatura_promedio=63.6, temperatura_calent=33, humedad_relativa=57, CAG="SI",
         PDI_C1_1=17.5,
         PDI_C1_2=0,
         PDI_C2_1=0,
         PDI_C2_2=0.1,
         PDI_C3_1=0,
         PDI_C3_2=0.1,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
                  
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()


    date=datetime.datetime(2018,3,17,13,43)
    p31=Mediciones_DP(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60 ,  potencia_activa=17.47, potencia_reactiva=4.8, temperatura_promedio=66, temperatura_calent=35, humedad_relativa=63, CAG="SI",
         PDI_C1_1=11.9,
         PDI_C1_2=0,
         PDI_C2_1=0,
         PDI_C2_2=0.1,
         PDI_C3_1=0.1,
         PDI_C3_2=0.3,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
                 
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()


    date=datetime.datetime(2018,4,26,17,5)
    p31=Mediciones_DP(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60,  potencia_activa=15.06, potencia_reactiva=1.7, temperatura_promedio=36, temperatura_calent=35, humedad_relativa=71, CAG="SI",
         PDI_C1_1=8.2,
         PDI_C1_2=0,
         PDI_C2_1=0,
         PDI_C2_2=0,
         PDI_C3_1=0,
         PDI_C3_2=0.1,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
                
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()


    date=datetime.datetime(2018,5,3,14,20)
    p31=Mediciones_DP(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=59.99,  potencia_activa=16.51, potencia_reactiva=4.7, temperatura_promedio=66.38, temperatura_calent=37, humedad_relativa=67, CAG="SI",
         PDI_C1_1=8.6,
         PDI_C1_2=0,
         PDI_C2_1=0,
         PDI_C2_2=0,
         PDI_C3_1=0,
         PDI_C3_2=0.1,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()


    date=datetime.datetime(2018,6,1,14,34)
    p31=Mediciones_DP(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60,  potencia_activa=17.03, potencia_reactiva=0.2, temperatura_promedio=60.03, temperatura_calent=39, humedad_relativa=74, CAG="SI",
         PDI_C1_1=9.9,
         PDI_C1_2=0,
         PDI_C2_1=0,
         PDI_C2_2=0,
         PDI_C3_1=0,
         PDI_C3_2=0.1,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()


    date=datetime.datetime(2018,7,10,10,45)
    p31=Mediciones_DP(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60,  potencia_activa=18.14, potencia_reactiva=3.8, temperatura_promedio=68, temperatura_calent=32, humedad_relativa=77, CAG="SI",
         PDI_C1_1=10.9,
         PDI_C1_2=0,
         PDI_C2_1=0,
         PDI_C2_2=0,
         PDI_C3_1=0,
         PDI_C3_2=0.1,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
              
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()


    date=datetime.datetime(2018,8,13,14,27)
    p31=Mediciones_DP(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60.01,  potencia_activa=16.88, potencia_reactiva=1.8, temperatura_promedio=64.62, temperatura_calent=37, humedad_relativa=75, CAG="SI",
         PDI_C1_1=138.6,
         PDI_C1_2=19.4,
         PDI_C2_1=46.8,
         PDI_C2_2=0,
         PDI_C3_1=16.3,
         PDI_C3_2=39.7,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
                  
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()


    date=datetime.datetime(2018,9,17,13,15)
    p31=Mediciones_DP(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60.01,  potencia_activa=16.94, potencia_reactiva=3.6, temperatura_promedio=66.01, temperatura_calent=35, humedad_relativa=78, CAG="SI",
         PDI_C1_1=125.2,
         PDI_C1_2=27.4,
         PDI_C2_1=17.3,
         PDI_C2_2=23.1,
         PDI_C3_1=56.3,
         PDI_C3_2=35,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
              
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()


    date=datetime.datetime(2018,10,3,13,23)
    p31=Mediciones_DP(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60,  potencia_activa=18.6, potencia_reactiva=3.6, temperatura_promedio=67.8, temperatura_calent=35, humedad_relativa=75, CAG="SI",
         PDI_C1_1=150.1,
         PDI_C1_2=47.5,
         PDI_C2_1=24.5,
         PDI_C2_2=38.3,
         PDI_C3_1=65,
         PDI_C3_2=32.6,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
           
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()


    date=datetime.datetime(2018,11,5,10,46)
    p31=Mediciones_DP(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=59.95,  potencia_activa=19.06, potencia_reactiva=3.9, temperatura_promedio=68.43, temperatura_calent=34, humedad_relativa=75, CAG="SI",
         PDI_C1_1=155.7,
         PDI_C1_2=26.9,
         PDI_C2_1=23.5,
         PDI_C2_2=41,
         PDI_C3_1=72.6,
         PDI_C3_2=36.3,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
                  
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

    date=datetime.datetime(2018,12,7,9,50)
    p31=Mediciones_DP(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60,  potencia_activa=14.9, potencia_reactiva=4.2, temperatura_promedio=59.4, temperatura_calent=34, humedad_relativa=70, CAG="SI",
         PDI_C1_1=155.7,
         PDI_C1_2=26.9,
         PDI_C2_1=23.5,
         PDI_C2_2=41,
         PDI_C3_1=72.6,
         PDI_C3_2=36.3,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
                  
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

    date=datetime.datetime(2019,1,7,9,56)
    p31=Mediciones_DP(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60.01,  potencia_activa=14.9, potencia_reactiva=4.2, temperatura_promedio=59.2, temperatura_calent=32, humedad_relativa=68, CAG="SI",
         PDI_C1_1=100.7,
         PDI_C1_2=15.1,
         PDI_C2_1=20.9,
         PDI_C2_2=43,
         PDI_C3_1=58.9,
         PDI_C3_2=39.2,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
                  
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

    date=datetime.datetime(2019,2,4,15,1)
    p31=Mediciones_DP(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=59.98,  potencia_activa=19.01, potencia_reactiva=0.9, temperatura_promedio=66, temperatura_calent=35, humedad_relativa=56, CAG="SI",
         PDI_C1_1=149.3,
         PDI_C1_2=34.5,
         PDI_C2_1=40.4,
         PDI_C2_2=40.9,
         PDI_C3_1=42.9,
         PDI_C3_2=28.7,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
                  
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

    date=datetime.datetime(2019,3,6,15,50)
    p31=Mediciones_DP(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60,  potencia_activa=17.76, potencia_reactiva=4.3, temperatura_promedio=45, temperatura_calent=71.28, humedad_relativa=56, CAG="SI",
         PDI_C1_1=158.7,
         PDI_C1_2=52.3,
         PDI_C2_1=88,
         PDI_C2_2=62.5,
         PDI_C3_1=95,
         PDI_C3_2=62.4,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
                  
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

    date=datetime.datetime(2019,4,8,10,41)
    p31=Mediciones_DP(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60.01,  potencia_activa=16.66, potencia_reactiva=3.2, temperatura_promedio=43, temperatura_calent=65.63, humedad_relativa=62, CAG="SI",
         PDI_C1_1=196.7,
         PDI_C1_2=52.4,
         PDI_C2_1=49.6,
         PDI_C2_2=39.4,
         PDI_C3_1=66.3,
         PDI_C3_2=57.5,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
                  
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()























#///////////////////////////////////////////////////
    #PRUEBAS DE DESCARGAS PARCIALES PARA LA UNIDAD 2 ///
    #///////////////////////////////////////////////////
    date=datetime.datetime(2018,1,1,16,58) 
    p21=Generadores(central=p1,codigo="U2-CH5N-ELIM",marca="ELIM",modelo="C0848A",cararcteristicas="GENERADOR 20MW",fecha_ingreso=date)
    p21.save()
      
    #ELIM U2
    #2018

    date=datetime.datetime(2018,1,11, 14,50)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60 ,  potencia_activa=13.35, potencia_reactiva=5.52, temperatura_promedio=71.6, temperatura_calent=36, humedad_relativa=63, CAG="SI",
         PDI_C1_1=0.3,
         PDI_C1_2=0,
         PDI_C2_1=0.1,
         PDI_C2_2=0.2,
         PDI_C3_1=0.1,
         PDI_C3_2=0,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

    date=datetime.datetime(2018,2,7, 10,9)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60 ,  potencia_activa=17.1, potencia_reactiva=2, temperatura_promedio=66.2, temperatura_calent=33, humedad_relativa=68, CAG="SI",
         PDI_C1_1=0.1,
         PDI_C1_2=0,
         PDI_C2_1=0.1,
         PDI_C2_2=0.1,
         PDI_C3_1=0,
         PDI_C3_2=0,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

    date=datetime.datetime(2018,3,17, 13,53)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60 ,  potencia_activa=16.55, potencia_reactiva=4.7, temperatura_promedio=73.12, temperatura_calent=35, humedad_relativa=68, CAG="SI",
         PDI_C1_1=0,
         PDI_C1_2=0,
         PDI_C2_1=0,
         PDI_C2_2=0,
         PDI_C3_1=0,
         PDI_C3_2=0.4,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()


    date=datetime.datetime(2018,4,26, 14,10)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60 ,  potencia_activa=15.08, potencia_reactiva=4.6, temperatura_promedio=76.24, temperatura_calent=33, humedad_relativa=68, CAG="SI",
         PDI_C1_1=0,
         PDI_C1_2=0,,
         PDI_C2_1=0,
         PDI_C2_2=0,
         PDI_C3_1=0,
         PDI_C3_2=0.4,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()


    date=datetime.datetime(2018,5,06, 9,10)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=59.9 ,  potencia_activa=15.81, potencia_reactiva=4.96, temperatura_promedio=71.94, temperatura_calent=37, humedad_relativa=74, CAG="SI",
         PDI_C1_1=0.1,
         PDI_C1_2=0,
         PDI_C2_1=0.2,
         PDI_C2_2=0.2,
         PDI_C3_1=0,
         PDI_C3_2=0,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0, 
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()



    date=datetime.datetime(2018,6,01, 15,57)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60 ,  potencia_activa=17.18, potencia_reactiva=0.3, temperatura_promedio=69.4, temperatura_calent=36, humedad_relativa=75, CAG="SI",
         PDI_C1_1=0.1,
         PDI_C1_2=0,
         PDI_C2_1=0,
         PDI_C2_2=0.1,
         PDI_C3_1=0,
         PDI_C3_2=0.6,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

    date=datetime.datetime(2018,7,01, 15,57)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60 ,  potencia_activa=17.18, potencia_reactiva=0.3, temperatura_promedio=69.4, temperatura_calent=36, humedad_relativa=75, CAG="SI",
         PDI_C1_1=0.1,
         PDI_C1_2=0,
         PDI_C2_1=0,
         PDI_C2_2=0.1,
         PDI_C3_1=0,
         PDI_C3_2=0.6,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

    date=datetime.datetime(2018,8,13, 13,44)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         PDI_C1_1=1.6,
         PDI_C1_2=3,
         PDI_C2_1=4.4,
         PDI_C2_2=3.1,
         PDI_C3_1=1.9,
         PDI_C3_2=11.2,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()





    date=datetime.datetime(2018,9,17, 13,26)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=59.95 ,  potencia_activa=16.2, potencia_reactiva=5, temperatura_promedio=79.4, temperatura_calent=40, humedad_relativa=78, CAG="SI",
         PDI_C1_1=9.8,
         PDI_C1_2=1,
         PDI_C2_1=5.4,
         PDI_C2_2=5.5,
         PDI_C3_1=3.8,
         PDI_C3_2=9.5,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()





    date=datetime.datetime(2018,10,15, 11,2)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60 ,  potencia_activa=15.16, potencia_reactiva=4.9, temperatura_promedio=76.63, temperatura_calent=37, humedad_relativa=78, CAG="SI",
         PDI_C1_1=2.7,
         PDI_C1_2=0.6,
         PDI_C2_1=1.9,
         PDI_C2_2=1.5,
         PDI_C3_1=1.1,
         PDI_C3_2=0.8,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()


    date=datetime.datetime(2018,11,5, 10,55)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=56.96 ,  potencia_activa=19.03, potencia_reactiva=4.8, temperatura_promedio=77.99, temperatura_calent=0, humedad_relativa=75, CAG="SI",
         PDI_C1_1=6,
         PDI_C1_2=0.8,
         PDI_C2_1=2.1,
         PDI_C2_2=2.4,
         PDI_C3_1=1.3,
         PDI_C3_2=7.8,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()


    date=datetime.datetime(2018,12,7, 9,5)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=56.96 ,  potencia_activa=19.03, potencia_reactiva=4.8, temperatura_promedio=77.99, temperatura_calent=0, humedad_relativa=75, CAG="SI",
         PDI_C1_1=7.5,
         PDI_C1_2=5.3,
         PDI_C2_1=16.6,
         PDI_C2_2=8.8,
         PDI_C3_1=17,
         PDI_C3_2=16.3,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

    date=datetime.datetime(2019,1,7,13,27)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60.03 ,  potencia_activa=16.02, potencia_reactiva=5, temperatura_promedio=68, temperatura_calent=32, humedad_relativa=63, CAG="SI",
         PDI_C1_1=22.01,
         PDI_C1_2=0,
         PDI_C2_1=9.5,
         PDI_C2_2=4,
         PDI_C3_1=9.4,
         PDI_C3_2=0.6,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

    date=datetime.datetime(2019,2,4, 14,9)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=59.99 ,  potencia_activa=18.91, potencia_reactiva=4.1, temperatura_promedio=83.11, temperatura_calent=35, humedad_relativa=56, CAG="SI",
         PDI_C1_1=9.3,
         PDI_C1_2=1.5,
         PDI_C2_1=5,
         PDI_C2_2=5.4,
         PDI_C3_1=9.6,
         PDI_C3_2=0.1,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

    date=datetime.datetime(2019,3,11,13,51)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=59.99 ,  potencia_activa=18.6, potencia_reactiva=4.2, temperatura_promedio=78.79, temperatura_calent=47, humedad_relativa=52, CAG="SI",
         PDI_C1_1=19.4,
         PDI_C1_2=1.7,
         PDI_C2_1=11.4,
         PDI_C2_2=6.5,
         PDI_C3_1=15.7,
         PDI_C3_2=3.1,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

    date=datetime.datetime(2019,4,23, 17,37)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60.01 ,  potencia_activa=15.79, potencia_reactiva=3.1, temperatura_promedio=75.75, temperatura_calent=47, humedad_relativa=65, CAG="SI",
         PDI_C1_1=6.9,
         PDI_C1_2=0.6,
         PDI_C2_1=4.7,
         PDI_C2_2=3.4,
         PDI_C3_1=4.9,
         PDI_C3_2=3.4,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

   









    date=datetime.datetime(2018,1,1,16,58) 
    p21=Generadores(central=p1,codigo="U3-CH5N-ELIM",marca="ELIM",modelo="C0848A",cararcteristicas="GENERADOR 20MW",fecha_ingreso=date)
    p21.save()
      
    #ELIM U3
    #2017

    date=datetime.datetime(2018,01,11, 17,5)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60 ,  potencia_activa=15.76, potencia_reactiva=1.2, temperatura_promedio=73.6, temperatura_calent=35, humedad_relativa=61, CAG="SI",
         PDI_C1_1=0.9,
         PDI_C1_2=0,
         PDI_C2_1=0,
         PDI_C2_2=1.6,
         PDI_C3_1=0.5,
         PDI_C3_2=2.1,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

    date=datetime.datetime(2018,02,27, 9,8)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60 ,  potencia_activa=12.15, potencia_reactiva=4.3, temperatura_promedio=57.1, temperatura_calent=30, humedad_relativa=72, CAG="SI",
         PDI_C1_1=0,
         PDI_C1_2=0,
         PDI_C2_1=0,
         PDI_C2_2=1.2,
         PDI_C3_1=0.5,
         PDI_C3_2=1.7,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()


    #ELIM U3
    #2018

    date=datetime.datetime(2018,03,11, 20,11)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60 ,  potencia_activa=18.21, potencia_reactiva=4.7, temperatura_promedio=63.38, temperatura_calent=65, humedad_relativa=32, CAG="SI",
         PDI_C1_1=0,
         PDI_C1_2=0,
         PDI_C2_1=0,
         PDI_C2_2=1.2,
         PDI_C3_1=0.5,
         PDI_C3_2=1.7,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()


    date=datetime.datetime(2018,04,26, 13,52)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60 ,  potencia_activa=15.6, potencia_reactiva=4.8, temperatura_promedio=62.76, temperatura_calent=33, humedad_relativa=37, CAG="SI",
         PDI_C1_1=1.2,
         PDI_C1_2=0,
         PDI_C2_1=0,
         PDI_C2_2=1.2,
         PDI_C3_1=2,
         PDI_C3_2=0,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0, 
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

    date=datetime.datetime(2018,05,06, 9,22)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60 ,  potencia_activa=10.8, potencia_reactiva=5, temperatura_promedio=58.4, temperatura_calent=33, humedad_relativa=79, CAG="SI",
         PDI_C1_1=1,
         PDI_C1_2=0,
         PDI_C2_1=0,
         PDI_C2_2=0.8,
         PDI_C3_1=0,
         PDI_C3_2=17,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0, 
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

    date=datetime.datetime(2018,06,06, 8,23)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60 ,  potencia_activa=15.49, potencia_reactiva=3.8, temperatura_promedio=60.47, temperatura_calent=42, humedad_relativa=70, CAG="SI",
         PDI_C1_1=0,
         PDI_C1_2=0,
         PDI_C2_1=0,
         PDI_C2_2=0.8,
         PDI_C3_1=0.2,
         PDI_C3_2=1.2,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

    date=datetime.datetime(2018,07,06, 8,23)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60 ,  potencia_activa=15.49, potencia_reactiva=3.8, temperatura_promedio=60.47, temperatura_calent=42, humedad_relativa=70, CAG="SI",
         PDI_C1_1=0,
         PDI_C1_2=0,
         PDI_C2_1=0,
         PDI_C2_2=0.8,
         PDI_C3_1=0.2,
         PDI_C3_2=1.2,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()
    date=datetime.datetime(2018,8,13, 14,51)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60.02 ,  potencia_activa=17.34, potencia_reactiva=1.5, temperatura_promedio=63.28, temperatura_calent=37.5, humedad_relativa=75, CAG="SI",
         PDI_C1_1=19.7,
         PDI_C1_2=4.3,
         PDI_C2_1=2.6,
         PDI_C2_2=0,
         PDI_C3_1=2.8,
         PDI_C3_2=12.1,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()


    date=datetime.datetime(2018,9,17, 13,37)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=59.96,  potencia_activa=16.85, potencia_reactiva=4.7, temperatura_promedio=65.78, temperatura_calent=34.5, humedad_relativa=78, CAG="SI",
         PDI_C1_1=20.3,
         PDI_C1_2=3.2,
         PDI_C2_1=0.4,
         PDI_C2_2=24.1,
         PDI_C3_1=2.5,
         PDI_C3_2=8.8,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()





    date=datetime.datetime(2018,10,8, 13,45)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60 ,  potencia_activa=12.48, potencia_reactiva=5.1, temperatura_promedio=58.3, temperatura_calent=33, humedad_relativa=80, CAG="SI",
         PDI_C1_1=17.6,
         PDI_C1_2=2.2,
         PDI_C2_1=11.7,
         PDI_C2_2=3,
         PDI_C3_1=2.8,
         PDI_C3_2=4.3,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

    date=datetime.datetime(2018,11,05, 13,30)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=59.95 ,  potencia_activa=15.09, potencia_reactiva=4.8, temperatura_promedio=58.43, temperatura_calent=0, humedad_relativa=75, CAG="SI",
         PDI_C1_1=18.2,
         PDI_C1_2=3.7,
         PDI_C2_1=0.7,
         PDI_C2_2=17.9,
         PDI_C3_1=2.6,
         PDI_C3_2=6.9,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

    date=datetime.datetime(2018,12,7, 10,5)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60.01 ,  potencia_activa=14.9, potencia_reactiva=4.9, temperatura_promedio=56.6, temperatura_calent=34, humedad_relativa=70, CAG="SI",
         PDI_C1_1=16,
         PDI_C1_2=1.7,
         PDI_C2_1=0.6,
         PDI_C2_2=3.5,
         PDI_C3_1=1.4,
         PDI_C3_2=9.1,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

    date=datetime.datetime(2019,1,7, 14,14)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60.01,  potencia_activa=16.3, potencia_reactiva=1.3, temperatura_promedio=56.3, temperatura_calent=31, humedad_relativa=61, CAG="SI",
         PDI_C1_1=12.2,
         PDI_C1_2=7.5,
         PDI_C2_1=0.2,
         PDI_C2_2=7,
         PDI_C3_1=1.5,
         PDI_C3_2=7,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

    date=datetime.datetime(2019,2,3, 14,41)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=59.98 ,  potencia_activa=18.92, potencia_reactiva=3.8, temperatura_promedio=68.48, temperatura_calent=36, humedad_relativa=56, CAG="SI",
         PDI_C1_1=11.9,
         PDI_C1_2=1.2,
         PDI_C2_1=5.8,
         PDI_C2_2=6,
         PDI_C3_1=1.1,
         PDI_C3_2=8.7,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

    date=datetime.datetime(2019,3,3, 13,19)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=59.98 ,  potencia_activa=19.63, potencia_reactiva=3.4, temperatura_promedio=68.15, temperatura_calent=42, humedad_relativa=50, CAG="SI",
         PDI_C1_1=17.2,
         PDI_C1_2=2.1,
         PDI_C2_1=5.2,
         PDI_C2_2=6.2,
         PDI_C3_1=1.6,
         PDI_C3_2=7.6,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

    date=datetime.datetime(2019,4,8, 11,05)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60.01 ,  potencia_activa=16.34, potencia_reactiva=1.9, temperatura_promedio=63.67, temperatura_calent=42, humedad_relativa=60, CAG="SI",
         PDI_C1_1=15.6,
         PDI_C1_2=1.7,
         PDI_C2_1=0,
         PDI_C2_2=11.2,
         PDI_C3_1=1.4,
         PDI_C3_2=8.4,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()
















    date=datetime.datetime(2018,1,1,16,58)
    p21=Generadores(central=p1,codigo="U4-CH5N-ELIM",marca="ELIM",modelo="C0848A",cararcteristicas="GENERADOR 20MW",fecha_ingreso=date)
    p21.save()
      
    #ELIM U4
    #2017

    date=datetime.datetime(2018,01,11, 17,47)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60 ,  potencia_activa=15.76, potencia_reactiva=2.1, temperatura_promedio=64.7, temperatura_calent=32, humedad_relativa=74, CAG="SI",
         PDI_C1_1=0.2,
         PDI_C1_2=0,
         PDI_C2_1=0,
         PDI_C2_2=0.2,
         PDI_C3_1=7.3,
         PDI_C3_2=11.7,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,   
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

    date=datetime.datetime(2018,02,21, 17,47)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60 ,  potencia_activa=17.79, potencia_reactiva=1.8, temperatura_promedio=66.2, temperatura_calent=33, humedad_relativa=68, CAG="SI",
         PDI_C1_1=0.3,
         PDI_C1_2=0,
         PDI_C2_1=0.1,
         PDI_C2_2=0.5,
         PDI_C3_1=4.4,
         PDI_C3_2=9.8,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,  
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()


    date=datetime.datetime(2018,03,21, 17,47)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60 ,  potencia_activa=17.79, potencia_reactiva=1.8, temperatura_promedio=66.2, temperatura_calent=33, humedad_relativa=68, CAG="SI",
         PDI_C1_1=0.3,
         PDI_C1_2=0,
         PDI_C2_1=0.1,
         PDI_C2_2=0.5,
         PDI_C3_1=4.4,
         PDI_C3_2=9.8,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,  
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()




    date=datetime.datetime(2018,04,26, 14,0)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60 ,  potencia_activa=14.2, potencia_reactiva=5.2, temperatura_promedio=72.4, temperatura_calent=36, humedad_relativa=76, CAG="SI",
         PDI_C1_1=0.2,
         PDI_C1_2=0,
         PDI_C2_1=0,
         PDI_C2_2=0,
         PDI_C3_1=3.1,
         PDI_C3_2=8.3,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()


    date=datetime.datetime(2018,05,12, 13,31)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=59.99,  potencia_activa=13.64, potencia_reactiva=1.7, temperatura_promedio=68.62, temperatura_calent=40, humedad_relativa=79, CAG="SI",
         PDI_C1_1=0.1,
         PDI_C1_2=0,
         PDI_C2_1=0,
         PDI_C2_2=0,
         PDI_C3_1=3.1,
         PDI_C3_2=7.7,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0, 
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

    date=datetime.datetime(2018,06,06, 8,46)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60,  potencia_activa=12.78, potencia_reactiva=3.2, temperatura_promedio=69.73, temperatura_calent=42, humedad_relativa=70, CAG="SI",
         PDI_C1_1=0,
         PDI_C1_2=0,
         PDI_C2_1=0,
         PDI_C2_2=0.3,
         PDI_C3_1=3.1,
         PDI_C3_2=7.9,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

    date=datetime.datetime(2018,07,07, 8,46)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60,  potencia_activa=12.78, potencia_reactiva=3.2, temperatura_promedio=69.73, temperatura_calent=42, humedad_relativa=70, CAG="SI",
         PDI_C1_1=0,
         PDI_C1_2=0,
         PDI_C2_1=0,
         PDI_C2_2=0.3,
         PDI_C3_1=3.1,
         PDI_C3_2=7.9,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()


    date=datetime.datetime(2018,8,21, 10,14)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=59.98,  potencia_activa=13.15, potencia_reactiva=1.7, temperatura_promedio=66.13, temperatura_calent=34, humedad_relativa=79, CAG="SI",
         PDI_C1_1=31,
         PDI_C1_2=2.6,
         PDI_C2_1=23.6,
         PDI_C2_2=0.3,
         PDI_C3_1=23.4,
         PDI_C3_2=67.3,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()


    date=datetime.datetime(2018,9,11, 16,9)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60,  potencia_activa=11.76, potencia_reactiva=3.8, temperatura_promedio=70.16, temperatura_calent=37, humedad_relativa=80, CAG="SI",
         PDI_C1_1=40.3,
         PDI_C1_2=20.5,
         PDI_C2_1=18.4,
         PDI_C2_2=11.6,
         PDI_C3_1=36.2,
         PDI_C3_2=96.9,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()





    date=datetime.datetime(2018,10,15, 11,11)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60,  potencia_activa=11.7, potencia_reactiva=4.4, temperatura_promedio=70.3, temperatura_calent=36, humedad_relativa=90, CAG="SI",
         PDI_C1_1=42.7,
         PDI_C1_2=0.6,
         PDI_C2_1=18.1,
         PDI_C2_2=13.8,
         PDI_C3_1=30.1,
         PDI_C3_2=99.7,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

    date=datetime.datetime(2018,11,05, 13,38)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60,  potencia_activa=13.08, potencia_reactiva=4.2, temperatura_promedio=70.69, temperatura_calent=0, humedad_relativa=75, CAG="SI",
         PDI_C1_1=46.6,
         PDI_C1_2=3.6,
         PDI_C2_1=28.6,
         PDI_C2_2=18.1,
         PDI_C3_1=36.2,
         PDI_C3_2=120.7,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)

    date=datetime.datetime(2018,12,12, 10,18)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60,  potencia_activa=13.9, potencia_reactiva=4.7, temperatura_promedio=65, temperatura_calent=34, humedad_relativa=72, CAG="SI",
         PDI_C1_1=35.6,
         PDI_C1_2=1,
         PDI_C2_1=11.5,
         PDI_C2_2=11.1,
         PDI_C3_1=31.7,
         PDI_C3_2=106.9,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

    date=datetime.datetime(2019,1,7, 13,38)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60,  potencia_activa=13.71, potencia_reactiva=4.7, temperatura_promedio=66.5, temperatura_calent=34, humedad_relativa=66.05, CAG="SI",
         PDI_C1_1=17.8,
         PDI_C1_2=23.3,
         PDI_C2_1=28.8,
         PDI_C2_2=14.1,
         PDI_C3_1=34.8,
         PDI_C3_2=132.1,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

    date=datetime.datetime(2019,2,4, 14,51)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60.02,  potencia_activa=16, potencia_reactiva=2.9, temperatura_promedio=77.07, temperatura_calent=36, humedad_relativa=56, CAG="SI",
         PDI_C1_1=79,
         PDI_C1_2=2.6,
         PDI_C2_1=34.3,
         PDI_C2_2=11.3,
         PDI_C3_1=48.3,
         PDI_C3_2=162.6,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

    date=datetime.datetime(2019,3,26, 14,51)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60.02,  potencia_activa=14.2, potencia_reactiva=3, temperatura_promedio=70.79, temperatura_calent=47, humedad_relativa=33, CAG="SI",
         PDI_C1_1=67.9,
         PDI_C1_2=2.9,
         PDI_C2_1=33.3,
         PDI_C2_2=16.8,
         PDI_C3_1=45.9,
         PDI_C3_2=130.1,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

    date=datetime.datetime(2019,4,1, 14,16)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60,  potencia_activa=15.94, potencia_reactiva=1.8, temperatura_promedio=76.91, temperatura_calent=46.9, humedad_relativa=60, CAG="SI",
         PDI_C1_1=63.9,
         PDI_C1_2=3.7,
         PDI_C2_1=35.4,
         PDI_C2_2=15,
         PDI_C3_1=65.2,
         PDI_C3_2=129.7,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0,
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()










#///////////////////////////////////////////////////
    #PRUEBAS DE DESCARGAS PARCIALES PARA LA UNIDAD 6 ///
    #///////////////////////////////////////////////////
    date=datetime.datetime(2018,1,1,16,58) 
    p21=Generadores(central=p1,codigo="U6-CH5N-ANDRITZ",marca="ANDRITZ HYDRO",modelo="NA",cararcteristicas="GENERADOR 40 MB",fecha_ingreso=date)
    p21.save()
      
    #ELIM U6
    #2017
    
    date=datetime.datetime(2019,1,21, 13,10)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60 ,  potencia_activa=40.03, potencia_reactiva=4.7, temperatura_promedio=0, temperatura_calent=0, humedad_relativa=0, CAG="SI",
         PDI_C1_1=0,
         PDI_C1_2=0,
         PDI_C2_1=0,
         PDI_C2_2=0,
         PDI_C3_1=0,
         PDI_C3_2=0,
         PDI_C4_1=0,
         PDI_C4_2=0,
         PDI_C5_1=0,
         PDI_C5_2=0,
         PDI_C6_1=0,
         PDI_C6_2=0, 
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()


    #ELIM U6
    #2018

    date=datetime.datetime(2019,02,19, 9,1)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60.02 ,  potencia_activa=38.21, potencia_reactiva=4.4, temperatura_promedio=76.24, temperatura_calent=0, humedad_relativa=0, CAG="SI",
         PDI_C1_1=1.2,
         PDI_C1_2=0,
         PDI_C2_1=6.2,
         PDI_C2_2=0.5,
         PDI_C3_1=6,
         PDI_C3_2=3.2,
         PDI_C4_1=4.3,
         PDI_C4_2=4,
         PDI_C5_1=17.2,
         PDI_C5_2=8.5,
         PDI_C6_1=13.5,
         PDI_C6_2=12.6,         
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

    date=datetime.datetime(2019,03,21, 7,55)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60.02 ,  potencia_activa=38.21, potencia_reactiva=4.4, temperatura_promedio=76.45, temperatura_calent=0, humedad_relativa=0, CAG="SI",
         PDI_C1_1=5.6,
         PDI_C1_2=2.7,
         PDI_C2_1=16.4,
         PDI_C2_2=14.4,
         PDI_C3_1=16.5,
         PDI_C3_2=12.8,
         PDI_C4_1=1.3,
         PDI_C4_2=0,
         PDI_C5_1=2,
         PDI_C5_2=1.5,
         PDI_C6_1=5.9,
         PDI_C6_2=4,         
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

    date=datetime.datetime(2019,04,23, 18,41)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60 ,  potencia_activa=39.14, potencia_reactiva=1.73, temperatura_promedio=77.45, temperatura_calent=0, humedad_relativa=0, CAG="SI",
         PDI_C1_1=6.7,
         PDI_C1_2=3.8,
         PDI_C2_1=17.9,
         PDI_C2_2=11,
         PDI_C3_1=16.8,
         PDI_C3_2=15.4,
         PDI_C4_1=3.8,
         PDI_C4_2=0,
         PDI_C5_1=7.9,
         PDI_C5_2=1.3,
         PDI_C6_1=7.9,
         PDI_C6_2=3.7,         
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()









      #///////////////////////////////////////////////////
      #PRUEBAS DE DESCARGAS PARCIALES PARA LA UNIDAD 7 ///
      #///////////////////////////////////////////////////
    date=datetime.datetime(2018,1,1,16,58) 
    p21=Generadores(central=p1,codigo="U7-CH5N-ANDRITZ",marca="ANDRITZ HYDRO",modelo="NA",cararcteristicas="GENERADOR 40 MW",fecha_ingreso=date)
    p21.save()
      
    #ELIM U7    
    #2017

    date=datetime.datetime(2019,01,29, 17,41)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60 ,  potencia_activa=25.50, potencia_reactiva=-1.68, temperatura_promedio=75.17, temperatura_calent=0, humedad_relativa=0, CAG="SI",
         PDI_C1_1=1,
         PDI_C1_2=0,
         PDI_C2_1=5.6,
         PDI_C2_2=1.4,
         PDI_C3_1=7.8,
         PDI_C3_2=6.2,
         PDI_C4_1=4.3,
         PDI_C4_2=12.2,
         PDI_C5_1=15.9,
         PDI_C5_2=19.6,
         PDI_C6_1=43,
         PDI_C6_2=17.5,      
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

#ELIM U7  
    #2018
    date=datetime.datetime(2019,02,27, 20,18)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60 ,  potencia_activa=34.75, potencia_reactiva=1.98, temperatura_promedio=79.12, temperatura_calent=0, humedad_relativa=0, CAG="SI",
         PDI_C1_1=3.2,
         PDI_C1_2=0,
         PDI_C2_1=2.1,
         PDI_C2_2=1,
         PDI_C3_1=5.3,
         PDI_C3_2=5.1,
         PDI_C4_1=1.3,
         PDI_C4_2=9.3,
         PDI_C5_1=15.2,
         PDI_C5_2=15.3,
         PDI_C6_1=36.2,
         PDI_C6_2=16.1,         
         fecha_ingreso=date,fecha_del_analisis=date)          
    p31.save()


    date=datetime.datetime(2019,03,19, 14,5)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60 ,  potencia_activa=37.37, potencia_reactiva=1.96, temperatura_promedio=79.12, temperatura_calent=0, humedad_relativa=0, CAG="SI",
         PDI_C1_1=4.4,
         PDI_C1_2=9.4,
         PDI_C2_1=15.2,
         PDI_C2_2=20.4,
         PDI_C3_1=43.4,
         PDI_C3_2=18.3,
         PDI_C4_1=8.4,
         PDI_C4_2=0.3,
         PDI_C5_1=3.8,
         PDI_C5_2=1.9,
         PDI_C6_1=6.6,
         PDI_C6_2=5.9,         
         fecha_ingreso=date,fecha_del_analisis=date)          
    p31.save()

    date=datetime.datetime(2019,04,24, 19,46)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=59.96 ,  potencia_activa=35.93, potencia_reactiva=2.42, temperatura_promedio=79.93, temperatura_calent=0, humedad_relativa=0, CAG="SI",
         PDI_C1_1=6.4,
         PDI_C1_2=13.8,
         PDI_C2_1=19.3,
         PDI_C2_2=23,
         PDI_C3_1=44.6,
         PDI_C3_2=19.2,
         PDI_C4_1=9.1,
         PDI_C4_2=0.2,
         PDI_C5_1=5.6,
         PDI_C5_2=2.1,
         PDI_C6_1=10.2,
         PDI_C6_2=6.3,         
         fecha_ingreso=date,fecha_del_analisis=date)          
    p31.save()

    #///////////////////////////////////////////////////
    #PRUEBAS DE DESCARGAS PARCIALE

    return render(request,'principal.html',locals())