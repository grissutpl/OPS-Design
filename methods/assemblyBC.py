# -*- coding: utf-8 -*-
"""
Created on Wed Jan 01 20:00:29 2020 

@author: Ing. Daniel Villarreal
"""

def unionesVC(ingreso_datos, D_optimizator,perfiles_aprobados,ExcelPrincipal):
    validate = True
    caracteristicas = []
    for i in range(len(ingreso_datos)): #--> Para cada fila en el rango de 'ingreso de DatosPrincipales'[i]...
        if D_optimizator == 1:
            Perfil_Data = perfiles_aprobados
            
        elif D_optimizator == 0:
            Perfil_Data = ExcelPrincipal.parse('W')   
            
        for j in range(len(Perfil_Data)): #--> Para cada fila en el rango de 'Pefil_Data' [j]...
            if ingreso_datos[i][14] == Perfil_Data.values[j][0]: #--> Si el valor de 'ingreso_datos' en [13] es igual a la
                                                                 #    primera columna de 'Perfil_Data'...
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
                                        Perfil_Data.values[j][31]]) #--> Entonces agrega sus correspondientes valores en tabla    
    pares =  []
    for i in range(len(ingreso_datos)):
        for j in range(len(ingreso_datos)):
            if ingreso_datos[i][11] == ingreso_datos[j][9] and ingreso_datos[i][12] == ingreso_datos[j][10]: 
                if ingreso_datos[i][0]+1 != ingreso_datos[j][0]: #--> Filtro listas con números consecutivos
                    pares.append([ingreso_datos[i][0], ingreso_datos[j][0]])     
    
    for i in range(len(ingreso_datos)):
        for j in range(i + 1, len(ingreso_datos)):
            if (ingreso_datos[i][11] == ingreso_datos[j][11] and ingreso_datos[i][12] == ingreso_datos[j][12]): 
                pares.append([ingreso_datos[i][0], ingreso_datos[j][0]])    
     
    for i in range(len(ingreso_datos)):
        for j in range(i + 1, len(ingreso_datos)):
            if (ingreso_datos[i][9] == ingreso_datos[j][9] and ingreso_datos[i][10] == ingreso_datos[j][10]): 
                pares.append([ingreso_datos[j][0], ingreso_datos[i][0]])    
    pares = [[a,b] for a,b in pares if a < b] #--> Filtro y elimino listas donde el primer valor es mayor que el segundo
    
    pares_VigaColumna = []
    for i in range(len(ingreso_datos)):
        for j in range(len(pares)):
            if ingreso_datos[i][0] == pares[j][1] and ingreso_datos[i][1] == 'Beam':
                pares_VigaColumna.append([pares[j][0], pares[j][1]])
    
    pares_ColumnaColumna = [x for x in pares if x not in pares_VigaColumna]
    
    
    pcv1 = []
    for i in range(len(ingreso_datos)): 
        for k in range(len(pares_VigaColumna)):
            if ingreso_datos[i][0] == pares_VigaColumna[k][0]:
                pcv1.append([caracteristicas[i][1]])   
    
    pcv2 = []
    for i in range(len(ingreso_datos)): 
        for k in range(len(pares_VigaColumna)):
            if ingreso_datos[i][0] == pares_VigaColumna[k][1]:
                pcv2.append([caracteristicas[i][1]]) 
    pcc1 = []
    for i in range(len(ingreso_datos)): 
        for k in range(len(pares_ColumnaColumna)):
            if ingreso_datos[i][0] == pares_ColumnaColumna[k][0]:
                pcc1.append([caracteristicas[i][0], caracteristicas[i][1]]) 
    
    pcc2 = []
    for i in range(len(ingreso_datos)): 
        for k in range(len(pares_ColumnaColumna)):
            if ingreso_datos[i][0] == pares_ColumnaColumna[k][1]:
                pcc2.append([caracteristicas[i][0], caracteristicas[i][1]]) 
    

    Restriccion_VigaColumnas = []
    for l in range(len(pcv2)): 
        bv = pcv2[l][0]
        bc = pcv1[l][0] 
        
        Restriccion_VigaColumna = round(bv/bc - 1,3)
        Restriccion_VigaColumnas.append(Restriccion_VigaColumna)
        if Restriccion_VigaColumna > 0:
            validate = False
    
    Restriccion_C2C1_hs = []
    Restriccion_C2C1_bs = []
    if len(pcc2) > 0:
        for m in range(len(pcc2)): 
            hc1 = pcc1[m][0]
            hc2 = pcc2[m][0]
            Restriccion_C2C1_h = round(hc2/hc1-1,3)
            Restriccion_C2C1_hs.append(Restriccion_C2C1_h)
        
            bc1 = pcc1[m][1]
            bc2 = pcc2[m][1]
            Restriccion_C2C1_b = round(bc2/bc1-1,3)
            Restriccion_C2C1_bs.append(Restriccion_C2C1_b)
            if Restriccion_C2C1_h > 0 or Restriccion_C2C1_b >0:
                validate = False
    else:
        Restriccion_C2C1_h = 0
        Restriccion_C2C1_b = 0
        m = 0
        
    return (validate, Restriccion_VigaColumna, Restriccion_C2C1_h, Restriccion_C2C1_b, 
            pares_VigaColumna, pares_ColumnaColumna, l, pcv2, m, pcc2,
            Restriccion_VigaColumnas, Restriccion_C2C1_hs, Restriccion_C2C1_bs)
