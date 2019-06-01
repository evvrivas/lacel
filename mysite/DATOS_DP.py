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

    date=datetime.datetime(2019,2,4,15,01)
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