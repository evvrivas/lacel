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






      
def total_gases_combustibles(central_x,transformador_x):
    MedicionesF=Mediciones.objects.filter(Q(central__nombre__icontains=central_x) &  Q(transformador__codigo__icontains=transformador_x))
    
    gases=["Hidrogeno","Metano","Monoxido_de_carbono","Etano","Etileno","Acetileno"]
   
    gas_analisis=[]
    valor=[]
    for i in gases:
        datos=MedicionesF.values_list(i, flat=True) 
        for y in datos: 
            if y!=0 and y!="":
                valor.append(y)

        gas_analisis.append((i,valor[-1]))        

    nombre_gases=[]
    valor_gases=[]
    
    SUMTDGC=0 
    GASES=[0,0,0,0,0,0,0,0,0]
    for i in gas_analisis:

        SUMTDGC=SUMTDGC+i[1]
        
        if i[0]=="Hidrogeno":
            GASES[0]=i[1]
        elif i[0]=="Metano":
            GASES[3]=i[1]
       
        elif i[0]=="Etano":
            GASES[5]=i[1]
        elif i[0]=="Etileno":
            GASES[7]=i[1]
        elif i[0]=="Acetileno":
            GASES[8]=i[1]
        else:
            pass
    
    #GASES=[Hidrogeno,Oxigeno,Nitrogeno,Metano,Monoxido_de_carbono,Etano,Dioxido_de_carbono,Etileno,Acetileno,Propileno,Propano,Butano]
    #INFERIOR=[H2           ,O2       ,N      ,CH4         ,CO     ,C2H6      ,CO2      ,C2H4      ,C2H2     ,propi    ,propa    ,buta]
    #GASES      =[12         ,34       ,22     ,34          ,44     ,55        ,66       ,88        ,65       ,45       ,1        ,22  ]
    
    NOMBRE_GAS_PRUEBA=["Hidrogeno H2"  ,"Metano CH4"     ,"Etano C2H6"  ,   "Etileno C2H4",    "Acecetileno C2H2"]
    GASES_DE_PRUEBA=  [GASES[0],         GASES[3],         GASES[5],         GASES[7],          GASES[8]         ]  
   



    LIMITE_1=        [100             ,120              ,65                ,50                 ,35              ]
    LIMITE_2=        [(101,700)       ,(121,400)        ,(66,100)          ,(51,100)           ,(36,50)         ]
    LIMITE_3=        [(701,1800)      ,(401,1000)       ,(101,150)         ,(101,200)          ,(51,80)         ]
    LIMITE_4=        [1800            ,1000             ,150               ,200                ,80              ]

    if SUMTDGC<=720:
        estado_trafo="EL TRANSFORMADOR ESTA OPERANDO SATISFACTORIAMENTE"
    elif SUMTDGC>720 and SUMTDGC<=1920:
        estado_trafo="NIVEL ALTO DE GAS COMBUSTIBLE, HAY QUE HACER INVESTIGACION ADICIANAL E INDIVIDUAL DE GASES "
    elif SUMTDGC>1920 and SUMTDGC<=4630:
        estado_trafo="ALTO NIVEL DE DESCOMPOSICION DE CELULOSA Y/O ACEITE , HAY QUE HACER INVESTIGACION ADICIANAL E INDIVIDUAL DE GASES FUERA DE RRANGO, UNA FALLA O FALLES PROBABLEMENTE ESTE PRESENTE "
    else:
        estado_trafo="EXCESIVA DESCOMPOSICION DE CELULOSA Y/O ACEITE, LA OPERACION CONTINUA PUEDE RESULTAR EN UNA FALLA DEL TRANSFORMADOR "
    
    ESTADO_DE_GASES=[]
    
    for i in range(len(GASES_DE_PRUEBA)):
        if GASES_DE_PRUEBA[i]<=LIMITE_1[i]:
            estado = "NORMAL"
        elif GASES_DE_PRUEBA[i]>LIMITE_2[i][0] and GASES_DE_PRUEBA[i]<LIMITE_2[i][1]:
            estado = "ANORMAL MODERDADO"
        elif GASES_DE_PRUEBA[i]>LIMITE_3[i][0] and GASES_DE_PRUEBA[i]<LIMITE_3[i][1]:
            estado = "ANORMAL EXESIVO"
        else:
            estado = "MUY ANORMAL"
        ESTADO_DE_GASES.append(estado)
    
    return estado_trafo,NOMBRE_GAS_PRUEBA,ESTADO_DE_GASES
    

    #return render(request,'analisis.html',locals())











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

     

    return render(request,'principal.html',locals())

   


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
     
    plt.figure()
    #barh(pos,datos,align = 'center')
    plt.plot(anios,limitemax, 'r')
    plt.figure()
    plt.plot(anios,datos)
    
    #plt.yticks(limitemax,color="r")
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
    
    

    return HttpResponse (buffer.getvalue(), content_type="Image/png")


def gas_clave(request):
        pass
        #suma de gases combustibles
        #GASES=[Hidrogeno,Oxigeno,Nitrogeno,Metano,Monoxido_de_carbono,Etano,Dioxido_de_carbono,Etileno,Acetileno,Propileno,Propano,Butano]
        #INFERIOR=[H2           ,O2       ,N      ,CH4         ,CO     ,C2H6      ,CO2      ,C2H4      ,C2H2     ,propi    ,propa    ,buta]
        #GASES      =[12         ,34       ,22     ,34          ,44     ,55        ,66       ,88        ,65       ,45       ,1        ,22  ]
        
        #NOMBRE_GAS_PRUEBA=["Hidrogeno H2"  ,"Metano CH4"    ,"MONOXIDO DE CARBONO CO" ,  "Etano C2H6"  ,   "Etileno C2H4",    "Acecetileno C2H2"]
        #GASES_DE_PRUEBA=  [GASES[0],         GASES[3],        GASES[4],                   GASES[5],         GASES[7],          GASES[8]         ]
        #SUMTDGC        =  GASES[0]+          GASES[3]+        GASES[4]+                   GASES[5]+         GASES[7]+          GASES[8]
        #SUMTDG=0
        #for i in GASES[0]:
        #    SUMTDG=SUMTDG+i
        #V_PORCENTAJE_GASES

        #for i in GASES_DE_PRUEBA:
        #    V_PORCENTAJE_GASES.append(100*i/SUMTDG)
        #Vmaximo=max( V_PORCENTAJE_GASES)
        #indice_Vmaximo= V_PORCENTAJE_GASES.index(Vmaximo)

        #Vminimo=min( V_PORCENTAJE_GASES) 
        
        #if indice_Vmaximo==3:#ETANO C2H6
        #       estado_trafo="SE DETECTO ACEITE SOBRE CALENTADO"
        #elif indice_Vmaximo==2:#MONOXIDO DE CARBONO CO
        #       estado_trafo="SE DETECTO PAPEL SOBRECALENTADO"
        #elif indice_Vmaximo==5:# ACETILENO C2H2
        #       estado_trafo="SE DETECTO ARCO INTERNO"
       #elif indice_Vmaximo==0:#HIDROGENO H
        #       estado_trafo="SE DETECTO EFECTO CORONA"
        #else:
        #   estado_trafo="NO APLICA"

        #return render(request,'principal.html',locals())






def Dornenberg(request):
    pass
def Relaciones_roger(request):
    pass
def Triangulo_duval(request):
    pass
def IEC_60599(request):
    pass
def Relaciones_adicionales(request):
    pass
#Hidrogeno H
#Oxigeno   O2
#Nitrogeno  N
#Metano   CH4
#Monoxido_de_carbono  C0
#Etano   C2H6
#Dioxido_de_carbono  CO2
#Etileno  C2H4
#Acetileno C2H2
#Propileno C3H6 
#Propano C3H8
#Butano  C4H10  

def limite_concentracion(request):
    GASES      =[12         ,34       ,22     ,34          ,44     ,55        ,66       ,88        ,65       ,45       ,1        ,22  ]
    NOMBRE_GAS_PRUEBA=["Hidrogeno H2"  ,"Metano CH4"  "MONOXIDO DE CARBONO"   ,"Etano C2H6"  ,   "Etileno C2H4",    "Acecetileno C2H2"]
    GASES_DE_PRUEBA=  [GASES[0],         GASES[3],         GASES[4],            GASES[5],         GASES[7],          GASES[8]          ]  
    SUMTDGC        =  GASES[0]+          GASES[3]+         GASES[4]+            GASES[5]+         GASES[7]+          GASES[8]       
    

    LIMITE_1=        [100             ,120               ,350                   ,65                ,50                 ,2              ]
    LIMITE_2=        [(100,700)       ,(120,400)         ,(350,570)             ,(65,100)          ,(50,100)           ,(2,5)         ]
    LIMITE_3=        [700             ,400               ,570                   ,100               ,100                ,5              ]

    if SUMTDGC<=700:
        estado_trafo="EN UN RANGO NORMAL: CONCENTRACION DE GASES DISUELTOS "
    elif SUMTDGC>700 and SUMTDGC<=1900:
        estado_trafo="PRECAUCION:  CONCENTRACION DE GASES DISUELTOS ELEVADOS"
    else:
        estado_trafo="ADVERTENCIA:  PROBLEMA GRAVE, INTERVENSION O REMOCION INMEDIATA"
    
    ESTADO_DE_GASES=[]
    
    for i in r/ange(len(GASES_DE_PRUEBA)):
        if GASES_DE_PRUEBA[i]<=LIMITE_1[i]:
            estado = "NORMAL"
        elif GASES_DE_PRUEBA[i]>LIMITE_2[i][0] and GASES_DE_PRUEBA[i]<LIMITE_2[i][1]:
            estado = "PRECAUCION"
        else:
            estado = "ADVERTENCIA"
        ESTADO_DE_GASES.append(estado)
    #return estado_trafo,NOMBRE_GAS_PRUEBA,ESTADO_DE_GASES
    return render(request,'analisis.html',locals())








def informacion(request):
  return render(request,'informacion.html',locals())

def principal(request):
    centrales=Centrales.objects.all()
    return render(request,'principal.html',locals())

def listado_de_transformadores(request,central_x):
    centrales=Centrales.objects.all()
       
    lista_transformadores=Transformadores.objects.filter(central__nombre__icontains=central_x)
    return render(request,'lista_de_transformadores.html',locals())

def listado_de_mediciones(request,central_x,transformador_x):
    centrales=Centrales.objects.all()
                                       
    lista_mediciones=Mediciones.objects.filter(Q(central__nombre__icontains=central_x) &  Q(transformador__codigo__icontains=transformador_x))
    identificador=lista_mediciones.first()
    return render(request,'lista_de_mediciones.html',locals())

def tendencias(request,central_x,transformador_x):
    central=central_x
    transformador=transformador_x
    return render(request,'tendencias.html',locals()) 


def analisis(request,central_x,transformador_x):
    central=central_x
    transformador=transformador_x
   
    return render(request,'analisis.html',locals())

##############################ejemplito
#class Make(models.Model):
#    name = models.CharField(max_length=200)

#class MakeContent(models.Model):
#    make = models.ForeignKey(Make, related_name='makecontent')
#    published = models.BooleanField()

#Make.objects.filter(makecontent__published=True)


def grafico_gases_presentes(request,central_x,transformador_x):  
    
   
    MedicionesF=Mediciones.objects.filter(Q(central__nombre__icontains=central_x) &  Q(transformador__codigo__icontains=transformador_x))
    
    gases=["Hidrogeno","Oxigeno","Nitrogeno","Metano","Monoxido_de_carbono","Etano","Dioxido_de_carbono","Etileno","Acetileno"]
   
    gas_analisis=[]
    valor=[]
    for i in gases:
        datos=MedicionesF.values_list(i, flat=True) 
        for y in datos: 
            if y!=0 and y!="":
                valor.append(y)

        gas_analisis.append((i,valor[-1]))        

    nombre_gases=[]
    valor_gases=[]

    for i in gas_analisis:
        nombre_gases.append(i[0])
        valor_gases.append(i[1])
     
    plt.figure()
    barh(nombre_gases,valor_gases,align = 'center')
    #plt.plot(anios,limitemax, 'r')
    #plt.plot(anios,datos)
    
    #plt.yticks(limitemax,color="r")
    #plt.yticks(datos,color="b")    
    #plt.xticks(anios,size="small",color="b",rotation=45)

    plt.xlabel('Nombre del gas ')
    plt.ylabel('CONCENTRACIONES ppm')
    titulo="Presencia del gases  disueltos en aceite"
    plt.title(titulo)
    subplots_adjust(left=0.21)
    


    #subplots_adjust(left=0.21)

    buffer = io.BytesIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()

    
    graphIMG = PIL.Image.fromstring('RGB', canvas.get_width_height(), canvas.tostring_rgb())
    graphIMG.save(buffer, "PNG")
    pylab.close()
    
    

    return HttpResponse (buffer.getvalue(), content_type="Image/png")

def grafico_gases_combustibles(request,central_x,transformador_x):  
    
   
    MedicionesF=Mediciones.objects.filter(Q(central__nombre__icontains=central_x) &  Q(transformador__codigo__icontains=transformador_x))
    
    gases=["Hidrogeno","Metano","Monoxido_de_carbono","Etano","Etileno","Acetileno"]
   
    gas_analisis=[]
    valor=[]
    for i in gases:
        datos=MedicionesF.values_list(i, flat=True) 
        for y in datos: 
            if y!=0 and y!="":
                valor.append(y)

        gas_analisis.append((i,valor[-1]))        

    nombre_gases=[]
    valor_gases=[]

    for i in gas_analisis:
        nombre_gases.append(i[0])
        valor_gases.append(i[1])
     
    plt.figure()
    barh(nombre_gases,valor_gases,align = 'center')
    #plt.plot(anios,limitemax, 'r')
    #plt.plot(anios,datos)
    
    #plt.yticks(limitemax,color="r")
    #plt.yticks(datos,color="b")    
    #plt.xticks(anios,size="small",color="b",rotation=45)
    trafo,nombre_gas,estado_gas=total_gases_combustibles(central_x,transformador_x)

    plt.xlabel('Nombre del gas ')
    plt.ylabel('CONCENTRACIONES ppm')
    titulo="Presencia del gases combustibles\n"+"Estado del Tx "+ trafo="\n"+"Nombre de gases "+ nombre_gas="\n"+"Estado del gas "+ estado_gas="\n"


    
    



    plt.title(titulo)
    subplots_adjust(left=0.21)
    


    #subplots_adjust(left=0.21)

    buffer = io.BytesIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()

    
    graphIMG = PIL.Image.fromstring('RGB', canvas.get_width_height(), canvas.tostring_rgb())
    graphIMG.save(buffer, "PNG")
    pylab.close()
    
    

    return HttpResponse (buffer.getvalue(), content_type="Image/png")