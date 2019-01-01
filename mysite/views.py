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

def informacion(request):
  centrales=Centrales.objects.all()
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
                            temp_agregada.save() #  

                            form.save() # Guardar los datos en la base de datos  print 
                            #return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
                            connection.close()
                            return render(request,'confirmar.html',locals())                  
                

        else:            
                         
                         form=MedicionesForm()

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
    p31=Mediciones(central=p1,transformador=p21,codigo_usuario="7807004",Hidrogeno=3,Oxigeno=0,Nitrogeno=0,Metano=1,Monoxido_de_carbono=4,Etano=1,Dioxido_de_carbono=203.41,Etileno=0.17,Acetileno=0.7,fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()
    #2015
    date=datetime.datetime(2015,6,30)
    p32=Mediciones(central=p1,transformador=p21,codigo_usuario="7807004",Hidrogeno=5.38,Oxigeno=29.92,Nitrogeno=36320,Metano=8.8,Monoxido_de_carbono=4.97,Etano=2.1,Dioxido_de_carbono=926,Etileno=0.68,Acetileno=1.2,fecha_ingreso=date,fecha_del_analisis=date)
    p32.save()
    #2016
    date=datetime.datetime(2016,6,30)
    p33=Mediciones(central=p1,transformador=p21,codigo_usuario="7807004",Hidrogeno=2,Oxigeno=0,Nitrogeno=0,Metano=50,Monoxido_de_carbono=137,Etano=67,Dioxido_de_carbono=2010,Etileno=5,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date)
    p33.save()
    #2017
    date=datetime.datetime(2017,6,30)
    p34=Mediciones(central=p1,transformador=p21,codigo_usuario="7807004",Hidrogeno=5,Oxigeno=0,Nitrogeno=0,Metano=57,Monoxido_de_carbono=155,Etano=79,Dioxido_de_carbono=2037,Etileno=10,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date)
    p34.save()
    #2018
    date=datetime.datetime(2018,6,30)
    p35=Mediciones(central=p1,transformador=p21,codigo_usuario="7807004",Hidrogeno=15,Oxigeno=0,Nitrogeno=0,Metano=89,Monoxido_de_carbono=159,Etano=134,Dioxido_de_carbono=2308,Etileno=12,Acetileno=3,fecha_ingreso=date,fecha_del_analisis=date)
    p35.save()





    p22=Transformadores(central=p1,codigo="33562",marca="TUBOS TRRANS ELECTRIC",modelo="NA",cararcteristicas="U2",fecha_ingreso=date)
    p22.save()
    #2010
    date=datetime.datetime(2010,6,30)
    p31=Mediciones(central=p1,transformador=p22,codigo_usuario="7807004",Hidrogeno=5,Oxigeno=0,Nitrogeno=0,Metano=4,Monoxido_de_carbono=132,Etano=12,Dioxido_de_carbono=2027,Etileno=25,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()
    #2012
    date=datetime.datetime(2012,6,30)
    p32=Mediciones(central=p1,transformador=p22,codigo_usuario="7807004",Hidrogeno=24,Oxigeno=0,Nitrogeno=0,Metano=7,Monoxido_de_carbono=352,Etano=10,Dioxido_de_carbono=3641,Etileno=34,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date)
    p32.save()
    #2013
    date=datetime.datetime(2013,6,30)
    p33=Mediciones(central=p1,transformador=p22,codigo_usuario="7807004",Hidrogeno=17,Oxigeno=0,Nitrogeno=87500,Metano=9,Monoxido_de_carbono=463,Etano=11,Dioxido_de_carbono=4140,Etileno=40,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date)
    p33.save()
    #2014
    date=datetime.datetime(2014,6,30)
    p34=Mediciones(central=p1,transformador=p22,codigo_usuario="7807004",Hidrogeno=16,Oxigeno=0,Nitrogeno=0,Metano=4,Monoxido_de_carbono=42,Etano=7,Dioxido_de_carbono=680,Etileno=11,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date)
    p34.save()
    #2015
    date=datetime.datetime(2015,6,30)
    p35=Mediciones(central=p1,transformador=p22,codigo_usuario="7807004",Hidrogeno=12,Oxigeno=0,Nitrogeno=0,Metano=11,Monoxido_de_carbono=228,Etano=3,Dioxido_de_carbono=2226,Etileno=5,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date)
    p35.save()

    #2016
    date=datetime.datetime(2016,6,30)
    p35=Mediciones(central=p1,transformador=p22,codigo_usuario="7807004",Hidrogeno=15,Oxigeno=0,Nitrogeno=0,Metano=9,Monoxido_de_carbono=247,Etano=9,Dioxido_de_carbono=2381,Etileno=14,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date)
    p35.save()






    p23=Transformadores(central=p1,codigo="L252373",marca="GENERAL ELECTRIC",modelo="NA",cararcteristicas="U3",fecha_ingreso=date)
    p23.save()

     #2012
    date=datetime.datetime(2012,6,30)
    p31=Mediciones(central=p1,transformador=p23,codigo_usuario="7807004",Hidrogeno=106,Oxigeno=0,Nitrogeno=0,Metano=17,Monoxido_de_carbono=552,Etano=8,Dioxido_de_carbono=6920,Etileno=34,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()
    #2013
    date=datetime.datetime(2013,6,30)
    p32=Mediciones(central=p1,transformador=p23,codigo_usuario="7807004",Hidrogeno=74,Oxigeno=0,Nitrogeno=0,Metano=14,Monoxido_de_carbono=553,Etano=6,Dioxido_de_carbono=6798,Etileno=32,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date)
    p32.save()
    #2014
    date=datetime.datetime(2014,6,30)
    p33=Mediciones(central=p1,transformador=p23,codigo_usuario="7807004",Hidrogeno=74,Oxigeno=727,Nitrogeno=65942,Metano=12,Monoxido_de_carbono=427,Etano=3,Dioxido_de_carbono=4351,Etileno=17,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date)
    p33.save()
    #2015
    date=datetime.datetime(2015,6,30)
    p34=Mediciones(central=p1,transformador=p23,codigo_usuario="7807004",Hidrogeno=43,Oxigeno=0,Nitrogeno=0,Metano=8,Monoxido_de_carbono=334,Etano=8,Dioxido_de_carbono=4162,Etileno=18,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date)
    p34.save()
    #2016
    date=datetime.datetime(2016,6,30)
    p35=Mediciones(central=p1,transformador=p23,codigo_usuario="7807004",Hidrogeno=46,Oxigeno=0,Nitrogeno=0,Metano=9,Monoxido_de_carbono=330,Etano=8,Dioxido_de_carbono=4320,Etileno=17,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date)
    p35.save()
    #2017
    date=datetime.datetime(2017,6,30)
    p35=Mediciones(central=p1,transformador=p23,codigo_usuario="7807004",Hidrogeno=5,Oxigeno=0,Nitrogeno=0,Metano=1,Monoxido_de_carbono=9,Etano=2,Dioxido_de_carbono=151,Etileno=0,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date)
    p35.save()
     #2018
    date=datetime.datetime(2018,6,30)
    p35=Mediciones(central=p1,transformador=p23,codigo_usuario="7807004",Hidrogeno=11,Oxigeno=0,Nitrogeno=0,Metano=4,Monoxido_de_carbono=177,Etano=5,Dioxido_de_carbono=1896,Etileno=5,Acetileno=3,fecha_ingreso=date,fecha_del_analisis=date)
    p35.save()





    p24=Transformadores(central=p1,codigo="89115",marca="TADEO CZERWENY",modelo="NA",cararcteristicas="U4",fecha_ingreso=date)
    p24.save()

     #2012
    date=datetime.datetime(2012,6,30)
    p31=Mediciones(central=p1,transformador=p24,codigo_usuario="7807004",Hidrogeno=36,Oxigeno=0,Nitrogeno=0,Metano=22,Monoxido_de_carbono=522,Etano=6,Dioxido_de_carbono=1953,Etileno=9,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()
    #2013
    date=datetime.datetime(2013,6,30)
    p32=Mediciones(central=p1,transformador=p24,codigo_usuario="7807004",Hidrogeno=24,Oxigeno=0,Nitrogeno=0,Metano=29,Monoxido_de_carbono=708,Etano=7,Dioxido_de_carbono=2512,Etileno=8,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date)
    p32.save()
    #2014
    date=datetime.datetime(2014,6,30)
    p33=Mediciones(central=p1,transformador=p24,codigo_usuario="7807004",Hidrogeno=34,Oxigeno=0,Nitrogeno=0,Metano=29,Monoxido_de_carbono=771,Etano=3,Dioxido_de_carbono=2633,Etileno=10,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date)
    p33.save()
    #2015
    date=datetime.datetime(2015,6,30)
    p34=Mediciones(central=p1,transformador=p24,codigo_usuario="7807004",Hidrogeno=36,Oxigeno=0,Nitrogeno=0,Metano=32,Monoxido_de_carbono=785,Etano=3,Dioxido_de_carbono=2745,Etileno=8,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date)
    p34.save()
    #2016
    date=datetime.datetime(2016,6,30)
    p35=Mediciones(central=p1,transformador=p24,codigo_usuario="7807004",Hidrogeno=26,Oxigeno=0,Nitrogeno=0,Metano=33,Monoxido_de_carbono=916,Etano=8,Dioxido_de_carbono=2978,Etileno=12,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date)
    p35.save()
    #2017
    date=datetime.datetime(2017,6,30)
    p35=Mediciones(central=p1,transformador=p24,codigo_usuario="7807004",Hidrogeno=0,Oxigeno=0,Nitrogeno=0,Metano=30,Monoxido_de_carbono=1006,Etano=7,Dioxido_de_carbono=3281,Etileno=8,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date)
    p35.save()





    p25=Transformadores(central=p1,codigo="E-74470689",marca="DELTA STAR",modelo="NA",cararcteristicas="U5",fecha_ingreso=date)
    p25.save()

    #2012
    date=datetime.datetime(2012,6,30)
    p31=Mediciones(central=p1,transformador=p25,codigo_usuario="7807004",Hidrogeno=30,Oxigeno=0,Nitrogeno=0,Metano=11,Monoxido_de_carbono=328,Etano=23,Dioxido_de_carbono=15922,Etileno=14,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()
    #2013
    date=datetime.datetime(2013,6,30)
    p32=Mediciones(central=p1,transformador=p25,codigo_usuario="7807004",Hidrogeno=21,Oxigeno=0,Nitrogeno=0,Metano=13,Monoxido_de_carbono=308,Etano=20,Dioxido_de_carbono=15521,Etileno=10,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date)
    p32.save()
    #2014
    date=datetime.datetime(2014,6,30)
    p33=Mediciones(central=p1,transformador=p25,codigo_usuario="7807004",Hidrogeno=18,Oxigeno=0,Nitrogeno=0,Metano=9,Monoxido_de_carbono=194,Etano=15,Dioxido_de_carbono=4940,Etileno=8,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date)
    p33.save()
    #2015
    date=datetime.datetime(2015,6,30)
    p34=Mediciones(central=p1,transformador=p25,codigo_usuario="7807004",Hidrogeno=10,Oxigeno=0,Nitrogeno=112000,Metano=7,Monoxido_de_carbono=219,Etano=3,Dioxido_de_carbono=8150,Etileno=3,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date)
    p34.save()
    #2016
    date=datetime.datetime(2016,6,30)
    p35=Mediciones(central=p1,transformador=p25,codigo_usuario="7807004",Hidrogeno=16,Oxigeno=0,Nitrogeno=0,Metano=1,Monoxido_de_carbono=234,Etano=35,Dioxido_de_carbono=8630,Etileno=10,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date)
    p35.save()











    p26=Transformadores(central=p1,codigo="A15051",marca="TOSHIBA",modelo="NA",cararcteristicas="U6",fecha_ingreso=date)
    p26.save()

     #2016
    date=datetime.datetime(2016,6,30)
    p31=Mediciones(central=p1,transformador=p26,codigo_usuario="7807004",Hidrogeno=10,Oxigeno=7760,Nitrogeno=26500,Metano=5,Monoxido_de_carbono=212,Etano=2,Dioxido_de_carbono=677,Etileno=2,Acetileno=2,fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()
    #2018
    date=datetime.datetime(2018,6,30)
    p32=Mediciones(central=p1,transformador=p26,codigo_usuario="7807004",Hidrogeno=18,Oxigeno=0,Nitrogeno=0,Metano=29,Monoxido_de_carbono=785,Etano=3,Dioxido_de_carbono=4062,Etileno=6,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date)
    p32.save()







    p27=Transformadores(central=p1,codigo="A15052",marca="TOSHIBA",modelo="NA",cararcteristicas="U7",fecha_ingreso=date)
    p27.save()

    #2016
    date=datetime.datetime(2016,6,30)
    p31=Mediciones(central=p1,transformador=p27,codigo_usuario="7807004",Hidrogeno=10,Oxigeno=7760,Nitrogeno=26500,Metano=5,Monoxido_de_carbono=212,Etano=2,Dioxido_de_carbono=677,Etileno=2,Acetileno=2,fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()
    #2018
    date=datetime.datetime(2018,6,30)
    p32=Mediciones(central=p1,transformador=p27,codigo_usuario="7807004",Hidrogeno=21,Oxigeno=0,Nitrogeno=0,Metano=32,Monoxido_de_carbono=887,Etano=6,Dioxido_de_carbono=4395,Etileno=8,Acetileno=3,fecha_ingreso=date,fecha_del_analisis=date)
    p32.save()






    p28=Transformadores(central=p1,codigo="544328",marca="MITSUBICHI",modelo="NA",cararcteristicas="RESERVA",fecha_ingreso=date)
    p28.save()

    #2012
    date=datetime.datetime(2012,6,30)
    p31=Mediciones(central=p1,transformador=p28,codigo_usuario="7807004",Hidrogeno=48,Oxigeno=0,Nitrogeno=0,Metano=2,Monoxido_de_carbono=12,Etano=61,Dioxido_de_carbono=4166,Etileno=19,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()
    #2013
    date=datetime.datetime(2013,6,30)
    p32=Mediciones(central=p1,transformador=p28,codigo_usuario="7807004",Hidrogeno=33,Oxigeno=0,Nitrogeno=0,Metano=3,Monoxido_de_carbono=11,Etano=60,Dioxido_de_carbono=3999,Etileno=6,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date)
    p32.save()
    #2014
    date=datetime.datetime(2014,6,30)
    p33=Mediciones(central=p1,transformador=p28,codigo_usuario="7807004",Hidrogeno=8,Oxigeno=250,Nitrogeno=82.065,Metano=8,Monoxido_de_carbono=14,Etano=53,Dioxido_de_carbono=4781,Etileno=0,Acetileno=0,fecha_ingreso=date,fecha_del_analisis=date)
    p33.save()
    #2015
    date=datetime.datetime(2015,6,30)
    p34=Mediciones(central=p1,transformador=p28,codigo_usuario="7807004",Hidrogeno=30,Oxigeno=0,Nitrogeno=89.8,Metano=4.9,Monoxido_de_carbono=4.9,Etano=44,Dioxido_de_carbono=4900,Etileno=1.9,Acetileno=1.9,fecha_ingreso=date,fecha_del_analisis=date)
    p34.save()


    u1=User.objects.create_user(username="7807004", password="4690",email="evvaldez@cel.gob.sv",first_name="Ernesto Vladimir",apellidos="Valdez Rivas")
    u1.save()
    u1=Usuarios.objects.create_user(codigo_usuario="7807004", pasword="4690",email="evvaldez@cel.gob.sv",nombres="Ernesto Vladimir",last_name="Valdez Rivas",privilegio="DE_BAJA",fecha_ingreso=date)
    u1.save()

    return render(request,'principal.html',locals())

################################################################################



################################################################################
def datos_de_analisis(central_x, transformador_x):

    MedicionesF=Mediciones.objects.filter(Q(central__nombre__icontains=central_x) &  Q(transformador__codigo__icontains=transformador_x))
       
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

def gas_clave( central_x, transformador_x):
        
        VALOR_DEL_GAS= datos_de_analisis(central_x, transformador_x)     

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
def limite_concentracion(central_x, transformador_x):
        #Segun IEEE c57.104-1991
        #SIMBOLO_GAS=["H2","CH4","C2H2","C2H4","C2H6","CO","O2","N2","CO2"]
        #NOMBRE_GAS_PRUEBA=["Hidrogeno","Metano","Acetileno","Etileno","Etano","Monoxido_de_carbono","Oxigeno","Nitrogeno","Dioxido_de_carbono"]
        VALOR_DEL_GAS= datos_de_analisis(central_x, transformador_x)  

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
            
            vector=[NOMBRE_GAS_PRUEBA[i], SIMBOLO_GAS[i],VALOR_DEL_GAS[i][0],estado]
            ESTADO_DE_GASES.append(vector)
        
        respuesta= [estado_trafo,ESTADO_DE_GASES]
        return respuesta

        #return render(request,'analisis.html',locals())

################################################################################
################################################################################
def total_gases_combustibles(central_x, transformador_x):
        #SIMBOLO_GAS=["H2","CH4","C2H2","C2H4","C2H6","CO","O2","N2","CO2"]
        #NOMBRE_GAS_PRUEBA=["Hidrogeno","Metano","Acetileno","Etileno","Etano","Monoxido_de_carbono","Oxigeno","Nitrogeno","Dioxido_de_carbono"]
        VALOR_DEL_GAS= datos_de_analisis(central_x, transformador_x)  

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

            vector=[NOMBRE_GAS_PRUEBA[i], SIMBOLO_GAS[i],VALOR_DEL_GAS[i][0],estado]
            ESTADO_DE_GASES.append(vector)         
        
        
        respuesta= [estado_trafo,ESTADO_DE_GASES]

        return respuesta
        
        #return render(request,'analisis.html',locals())

################################################################################

################################################################################

def roger(central_x, transformador_x):
        
        VALOR_DEL_GAS= datos_de_analisis(central_x, transformador_x)     

        #SIMBOLO_GAS=["H2","CH4","C2H2","C2H4","C2H6","CO","O2","N2","CO2"]
        #NOMBRE_GAS_PRUEBA=["Hidrogeno","Metano","Acetileno","Etileno","Etano","Monoxido_de_carbono","Oxigeno","Nitrogeno","Dioxido_de_carbono"]

        #SIMBOLO_GAS_COMBUSTIBLE=["H2","CH4","C2H2","C2H4","C2H6","CO"]
        #NOMBRE_GAS_COMBUSTIBLE=["Hidrogeno","Metano","Acetileno","Etileno","Etano","Monoxido_de_carbono"]

        R1=VALOR_DEL_GAS[2][1]/VALOR_DEL_GAS[3][1]
        R2=VALOR_DEL_GAS[1][1]/VALOR_DEL_GAS[0][1]
        R3=VALOR_DEL_GAS[3][1]/VALOR_DEL_GAS[4][1]

        if R1<0.1 and R2>0.1 and R2<1 and R3<1 :
            estado_trafo="Estado Normal"

        if R1<0.1 and R2<0.1 and R3<1 :
            estado_trafo="Descarga parcial (corona)\n Arco de baja dencidad de energia"

        if R1>0.1 and R1<3 and R2>0.1 and R2<1 and R3>3 :
            estado_trafo="Arco\n Descarga de alta energia"

        if R1<0.1 and R2>0.1 and R2<1 and R3>1 and R3<3  :
            estado_trafo="Sobrecalentamiento termico a baja temperatura" 
        
        if R1<0.1 and R2>0.1 and R3>1 and R3<3  :
            estado_trafo="Calentamiento de alta temperatura menor de 700 grados celcius"

        if R1<0.1 and R2>0.1 and R3>3  :
            estado_trafo="Calentamiento de alta temperatura mayor de 700 grados celcius"
        
        else:
            estado_trafo="NO APLICA" 

        return estado_trafo
        #return render(request,'analisis.html',locals())

################################################################################

def donenberg(central_x, transformador_x):
        
        VALOR_DEL_GAS= datos_de_analisis(central_x, transformador_x)     

        #SIMBOLO_GAS=["H2","CH4","C2H2","C2H4","C2H6","CO","O2","N2","CO2"]
        #NOMBRE_GAS_PRUEBA=["Hidrogeno","Metano","Acetileno","Etileno","Etano","Monoxido_de_carbono","Oxigeno","Nitrogeno","Dioxido_de_carbono"]

        #SIMBOLO_GAS_COMBUSTIBLE=["H2","CH4","C2H2","C2H4","C2H6","CO"]
        #NOMBRE_GAS_COMBUSTIBLE=["Hidrogeno","Metano","Acetileno","Etileno","Etano","Monoxido_de_carbono"]
        
        R1=VALOR_DEL_GAS[1][1]/VALOR_DEL_GAS[0][1]
        R2=VALOR_DEL_GAS[2][1]/VALOR_DEL_GAS[3][1]

        if R1>0.87 and R1<=100 and R2>=0.01 and R2<=0.87  :
            estado_trafo="Se detecto un problema termico"

        if R1>=0.087 and R1<=0.87 and R2>0.1 and R2<=110 :
            estado_trafo="Se detecto un problema de Arco"

        if R1>=0 and R1<=0.087 and R2>0.087 and R2<100 :
            estado_trafo="Se detecto un problema de efecto Corona"       
        
        else:
            estado_trafo="NO APLICA" 

        return estado_trafo
        #return render(request,'analisis.html',locals())
################################################################################

def duval( central_x, transformador_x):
        
        VALOR_DEL_GAS= datos_de_analisis(central_x, transformador_x)     

        #SIMBOLO_GAS=["H2","CH4","C2H2","C2H4","C2H6","CO","O2","N2","CO2"]
        #NOMBRE_GAS_PRUEBA=["Hidrogeno","Metano","Acetileno","Etileno","Etano","Monoxido_de_carbono","Oxigeno","Nitrogeno","Dioxido_de_carbono"]

        #SIMBOLO_GAS_COMBUSTIBLE=["H2","CH4","C2H2","C2H4","C2H6","CO"]
        #NOMBRE_GAS_COMBUSTIBLE=["Hidrogeno","Metano","Acetileno","Etileno","Etano","Monoxido_de_carbono"]
        SUMAGASES=VALOR_DEL_GAS[1][1]+VALOR_DEL_GAS[2][1]+VALOR_DEL_GAS[3][1]

        PCH4=VALOR_DEL_GAS[1][1]/SUMAGASES
        PC2H2=VALOR_DEL_GAS[2][1]/SUMAGASES
        PC2H4=VALOR_DEL_GAS[3][1]/SUMAGASES        
        respuesta=[PCH4,PC2H2,PC2H4]
        return respuesta 
        #return render(request,'analisis.html',locals())

################################################################################

def IEC_60599(request):
    pass
def Relaciones_adicionales(request):
    pass



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
    
    
    MedicionesF=Mediciones.objects.filter(Q(central__nombre__icontains=central_x) &  Q(transformador__codigo__icontains=transformador_x))
    
    datos=MedicionesF.values_list(gas_analizar, flat=True) 
    fecha=MedicionesF.values_list("fecha_del_analisis", flat=True)     
    anios=[]
    limitemax=[]

    for i in  fecha:
        an=i.strftime('%Y') 
        anios.append(an)
        limitemax.append(limite)    
    

    

    X= np.arange(len(fecha))
    Y1 = np.asarray(datos) 
   

    f=plt.figure()
    #barh(pos,datos,align = 'center')
    plt.plot(anios,limitemax, 'r')
    plt.plot(anios,datos)


    z=0 
    for x, y in zip(X, Y1):
            plt.text(x, y ,str(y), ha='center', va= 'bottom')
            z=z+1


    plt.yticks(limitemax,color="r")
    #plt.yticks(datos,color="b")    
    #plt.xticks(anios,size="small",color="b",rotation=45)

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
  return render(request,'informacion.html',locals())

def principal(request):
    centrales=Centrales.objects.all()
    return render(request,'principal.html',locals())

def listado_de_transformadores(request,central_x):
    centrales=Centrales.objects.all()
    usuario_comun=Usuarios.objects.get(codigo_usuario=request.user.username)
       
    lista_transformadores=Transformadores.objects.filter(central__nombre__icontains=central_x)
    return render(request,'lista_de_transformadores.html',locals())

def listado_de_mediciones(request,central_x,transformador_x):
    centrales=Centrales.objects.all()
                                       
    lista_mediciones=Mediciones.objects.filter(Q(central__nombre__icontains=central_x) &  Q(transformador__codigo__icontains=transformador_x))
    identificador=lista_mediciones.first()
    
    VALOR_DEL_GAS= datos_de_analisis(central_x, transformador_x) 

        





    return render(request,'lista_de_mediciones.html',locals())

def tendencias(request,central_x,transformador_x,gas_x):
    gas=gas_x
    central=central_x
    transformador=transformador_x


    return render(request,'tendencias.html',locals()) 


def analisis(request,central_x,transformador_x):
    centrales=Centrales.objects.all()
    central=central_x
    transformador=transformador_x

    segun_gas_clave=gas_clave(central, transformador)#valor
    
    concentraciones_limite=limite_concentracion(central, transformador)#vector
    gases_combustibles= total_gases_combustibles(central, transformador)#vector    
    
    Triangulo_duval=duval( central, transformador)    
    segun_donenberg=donenberg(central, transformador)
    segun_roger=roger(central, transformador)         
   

    lista_mediciones=Mediciones.objects.filter(Q(central__nombre__icontains=central_x) &  Q(transformador__codigo__icontains=transformador_x))
    identificador=lista_mediciones.first()
    
    VALOR_DEL_GAS= datos_de_analisis(central_x, transformador_x)


    return render(request,'analisis.html',locals())

##############################ejemplito
#class Make(models.Model):
#    name = models.CharField(max_length=200)

#class MakeContent(models.Model):
#    make = models.ForeignKey(Make, related_name='makecontent')
#    published = models.BooleanField()

#Make.objects.filter(makecontent__published=True)


def grafico_gases_presentes(request,central_x,transformador_x):  
       
        VALOR_DEL_GAS= datos_de_analisis(central_x, transformador_x)             

        nombre_gases=[]
        valor_gases=[]

        for i in VALOR_DEL_GAS:
            nombre_gases.append(i[0])
            valor_gases.append(i[1])

        X= np.arange(len(nombre_gases))
        X2= np.arange(len(valor_gases))
        Y1 = np.asarray(valor_gases)  

        LIMITE_1=[100,120,35,50,65,350,0,0,2500]     
                   
        Y2= np.asarray(LIMITE_1)

        
        f=plt.figure()
        ax = f.add_subplot(111)
        f, axes = plt.subplots(ncols=1, nrows=1)

        plt.gca().set_yscale('log')
        bar_width = 0.45
        axes.bar(X, Y1, bar_width, facecolor='#9999ff', edgecolor='white')

        bar_width = 0.1
        axes.bar(X2, Y2, bar_width, facecolor='#6666ff', edgecolor='white',color='r')

        SIMBOLO_GAS=["H2","CH4","C2H2","C2H4","C2H6","CO","O2","N2","CO2"]
      
        z=0 
        for x, y in zip(X, Y1):
            plt.text(x, y ,str(y)+ "\n"+SIMBOLO_GAS[z], ha='center', va= 'bottom')
            z=z+1
 
      
        axes.xlabel('Gases combustibles (H2,CH4,C2H2,C2H4,C2H6) +CO +O2 +N2 +CO2 ')
        axes.ylabel('Concentraciones de gas (ppm) ')
        titulo=""
        axes.title(titulo)
        axes.xticks(())

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
    
 
  