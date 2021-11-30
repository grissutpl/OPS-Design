# -*- coding: utf-8 -*-
"""
Created on Wed Jan 01 20:00:29 2020 

@author: Ing. Daniel Villarreal
"""

def Comp_Eficc(ExcelPrincipal, ingreso_datos, perfiles_aprobados, D_optimizator):

    caracteristicas = []    
    for i in range(len(ingreso_datos)): 
        
        if D_optimizator == 1:
            Perfil_Data = perfiles_aprobados
            
        elif D_optimizator == 0:
            Perfil_Data = ExcelPrincipal.parse('W')     
            
        for j in range(len(Perfil_Data)): 
            if ingreso_datos[i][14] == Perfil_Data.values[j][0]: 
                                                                
                caracteristicas.append([Perfil_Data.values[j][1], Perfil_Data.values[j][2], Perfil_Data.values[j][3], 
                                        Perfil_Data.values[j][4], Perfil_Data.values[j][5], Perfil_Data.values[j][6], 
                                        Perfil_Data.values[j][7], Perfil_Data.values[j][8], Perfil_Data.values[j][9], 
                                        Perfil_Data.values[j][10], Perfil_Data.values[j][11], Perfil_Data.values[j][12], 
                                        Perfil_Data.values[j][13], Perfil_Data.values[j][14], Perfil_Data.values[j][15], 
                                        Perfil_Data.values[j][16], Perfil_Data.values[j][17], Perfil_Data.values[j][18], 
                                        Perfil_Data.values[j][19], Perfil_Data.values[j][20], Perfil_Data.values[j][21], 
                                        Perfil_Data.values[j][22], Perfil_Data.values[j][23], Perfil_Data.values[j][24], 
                                        Perfil_Data.values[j][25], Perfil_Data.values[j][26], Perfil_Data.values[j][27], 
                                        Perfil_Data.values[j][28], Perfil_Data.values[j][29], Perfil_Data.values[j][30],
                                        Perfil_Data.values[j][31]]) 
    Restriccion_MiembroCompresiones = []
    for i in range(len(ingreso_datos)):
        if ingreso_datos[i][1] == 'Column':
            Restriccion_MiembroCompresion = round(caracteristicas[i][15]/caracteristicas[i][9],3) 
            Restriccion_MiembroCompresiones.append(Restriccion_MiembroCompresion)
            
    return Restriccion_MiembroCompresion, Restriccion_MiembroCompresiones