def datos_prueba_DP(request):
    p21=Generadores(central=p1,codigo="C0848A",marca="ELIM",modelo="NA",cararcteristicas="U1",fecha_ingreso=date)
    p21.save()
      
    #ELIM U1
    #2018

    date=datetime.datetime(2018,01,11,16,58)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60 ,  potencia_activa=16.11, potencia_reactiva=2.0, temperatura_promedio=59.3, temperatura_calent=35, humedad_relativa=61, CAG="SI",
         NQNC1posA1= 1522, NQNC2posA1=0 , NQNC1negA1=2157,NQNC2negA1=0, QMAXC1posA1=425, QMAXC2posA1=0, QMAXC1negA1=330, QMAXC2negA1=0, 
         NQNC1posB1= 0, NQNC2posB1= 135, NQNC1negB1=0,NQNC2negB1=64, QMAXC1posB1=0, QMAXC2posB1=43, QMAXC1negB1=0, QMAXC2negB1=43, 
         NQNC1posC1= 2, NQNC2posC1= 146, NQNC1negC1=0,NQNC2negC1=95, QMAXC1posC1=20, QMAXC2posC1=43, QMAXC1negC1=0, QMAXC2negC1=34, 
 
         NQNC3posA2= 0, NQNC4posA2= 0, NQNC3negA2=0,NQNC4negA2=0, QMAXC3posA2=0, QMAXC4posA2=0, QMAXC3negA2=0, QMAXC4negA2=0, 
         NQNC3posB2= 0, NQNC4posB2= 0, NQNC3negB2=0,NQNC4negB2=0, QMAXC3posB2=0, QMAXC4posB2=0, QMAXC3negB2=0, QMAXC4negB2=0, 
         NQNC3posC2= 0, NQNC4posC2= 0, NQNC3negC2=0,NQNC4negC2=0, QMAXC3posC2=0, QMAXC4posC2=0, QMAXC3negC2=0, QMAXC4negC2=0, 
         
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()
    

    date=datetime.datetime(2018,02,12,14,15)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60 ,  potencia_activa=15.9, potencia_reactiva=4.7, temperatura_promedio=63.6, temperatura_calent=33, humedad_relativa=57, CAG="SI",
         NQNC1posA1= 1697, NQNC2posA1=5 , NQNC1negA1=1818,NQNC2negA1=6, QMAXC1posA1=425, QMAXC2posA1=72, QMAXC1negA1=425, QMAXC2negA1=72, 
         NQNC1posB1= 12, NQNC2posB1= 106, NQNC1negB1=30,NQNC2negB1=36, QMAXC1posB1=20, QMAXC2posB1=43, QMAXC1negB1=20, QMAXC2negB1=43, 
         NQNC1posC1= 0, NQNC2posC1= 96, NQNC1negC1=0,NQNC2negC1=75, QMAXC1posC1=0, QMAXC2posC1=34, QMAXC1negC1=0, QMAXC2negC1=43, 
 
         NQNC3posA2= 0, NQNC4posA2= 0, NQNC3negA2=0,NQNC4negA2=0, QMAXC3posA2=0, QMAXC4posA2=0, QMAXC3negA2=0, QMAXC4negA2=0, 
         NQNC3posB2= 0, NQNC4posB2= 0, NQNC3negB2=0,NQNC4negB2=0, QMAXC3posB2=0, QMAXC4posB2=0, QMAXC3negB2=0, QMAXC4negB2=0, 
         NQNC3posC2= 0, NQNC4posC2= 0, NQNC3negC2=0,NQNC4negC2=0, QMAXC3posC2=0, QMAXC4posC2=0, QMAXC3negC2=0, QMAXC4negC2=0, 
         
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()


    date=datetime.datetime(2018,03,17,13,43)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60 ,  potencia_activa=17.47, potencia_reactiva=4.8, temperatura_promedio=66, temperatura_calent=35, humedad_relativa=63, CAG="SI",
         NQNC1posA1= 1523, NQNC2posA1=11 , NQNC1negA1=1693,NQNC2negA1=16, QMAXC1posA1=330, QMAXC2posA1=20, QMAXC1negA1=256, QMAXC2negA1=16, 
         NQNC1posB1= 17, NQNC2posB1= 140, NQNC1negB1=9,NQNC2negB1=95, QMAXC1posB1=16, QMAXC2posB1=43, QMAXC1negB1=20, QMAXC2negB1=26, 
         NQNC1posC1= 121, NQNC2posC1= 347, NQNC1negC1=37,NQNC2negC1=198, QMAXC1posC1=34, QMAXC2posC1=43, QMAXC1negC1=26, QMAXC2negC1=43, 
 
         NQNC3posA2= 0, NQNC4posA2= 0, NQNC3negA2=0,NQNC4negA2=0, QMAXC3posA2=0, QMAXC4posA2=0, QMAXC3negA2=0, QMAXC4negA2=0, 
         NQNC3posB2= 0, NQNC4posB2= 0, NQNC3negB2=0,NQNC4negB2=0, QMAXC3posB2=0, QMAXC4posB2=0, QMAXC3negB2=0, QMAXC4negB2=0, 
         NQNC3posC2= 0, NQNC4posC2= 0, NQNC3negC2=0,NQNC4negC2=0, QMAXC3posC2=0, QMAXC4posC2=0, QMAXC3negC2=0, QMAXC4negC2=0,  
         
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()


    date=datetime.datetime(2018,04,26,17,05)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60,  potencia_activa=15.06, potencia_reactiva=1.7, temperatura_promedio=36, temperatura_calent=35, humedad_relativa=71, CAG="SI",
         NQNC1posA1= 1323, NQNC2posA1=2 , NQNC1negA1=1994,NQNC2negA1=3, QMAXC1posA1=200, QMAXC2posA1=12, QMAXC1negA1=150, QMAXC2negA1=26, 
         NQNC1posB1= 1, NQNC2posB1= 40, NQNC1negB1=0,NQNC2negB1=11, QMAXC1posB1=0, QMAXC2posB1=260, QMAXC1negB1=0, QMAXC2negB1=260, 
         NQNC1posC1= 0, NQNC2posC1= 109, NQNC1negC1=0,NQNC2negC1=75, QMAXC1posC1=0, QMAXC2posC1=34, QMAXC1negC1=0, QMAXC2negC1=43, 
 
         NQNC3posA2= 0, NQNC4posA2= 0, NQNC3negA2=0,NQNC4negA2=0, QMAXC3posA2=0, QMAXC4posA2=0, QMAXC3negA2=0, QMAXC4negA2=0, 
         NQNC3posB2= 0, NQNC4posB2= 0, NQNC3negB2=0,NQNC4negB2=0, QMAXC3posB2=0, QMAXC4posB2=0, QMAXC3negB2=0, QMAXC4negB2=0, 
         NQNC3posC2= 0, NQNC4posC2= 0, NQNC3negC2=0,NQNC4negC2=0, QMAXC3posC2=0, QMAXC4posC2=0, QMAXC3negC2=0, QMAXC4negC2=0, 
         
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()


    date=datetime.datetime(2018,05,03,14,20)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=59.99,  potencia_activa=16.51, potencia_reactiva=4.7, temperatura_promedio=66.38, temperatura_calent=37, humedad_relativa=67, CAG="SI",
         NQNC1posA1= 1204, NQNC2posA1=1 , NQNC1negA1=1470,NQNC2negA1=1, QMAXC1posA1=298, QMAXC2posA1=34, QMAXC1negA1=192, QMAXC2negA1=26, 
         NQNC1posB1= 54, NQNC2posB1= 55, NQNC1negB1=53,NQNC2negB1=35, QMAXC1posB1=20, QMAXC2posB1=26, QMAXC1negB1=20, QMAXC2negB1=26, 
         NQNC1posC1= 8, NQNC2posC1= 92, NQNC1negC1=17,NQNC2negC1=69, QMAXC1posC1=20, QMAXC2posC1=56, QMAXC1negC1=26, QMAXC2negC1=34, 
 
         NQNC3posA2= 0, NQNC4posA2= 0, NQNC3negA2=0,NQNC4negA2=0, QMAXC3posA2=0, QMAXC4posA2=0, QMAXC3negA2=0, QMAXC4negA2=0, 
         NQNC3posB2= 0, NQNC4posB2= 0, NQNC3negB2=0,NQNC4negB2=0, QMAXC3posB2=0, QMAXC4posB2=0, QMAXC3negB2=0, QMAXC4negB2=0, 
         NQNC3posC2= 0, NQNC4posC2= 0, NQNC3negC2=0,NQNC4negC2=0, QMAXC3posC2=0, QMAXC4posC2=0, QMAXC3negC2=0, QMAXC4negC2=0, 

         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()


    date=datetime.datetime(2018,06,01,14,34)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60,  potencia_activa=17.03, potencia_reactiva=0.2, temperatura_promedio=60.03, temperatura_calent=39, humedad_relativa=74, CAG="SI",
         NQNC1posA1= 1240, NQNC2posA1=1 , NQNC1negA1=1793,NQNC2negA1=2, QMAXC1posA1=317, QMAXC2posA1=16, QMAXC1negA1=256, QMAXC2negA1=16, 
         NQNC1posB1= 20, NQNC2posB1= 41, NQNC1negB1=7,NQNC2negB1=12, QMAXC1posB1=20, QMAXC2posB1=34, QMAXC1negB1=20, QMAXC2negB1=34, 
         NQNC1posC1= 0, NQNC2posC1= 122, NQNC1negC1=1,NQNC2negC1=80, QMAXC1posC1=0, QMAXC2posC1=43, QMAXC1negC1=16, QMAXC2negC1=34, 
 
         NQNC3posA2= 0, NQNC4posA2= 0, NQNC3negA2=0,NQNC4negA2=0, QMAXC3posA2=0, QMAXC4posA2=0, QMAXC3negA2=0, QMAXC4negA2=0, 
         NQNC3posB2= 0, NQNC4posB2= 0, NQNC3negB2=0,NQNC4negB2=0, QMAXC3posB2=0, QMAXC4posB2=0, QMAXC3negB2=0, QMAXC4negB2=0, 
         NQNC3posC2= 0, NQNC4posC2= 0, NQNC3negC2=0,NQNC4negC2=0, QMAXC3posC2=0, QMAXC4posC2=0, QMAXC3negC2=0, QMAXC4negC2=0, 

         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()


    date=datetime.datetime(2018,07,10,10,45)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60,  potencia_activa=18.14, potencia_reactiva=3.8, temperatura_promedio=68, temperatura_calent=32, humedad_relativa=77, CAG="SI",
         NQNC1posA1= 1381, NQNC2posA1=2 , NQNC1negA1=1725,NQNC2negA1=0, QMAXC1posA1=313, QMAXC2posA1=0, QMAXC1negA1=256, QMAXC2negA1=0, 
         NQNC1posB1= 3, NQNC2posB1= 49, NQNC1negB1=1,NQNC2negB1=35, QMAXC1posB1=16, QMAXC2posB1=20, QMAXC1negB1=16, QMAXC2negB1=26, 
         NQNC1posC1= 34, NQNC2posC1= 71, NQNC1negC1=24,NQNC2negC1=55, QMAXC1posC1=26, QMAXC2posC1=34, QMAXC1negC1=20, QMAXC2negC1=56, 
 
         NQNC3posA2= 0, NQNC4posA2= 0, NQNC3negA2=0,NQNC4negA2=0, QMAXC3posA2=0, QMAXC4posA2=0, QMAXC3negA2=0, QMAXC4negA2=0, 
         NQNC3posB2= 0, NQNC4posB2= 0, NQNC3negB2=0,NQNC4negB2=0, QMAXC3posB2=0, QMAXC4posB2=0, QMAXC3negB2=0, QMAXC4negB2=0, 
         NQNC3posC2= 0, NQNC4posC2= 0, NQNC3negC2=0,NQNC4negC2=0, QMAXC3posC2=0, QMAXC4posC2=0, QMAXC3negC2=0, QMAXC4negC2=0, 
         
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()


    date=datetime.datetime(2018,8,13,14,27)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60.01,  potencia_activa=16.88, potencia_reactiva=1.8, temperatura_promedio=64.62, temperatura_calent=37, humedad_relativa=75, CAG="SI",
         NQNC1posA1= 2311, NQNC2posA1=815 , NQNC1negA1=1589, NQNC2negA1=741, QMAXC1posA1=0.199, QMAXC2posA1=0.12, QMAXC1negA1=0.093, QMAXC2negA1=0.093, 
         NQNC1posB1= 2139, NQNC2posB1=0, NQNC1negB1=770, NQNC2negB1=0, QMAXC1posB1=0.093, QMAXC2posB1=0, QMAXC1negB1=0.093, QMAXC2negB1=0, 
         NQNC1posC1= 1081, NQNC2posC1= 1014, NQNC1negC1=476, NQNC2negC1=1509, QMAXC1posC1=0.119, QMAXC2posC1=0.12, QMAXC1negC1=0.056, QMAXC2negC1=0.12, 
 
         NQNC3posA2= 0, NQNC4posA2= 0, NQNC3negA2=0,NQNC4negA2=0, QMAXC3posA2=0, QMAXC4posA2=0, QMAXC3negA2=0, QMAXC4negA2=0, 
         NQNC3posB2= 0, NQNC4posB2= 0, NQNC3negB2=0,NQNC4negB2=0, QMAXC3posB2=0, QMAXC4posB2=0, QMAXC3negB2=0, QMAXC4negB2=0, 
         NQNC3posC2= 0, NQNC4posC2= 0, NQNC3negC2=0,NQNC4negC2=0, QMAXC3posC2=0, QMAXC4posC2=0, QMAXC3negC2=0, QMAXC4negC2=0, 
         
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()


    date=datetime.datetime(2018,9,17,13,15)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60.01,  potencia_activa=16.94, potencia_reactiva=3.6, temperatura_promedio=66.01, temperatura_calent=35, humedad_relativa=78, CAG="SI",
         NQNC1posA1= 1296, NQNC2posA1=796 , NQNC1negA1=1319,NQNC2negA1=509, QMAXC1posA1=0.256, QMAXC2posA1=0.12, QMAXC1negA1=0.256, QMAXC2negA1=0.12, 
         NQNC1posB1= 428, NQNC2posB1= 1104, NQNC1negB1=421,NQNC2negB1=240, QMAXC1posB1=0.072, QMAXC2posB1=0.043, QMAXC1negB1=0.072, QMAXC2negB1=0.043, 
         NQNC1posC1= 1068, NQNC2posC1= 1576, NQNC1negC1=1729,NQNC2negC1=585, QMAXC1posC1=0.072, QMAXC2posC1=0.093, QMAXC1negC1=0.154, QMAXC2negC1=0.043, 
 
         NQNC3posA2= 0, NQNC4posA2= 0, NQNC3negA2=0,NQNC4negA2=0, QMAXC3posA2=0, QMAXC4posA2=0, QMAXC3negA2=0, QMAXC4negA2=0, 
         NQNC3posB2= 0, NQNC4posB2= 0, NQNC3negB2=0,NQNC4negB2=0, QMAXC3posB2=0, QMAXC4posB2=0, QMAXC3negB2=0, QMAXC4negB2=0, 
         NQNC3posC2= 0, NQNC4posC2= 0, NQNC3negC2=0,NQNC4negC2=0, QMAXC3posC2=0, QMAXC4posC2=0, QMAXC3negC2=0, QMAXC4negC2=0, 
         
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()


    date=datetime.datetime(2018,10,03,13,23)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=60,  potencia_activa=18.6, potencia_reactiva=3.6, temperatura_promedio=67.8, temperatura_calent=0, humedad_relativa=75, CAG="SI",
         NQNC1posA1= 1289, NQNC2posA1=1255 , NQNC1negA1=1379, NQNC2negA1=943, QMAXC1posA1=254, QMAXC2posA1=120, QMAXC1negA1=249, QMAXC2negA1=117, 
         NQNC1posB1= 342, NQNC2posB1= 1278, NQNC1negB1=589, NQNC2negB1=80, QMAXC1posB1=92, QMAXC2posB1=95, QMAXC1negB1=118, QMAXC2negB1=52, 
         NQNC1posC1= 1157, NQNC2posC1= 1200, NQNC1negC1=1410, NQNC2negC1=480, QMAXC1posC1=71, QMAXC2posC1=92, QMAXC1negC1=137, QMAXC2negC1=42, 
 
         NQNC3posA2= 0, NQNC4posA2= 0, NQNC3negA2=0,NQNC4negA2=0, QMAXC3posA2=0, QMAXC4posA2=0, QMAXC3negA2=0, QMAXC4negA2=0, 
         NQNC3posB2= 0, NQNC4posB2= 0, NQNC3negB2=0,NQNC4negB2=0, QMAXC3posB2=0, QMAXC4posB2=0, QMAXC3negB2=0, QMAXC4negB2=0, 
         NQNC3posC2= 0, NQNC4posC2= 0, NQNC3negC2=0,NQNC4negC2=0, QMAXC3posC2=0, QMAXC4posC2=0, QMAXC3negC2=0, QMAXC4negC2=0, 
         
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()


    date=datetime.datetime(2018,11,05,10,45)
    p31=Mediciones(central=p1,generador=p21,codigo_usuario="7807004",
         #frecuencia=Hz,  potencia_activa=Mw, potencia_reactiva=Mvar, temperatura_promedio=°C, temperatura_calent=°C, humedad_relativa=%,
         frecuencia=59.95,  potencia_activa=19.06, potencia_reactiva=3.9, temperatura_promedio=68.43, temperatura_calent=0, humedad_relativa=75, CAG="SI",
         NQNC1posA1= 1573, NQNC2posA1=570 , NQNC1negA1=1483, NQNC2negA1=522, QMAXC1posA1=330, QMAXC2posA1=199, QMAXC1negA1=330, QMAXC2negA1=150, 
         NQNC1posB1= 808, NQNC2posB1= 1255, NQNC1negB1=555, NQNC2negB1=565, QMAXC1posB1=199, QMAXC2posB1=43, QMAXC1negB1=120, QMAXC2negB1=120, 
         NQNC1posC1= 1755, NQNC2posC1= 1609, NQNC1negC1=1302, NQNC2negC1=651, QMAXC1posC1=154, QMAXC2posC1=43, QMAXC1negC1=72, QMAXC2negC1=120, 
 
         NQNC3posA2= 0, NQNC4posA2= 0, NQNC3negA2=0,NQNC4negA2=0, QMAXC3posA2=0, QMAXC4posA2=0, QMAXC3negA2=0, QMAXC4negA2=0, 
         NQNC3posB2= 0, NQNC4posB2= 0, NQNC3negB2=0,NQNC4negB2=0, QMAXC3posB2=0, QMAXC4posB2=0, QMAXC3negB2=0, QMAXC4negB2=0, 
         NQNC3posC2= 0, NQNC4posC2= 0, NQNC3negC2=0,NQNC4negC2=0, QMAXC3posC2=0, QMAXC4posC2=0, QMAXC3negC2=0, QMAXC4negC2=0, 
         
         fecha_ingreso=date,fecha_del_analisis=date)
    p31.save()

    return render(request,'principal.html',locals())