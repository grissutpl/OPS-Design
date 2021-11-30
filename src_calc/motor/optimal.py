# -*- coding: utf-8 -*-
"""
Created on Wed Jan 01 20:00:29 2020 

@author: Ing. Daniel Villarreal
"""

import itertools # Librería para generar combinaciones random

from src_calc.loggerPrint import Logger

from src_calc.methods.inputs_excel import ingreso_de_datos_excel
from src_calc.methods.dataprogram import DatosPrograma
from src_calc.methods.mselection import selectionBeamCol
from src_calc.motor.validation import constraintValidation

def optimalframe(D_optimizator, D_criterio, D_nodos_totales, D_nodos_restringidos, ExcelPrincipal, DatosPrincipales, Perfil_Data):
    
    my_console = Logger('src_calc/files/optimice_motor.txt') 

    ingreso_datos = ingreso_de_datos_excel(DatosPrincipales)
    
    for i in range(len(ingreso_datos)):
        if ingreso_datos[i][2] > 2:

            if ingreso_datos[i][2] == 1 or ingreso_datos[i][2] == 2:
                ingreso_datos[i][2] = 1
        
            elif ingreso_datos[i][2] == 3 or ingreso_datos[i][2] == 4:
                ingreso_datos[i][2] = 2   
                
            elif ingreso_datos[i][2] == 5 or ingreso_datos[i][2] == 6:
                ingreso_datos[i][2] = 3
                
            elif ingreso_datos[i][2] == 7 or ingreso_datos[i][2] == 8:
                ingreso_datos[i][2] = 4 
                
            elif ingreso_datos[i][2] == 9 or ingreso_datos[i][2] == 10:
                ingreso_datos[i][2] = 5          
    

#        Perfil_Data = ExcelPrincipal.parse('W') #---> La subbase de DatosPrincipales utilizada 'Perfil_Data' será la perteneciente 
                                                      #     a la hoja del excel que corresponda.
    ingreso_datos, DatosPrincipales_actualizados = DatosPrograma(D_criterio, ingreso_datos, ExcelPrincipal) 

    dict_vigas_final, dict_columas_final, lista_TodasColumnasAptas_dePisos, lista_TodasVigasAptas_dePisos, lista_posibles_combinaciones, cantidad_pisos_columnas, perfiles_aprobados = selectionBeamCol(D_nodos_totales, D_nodos_restringidos, D_criterio, ExcelPrincipal, DatosPrincipales, Perfil_Data)

#        lista_posibles_combinaciones = []
    contador = 0
    lista_los_mejores = []

    # Defino Lista para el plot del optimizador
    lista_Peso_estructural = []

    
    list_of_all_combination = list(itertools.product(*lista_posibles_combinaciones))
    n =len(ingreso_datos)

    for lista_posibles in list_of_all_combination:
        for i in range(0,n):
            if ingreso_datos[i][1] == 'Beam':
                ingreso_datos[i][14]=lista_posibles[cantidad_pisos_columnas + ingreso_datos[i][2] -1]
            else:
                ingreso_datos[i][14]=lista_posibles[ingreso_datos[i][2] -1]
                
        contador , lista_Peso_estructural, lista_los_mejores = constraintValidation(D_criterio, contador, ingreso_datos, lista_posibles, lista_Peso_estructural, lista_los_mejores, 0, D_optimizator, perfiles_aprobados, ExcelPrincipal, D_nodos_totales, D_nodos_restringidos)
        


    if len(lista_los_mejores) == 0:
        for lista_posibles in list_of_all_combination:
            for i in range(0,n):
                if ingreso_datos[i][1] == 'Beam':
                    ingreso_datos[i][14]=lista_posibles[cantidad_pisos_columnas + ingreso_datos[i][2] -1]
                else:
                    ingreso_datos[i][14]=lista_posibles[ingreso_datos[i][2] -1]
                    
            contador , lista_Peso_estructural, lista_los_mejores = constraintValidation(D_criterio, contador, ingreso_datos, lista_posibles, lista_Peso_estructural, lista_los_mejores, 1, D_optimizator, perfiles_aprobados, ExcelPrincipal, D_nodos_totales, D_nodos_restringidos)



    
    lista_Peso_estructural.sort(reverse=True)

    if len(lista_los_mejores) != 0:
        
        print('')
        print(170*'=')
        print(170*'=')
        
        print('\n',"The most optimal options :",'\n')        
        for i in lista_los_mejores: # ================================================ 3.
            list_data_final = []
            list_data_final.extend([i[0],i[1],i[2],i[3],i[4],i[5]])
            print(list_data_final) 
    
        valor_minimo_variabilidad = 1
        list_variabilidad_final = []
        for lista_auxiliar in lista_los_mejores: # ================================================ 3.
            if lista_auxiliar[5] < valor_minimo_variabilidad:
                list_variabilidad_final.clear()
                valor_minimo_variabilidad = lista_auxiliar[5]
                list_variabilidad_final.append(lista_auxiliar)
            elif lista_auxiliar[5] == valor_minimo_variabilidad:
                list_variabilidad_final.append(lista_auxiliar)
        print('')
        print(170*'=')
        print(170*'=')

        print('\n','Representative Optimal Designs:')
        if len(list_variabilidad_final) >= 1:
            print('\n',"1.- Lower constructive complexity index:",'\n')
            valor_minimo_peso_variabilidad = list_variabilidad_final[0][3]
            lista_minimo_peso_variabilidad = []
            lista_minimo_peso_variabilidad.append(list_variabilidad_final[0])
            for lista_aux in list_variabilidad_final: # ================================================ 3.
                if lista_aux[3] < valor_minimo_peso_variabilidad:
                    valor_minimo_peso_variabilidad = lista_aux[3]
                    lista_minimo_peso_variabilidad.clear()
                    lista_minimo_peso_variabilidad.append(lista_aux)
            
            for lista_final_pv_bajo in lista_minimo_peso_variabilidad: # ================================================ 3.
                print('    ',lista_final_pv_bajo) 
    
        print('\n',"2.- Lowest possible weight:",'\n')
        valor_minimo_peso = lista_los_mejores[0][3]
        Opcion_pesominimo = []
        Opcion_pesominimo.append(lista_los_mejores[0])
        for lista_comprobar in lista_los_mejores: # ================================================ 3.
            if lista_comprobar[3] < valor_minimo_peso:
                Opcion_pesominimo.clear()
                Opcion_pesominimo.append(lista_comprobar)
                valor_minimo_peso = lista_comprobar[3]
        
        for lista_final_p_bajo in Opcion_pesominimo: # ================================================ 3.
                print('    ',lista_final_p_bajo) 

    else:
        print("THERE ARE NO AN OPTIMAL OPTION.")
        lista_final_pv_bajo = 'NONE'
        lista_minimo_peso_variabilidad = 'NONE'
        
        lista_final_p_bajo = 'NONE'
        lista_los_mejores = 'NONE'
        Opcion_pesominimo = 'NONE'
        lista_Peso_estructural = 'NONE'
        



    print('')    
    print(170*'=') 
    print(170*'=')
    
    print('\n','✔✔✔ The optimization process has been finished successfully, close this window and then go to see the results. ✔✔✔','\n')

    print(170*'=')
    print(170*'=')

    my_console.close()
    
    return lista_final_pv_bajo, lista_final_p_bajo, perfiles_aprobados, lista_los_mejores, lista_minimo_peso_variabilidad, Opcion_pesominimo, lista_Peso_estructural, ingreso_datos
        
