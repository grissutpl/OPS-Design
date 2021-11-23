# -*- coding: utf-8 -*-
"""
Created on Wed Jan 01 20:00:29 2020 

@author: Ing. Daniel Villarreal
"""

def ingreso_de_datos_excel(DatosPrincipales):
    ingreso_datos = []
    for i in range(len(DatosPrincipales)):
        ingreso_datos.append([DatosPrincipales.values[i][0], DatosPrincipales.values[i][1], DatosPrincipales.values[i][2], 
                                DatosPrincipales.values[i][3], DatosPrincipales.values[i][4], DatosPrincipales.values[i][5], 
                                DatosPrincipales.values[i][6], DatosPrincipales.values[i][7], DatosPrincipales.values[i][8],
                                DatosPrincipales.values[i][9], DatosPrincipales.values[i][10], DatosPrincipales.values[i][11],
                                DatosPrincipales.values[i][12], DatosPrincipales.values[i][13], DatosPrincipales.values[i][14],
                                DatosPrincipales.values[i][15], DatosPrincipales.values[i][16], DatosPrincipales.values[i][17],
                                DatosPrincipales.values[i][18], DatosPrincipales.values[i][19], DatosPrincipales.values[i][20],
                                DatosPrincipales.values[i][21], DatosPrincipales.values[i][22]])
    return ingreso_datos