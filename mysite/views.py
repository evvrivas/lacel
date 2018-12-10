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
  return render(request,'principal.html',locals())  
          
def Total_gases_combustibles(request):

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

    	  elif GASES_DE_PRUEBA[i]>LIMITE_2[i][0] and GASES_DE_PRUEBA[i]>LIMITE_2[i][0]:
    	  	  estado = "ANORMAL MODERDADO"

          elif GASES_DE_PRUEBA[i]>LIMITE_2[i][0] and GASES_DE_PRUEBA[i]>LIMITE_2[i][0]:
          	  estado = "ANORMAL EXESIVO"

          else:
          	  estado = "MUY ANORMAL"
          ESTADO_DE_GASES.append(estado)

    #return estado_trafo,NOMBRE_GAS_PRUEBA,ESTADO_DE_GASES
    return render(request,'principal.html',locals())


def show(request):
	    from django.shortcuts import render
		from matplotlib import pylab
		from pylab import *
		import PIL
		import PIL.Image
		import io
		from io import *

		x = np.arange(10)
		y = x
		fig = plt.figure()
		plt.plot(x, y)
		canvas = fig.canvas
		buf, size = canvas.print_to_buffer()
		image = Image.frombuffer('RGBA', size, buf, 'raw', 'RGBA', 0, 1)
		buffer=io.BytesIO()
		image.save(buffer,'PNG')
		graphic = buffer.getvalue()
		graphic = base64.b64encode(graphic)
		buffer.close()
		return render(request, 'graphic.html',{'graphic':graphic})



def Tas_clave(request):
	pass
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
        

def Limite_conecentracion():	
    TDGC = Hidrogeno + Metano + Acetileno + Etileno + Etano + Monoxido_de_carbono

	if TDGC<700 or Hidrogeno<100 or Metano<120 or Acetileno<2 or Etileno<50 or Etano<65 or Monoxido_de_carbono<350:
		estado_trafo="NORMAL"
	elif TDGC>1900 Hidrogen>700 or Metano>400 or Acetileno>5 or Etileno>100 or Etano>100 or Monoxido_de_carbono>570: 
		estado_trafo="PRECAUCION"
	else:
	    estado_trafo="ADVERTENCA"

return estado_trafo

	
	



