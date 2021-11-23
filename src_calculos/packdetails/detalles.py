# -*- coding: utf-8 -*-
"""
Created on Wed Jan 01 20:00:29 2020 

@author: Ing. Daniel Villarreal
"""

#importa estas dos
#import sys
#import io

import pandas as pd # Conectar con hojas de excel
from decimal import Decimal # Para el formato de números en decimal

from src_calculos.loggerPrint import Logger

from src_calculos.methods.analysis import analisis
from src_calculos.methods.designlrfd import disenioLRFD
from src_calculos.methods.datosprograma import DatosPrograma
from src_calculos.methods.assemblyBC import unionesVC
from src_calculos.methods.compresioneficiente import Comp_Eficc


def detallado(ExcelPrincipal, lista_detalle, ingreso_datos, D_optimizator, perfiles_aprobados,  D_nodos_totales, D_nodos_restringidos, D_criterio):
    
    my_console = Logger('src_calculos/onefile/onedetailed.txt') 
    
    print('DETALLE GENERAL DE RESULTADOS','\n')

    print('Nota: Los resultados de esta sección reflejan el análisis y diseño del modelo realizado, si desea optimizar, diríjase al boton respectivo en la ventana anterior.','\n')


    
    if len(lista_detalle) != 0:
        for i in range(0,len(ingreso_datos)):
            if ingreso_datos[i][1] == 'Vig':
                ingreso_datos[i][14]= lista_detalle[0][(len(lista_detalle[0])//2)+ingreso_datos[i][2]-1]
            else:
                ingreso_datos[i][14]=lista_detalle[0][ingreso_datos[i][2]-1]
    

    ingreso_datos, DatosPrincipales_actualizados = DatosPrograma(D_criterio, ingreso_datos, ExcelPrincipal)  
    


    print(188*'=')
    print('\n','Análisis Estructural')  
    print(' ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    

    Longitudes, Qc_estructura, k_global_estructura, qnc_estructura, Qnc_estructura, F_elementos , PesoEstructural, nGDL_libres, k_global_estructura_presentacion_print, caracteristicas = analisis(ExcelPrincipal, D_nodos_totales, D_nodos_restringidos, 
                                                                                                                             D_criterio, ingreso_datos, D_optimizator, perfiles_aprobados)
    


    vcg = pd.DataFrame(Qc_estructura)
    vcg.columns = ['Qc\n[kgf]']
    vcg.index += 0
    vcg.index.rename('nGDLT', inplace=True)


    matr = pd.DataFrame(k_global_estructura)
    matr.index.rename('kgf/m', inplace=True)


    desp = pd.DataFrame(qnc_estructura)
    desp.columns = ['qnc\n[m]']
    desp.index += 0
    desp.index.rename('nGDLT_Libres', inplace=True)

        
    rb = pd.DataFrame(Qnc_estructura)
    rb.columns = ['Qnc\n[kgf]']
    rb.index += nGDL_libres
    rb.index.rename('nGDLT_Restringidos', inplace=True)

    print('Las fuerzas en los elementos son: ','\n') 
    print('Elemento',1*' ','Tipo',14*' ','Pu_i',16*' ','Vu_i',18*' ','Mu_i',18*' ','Pu_j',18*' ','Vu_j',18*' ','Mu_j')             
    print('                ',1*' ','    ',13*' ','[kgf]',16*' ','[kgf]',15*' ','[kgf.m]',16*' ','[kgf]',18*' ','[kgf]',16*' ','[kgf.m]')             

    for i in range(len(ingreso_datos)): #--> Para cada fila en el rango de 'ingreso de DatosPrincipales'[i]...
        
        print(f"{i+1:02} {ingreso_datos[i][1]:>16} {F_elementos[i][0]:>20} {F_elementos[i][1]:>20}" 
                f"{F_elementos[i][2]:>20} {F_elementos[i][3]:>20} {F_elementos[i][4]:>20}" 
                f"{F_elementos[i][5]:>20}")            

    forc = pd.DataFrame(F_elementos)
    forc.columns = ['Pu_i\n[kgf]','Vui\n[kgf]','Mu_i\n[kgf*m]','Pu_j\n[kgf]','Vuj\n[kgf]','Muj\n[kgf*m]']
    forc.index += 1 
    forc.index.rename('Elemento', inplace=True)
    
    with pd.ExcelWriter('src_calculos/onefile/Resultados_Analisis.xlsx') as writer:

        vcg.to_excel(writer, sheet_name='CargasGeneralizadas')
        matr.to_excel(writer, sheet_name='MatrizGlobalEstructura')
        desp.to_excel(writer, sheet_name='Desplazamientos')
        rb.to_excel(writer, sheet_name='Reacciones')
        forc.to_excel(writer, sheet_name='FuerzasElementales')

    print('')    
    print(188*'=')
    print('\n','Diseño estructural [LRFD]')   
    print(' ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯') 
    
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



    compresion = pd.DataFrame({'kl/r_Diseño':KLR_diseno_listas[:len(ingreso_datos)],'λf':lamb_f_lista[:len(ingreso_datos)],
                               'λrf':lamb_rf_lista[:len(ingreso_datos)], 'Esbeltez del ala':Ala_C_lista[:len(ingreso_datos)], 
                               'λw':lamb_w_lista[:len(ingreso_datos)],'λrw':lamb_rw_lista[:len(ingreso_datos)], 'Esbeltez del alma':Alma_C_lista[:len(ingreso_datos)],
                               'Tipo de Sección':TipoSeccion_Compresion_lista[:len(ingreso_datos)], 'Fe\n[kgf/m2]':Fe_lista[:len(ingreso_datos)], 'Frontera Le':O1_lista[:len(ingreso_datos)],
                               'Qs\nEsbeltos no Rigidizados':Qs_lista[:len(ingreso_datos)],'f\nFcr_Y - No Esbeltas\n[kgf/m2]':f_lista[:len(ingreso_datos)],'be\nEsbeltos no Rigidizados\n[m]':be_lista[:len(ingreso_datos)],
                               'Ae\nEsbeltos no Rigidizados\n[m2]':Ae_lista[:len(ingreso_datos)],'Q\nSecciones Esbeltas':Q_lista[:len(ingreso_datos)], 'Forma de Pandeo':FormaPandeo_Compresion_lista[:len(ingreso_datos)],
                               'Fcr - FB\nPandeo Flexional\n[kgf/m2]':Fcr_FB_lista[:len(ingreso_datos)], 'Pn - FB\nPandeo Flexional\n[kgf]':Pn_FB_lista[:len(ingreso_datos)], 'Fez\n[kgf/m2]':Fez_lista[:len(ingreso_datos)],
                               'FCR - FTB\nPandeo Flexotorsional\n[kgf/m2]':Fcr_FTB_lista[:len(ingreso_datos)], 'Pn - FTB\nPandeo Flexotorsional\n[kgf]':Pn_FTB_lista[:len(ingreso_datos)], 
                               'Pn\n[kgf]':Pn_lista[:len(ingreso_datos)], 'ΦPn [LRFD]\n[kgf]':Fhi_Pn_demo[:len(ingreso_datos)]})
    compresion.index += 1 
    compresion.index.rename('Elemento', inplace=True)


        

    flexionx = pd.DataFrame({'λf':lamb_f_lista[:len(ingreso_datos)], 'λpf':lamb_pf_lista[:len(ingreso_datos)],'λprf':lamb_prf_lista[:len(ingreso_datos)], 
                               'Esbeltez del ala':Ala_F_lista[:len(ingreso_datos)], 'λw':lamb_w_lista[:len(ingreso_datos)],'λpw':lamb_pw_lista[:len(ingreso_datos)],
                               'λprw':lamb_prw_lista[:len(ingreso_datos)], 'Esbeltez del alma':Alma_F_lista[:len(ingreso_datos)], 'Tipo de Sección':TipoSeccion_Flexion_lista[:len(ingreso_datos)], 
                               'Lp\n[m]':Lp_lista[:len(ingreso_datos)], 'Lr':Lr_lista[:len(ingreso_datos)], 'Zona de pandeo a Flexión':ZonaPandeo_Flexion_lista[:len(ingreso_datos)],
                               'Mpx\n[kgf*m]':Mpx_lista[:len(ingreso_datos)],'Mnx - Y\nFluencia\n[kgf*m]':Mnx_Y_lista[:len(ingreso_datos)], 'Cb':Cb_lista[:len(ingreso_datos)],
                               'Fcrx - LTB\nPandeo Lateral Torsional\n[kgf/m2]':Fcrx_LTB_lista[:len(ingreso_datos)], 'Mnx - LTB\nPandeo Lateral Torsional\n[kgf*m]':Mnx_LTB_lista[:len(ingreso_datos)],
                               'kc - FLB\nPandeo Local del ala':kc_lista[:len(ingreso_datos)], 'Mnx\nPandeo Local del ala\n[kgf*m]':Mnx_FLB_lista[:len(ingreso_datos)], 
                               'Mnx\n[kgf*m]':Mnx_lista[:len(ingreso_datos)],'ΦMn [LRFD]\n[kgf*m]':Fhi_Mnx_demo[:len(ingreso_datos)]})   

    flexionx.index += 1 
    flexionx.index.rename('Elemento', inplace=True)   




    flexiony = pd.DataFrame({'Tipo de Sección':TipoSeccion_Flexion_Y_lista[:len(ingreso_datos)],'Mpy\n[kgf*m]':Mpy_lista[:len(ingreso_datos)],'Mny - Y\nFluencia\n[kgf*m]':Mny_Y_lista[:len(ingreso_datos)], 
                             'Fcry - FLB\nPandeo Local del ala\n[kgf/m2]':Fcr_FLB_lista[:len(ingreso_datos)], 'Mny\nPandeo Local del ala\n[kgf*m]':Mny_FLB_lista[:len(ingreso_datos)], 
                               'Mny\n[kgf*m]':Mny_lista[:len(ingreso_datos)],'ΦMn [LRFD]\n[kgf*m]':Fhi_Mny_demo[:len(ingreso_datos)]})   

    flexiony.index += 1 
    flexiony.index.rename('Elemento', inplace=True)  

    
#    print('\n','Sumario de diseño LRFD: ','\n')
    print('Indicaciones:','\n',' * Mientras más cercana es la relación Demanda/Capacidad a 1 por la izquierda, más óptimo es el diseño.','\n')
    print('Elemento',1*' ','Tipo',14*' ','Sección',14*' ','Peso',10*' ','Longitud',4*' ',
          'Peso elemento',1*' ','Tipo de Verificación',58*' ','Pu',25*' ','Mux',20*' ','Muy',15*' ','Fhi_Pn',20*' ','Fhi_Mnx',16*' ',
          'Fhi_Mny',10*' ','Relación D/C')

    print('        ',1*' ','    ',14*' ','       ',25*' ','[kgf/m]',12*' ','[m]',13*' ',
          '[kgf]',94*' ',' ',1*'','[kgf]',20*' ','[kgf.m]',16*' ','[kgf.m]',13*' ','[kgf]',22*' ','[kgf.m]',18*' ',
          '[kgf.m]',1*' ','            ')


    for i in range(len(ingreso_datos)): 

        print(f"{i+1:02} {ingreso_datos[i][1]:>16} {ingreso_datos[i][13]:>18} {ingreso_datos[i][14]:>1}" 
                f"{'%.3f'%Decimal(peso_elemento_lista[i]):>20} {Longitudes[i]:>15} {'%.3f'%Decimal(PesoTotalElemento_lista[i]):>20} {Verificacion_lista[i]:>55}" 
                f"{max(abs(F_elementos[i][0]), abs(F_elementos[i][3])):>25}" 
                f"{max(abs(F_elementos[i][2]), abs(F_elementos[i][5])):>25}" 
                f"{Muy_lista[i]:>18} {Fhi_Pn_demo[i]:>25} {Fhi_Mnx_demo[i]:>25} {Fhi_Mny_demo[i]:>25} {Restriccion_Demanda_Capacidades[i]:>20}")  


    diseo = pd.DataFrame({'Tipo de Elemento':tipoelementos[:len(ingreso_datos)],'Perfil Estructural':seccions[:len(ingreso_datos)],'Peso unitario\n[kgf/m]':peso_elemento_lista[:len(ingreso_datos)], 
                          'Longitud\n[m]':Longitudes[:len(ingreso_datos)], 'Peso del elemento\n[kgf]':PesoTotalElemento_lista[:len(ingreso_datos)], 
                          'Tipo de verificación\nDiseño':Verificacion_lista[:len(ingreso_datos)],'ΦPn [LRFD]\n[kgf]':Fhi_Pn_demo[:len(ingreso_datos)],
                          'ΦMnx [LRFD]\n[kgf*m]':Fhi_Mnx_demo[:len(ingreso_datos)], 'ΦMny [LRFD]\n[kgf*m]':Fhi_Mny_demo[:len(ingreso_datos)], 'Relación Demanda/Capacidad':Restriccion_Demanda_Capacidades[:len(ingreso_datos)]})   

    diseo.index += 1 
    diseo.index.rename('Elemento', inplace=True)  

    with pd.ExcelWriter('src_calculos/onefile/Resultados_Diseno_Restriccion.xlsx') as writer:

        compresion.to_excel(writer, sheet_name='DisenioCompresion')
        flexionx.to_excel(writer, sheet_name='DisenioFlexion_X')
        flexiony.to_excel(writer, sheet_name='DisenioFlexion_Y')
        diseo.to_excel(writer, sheet_name='Restriccion_DC')


    print('\n','El peso de todos los elementos es de: ',round(PesoEstructural,3),' kgf')
    
    print('El promedio de demanda/capacidad es de: ', promedio_DC)

    print('')    
    print(188*'=')
    print('\n','Criterio correcto de ensamble en las uniones') 
    print(' ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    print('\n',' Indicaciones:','\n',' * Valores menores o iguales a 0 indican un correcto ensamble')

    (validate, Restriccion_VigaColumna, Restriccion_C2C1_h, Restriccion_C2C1_b, 
     pares_VigaColumna, pares_ColumnaColumna, l, pcv2, m, pcc2,
     Restriccion_VigaColumnas, Restriccion_C2C1_hs, Restriccion_C2C1_bs) = unionesVC(ingreso_datos, D_optimizator, perfiles_aprobados, ExcelPrincipal)
    
    print('')
    print('Restricciones para uniones Columna-Viga (Ancho de Patín)', '\n')   

    for l in range(len(pcv2)): 

        print(f"{[pares_VigaColumna[l][0], pares_VigaColumna[l][1]]} {Restriccion_VigaColumnas[l]:>27}")  

    uvc = pd.DataFrame({'Pares Viga - Columna\nAncho de Patín':pares_VigaColumna[:len(pcv2)], 'Validación':Restriccion_VigaColumnas})   

    uvc.index += 1 
    uvc.index.rename('Union', inplace=True)  

    if len(pcc2) > 0:
        print('\n')
        print('Restricciones para uniones Columna-Columna (Peralte)')
        for m in range(len(pcc2)): 
            print(f"{[pares_ColumnaColumna[m][0], pares_ColumnaColumna[m][1]]}  {Restriccion_C2C1_hs[m]:>27} ")   
            
        print('\n')
        print('Restricciones para uniones Columna-Columna (Ancho de Patín)')  
        for m in range(len(pcc2)): 
            print(f"{[pares_ColumnaColumna[m][0], pares_ColumnaColumna[m][1]]}  {Restriccion_C2C1_bs[m]:>27} ")  

        ucc_h = pd.DataFrame({'Pares Columna - Columna\nPeralte':pares_VigaColumna[:len(pcc2)], 'Validación':Restriccion_C2C1_hs})   
        ucc_h.index += 1 
        ucc_h.index.rename('Union', inplace=True)  
        
        ucc_b = pd.DataFrame({'Pares Columna - Columna\nPeralte':pares_VigaColumna[:len(pcc2)], 'Validación':Restriccion_C2C1_bs})   
        ucc_b.index += 1 
        ucc_b.index.rename('Union', inplace=True)  
 
        with pd.ExcelWriter('src_calculos/onefile/Resultados_Uniones_Restriccion.xlsx') as writer:

            uvc.to_excel(writer, sheet_name='Union_VigCol')
            ucc_h.to_excel(writer, sheet_name='Union_ColCol_Peralte')
            ucc_b.to_excel(writer, sheet_name='Union_ColCol_Patin')            

    else:
        Restriccion_C2C1_h = 0
        Restriccion_C2C1_b = 0
        m = 0
        pcc2 = 0
        ucc_h = [0,0]
        ucc_b = [0,0]
        print('Restricciones para uniones Columna-Columna - No aplica')
        print(f"None {Restriccion_C2C1_h:>27} ")   
        print(f"None {Restriccion_C2C1_b:>27} ")    
        
        with pd.ExcelWriter('src_calculos/onefile/Resultados_Uniones_Restriccion.xlsx') as writer:

            uvc.to_excel(writer, sheet_name='Union_VigCol')
#        print(f"{pares_ColumnaColumna, pares_ColumnaColumna}  {Restriccion_C2C1_h:>24} {Restriccion_C2C1_b:>63}")  

    print('')    
    print(188*'=')
    print('\n','Criterio de miembros a compresión eficiente en ambos ejes')   
    print(' ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')  
    print('\n',' Indicaciones:','\n',' * Valores mayores o iguales a 0.35 indican un comportamiento en ambos ejes debido a su relación geométrica')  
    Restriccion_MiembroCompresion, Restriccion_MiembroCompresiones = Comp_Eficc(ExcelPrincipal, ingreso_datos, perfiles_aprobados, D_optimizator)      
 
    print('')
    print('Elemento a',5*' ','Relación Ry/Rx') 
    print('compresión') 

    
    for i in range(len(ingreso_datos)): 
        if ingreso_datos[i][1] == 'Col':
            print(f"{i+1:02} {Restriccion_MiembroCompresiones[i]:>31}")            

    
    rmc = pd.DataFrame({'Relación Ry/Rx':Restriccion_MiembroCompresiones[:len(Restriccion_MiembroCompresiones)]})   
    rmc.index += 1 
    rmc.index.rename('Miembros a\nCompresion', inplace=True)  

    with pd.ExcelWriter('src_calculos/onefile/Resultados_CompEficc_Restriccion.xlsx') as writer:

        rmc.to_excel(writer, sheet_name='C.E_AmbosEjes')          
    

    my_console.close()

#    sys.stdout = orig_stdout
#    f.close()
        

#    elif D_criterio == 0:
#        print('\n','Esta restricción no aplica en base al cumplimiento que se quiere satisfacer','\n') 



















































def detallado_a(lista_los_mejores, ExcelPrincipal, lista_final_pv_bajo, ingreso_datos_a, D_optimizator, perfiles_aprobados,  D_nodos_totales, D_nodos_restringidos, D_criterio, lista_minimo_peso_variabilidad):
   
    my_console = Logger('src_calculos/files/detailed_a.txt') 
    
    if (len(lista_los_mejores)) != 0:    

        print('DETALLE GENERAL DE RESULTADOS','\n')

        print('Nota: Es posible que exista una única opción, en cualquier caso se busca minimizar el peso estructural.','\n')

        print("Opción con el índice de complejidad constructiva más bajo de todas las opciones más óptimas:")
        print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯','\n')    


        
        lista_detalle = lista_final_pv_bajo
        
        for lista_final_pv_bajo in lista_minimo_peso_variabilidad: # ================================================ 3.
            
            if len(lista_detalle) != 0:
                for i in range(0,len(ingreso_datos_a)):
                    if ingreso_datos_a[i][1] == 'Vig':
                        ingreso_datos_a[i][14]= lista_detalle[0][(len(lista_detalle[0])//2)+ingreso_datos_a[i][2]-1]
                    else:
                        ingreso_datos_a[i][14]=lista_detalle[0][ingreso_datos_a[i][2]-1]
                        
            ingreso_datos_a, DatosPrincipales_actualizados = DatosPrograma(D_criterio, ingreso_datos_a, ExcelPrincipal)  
            
        
            Longitudes, Qc_estructura, k_global_estructura, qnc_estructura, Qnc_estructura, F_elementos , PesoEstructural, nGDL_libres, k_global_estructura_presentacion_print, caracteristicas = analisis(ExcelPrincipal, D_nodos_totales, D_nodos_restringidos, 
                                                                                                                                     D_criterio, ingreso_datos_a, D_optimizator, perfiles_aprobados)
            
        
        
        
            vcg = pd.DataFrame(Qc_estructura)
            vcg.columns = ['Qc\n[kgf]']
            vcg.index += 0
            vcg.index.rename('nGDLT', inplace=True)
        
        
            matr = pd.DataFrame(k_global_estructura)
            matr.index.rename('kgf/m', inplace=True)
        
        
            desp = pd.DataFrame(qnc_estructura)
            desp.columns = ['qnc\n[m]']
            desp.index += 0
            desp.index.rename('nGDLT_Libres', inplace=True)
        
                
            rb = pd.DataFrame(Qnc_estructura)
            rb.columns = ['Qnc\n[kgf]']
            rb.index += nGDL_libres
            rb.index.rename('nGDLT_Restringidos', inplace=True)
        
            print('Las fuerzas en los elementos son: ','\n') 
            print('Elemento',1*' ','Tipo',14*' ','Pu_i',16*' ','Vu_i',18*' ','Mu_i',18*' ','Pu_j',18*' ','Vu_j',18*' ','Mu_j')             
            print('                ',1*' ','    ',13*' ','[kgf]',16*' ','[kgf]',15*' ','[kgf.m]',16*' ','[kgf]',18*' ','[kgf]',16*' ','[kgf.m]')        
        
            for i in range(len(ingreso_datos_a)): #--> Para cada fila en el rango de 'ingreso de DatosPrincipales'[i]...
                
                print(f"{i+1:02} {ingreso_datos_a[i][1]:>16} {F_elementos[i][0]:>20} {F_elementos[i][1]:>20}" 
                        f"{F_elementos[i][2]:>20} {F_elementos[i][3]:>20} {F_elementos[i][4]:>20}" 
                        f"{F_elementos[i][5]:>20}")            
        
            forc = pd.DataFrame(F_elementos)
            forc.columns = ['Pu_i\n[kgf]','Vui\n[kgf]','Mu_i\n[kgf*m]','Pu_j\n[kgf]','Vuj\n[kgf]','Muj\n[kgf*m]']
            forc.index += 1 
            forc.index.rename('Elemento', inplace=True)
            
            with pd.ExcelWriter('src_calculos/files/A_Resultados_Analisis.xlsx') as writer:
        
                vcg.to_excel(writer, sheet_name='CargasGeneralizadas')
                matr.to_excel(writer, sheet_name='MatrizGlobalEstructura')
                desp.to_excel(writer, sheet_name='Desplazamientos')
                rb.to_excel(writer, sheet_name='Reacciones')
                forc.to_excel(writer, sheet_name='FuerzasElementales')
        
            print('')    
            print(188*'=')
            print('\n','Diseño estructural [LRFD]')   
            print(' ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯') 
            
            (Restriccion_Demanda_Capacidades, promedio_DC, PesoEstructural, 
                
                KLR_diseno_listas, lamb_f_lista, lamb_rf_lista, Ala_C_lista,lamb_w_lista, lamb_rw_lista, Alma_C_lista, 
                TipoSeccion_Compresion_lista, Fe_lista, O1_lista, Qs_lista, f_lista, be_lista, Ae_lista, Q_lista, O2_lista, 
                FormaPandeo_Compresion_lista, Fcr_FB_lista, Pn_FB_lista, Fez_lista, Fcr_FTB_lista, Pn_FTB_lista, Pn_lista, Fhi_Pn_demo,
                
                lamb_pf_lista, lamb_prf_lista, Ala_F_lista, lamb_pw_lista, lamb_prw_lista, Alma_F_lista, TipoSeccion_Flexion_lista,
                Lp_lista, Lr_lista, ZonaPandeo_Flexion_lista, Mpx_lista, Mnx_Y_lista, Cb_lista, Fcrx_LTB_lista, Mnx_LTB_lista, ff1_lista,
                kc_lista, Mnx_FLB_lista, Mnx_lista, Fhi_Mnx_demo,
                
                TipoSeccion_Flexion_Y_lista, Mpy_lista, Mny_Y_lista, Fcr_FLB_lista, Mny_FLB_lista, Mny_lista, Fhi_Mny_demo,
                
                peso_elemento_lista, Longitudes, PesoTotalElemento_lista, Verificacion_lista, Muy_lista,
                
                tipoelementos, seccions) = disenioLRFD(ExcelPrincipal, ingreso_datos_a, F_elementos, D_optimizator, perfiles_aprobados)       
        
        
        
        
            compresion = pd.DataFrame({'kl/r_Diseño':KLR_diseno_listas[:len(ingreso_datos_a)],'λf':lamb_f_lista[:len(ingreso_datos_a)],
                                       'λrf':lamb_rf_lista[:len(ingreso_datos_a)], 'Esbeltez del ala':Ala_C_lista[:len(ingreso_datos_a)], 
                                       'λw':lamb_w_lista[:len(ingreso_datos_a)],'λrw':lamb_rw_lista[:len(ingreso_datos_a)], 'Esbeltez del alma':Alma_C_lista[:len(ingreso_datos_a)],
                                       'Tipo de Sección':TipoSeccion_Compresion_lista[:len(ingreso_datos_a)], 'Fe\n[kgf/m2]':Fe_lista[:len(ingreso_datos_a)], 'Frontera Le':O1_lista[:len(ingreso_datos_a)],
                                       'Qs\nEsbeltos no Rigidizados':Qs_lista[:len(ingreso_datos_a)],'f\nFcr_Y - No Esbeltas\n[kgf/m2]':f_lista[:len(ingreso_datos_a)],'be\nEsbeltos no Rigidizados\n[m]':be_lista[:len(ingreso_datos_a)],
                                       'Ae\nEsbeltos no Rigidizados\n[m2]':Ae_lista[:len(ingreso_datos_a)],'Q\nSecciones Esbeltas':Q_lista[:len(ingreso_datos_a)], 'Forma de Pandeo':FormaPandeo_Compresion_lista[:len(ingreso_datos_a)],
                                       'Fcr - FB\nPandeo Flexional\n[kgf/m2]':Fcr_FB_lista[:len(ingreso_datos_a)], 'Pn - FB\nPandeo Flexional\n[kgf]':Pn_FB_lista[:len(ingreso_datos_a)], 'Fez\n[kgf/m2]':Fez_lista[:len(ingreso_datos_a)],
                                       'FCR - FTB\nPandeo Flexotorsional\n[kgf/m2]':Fcr_FTB_lista[:len(ingreso_datos_a)], 'Pn - FTB\nPandeo Flexotorsional\n[kgf]':Pn_FTB_lista[:len(ingreso_datos_a)], 
                                       'Pn\n[kgf]':Pn_lista[:len(ingreso_datos_a)], 'ΦPn [LRFD]\n[kgf]':Fhi_Pn_demo[:len(ingreso_datos_a)]})
            compresion.index += 1 
            compresion.index.rename('Elemento', inplace=True)
        
        
                
        
            flexionx = pd.DataFrame({'λf':lamb_f_lista[:len(ingreso_datos_a)], 'λpf':lamb_pf_lista[:len(ingreso_datos_a)],'λprf':lamb_prf_lista[:len(ingreso_datos_a)], 
                                       'Esbeltez del ala':Ala_F_lista[:len(ingreso_datos_a)], 'λw':lamb_w_lista[:len(ingreso_datos_a)],'λpw':lamb_pw_lista[:len(ingreso_datos_a)],
                                       'λprw':lamb_prw_lista[:len(ingreso_datos_a)], 'Esbeltez del alma':Alma_F_lista[:len(ingreso_datos_a)], 'Tipo de Sección':TipoSeccion_Flexion_lista[:len(ingreso_datos_a)], 
                                       'Lp\n[m]':Lp_lista[:len(ingreso_datos_a)], 'Lr':Lr_lista[:len(ingreso_datos_a)], 'Zona de pandeo a Flexión':ZonaPandeo_Flexion_lista[:len(ingreso_datos_a)],
                                       'Mpx\n[kgf*m]':Mpx_lista[:len(ingreso_datos_a)],'Mnx - Y\nFluencia\n[kgf*m]':Mnx_Y_lista[:len(ingreso_datos_a)], 'Cb':Cb_lista[:len(ingreso_datos_a)],
                                       'Fcrx - LTB\nPandeo Lateral Torsional\n[kgf/m2]':Fcrx_LTB_lista[:len(ingreso_datos_a)], 'Mnx - LTB\nPandeo Lateral Torsional\n[kgf*m]':Mnx_LTB_lista[:len(ingreso_datos_a)],
                                       'kc - FLB\nPandeo Local del ala':kc_lista[:len(ingreso_datos_a)], 'Mnx\nPandeo Local del ala\n[kgf*m]':Mnx_FLB_lista[:len(ingreso_datos_a)], 
                                       'Mnx\n[kgf*m]':Mnx_lista[:len(ingreso_datos_a)],'ΦMn [LRFD]\n[kgf*m]':Fhi_Mnx_demo[:len(ingreso_datos_a)]})   
        
            flexionx.index += 1 
            flexionx.index.rename('Elemento', inplace=True)   
        
        
        
        
            flexiony = pd.DataFrame({'Tipo de Sección':TipoSeccion_Flexion_Y_lista[:len(ingreso_datos_a)],'Mpy\n[kgf*m]':Mpy_lista[:len(ingreso_datos_a)],'Mny - Y\nFluencia\n[kgf*m]':Mny_Y_lista[:len(ingreso_datos_a)], 
                                     'Fcry - FLB\nPandeo Local del ala\n[kgf/m2]':Fcr_FLB_lista[:len(ingreso_datos_a)], 'Mny\nPandeo Local del ala\n[kgf*m]':Mny_FLB_lista[:len(ingreso_datos_a)], 
                                       'Mny\n[kgf*m]':Mny_lista[:len(ingreso_datos_a)],'ΦMn [LRFD]\n[kgf*m]':Fhi_Mny_demo[:len(ingreso_datos_a)]})   
        
            flexiony.index += 1 
            flexiony.index.rename('Elemento', inplace=True)  
        
            
            print('Indicaciones:','\n',' * Mientras más cercana es la relación Demanda/Capacidad a 1 por la izquierda, más óptimo es el diseño.','\n')
            print('Elemento',1*' ','Tipo',14*' ','Sección',14*' ','Peso',10*' ','Longitud',4*' ',
                  'Peso elemento',1*' ','Tipo de Verificación',58*' ','Pu',25*' ','Mux',20*' ','Muy',15*' ','Fhi_Pn',20*' ','Fhi_Mnx',16*' ',
                  'Fhi_Mny',10*' ','Relación D/C')
        
            print('        ',1*' ','    ',14*' ','       ',25*' ','[kgf/m]',12*' ','[m]',13*' ',
                  '[kgf]',94*' ',' ',1*'','[kgf]',20*' ','[kgf.m]',16*' ','[kgf.m]',13*' ','[kgf]',22*' ','[kgf.m]',18*' ',
                  '[kgf.m]',1*' ','            ')
        
        
            for i in range(len(ingreso_datos_a)): 
        
                print(f"{i+1:02} {ingreso_datos_a[i][1]:>16} {ingreso_datos_a[i][13]:>18} {ingreso_datos_a[i][14]:>1}" 
                        f"{'%.3f'%Decimal(peso_elemento_lista[i]):>20} {Longitudes[i]:>15} {'%.3f'%Decimal(PesoTotalElemento_lista[i]):>20} {Verificacion_lista[i]:>55}" 
                        f"{max(abs(F_elementos[i][0]), abs(F_elementos[i][3])):>25}" 
                        f"{max(abs(F_elementos[i][2]), abs(F_elementos[i][5])):>25}" 
                        f"{Muy_lista[i]:>18} {Fhi_Pn_demo[i]:>25} {Fhi_Mnx_demo[i]:>25} {Fhi_Mny_demo[i]:>25} {Restriccion_Demanda_Capacidades[i]:>20}")  
        
        
            diseo = pd.DataFrame({'Tipo de Elemento':tipoelementos[:len(ingreso_datos_a)],'Perfil Estructural':seccions[:len(ingreso_datos_a)],'Peso unitario\n[kgf/m]':peso_elemento_lista[:len(ingreso_datos_a)], 
                                  'Longitud\n[m]':Longitudes[:len(ingreso_datos_a)], 'Peso del elemento\n[kgf]':PesoTotalElemento_lista[:len(ingreso_datos_a)], 
                                  'Tipo de verificación\nDiseño':Verificacion_lista[:len(ingreso_datos_a)],'ΦPn [LRFD]\n[kgf]':Fhi_Pn_demo[:len(ingreso_datos_a)],
                                  'ΦMnx [LRFD]\n[kgf*m]':Fhi_Mnx_demo[:len(ingreso_datos_a)], 'ΦMny [LRFD]\n[kgf*m]':Fhi_Mny_demo[:len(ingreso_datos_a)], 'Relación Demanda/Capacidad':Restriccion_Demanda_Capacidades[:len(ingreso_datos_a)]})   
        
            diseo.index += 1 
            diseo.index.rename('Elemento', inplace=True)  
        
            with pd.ExcelWriter('src_calculos/files/A_Resultados_Diseno_Restriccion.xlsx') as writer:
        
                compresion.to_excel(writer, sheet_name='DisenioCompresion')
                flexionx.to_excel(writer, sheet_name='DisenioFlexion_X')
                flexiony.to_excel(writer, sheet_name='DisenioFlexion_Y')
                diseo.to_excel(writer, sheet_name='Restriccion_DC')
        
        
            print('\n','El peso de todos los elementos es de: ',round(PesoEstructural,3),' kgf')
            
            print('El promedio de demanda/capacidad es de: ', promedio_DC)
        
            print('')    
            print(188*'=')
            print('\n','Criterio correcto de ensamble en las uniones') 
            print(' ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
            print('\n',' Indicaciones:','\n',' * Valores menores o iguales a 0 indican un correcto ensamble')
        
        
            (validate, Restriccion_VigaColumna, Restriccion_C2C1_h, Restriccion_C2C1_b, 
             pares_VigaColumna, pares_ColumnaColumna, l, pcv2, m, pcc2,
             Restriccion_VigaColumnas, Restriccion_C2C1_hs, Restriccion_C2C1_bs) = unionesVC(ingreso_datos_a, D_optimizator, perfiles_aprobados, ExcelPrincipal)
            
            print('')
            print('Restricciones para uniones Columna-Viga (Ancho de Patín)', '\n')   
        
            for l in range(len(pcv2)): 
        
                print(f"{[pares_VigaColumna[l][0], pares_VigaColumna[l][1]]} {Restriccion_VigaColumnas[l]:>27}")  
        
        
            uvc = pd.DataFrame({'Pares Viga - Columna\nAncho de Patín':pares_VigaColumna[:len(pcv2)], 'Validación':Restriccion_VigaColumnas})   
        
            uvc.index += 1 
            uvc.index.rename('Union', inplace=True)  
        
            if len(pcc2) > 0:
                print('\n')
                print('Restricciones para uniones Columna-Columna (Peralte)')
                for m in range(len(pcc2)): 
                    print(f"{[pares_ColumnaColumna[m][0], pares_ColumnaColumna[m][1]]}  {Restriccion_C2C1_hs[m]:>27} ")   
                    
                print('\n')
                print('Restricciones para uniones Columna-Columna (Ancho de Patín)')  
                for m in range(len(pcc2)): 
                    print(f"{[pares_ColumnaColumna[m][0], pares_ColumnaColumna[m][1]]}  {Restriccion_C2C1_bs[m]:>27} ")  
                    

                ucc_h = pd.DataFrame({'Pares Columna - Columna\nPeralte':pares_VigaColumna[:len(pcc2)], 'Validación':Restriccion_C2C1_hs})   
                ucc_h.index += 1 
                ucc_h.index.rename('Union', inplace=True)  
                
                ucc_b = pd.DataFrame({'Pares Columna - Columna\nPeralte':pares_VigaColumna[:len(pcc2)], 'Validación':Restriccion_C2C1_bs})   
                ucc_b.index += 1 
                ucc_b.index.rename('Union', inplace=True)  
         
                with pd.ExcelWriter('src_calculos/files/A_Resultados_Uniones_Restriccion.xlsx') as writer:
        
                    uvc.to_excel(writer, sheet_name='Union_VigCol')
                    ucc_h.to_excel(writer, sheet_name='Union_ColCol_Peralte')
                    ucc_b.to_excel(writer, sheet_name='Union_ColCol_Patin')       

         
            else:
                Restriccion_C2C1_h = 0
                Restriccion_C2C1_b = 0
                m = 0
                pcc2 = 0
                ucc_h = [0,0]
                ucc_b = [0,0]
                print('Restricciones para uniones Columna-Columna - No aplica')
                print(f"None {Restriccion_C2C1_h:>27} ")   
                print(f"None {Restriccion_C2C1_b:>27} ")   
                
        
                with pd.ExcelWriter('src_calculos/files/A_Resultados_Uniones_Restriccion.xlsx') as writer:
        
                    uvc.to_excel(writer, sheet_name='Union_VigCol')
        #        print(f"{pares_ColumnaColumna, pares_ColumnaColumna}  {Restriccion_C2C1_h:>24} {Restriccion_C2C1_b:>63}")  
        
            print('')    
            print(188*'=')
            print('\n','Criterio de miembros a compresión eficiente en ambos ejes')   
            print(' ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')  
            print('\n',' Indicaciones:','\n',' * Valores mayores o iguales a 0.35 indican un comportamiento en ambos ejes debido a su relación geométrica')  
            Restriccion_MiembroCompresion, Restriccion_MiembroCompresiones = Comp_Eficc(ExcelPrincipal, ingreso_datos_a, perfiles_aprobados, D_optimizator)      
        
            print('')
            print('Elemento a',5*' ','Relación Ry/Rx') 
            print('compresión') 
        
            
            for i in range(len(ingreso_datos_a)): 
                if ingreso_datos_a[i][1] == 'Col':
                    print(f"{i+1:02} {Restriccion_MiembroCompresiones[i]:>31}")            
        
            
            rmc = pd.DataFrame({'Relación Ry/Rx':Restriccion_MiembroCompresiones[:len(Restriccion_MiembroCompresiones)]})   
            rmc.index += 1 
            rmc.index.rename('Miembros a\nCompresion', inplace=True)  
        
            with pd.ExcelWriter('src_calculos/files/A_Resultados_CompEficc_Restriccion.xlsx') as writer:
        
                rmc.to_excel(writer, sheet_name='C.E_AmbosEjes')          
            

    my_console.close()
            






























































def detallado_b(lista_los_mejores, ExcelPrincipal, lista_final_p_bajo, ingreso_datos_b, D_optimizator, perfiles_aprobados,  D_nodos_totales, D_nodos_restringidos, D_criterio, Opcion_pesominimo):

    my_console = Logger('src_calculos/files/detailed_b.txt') 
    
    if (len(lista_los_mejores)) != 0:    
        print('DETALLE GENERAL DE RESULTADOS','\n')

        print('Nota: Es posible que exista una única opción, en cualquier caso se busca minimizar el peso estructural.','\n')

        print("Opción con el peso estructural más bajo de todas las opciones más óptimas:")
        print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯','\n')    
        
        lista_detalle = lista_final_p_bajo
        
        for lista_final_p_bajo in Opcion_pesominimo: # ================================================ 3.

            if len(lista_detalle) != 0:
                for i in range(0,len(ingreso_datos_b)):
                    if ingreso_datos_b[i][1] == 'Vig':
                        ingreso_datos_b[i][14]= lista_detalle[0][(len(lista_detalle[0])//2)+ingreso_datos_b[i][2]-1]
                    else:
                        ingreso_datos_b[i][14]=lista_detalle[0][ingreso_datos_b[i][2]-1]

            ingreso_datos_b, DatosPrincipales_actualizados = DatosPrograma(D_criterio, ingreso_datos_b, ExcelPrincipal)  
            
            print(188*'=')
            print('\n','Análisis Estructural')  
            print(' ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
        
            Longitudes, Qc_estructura, k_global_estructura, qnc_estructura, Qnc_estructura, F_elementos , PesoEstructural, nGDL_libres, k_global_estructura_presentacion_print, caracteristicas = analisis(ExcelPrincipal, D_nodos_totales, D_nodos_restringidos, 
                                                                                                                                     D_criterio, ingreso_datos_b, D_optimizator, perfiles_aprobados)
            
        
        
            vcg = pd.DataFrame(Qc_estructura)
            vcg.columns = ['Qc\n[kgf]']
            vcg.index += 0
            vcg.index.rename('nGDLT', inplace=True)
        
        
            matr = pd.DataFrame(k_global_estructura)
            matr.index.rename('kgf/m', inplace=True)
        
        
            desp = pd.DataFrame(qnc_estructura)
            desp.columns = ['qnc\n[m]']
            desp.index += 0
            desp.index.rename('nGDLT_Libres', inplace=True)
        
                
            rb = pd.DataFrame(Qnc_estructura)
            rb.columns = ['Qnc\n[kgf]']
            rb.index += nGDL_libres
            rb.index.rename('nGDLT_Restringidos', inplace=True)
        
            print('Las fuerzas en los elementos son: ','\n') 
            print('Elemento',1*' ','Tipo',14*' ','Pu_i',16*' ','Vu_i',18*' ','Mu_i',18*' ','Pu_j',18*' ','Vu_j',18*' ','Mu_j')             
            print('                ',1*' ','    ',13*' ','[kgf]',16*' ','[kgf]',15*' ','[kgf.m]',16*' ','[kgf]',18*' ','[kgf]',16*' ','[kgf.m]')             
        
            for i in range(len(ingreso_datos_b)): #--> Para cada fila en el rango de 'ingreso de DatosPrincipales'[i]...
                
                print(f"{i+1:02} {ingreso_datos_b[i][1]:>16} {F_elementos[i][0]:>20} {F_elementos[i][1]:>20}" 
                        f"{F_elementos[i][2]:>20} {F_elementos[i][3]:>20} {F_elementos[i][4]:>20}" 
                        f"{F_elementos[i][5]:>20}")            
        
            forc = pd.DataFrame(F_elementos)
            forc.columns = ['Pu_i\n[kgf]','Vui\n[kgf]','Mu_i\n[kgf*m]','Pu_j\n[kgf]','Vuj\n[kgf]','Muj\n[kgf*m]']
            forc.index += 1 
            forc.index.rename('Elemento', inplace=True)
            
            with pd.ExcelWriter('src_calculos/files/B_Resultados_Analisis.xlsx') as writer:
        
                vcg.to_excel(writer, sheet_name='CargasGeneralizadas')
                matr.to_excel(writer, sheet_name='MatrizGlobalEstructura')
                desp.to_excel(writer, sheet_name='Desplazamientos')
                rb.to_excel(writer, sheet_name='Reacciones')
                forc.to_excel(writer, sheet_name='FuerzasElementales')
        
            print('')    
            print(188*'=')
            print('\n','Diseño estructural [LRFD]')   
            print(' ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯') 
            
            (Restriccion_Demanda_Capacidades, promedio_DC, PesoEstructural, 
                
                KLR_diseno_listas, lamb_f_lista, lamb_rf_lista, Ala_C_lista,lamb_w_lista, lamb_rw_lista, Alma_C_lista, 
                TipoSeccion_Compresion_lista, Fe_lista, O1_lista, Qs_lista, f_lista, be_lista, Ae_lista, Q_lista, O2_lista, 
                FormaPandeo_Compresion_lista, Fcr_FB_lista, Pn_FB_lista, Fez_lista, Fcr_FTB_lista, Pn_FTB_lista, Pn_lista, Fhi_Pn_demo,
                
                lamb_pf_lista, lamb_prf_lista, Ala_F_lista, lamb_pw_lista, lamb_prw_lista, Alma_F_lista, TipoSeccion_Flexion_lista,
                Lp_lista, Lr_lista, ZonaPandeo_Flexion_lista, Mpx_lista, Mnx_Y_lista, Cb_lista, Fcrx_LTB_lista, Mnx_LTB_lista, ff1_lista,
                kc_lista, Mnx_FLB_lista, Mnx_lista, Fhi_Mnx_demo,
                
                TipoSeccion_Flexion_Y_lista, Mpy_lista, Mny_Y_lista, Fcr_FLB_lista, Mny_FLB_lista, Mny_lista, Fhi_Mny_demo,
                
                peso_elemento_lista, Longitudes, PesoTotalElemento_lista, Verificacion_lista, Muy_lista,
                
                tipoelementos, seccions) = disenioLRFD(ExcelPrincipal, ingreso_datos_b, F_elementos, D_optimizator, perfiles_aprobados)       
        
        
        
            compresion = pd.DataFrame({'kl/r_Diseño':KLR_diseno_listas[:len(ingreso_datos_b)],'λf':lamb_f_lista[:len(ingreso_datos_b)],
                                       'λrf':lamb_rf_lista[:len(ingreso_datos_b)], 'Esbeltez del ala':Ala_C_lista[:len(ingreso_datos_b)], 
                                       'λw':lamb_w_lista[:len(ingreso_datos_b)],'λrw':lamb_rw_lista[:len(ingreso_datos_b)], 'Esbeltez del alma':Alma_C_lista[:len(ingreso_datos_b)],
                                       'Tipo de Sección':TipoSeccion_Compresion_lista[:len(ingreso_datos_b)], 'Fe\n[kgf/m2]':Fe_lista[:len(ingreso_datos_b)], 'Frontera Le':O1_lista[:len(ingreso_datos_b)],
                                       'Qs\nEsbeltos no Rigidizados':Qs_lista[:len(ingreso_datos_b)],'f\nFcr_Y - No Esbeltas\n[kgf/m2]':f_lista[:len(ingreso_datos_b)],'be\nEsbeltos no Rigidizados\n[m]':be_lista[:len(ingreso_datos_b)],
                                       'Ae\nEsbeltos no Rigidizados\n[m2]':Ae_lista[:len(ingreso_datos_b)],'Q\nSecciones Esbeltas':Q_lista[:len(ingreso_datos_b)], 'Forma de Pandeo':FormaPandeo_Compresion_lista[:len(ingreso_datos_b)],
                                       'Fcr - FB\nPandeo Flexional\n[kgf/m2]':Fcr_FB_lista[:len(ingreso_datos_b)], 'Pn - FB\nPandeo Flexional\n[kgf]':Pn_FB_lista[:len(ingreso_datos_b)], 'Fez\n[kgf/m2]':Fez_lista[:len(ingreso_datos_b)],
                                       'FCR - FTB\nPandeo Flexotorsional\n[kgf/m2]':Fcr_FTB_lista[:len(ingreso_datos_b)], 'Pn - FTB\nPandeo Flexotorsional\n[kgf]':Pn_FTB_lista[:len(ingreso_datos_b)], 
                                       'Pn\n[kgf]':Pn_lista[:len(ingreso_datos_b)], 'ΦPn [LRFD]\n[kgf]':Fhi_Pn_demo[:len(ingreso_datos_b)]})
            compresion.index += 1 
            compresion.index.rename('Elemento', inplace=True)
        
        
                
        
            flexionx = pd.DataFrame({'λf':lamb_f_lista[:len(ingreso_datos_b)], 'λpf':lamb_pf_lista[:len(ingreso_datos_b)],'λprf':lamb_prf_lista[:len(ingreso_datos_b)], 
                                       'Esbeltez del ala':Ala_F_lista[:len(ingreso_datos_b)], 'λw':lamb_w_lista[:len(ingreso_datos_b)],'λpw':lamb_pw_lista[:len(ingreso_datos_b)],
                                       'λprw':lamb_prw_lista[:len(ingreso_datos_b)], 'Esbeltez del alma':Alma_F_lista[:len(ingreso_datos_b)], 'Tipo de Sección':TipoSeccion_Flexion_lista[:len(ingreso_datos_b)], 
                                       'Lp\n[m]':Lp_lista[:len(ingreso_datos_b)], 'Lr':Lr_lista[:len(ingreso_datos_b)], 'Zona de pandeo a Flexión':ZonaPandeo_Flexion_lista[:len(ingreso_datos_b)],
                                       'Mpx\n[kgf*m]':Mpx_lista[:len(ingreso_datos_b)],'Mnx - Y\nFluencia\n[kgf*m]':Mnx_Y_lista[:len(ingreso_datos_b)], 'Cb':Cb_lista[:len(ingreso_datos_b)],
                                       'Fcrx - LTB\nPandeo Lateral Torsional\n[kgf/m2]':Fcrx_LTB_lista[:len(ingreso_datos_b)], 'Mnx - LTB\nPandeo Lateral Torsional\n[kgf*m]':Mnx_LTB_lista[:len(ingreso_datos_b)],
                                       'kc - FLB\nPandeo Local del ala':kc_lista[:len(ingreso_datos_b)], 'Mnx\nPandeo Local del ala\n[kgf*m]':Mnx_FLB_lista[:len(ingreso_datos_b)], 
                                       'Mnx\n[kgf*m]':Mnx_lista[:len(ingreso_datos_b)],'ΦMn [LRFD]\n[kgf*m]':Fhi_Mnx_demo[:len(ingreso_datos_b)]})   
        
            flexionx.index += 1 
            flexionx.index.rename('Elemento', inplace=True)   
        
        
        
            flexiony = pd.DataFrame({'Tipo de Sección':TipoSeccion_Flexion_Y_lista[:len(ingreso_datos_b)],'Mpy\n[kgf*m]':Mpy_lista[:len(ingreso_datos_b)],'Mny - Y\nFluencia\n[kgf*m]':Mny_Y_lista[:len(ingreso_datos_b)], 
                                     'Fcry - FLB\nPandeo Local del ala\n[kgf/m2]':Fcr_FLB_lista[:len(ingreso_datos_b)], 'Mny\nPandeo Local del ala\n[kgf*m]':Mny_FLB_lista[:len(ingreso_datos_b)], 
                                       'Mny\n[kgf*m]':Mny_lista[:len(ingreso_datos_b)],'ΦMn [LRFD]\n[kgf*m]':Fhi_Mny_demo[:len(ingreso_datos_b)]})   
        
            flexiony.index += 1 
            flexiony.index.rename('Elemento', inplace=True)  
        
            
        #    print('\n','Sumario de diseño LRFD: ','\n')
            print('Indicaciones:','\n',' * Mientras más cercana es la relación Demanda/Capacidad a 1 por la izquierda, más óptimo es el diseño.','\n')
            print('Elemento',1*' ','Tipo',14*' ','Sección',14*' ','Peso',10*' ','Longitud',4*' ',
                  'Peso elemento',1*' ','Tipo de Verificación',58*' ','Pu',25*' ','Mux',20*' ','Muy',15*' ','Fhi_Pn',20*' ','Fhi_Mnx',16*' ',
                  'Fhi_Mny',10*' ','Relación D/C')
        
            print('        ',1*' ','    ',14*' ','       ',25*' ','[kgf/m]',12*' ','[m]',13*' ',
                  '[kgf]',94*' ',' ',1*'','[kgf]',20*' ','[kgf.m]',16*' ','[kgf.m]',13*' ','[kgf]',22*' ','[kgf.m]',18*' ',
                  '[kgf.m]',1*' ','            ')
        
        
            for i in range(len(ingreso_datos_b)): 
        
                print(f"{i+1:02} {ingreso_datos_b[i][1]:>16} {ingreso_datos_b[i][13]:>18} {ingreso_datos_b[i][14]:>1}" 
                        f"{'%.3f'%Decimal(peso_elemento_lista[i]):>20} {Longitudes[i]:>15} {'%.3f'%Decimal(PesoTotalElemento_lista[i]):>20} {Verificacion_lista[i]:>55}" 
                        f"{max(abs(F_elementos[i][0]), abs(F_elementos[i][3])):>25}" 
                        f"{max(abs(F_elementos[i][2]), abs(F_elementos[i][5])):>25}" 
                        f"{Muy_lista[i]:>18} {Fhi_Pn_demo[i]:>25} {Fhi_Mnx_demo[i]:>25} {Fhi_Mny_demo[i]:>25} {Restriccion_Demanda_Capacidades[i]:>20}")  
        
        
            diseo = pd.DataFrame({'Tipo de Elemento':tipoelementos[:len(ingreso_datos_b)],'Perfil Estructural':seccions[:len(ingreso_datos_b)],'Peso unitario\n[kgf/m]':peso_elemento_lista[:len(ingreso_datos_b)], 
                                  'Longitud\n[m]':Longitudes[:len(ingreso_datos_b)], 'Peso del elemento\n[kgf]':PesoTotalElemento_lista[:len(ingreso_datos_b)], 
                                  'Tipo de verificación\nDiseño':Verificacion_lista[:len(ingreso_datos_b)],'ΦPn [LRFD]\n[kgf]':Fhi_Pn_demo[:len(ingreso_datos_b)],
                                  'ΦMnx [LRFD]\n[kgf*m]':Fhi_Mnx_demo[:len(ingreso_datos_b)], 'ΦMny [LRFD]\n[kgf*m]':Fhi_Mny_demo[:len(ingreso_datos_b)], 'Relación Demanda/Capacidad':Restriccion_Demanda_Capacidades[:len(ingreso_datos_b)]})   
        
            diseo.index += 1 
            diseo.index.rename('Elemento', inplace=True)  
        
            with pd.ExcelWriter('src_calculos/files/B_Resultados_Diseno_Restriccion.xlsx') as writer:
        
                compresion.to_excel(writer, sheet_name='DisenioCompresion')
                flexionx.to_excel(writer, sheet_name='DisenioFlexion_X')
                flexiony.to_excel(writer, sheet_name='DisenioFlexion_Y')
                diseo.to_excel(writer, sheet_name='Restriccion_DC')
        
        
            print('\n','El peso de todos los elementos es de: ',round(PesoEstructural,3),' kgf')
            
            print('El promedio de demanda/capacidad es de: ', promedio_DC)
        
            print('')    
            print(188*'=')
            print('\n','Criterio correcto de ensamble en las uniones') 
            print(' ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
            print('\n',' Indicaciones:','\n',' * Valores menores o iguales a 0 indican un correcto ensamble')
        
            (validate, Restriccion_VigaColumna, Restriccion_C2C1_h, Restriccion_C2C1_b, 
             pares_VigaColumna, pares_ColumnaColumna, l, pcv2, m, pcc2,
             Restriccion_VigaColumnas, Restriccion_C2C1_hs, Restriccion_C2C1_bs) = unionesVC(ingreso_datos_b, D_optimizator, perfiles_aprobados, ExcelPrincipal)
            
            print('')
            print('Restricciones para uniones Columna-Viga (Ancho de Patín)', '\n')   
        
            for l in range(len(pcv2)): 
        
                print(f"{[pares_VigaColumna[l][0], pares_VigaColumna[l][1]]} {Restriccion_VigaColumnas[l]:>27}")  
        
            uvc = pd.DataFrame({'Pares Viga - Columna\nAncho de Patín':pares_VigaColumna[:len(pcv2)], 'Validación':Restriccion_VigaColumnas})   
        
            uvc.index += 1 
            uvc.index.rename('Union', inplace=True)  
        
            if len(pcc2) > 0:
                print('\n')
                print('Restricciones para uniones Columna-Columna (Peralte)')
                for m in range(len(pcc2)): 
                    print(f"{[pares_ColumnaColumna[m][0], pares_ColumnaColumna[m][1]]}  {Restriccion_C2C1_hs[m]:>27} ")   
                    
                print('\n')
                print('Restricciones para uniones Columna-Columna (Ancho de Patín)')  
                for m in range(len(pcc2)): 
                    print(f"{[pares_ColumnaColumna[m][0], pares_ColumnaColumna[m][1]]}  {Restriccion_C2C1_bs[m]:>27} ")  

                ucc_h = pd.DataFrame({'Pares Columna - Columna\nPeralte':pares_VigaColumna[:len(pcc2)], 'Validación':Restriccion_C2C1_hs})   
                ucc_h.index += 1 
                ucc_h.index.rename('Union', inplace=True)  
                
                ucc_b = pd.DataFrame({'Pares Columna - Columna\nPeralte':pares_VigaColumna[:len(pcc2)], 'Validación':Restriccion_C2C1_bs})   
                ucc_b.index += 1 
                ucc_b.index.rename('Union', inplace=True)  
         
                with pd.ExcelWriter('src_calculos/files/B_Resultados_Uniones_Restriccion.xlsx') as writer:
        
                    uvc.to_excel(writer, sheet_name='Union_VigCol')
                    ucc_h.to_excel(writer, sheet_name='Union_ColCol_Peralte')
                    ucc_b.to_excel(writer, sheet_name='Union_ColCol_Patin')     
                    
        
            else:
                Restriccion_C2C1_h = 0
                Restriccion_C2C1_b = 0
                m = 0
                pcc2 = 0
                ucc_h = [0,0]
                ucc_b = [0,0]
                print('Restricciones para uniones Columna-Columna - No aplica')
                print(f"None {Restriccion_C2C1_h:>27} ")   
                print(f"None {Restriccion_C2C1_b:>27} ")   
                
        
                with pd.ExcelWriter('src_calculos/files/B_Resultados_Uniones_Restriccion.xlsx') as writer:
        
                    uvc.to_excel(writer, sheet_name='Union_VigCol')
        #        print(f"{pares_ColumnaColumna, pares_ColumnaColumna}  {Restriccion_C2C1_h:>24} {Restriccion_C2C1_b:>63}")  
        
            print('')    
            print(188*'=')
            print('\n','Criterio de miembros a compresión eficiente en ambos ejes')   
            print(' ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')  
            print('\n',' Indicaciones:','\n',' * Valores mayores o iguales a 0.35 indican un comportamiento en ambos ejes debido a su relación geométrica')  
            Restriccion_MiembroCompresion, Restriccion_MiembroCompresiones = Comp_Eficc(ExcelPrincipal, ingreso_datos_b, perfiles_aprobados, D_optimizator)      
        
            print('')
            print('Elemento a',5*' ','Relación Ry/Rx') 
            print('compresión') 
        
            
            for i in range(len(ingreso_datos_b)): 
                if ingreso_datos_b[i][1] == 'Col':
                    print(f"{i+1:02} {Restriccion_MiembroCompresiones[i]:>31}")            
        
            
            rmc = pd.DataFrame({'Relación Ry/Rx':Restriccion_MiembroCompresiones[:len(Restriccion_MiembroCompresiones)]})   
            rmc.index += 1 
            rmc.index.rename('Miembros a\nCompresion', inplace=True)  
        
            with pd.ExcelWriter('src_calculos/files/B_Resultados_CompEficc_Restriccion.xlsx') as writer:
        
                rmc.to_excel(writer, sheet_name='C.E_AmbosEjes')         
            

    my_console.close()
            


















     