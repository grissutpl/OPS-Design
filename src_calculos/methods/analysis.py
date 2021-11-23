# -*- coding: utf-8 -*-
"""
Created on Wed Jan 01 20:00:29 2020 

@author: Ing. Daniel Villarreal
"""

import pandas as pd # Conectar con hojas de excel
import numpy as np # Creación de matrices


def analisis(ExcelPrincipal,D_nodos_totales, D_nodos_restringidos, D_criterio, ingreso_datos, D_optimizator, perfiles_aprobados):

    nodos_libres = D_nodos_totales - D_nodos_restringidos       
    nGDL_totales = D_nodos_totales * 3                   
    nGDL_libres = nodos_libres * 3                 
    nGDL_restringidos = D_nodos_restringidos * 3               
    
    k_global_estructura = np.zeros((nGDL_totales,nGDL_totales))   
                                                                   
                                                                   
    Qc_estructura = np.zeros((nGDL_totales,1))    
    PesoEstructural = 0    
    
    m_transf_demo = []
    rs_elemento_demo = [] 
    s_elementaLongitudes = [] 
    k_local_elemento_demo = []
    S_globaLongitudes = []
    Longitudes = []
    indices = [] # new list
    
    caracteristicas = []    
    for i in range(len(ingreso_datos)): #--> Para cada fila en el rango de 'ingreso de DatosPrincipales'[i]...
    
        k_global_i = np.zeros((nGDL_totales,nGDL_totales)) 
        Qc_i = np.zeros((nGDL_totales,1)) 
    
        index = np.array([ingreso_datos[i][3], ingreso_datos[i][4], ingreso_datos[i][5],
                        ingreso_datos[i][6], ingreso_datos[i][7], ingreso_datos[i][8]])  
        indices.append(index-1) #--> Extraigo los índices para cada elemento, dentro del bucle i 
    
        # DatosPrincipales geométricos del proyecto por coordenadas.       
        xi = ingreso_datos[i][9]
        yi = ingreso_datos[i][10]
        xf = ingreso_datos[i][11]
        yf = ingreso_datos[i][12]

        
        L = round(np.sqrt((xf-xi)**2+(yf-yi)**2),3)
        Longitudes.append(L)
        
        lx = (ingreso_datos[i][11]-ingreso_datos[i][9])/L
        ly = (ingreso_datos[i][12]-ingreso_datos[i][10])/L        
        
    #    w = ingreso_datos[i][15]
    #    p = ingreso_datos[i][18]
        if D_criterio == 0:
            w = ingreso_datos[i][15]    
            p = 1.2*ingreso_datos[i][16]
            
        elif D_criterio == 1 or D_criterio == 2:
            pass
            
        m1 = ingreso_datos[i][17]
        m2 = ingreso_datos[i][18]
        v1 = ingreso_datos[i][19]
        v2 = ingreso_datos[i][20]
        ax1 = ingreso_datos[i][21]
        ax2 = ingreso_datos[i][22]
        
#        Perfil_Data = ExcelPrincipal.parse('W')
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
        
        A = caracteristicas [i][6]              
        Ixx = caracteristicas [i][8]            
        #Iyy = caracteristicas [i][14]           
        E = caracteristicas [i][29]             
        Poisson = caracteristicas [i][30]      
        G = E/(2*(1+Poisson))                   
        Acorte = 5*A/6                          
        Fhi = (12*E*Ixx)/(G*Acorte*L**2)        
         
    
        m_transf = np.array([[lx,  ly,    0,    0,    0,    0],
                             [-ly, lx,    0,    0,    0,    0],
                             [0,    0,    1,    0,    0,    0],
                             [0,    0,    0,   lx,   ly,    0],
                             [0,    0,    0,  -ly,   lx,    0],
                             [0,    0,    0,    0,    0,    1]])
        
        m_transf_demo.append(m_transf)
        
        
        m_transf_traspuesta = m_transf.transpose()
    
    
        rs_elemento = np.array([0,    w*L/2+p/2,   (w*L**2)/12+p*L/8,   0,     w*L/2+p/2,   (-w*L**2)/12-p*L/8])
        rs_elemento_demo.append(rs_elemento)
        
    
        s_elemental = np.array([ax1,    w*L/2+p/2+v1,   (w*L**2)/12+p*L/8+m1,   ax2,     w*L/2+p/2+v2,   (-w*L**2)/12-p*L/8+m2])    
        s_elementaLongitudes.append(s_elemental)
    
        
        S_global = np.dot(m_transf_traspuesta,s_elemental)
        S_globaLongitudes.append(S_global)
    
    
        Qc_i[indices[i], 0] = S_global # Me ubica los valores del vector de cargas local a global para el ensamblaje 
        for row in range(nGDL_totales):
            Qc_estructura[row]+=Qc_i[row] # Me suma los valores de cada vector ensamblado de cada elemento para cada fila 
     
     
        k_local_elemento = np.array([[ A*E/L,                         0,                        0,  -A*E/L,                         0,                        0],
                                     [     0,   (12/(1+Fhi))*E*Ixx/L**3,   (6/(1+Fhi))*E*Ixx/L**2,       0,  -(12/(1+Fhi))*E*Ixx/L**3,   (6/(1+Fhi))*E*Ixx/L**2],
                                     [     0,    (6/(1+Fhi))*E*Ixx/L**2,  (4+Fhi)/(1+Fhi)*E*Ixx/L,       0,   -(6/(1+Fhi))*E*Ixx/L**2,  (2-Fhi)/(1+Fhi)*E*Ixx/L],
                                     [-A*E/L,                         0,                        0,   A*E/L,                         0,                        0],
                                     [     0,  -(12/(1+Fhi))*E*Ixx/L**3,  -(6/(1+Fhi))*E*Ixx/L**2,       0,   (12/(1+Fhi))*E*Ixx/L**3,  -(6/(1+Fhi))*E*Ixx/L**2],
                                     [     0,    (6/(1+Fhi))*E*Ixx/L**2,  (2-Fhi)/(1+Fhi)*E*Ixx/L,       0,   -(6/(1+Fhi))*E*Ixx/L**2,  (4+Fhi)/(1+Fhi)*E*Ixx/L]])
        k_local_elemento_demo.append(k_local_elemento)
    
        
        k_global_elemento = np.dot(np.dot(m_transf_traspuesta,k_local_elemento),m_transf)
    
    
        k_global_i[np.ix_(indices[i], indices[i])] = k_global_elemento # Me ubica los valores de la matriz de rigidez local a global para 
                                                                 # el ensamblaje
        for row in range(nGDL_totales):
            for col in range(nGDL_totales):
                k_global_estructura[row][col] +=  k_global_i[row][col] # Me suma los valores de cada matriz ensamblada de cada elemento
                                                                       # para cada fila y columna

        k_global_estructura_presentacion = pd.DataFrame(k_global_estructura)
        pd.set_option('display.float_format', '{:.2g}'.format)
        k_global_estructura_presentacion_print = k_global_estructura_presentacion.to_string()

        PesoElemento = L*caracteristicas[i][7]
        PesoEstructural += round(PesoElemento,3) 

    
    k11 = k_global_estructura[ :nGDL_libres , :nGDL_libres] 
    
    k11_inversa = np.linalg.inv(k11)
    
    k21 = k_global_estructura[ nGDL_libres :nGDL_totales, :nGDL_libres]
    k22 = k_global_estructura[ nGDL_libres :nGDL_totales, nGDL_libres:nGDL_totales]
    
    Qc_libre_estructura = Qc_estructura[ :nGDL_libres]     
    
    
    qc_estructura = np.zeros((nGDL_restringidos,1))         
        
    
    J_estructura = Qc_estructura[ nGDL_libres:]  
    
    
    qnc_estructura = np.dot(k11_inversa, Qc_libre_estructura)

    
    Qnc_estructura = np.dot(k21, qnc_estructura) + np.dot(k22, qc_estructura) + J_estructura

    
    q_estructura = np.append(qnc_estructura, qc_estructura)

    
    F_elementos = []
    
    for i in range(len(ingreso_datos)): #--> Para cada fila en el rango de 'ingreso de DatosPrincipales'[i]...
        
        q_estructura_i = q_estructura[ indices[i] ]
    
        F_elemento = np.round(np.dot(np.dot(k_local_elemento_demo[i], m_transf_demo[i]), q_estructura_i) - rs_elemento_demo[i],3)
        F_elementos.append(F_elemento)
        
    return Longitudes, Qc_estructura, k_global_estructura, qnc_estructura, Qnc_estructura, F_elementos , PesoEstructural, nGDL_libres, k_global_estructura_presentacion_print, caracteristicas



