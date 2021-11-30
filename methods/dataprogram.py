# -*- coding: utf-8 -*-
"""
Created on Wed Jan 01 20:00:29 2020 

@author: Ing. Daniel Villarreal
"""

import pandas as pd # Conectar con hojas de excel

def DatosPrograma(D_criterio, ingreso_datos, ExcelPrincipal):

    if D_criterio == 0:
        DatosPrincipales_actualizados = pd.DataFrame(ingreso_datos)
#        print(DatosPrincipales_actualizados.to_string(index=False , header=False))    
        return ingreso_datos, DatosPrincipales_actualizados
    
