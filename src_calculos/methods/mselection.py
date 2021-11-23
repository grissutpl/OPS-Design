# -*- coding: utf-8 -*-
"""
Created on Wed Jan 01 20:00:29 2020 

@author: Ing. Daniel Villarreal
"""

import pandas as pd # Conectar con hojas de excel
import numpy as np # Creación de matrices

#from loggerPrint import Logger


def selectionBeamCol(D_nodos_totales, D_nodos_restringidos, D_criterio, ExcelPrincipal, DatosPrincipales, Perfil_Data):

#    my_console = Logger('files/preselect.txt') 

    #ExcelPrincipal = pd.ExcelFile('DatosExcel.xlsx')
    #DatosPrincipales = ExcelPrincipal.parse('Datos') #--> DatosPrincipalesPrincipales

    print('Mensaje: La limpieza de variables se ha completado exitosamente ✔✔✔✔✔✔✔✔✔✔')
    print('')
    print('Programa: OPS Design')  
    print('Autor de Proyecto: Ing. Daniel Villarreal Leiva')      
    print('Director TFT: Ing. Henrry Rojas Asuero, MSc.')      
    
#    height = max(DatosPrincipales['y(j)'])
#    lenght = max(DatosPrincipales['x(j)'])
    print('')    
    print(174*'=')
    print(174*'=')
#    print('\n','Preselección de elementos estructurales en vigas y columnas:')
#    print(' ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')

    
    ingreso_predatos = []
    for i in range(len(DatosPrincipales)):
        ingreso_predatos.append([DatosPrincipales.values[i][0], DatosPrincipales.values[i][1], DatosPrincipales.values[i][2], 
                            DatosPrincipales.values[i][3], DatosPrincipales.values[i][4], DatosPrincipales.values[i][5], 
                            DatosPrincipales.values[i][6], DatosPrincipales.values[i][7], DatosPrincipales.values[i][8],
                            DatosPrincipales.values[i][9], DatosPrincipales.values[i][10], DatosPrincipales.values[i][11],
                            DatosPrincipales.values[i][12], DatosPrincipales.values[i][15], DatosPrincipales.values[i][16], 
                            DatosPrincipales.values[i][17], DatosPrincipales.values[i][18], DatosPrincipales.values[i][19], 
                            DatosPrincipales.values[i][20], DatosPrincipales.values[i][21], DatosPrincipales.values[i][22]]) 
    

#    predatos = pd.DataFrame(ingreso_predatos)
    
    nl = D_nodos_totales - D_nodos_restringidos       
    ngdlt_t = D_nodos_totales * 3                  
    ngdlt_l = nl * 3
    ngdlt_r = D_nodos_restringidos * 3                 
    
    kGE = np.zeros((ngdlt_t,ngdlt_t))    
    QcE = np.zeros((ngdlt_t,1))    
    
    
    mt_lista = []
    rse_lista = [] 
    sel_lista = [] 
    kle_lista = []
    Sg_lista = []
    ind_lista = [] 
    
    
    for i in range(len(ingreso_predatos)): 
    
        kgi = np.zeros((ngdlt_t,ngdlt_t)) 
        Qci = np.zeros((ngdlt_t,1)) 
    
        indx = np.array([ingreso_predatos[i][3], ingreso_predatos[i][4], ingreso_predatos[i][5],
                        ingreso_predatos[i][6], ingreso_predatos[i][7], ingreso_predatos[i][8]])  
        ind_lista.append(indx-1) #--> Extraigo los índices para cada elemento, dentro del bucle i 
        
        Lpre = round(np.sqrt((ingreso_predatos[i][11]-ingreso_predatos[i][9])**2+(ingreso_predatos[i][12]-ingreso_predatos[i][10])**2),3)
        
        lx_pre = (ingreso_predatos[i][11]-ingreso_predatos[i][9])/Lpre
        ly_pre = (ingreso_predatos[i][12]-ingreso_predatos[i][10])/Lpre        
        
        w_pre = ingreso_predatos[i][13]    
        p_pre = 1.2*ingreso_predatos[i][14]
        m1_pre = ingreso_predatos[i][15]
        m2_pre = ingreso_predatos[i][16]
        v1_pre = ingreso_predatos[i][17]
        v2_pre = ingreso_predatos[i][18]
        ax1_pre = ingreso_predatos[i][19]
        ax2_pre = ingreso_predatos[i][20]
        
    
        mt_pre = np.array([[lx_pre,  ly_pre,       0,        0,        0,    0],
                        [-ly_pre, lx_pre,       0,        0,        0,    0],
                        [0,            0,       1,        0,        0,    0],
                        [0,            0,       0,   lx_pre,   ly_pre,    0],
                        [0,            0,       0,  -ly_pre,   lx_pre,    0],
                        [0,            0,       0,        0,        0,    1]])
        mt_lista.append(mt_pre)
        mt_pre_traspuesta = mt_pre.transpose()
    
        rse = np.array([0,    w_pre*Lpre/2+p_pre/2,   (w_pre*Lpre**2)/12+p_pre*Lpre/8,   0,     w_pre*Lpre/2+p_pre/2,   (-w_pre*Lpre**2)/12-p_pre*Lpre/8])
        rse_lista.append(rse)
        
        se = np.array([ax1_pre,    w_pre*Lpre/2+p_pre/2+v1_pre,   (w_pre*Lpre**2)/12+p_pre*Lpre/8+m1_pre,   ax2_pre,     w_pre*Lpre/2+p_pre/2+v2_pre,   (-w_pre*Lpre**2)/12-p_pre*Lpre/8+m2_pre])    
        sel_lista.append(se)
    
        Sg = np.dot(mt_pre_traspuesta,se)
        Sg_lista.append(Sg)
    
        Qci[ind_lista[i], 0] = Sg # Me ubica los valores del vector de cargas local a global para el ensamblaje 
        for row in range(ngdlt_t):
            QcE[row]+=Qci[row] # Me suma los valores de cada vector ensamblado de cada elemento para cada fila 
    
    
        kle = np.array([[ 1, 0, 0,-1, 0, 0],
                        [ 0, 1, 1, 0,-1, 1],
                        [ 0, 1, 1, 0,-1, 1],
                        [-1, 0, 0, 1, 0, 0],
                        [ 0,-1,-1, 0, 1,-1],
                        [ 0, 1, 1, 0,-1, 1]])
        kle_lista.append(kle)
        kge = np.dot(np.dot(mt_pre_traspuesta,kle),mt_pre)
        kgi[np.ix_(ind_lista[i], ind_lista[i])] = kge # Me ubica los valores de la matriz de rigidez local a global para 
                                                                # el ensamblaje
        for row in range(ngdlt_t):
            for col in range(ngdlt_t):
                kGE[row][col] +=  kgi[row][col] # Me suma los valores de cada matriz ensamblada de cada elemento
    
    
    k11_pre = kGE[ :ngdlt_l , :ngdlt_l] 
    k11_inversa_pre = np.linalg.inv(k11_pre)
    Qcle = QcE[ :ngdlt_l]     
    
    QcE = np.zeros((ngdlt_r,1))         
    qnce = np.dot(k11_inversa_pre, Qcle)
    qe = np.append(qnce, QcE)
    
    
    Pre_Fuerzas = []
    for i in range(len(ingreso_predatos)): #--> Para cada fila en el rango de 'ingreso de DatosPrincipales'[i]...
        
        qe_i = qe[ ind_lista[i] ]
        Pre_Fuerza = np.round(np.dot(np.dot(kle_lista[i], mt_lista[i]), qe_i) - rse_lista[i],3)
        Pre_Fuerzas.append(Pre_Fuerza)
        
    print('\n', 'Secciones privilegiadas aptas para vigas: ') 
    
    dict_vigas = {} #--> Diccionario para alojar mis vigas preseleccionadas
    listaPiso_Zx_Vigas = [] #--> Lista que agrupa características de: Piso, Z_req, y Secciones
    
    for i in range(len(ingreso_predatos)): #--> Para cada fila en el rango de 'ingreso de DatosPrincipales'[i]...

        if ingreso_predatos[i][2] > 2:

            if ingreso_predatos[i][2] == 1 or ingreso_predatos[i][2] == 2:
                ingreso_predatos[i][2] = 1
        
            elif ingreso_predatos[i][2] == 3 or ingreso_predatos[i][2] == 4:
                ingreso_predatos[i][2] = 2   
                
            elif ingreso_predatos[i][2] == 5 or ingreso_predatos[i][2] == 6:
                ingreso_predatos[i][2] = 3
                
            elif ingreso_predatos[i][2] == 7 or ingreso_predatos[i][2] == 8:
                ingreso_predatos[i][2] = 4 
                
            elif ingreso_predatos[i][2] == 9 or ingreso_predatos[i][2] == 10:
                ingreso_predatos[i][2] = 5  
    
        perfilesw = ExcelPrincipal.parse('W') #--> Base de datos de perfiles W
#        proporcion_estructura_H_A = height/lenght
            
        if ingreso_predatos[i][1] == 'Vig':
            #--> Fórmulas para el predimensionamiento en vigas
            key = ingreso_predatos[i][2]
            muv = max(abs(Pre_Fuerzas[i][2]), abs(Pre_Fuerzas[i][5]))
            z_req = muv / (0.9 * 25310506.54)
            

            if D_criterio == 1 or D_criterio == 2:
                pass
                    
            elif D_criterio == 0:                    
                    
                aptos_zx_lista = []
                for perf in range(len(perfilesw)):        
                    cv = z_req - perfilesw.values[perf][13]
                    
                    if (cv*10000) > -1.2 and (cv*10000) < -0.5: 
                        aptos_zx = perfilesw.values[perf][0]
                        aptos_zx_lista.append(aptos_zx)
                
                listaPiso_Zx_Vigas.append([key,z_req,aptos_zx_lista])
                
                if key not in dict_vigas:
                    dict_vigas[key] = []
                dict_vigas[key].append(z_req)
                dict_vigas = {key:[max(valor)] for key, valor in dict_vigas.items()} 
    
    
    for variable_lista in listaPiso_Zx_Vigas:
        valor_key = dict_vigas[variable_lista[0]][0]
        
        valor_lista = variable_lista[1] 
        if valor_key == valor_lista:
            dict_vigas[variable_lista[0]]=variable_lista[2] 
    
    
    # -----------------------------------------------------------------------------@
    
    lista_TodasVigasAptas_dePisos = []
    for i in range(len(dict_vigas)):
        for j in dict_vigas[i+1]:
            if  (j in lista_TodasVigasAptas_dePisos) == False: 
                lista_TodasVigasAptas_dePisos.append(j)
    
    dict_vigas_final = {}
    for i in range(len(dict_vigas)):
        dict_vigas_final[i+1] = lista_TodasVigasAptas_dePisos
    
    print(dict_vigas_final)
    
    # -----------------------------------------------------------------------------@
    
    
    print('\n', 'Secciones privilegiadas aptas para columnas: ') 
    
    dict_pm = {}    
    
    for i in range(len(ingreso_predatos)): 
        if ingreso_predatos[i][1] == 'Col': 
            key = ingreso_predatos[i][2]        
            dict_pm[key]= [0,0] 
    
    for i in range(len(ingreso_predatos)):        
        if ingreso_predatos[i][1] == 'Col': 
            
            key = ingreso_predatos[i][2]        
            puc = max(abs(Pre_Fuerzas[i][0]), abs(Pre_Fuerzas[i][3]))
            muc = max(abs(Pre_Fuerzas[i][2]), abs(Pre_Fuerzas[i][5]))
            
            if puc > dict_pm[key][0]:
                dict_pm[key] = [puc, dict_pm[key][1]] # --> Máximo de la clave
            if muc > dict_pm[key][1]:
                dict_pm[key] = [dict_pm[key][0],muc] # --> Máximo de la clave 
    
    
    Columnas_perfilesw = ExcelPrincipal.parse('CP_W') #--> Cargo
    datos_para_operar = [] 
    
    for i in range(len(Columnas_perfilesw)):
        for valores_key in range(len(dict_pm)):
            lista_CPW_aux = []
            for j in range(135):
                lista_CPW_aux.append(Columnas_perfilesw.values[i][j])
                                                                    
            
            # Extraigo los valores de Puc y Muc para operarlos en el dataframe 
            puc_max = dict_pm[valores_key+1][0]
            muc_max = dict_pm[valores_key+1][1]
    
            muc_p = muc_max / lista_CPW_aux[1] #--> Opero Mu/Mn
    
            
            if D_criterio == 1 or D_criterio == 2:
                pass
                                                                                
            elif D_criterio == 0:
                validation_colum = True
                for j in range(133):
                    puc_p = puc_max / lista_CPW_aux[j+2] 
                  
                    if puc_p >= 0.2:
                        cc = puc_p + (8/9)* muc_p
                        if cc < 0.9 or cc > 1.8: 
                            validation_colum = False   
                            break
                    else:
                        cc = puc_p/2 + muc_p
                        if cc < 0.9 or cc > 1.8: 
                            validation_colum = False   
                            break
                if validation_colum == True:
                    datos_para_operar.append([valores_key + 1,lista_CPW_aux[0]]) #--> Aquí añado el piso y las
    
    lista_TodasColumnasAptas_dePisos = []
    for i in range(len(datos_para_operar)):
        if (datos_para_operar[i][1] in lista_TodasColumnasAptas_dePisos) == False: #--> De esta manera hago comparaciones y agrego cada vez los que faltan
            lista_TodasColumnasAptas_dePisos.append(datos_para_operar[i][1])
    
    dict_columas_final = {}
    for i in range(len(dict_pm)):
        dict_columas_final[i+1] = lista_TodasColumnasAptas_dePisos
    
    print(dict_columas_final)
    


# VAMOS A RETORNAR ESTO DESDE ESTA FUNCIÓN, NO DESDE EL MAIN, PORQUE ASÍ DEBERÍA SER DE ACUERDO A LAS COSAS QUE DESEMPEÑA ESTA FUNCIÓN
   
    # LA IDEA ES QUE EL MAIN SEA UNA FUNCIÓN DE ENTRADA Y SALIDA DE COSAS, NADA MAS, NO QUE EJECUTE PROCESOS.
    
    # ESTO PARA FACILITAR LOS DISEÑOS DE QT


    lista_posibles_combinaciones = []


    cantidad_pisos_columnas = len(dict_columas_final) 
    cantidad_pisos_vigas = len(dict_vigas_final)

    CombinacionesPosibles = ((len(lista_TodasColumnasAptas_dePisos))**cantidad_pisos_columnas) * ((len(lista_TodasVigasAptas_dePisos))**cantidad_pisos_vigas)
    print('\n','El número máximo de combinaciones posibles para este ejemplo es de: ',CombinacionesPosibles)

    print('\n','Combinaciones Validadas: ')
    
    for i in range(len(dict_columas_final)):
        lista_posibles_combinaciones.append(dict_columas_final[i+1])

    for i in range(len(dict_vigas_final)):
        lista_posibles_combinaciones.append(dict_vigas_final[i+1])


    lista_sin_repetir_perfiles = []
    for lista_valores in lista_posibles_combinaciones:
        for valores in lista_valores:
            if (valores in lista_sin_repetir_perfiles) == False:
                lista_sin_repetir_perfiles.append(valores)

    datos_totales = []
    for i in range(len(lista_sin_repetir_perfiles)):
        for j in range(len(Perfil_Data)): #--> Para cada fila en el rango de 'Pefil_Data' [j]...
            if lista_sin_repetir_perfiles[i] == Perfil_Data.values[j][0]: #--> Si el valor de 'ingreso_datos' en [13] es igual a la
                                                                 #    primera columna de 'Perfil_Data'...
                datos_totales.append([Perfil_Data.values[j][0],Perfil_Data.values[j][1], Perfil_Data.values[j][2], Perfil_Data.values[j][3], 
                                        Perfil_Data.values[j][4], Perfil_Data.values[j][5], Perfil_Data.values[j][6], 
                                        Perfil_Data.values[j][7], Perfil_Data.values[j][8], Perfil_Data.values[j][9], 
                                        Perfil_Data.values[j][10], Perfil_Data.values[j][11], Perfil_Data.values[j][12], 
                                        Perfil_Data.values[j][13], Perfil_Data.values[j][14], Perfil_Data.values[j][15], 
                                        Perfil_Data.values[j][16], Perfil_Data.values[j][17], Perfil_Data.values[j][18], 
                                        Perfil_Data.values[j][19], Perfil_Data.values[j][20], Perfil_Data.values[j][21], 
                                        Perfil_Data.values[j][22], Perfil_Data.values[j][23], Perfil_Data.values[j][24], 
                                        Perfil_Data.values[j][25], Perfil_Data.values[j][26], Perfil_Data.values[j][27], 
                                        Perfil_Data.values[j][28], Perfil_Data.values[j][29], Perfil_Data.values[j][30],
                                        Perfil_Data.values[j][31]]) #--> Entonces agrega sus correspondientes valores en tabla    

    perfiles_aprobados = pd.DataFrame(datos_totales,columns=('1', '2', '3','4', '5', '6','7', '8', '9','10','11', '12', '13','14', '15', '16',
                                                             '17', '18', '19','20','21', '22', '23','24', '25', '26','27', '28', '29','30', '31', '32'))



#    my_console.close()
    
    return dict_vigas_final, dict_columas_final, lista_TodasColumnasAptas_dePisos, lista_TodasVigasAptas_dePisos, lista_posibles_combinaciones, cantidad_pisos_columnas, perfiles_aprobados 
