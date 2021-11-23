# -*- coding: utf-8 -*-
"""
Created on Wed Jan 01 20:00:29 2020 

@author: Ing. Daniel Villarreal
"""

import numpy as np # Creación de matrices

from src_calculos.methods.analysis import analisis
from src_calculos.methods.designlrfd import disenioLRFD
from src_calculos.methods.assemblyBC import unionesVC

def constraintValidation(D_criterio, contador, ingreso_datos, lista_posibles, lista_Peso_estructural, lista_los_mejores, validacion_auxiliar, D_optimizator, perfiles_aprobados,ExcelPrincipal, D_nodos_totales, D_nodos_restringidos):
    
    
    (validate, Restriccion_VigaColumna, Restriccion_C2C1_h, Restriccion_C2C1_b, 
     pares_VigaColumna, pares_ColumnaColumna, l, pcv2, m, pcc2,
     Restriccion_VigaColumnas, Restriccion_C2C1_hs, Restriccion_C2C1_bs) = unionesVC(ingreso_datos, D_optimizator, perfiles_aprobados, ExcelPrincipal)
    
    if validate == True:
        Longitudes, Qc_estructura, k_global_estructura, qnc_estructura, Qnc_estructura, F_elementos , PesoEstructural, nGDL_libres, k_global_estructura_presentacion_print, caracteristicas = analisis(ExcelPrincipal, D_nodos_totales, D_nodos_restringidos, 
                                                                                                                                 D_criterio, ingreso_datos, D_optimizator, perfiles_aprobados)
        
        if D_criterio == 1:
            pass
                
        elif D_criterio == 0:
            
            (Restriccion_Demanda_Capacidades, promedio_DC, PesoEstructural, 
             
             KLR_diseno_listas, lamb_f_lista, lamb_rf_lista, Ala_C_lista,lamb_w_lista, lamb_rw_lista, Alma_C_lista, 
             TipoSeccion_Compresion_lista, Fe_lista, O1_lista, Qs_lista, f_lista, be_lista, Ae_lista, Q_lista, O2_lista, 
             FormaPandeo_Compresion_lista, Fcr_FB_lista, Pn_FB_lista, Fez_lista, Fcr_FTB_lista, Pn_FTB_lista, Pn_lista, Fhi_Pn_demo,
             
             lamb_pf_lista, lamb_prf_lista, Ala_F_lista, lamb_pw_lista, lamb_prw_lista, Alma_F_lista, TipoSeccion_Flexion_lista,
             Lp_lista, Lr_lista, ZonaPandeo_Flexion_lista, Mpx_lista, Mnx_Y_lista, Cb_lista, Fcrx_LTB_lista, Mnx_LTB_lista, ff1_lista,
             kc_lista, Mnx_FLB_lista, Mnx_lista, Fhi_Mnx_demo,
             
             TipoSeccion_Flexion_Y_lista, Mpy_lista, Mny_Y_lista, Fcr_FLB_lista, Mny_FLB_lista, Mny_lista, Fhi_Mny_demo,
             
             peso_elemento_lista, Longitudes, PesoTotalElemento_lista, Verificacion_lista, Muy_lista,
             
             tipoelementos, seccions) = disenioLRFD(ExcelPrincipal, ingreso_datos, F_elementos, D_optimizator, perfiles_aprobados)
            
            lista_aux = []
            for i in range(len(lista_posibles)):
                if lista_posibles[i] not in lista_aux:
                    lista_aux.append(lista_posibles[i])
            indice_variacion= len(lista_aux)
            indice_complejidad = indice_variacion / len(ingreso_datos)
            print((contador+1), "   ", lista_posibles,"  ", Restriccion_Demanda_Capacidades)        
            contador += 1
            lista_Peso_estructural.append(PesoEstructural)
            
            value = True
            promedio_cal = np.mean(Restriccion_Demanda_Capacidades)
            minimo_cal = min(Restriccion_Demanda_Capacidades)
            maximo_cal = max(Restriccion_Demanda_Capacidades)
            if validacion_auxiliar == 0:
                if (promedio_cal > 0.5 and promedio_cal < 0.99 and minimo_cal >= 0.09 and maximo_cal <=1.0) == False:
                    value = False

                if value == True:
                    lista_los_mejores.append([lista_posibles,Restriccion_Demanda_Capacidades,promedio_DC,PesoEstructural, indice_variacion, indice_complejidad])
            else:    
                if (promedio_cal > 0.5 and promedio_cal < 0.99 and minimo_cal >= 0.09 and maximo_cal <=1.3) == False:
                    value = False
                        
                if value == True:
                    lista_los_mejores.append([lista_posibles,Restriccion_Demanda_Capacidades,promedio_DC,PesoEstructural, indice_variacion, indice_complejidad])
                


        elif D_criterio == 2:
            pass
            
                
    return contador, lista_Peso_estructural, lista_los_mejores

