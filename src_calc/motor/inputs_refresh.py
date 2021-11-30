# -*- coding: utf-8 -*-
"""
Created on Wed Jan 01 20:00:29 2020 

@author: Ing. Daniel Villarreal
"""

def ingr_actual_a(lista_los_mejores, lista_final_pv_bajo, lista_minimo_peso_variabilidad, ingreso_datos):

    if (len(lista_los_mejores)) != 0:    
        
        ingreso_datos_a = []
        for lista_final_pv_bajo in lista_minimo_peso_variabilidad: # ================================================ 3.
            
            if len(lista_final_pv_bajo) != 0:
                
                for i in range(0,len(ingreso_datos)):
                    if ingreso_datos[i][1] == 'Beam':
                        ingreso_datos[i][14]= lista_final_pv_bajo[0][(len(lista_final_pv_bajo[0])//2)+ingreso_datos[i][2]-1]
                    else:
                        ingreso_datos[i][14]=lista_final_pv_bajo[0][ingreso_datos[i][2]-1]
                        
            ingreso_datos_a.extend(ingreso_datos)
                    
                        
    return ingreso_datos_a







def ingr_actual_b(lista_los_mejores, lista_final_p_bajo, Opcion_pesominimo, ingreso_datos):

    if (len(lista_los_mejores)) != 0:                       
        
        ingreso_datos_b = []        
        for lista_final_p_bajo in Opcion_pesominimo: # ================================================ 3.
    
            if len(lista_final_p_bajo) != 0:
                
                for i in range(0,len(ingreso_datos)):
                    if ingreso_datos[i][1] == 'Beam':
                        ingreso_datos[i][14]= lista_final_p_bajo[0][(len(lista_final_p_bajo[0])//2)+ingreso_datos[i][2]-1]
                    else:
                        ingreso_datos[i][14]=lista_final_p_bajo[0][ingreso_datos[i][2]-1]
    
            ingreso_datos_b.extend(ingreso_datos)
    
                        
    return ingreso_datos_b

