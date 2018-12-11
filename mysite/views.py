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
  return render(request,'informacion.html',locals())   


def principal(request):
    centrales=Centrales.objects.all()
    return render(request,'principal.html',locals())  


from random import *
def datos_aleatorios():

    usuarios=Usuarios(codigo="7807004",pasword="1111",privilegio="DE_BAJA",fecha_ingreso = =datetime.now)    
    usuarios.save()
    
    centrales=Central( nombre="GUAJOYO", fecha_ingreso = datetime.now)         
    centrales.save()

    centrales=Central( nombre="5 DE NOVIEMBRE", fecha_ingreso = datetime.now)         
    centrales.save()

    centrales=Central( nombre="CERRON GRANDE", fecha_ingreso = datetime.now)         
    centrales.save()
        
    
    
def ingresar_datos_trafo(request): 
        #!/usr/bin/python
        # -*- coding: latin-1 -*-        
        import os, sys       
        if request.method == 'POST': # si el usuario est enviando el formulario con datos
                             
                    form = MedicionForm(request.POST,request.FILES)                      
                    
                    if form.is_valid() :
                           
                            fecha_agregada = form.save(commit=False)
                            # commit=False tells Django that "Don't send this to database yet.
                            # I have more things I want to do with it."
                            
                            fecha_agregada.fecha=datetime.datetime.now()             
                            fecha_agregada.save() #  

                            form.save() # Guardar los datos en la base de datos  print 
                            #return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
                            connection.close()
                            return render(request,'confirmar.html',locals())                  
                

        else:            
                         
                         form=MedicionForm()
        connection.close()                  
        return render(request,'ingreso_de_datos.html',locals()) 

        




          
def total_gases_combustibles(request):

    #GASES=[Hidrogeno,Oxigeno,Nitrogeno,Metano,Monoxido_de_carbono,Etano,Dioxido_de_carbono,Etileno,Acetileno,Propileno,Propano,Butano]
    #INFERIOR=[H2           ,O2       ,N      ,CH4         ,CO     ,C2H6      ,CO2      ,C2H4      ,C2H2     ,propi    ,propa    ,buta]
    GASES      =[12         ,34       ,22     ,34          ,44     ,55        ,66       ,88        ,65       ,45       ,1        ,22  ]
    NOMBRE_GAS_PRUEBA=["Hidrogeno H2"  ,"Metano CH4"     ,"Etano C2H6"  ,   "Etileno C2H4",    "Acecetileno C2H2"]
    GASES_DE_PRUEBA=  [GASES[0],         GASES[3],         GASES[5],         GASES[7],          GASES[8]         ]  
    SUMTDGC        =  GASES[0]+          GASES[3]+         GASES[5]+         GASES[7]+          GASES[8]
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
    #return estado_trafo,NOMBRE_GAS_PRUEBA,ESTADO_DE_GASES
    return render(request,'principal.html',locals())




from django.shortcuts import render
from matplotlib import pylab
from pylab import *
import PIL
import PIL.Image
import io
from io import *

def grafico (request):
    pos = arange(10)+ 2 

    barh(pos,(1,2,3,4,5,6,7,8,9,10,11,12,13),align = 'center')

    yticks(pos,('#hcsm','#ukmedlibs','#ImmunoChat','#HCLDR','#ICTD2015','#hpmglobal','#BRCA','#BCSM','#BTSM','#OTalk'))
    #yticks=[Hidrogeno,Oxigeno,Nitrogeno,Metano,Monoxido_de_carbono,Etano,Dioxido_de_carbono,Etileno,Acetileno,Propileno,Propano,Butano]
    
    xlabel('Tipo de aceitr')
    ylabel('Concentracion')
    title('GASES DISUELTOS EN ACEITE')
    subplots_adjust(left=0.21)

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
    
    for i in range(len(GASES_DE_PRUEBA)):
        if GASES_DE_PRUEBA[i]<=LIMITE_1[i]:
            estado = "NORMAL"
        elif GASES_DE_PRUEBA[i]>LIMITE_2[i][0] and GASES_DE_PRUEBA[i]<LIMITE_2[i][1]:
            estado = "PRECAUCION"
        else:
            estado = "ADVERTENCIA"
        ESTADO_DE_GASES.append(estado)
    #return estado_trafo,NOMBRE_GAS_PRUEBA,ESTADO_DE_GASES
    return render(request,'principal.html',locals())

