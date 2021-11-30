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

from src_calc.loggerPrint import Logger

from src_calc.methods.analysis import analisis
from src_calc.methods.designlrfd import disenioLRFD
from src_calc.methods.dataprogram import DatosPrograma
from src_calc.methods.assemblyBC import unionesVC
from src_calc.methods.compressioneficc import Comp_Eficc


def detallado(ExcelPrincipal, lista_detalle, ingreso_datos, D_optimizator, perfiles_aprobados,  D_nodos_totales, D_nodos_restringidos, D_criterio):
    
    my_console = Logger('src_calc/onefile/onedetailed.txt') 
    
    print('GENERAL DETAIL OF RESULTS','\n')

    print('Note: the results of the current window, are only analysis and design of the model, if you wish to optimize, go to the respective button at previous window.','\n')


    
    if len(lista_detalle) != 0:
        for i in range(0,len(ingreso_datos)):
            if ingreso_datos[i][1] == 'Beam':
                ingreso_datos[i][14]= lista_detalle[0][(len(lista_detalle[0])//2)+ingreso_datos[i][2]-1]
            else:
                ingreso_datos[i][14]=lista_detalle[0][ingreso_datos[i][2]-1]
    

    ingreso_datos, DatosPrincipales_actualizados = DatosPrograma(D_criterio, ingreso_datos, ExcelPrincipal)  
    


    print(188*'=')
    print('\n','Structural Analysis')  
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
    desp.index.rename('nGDLT_Free', inplace=True)

        
    rb = pd.DataFrame(Qnc_estructura)
    rb.columns = ['Qnc\n[kgf]']
    rb.index += nGDL_libres
    rb.index.rename('nGDLT_Restrained', inplace=True)

    print('Forces at the elements are: ','\n') 
    print('Element',7*' ','Type Element',10*' ','Pu_i',16*' ','Vu_i',18*' ','Mu_i',18*' ','Pu_j',18*' ','Vu_j',18*' ','Mu_j')             
    print('                ',1*' ','    ',27*' ','[kgf]',16*' ','[kgf]',15*' ','[kgf.m]',16*' ','[kgf]',18*' ','[kgf]',16*' ','[kgf.m]')             

    for i in range(len(ingreso_datos)): #--> Para cada fila en el rango de 'ingreso de DatosPrincipales'[i]...
        
        print(f"{i+1:>2} {ingreso_datos[i][1]:>26} {F_elementos[i][0]:>25} {F_elementos[i][1]:>20}" 
                f"{F_elementos[i][2]:>22} {F_elementos[i][3]:>23} {F_elementos[i][4]:>23}" 
                f"{F_elementos[i][5]:>24}")            

    forc = pd.DataFrame(F_elementos)
    forc.columns = ['Pu_i\n[kgf]','Vui\n[kgf]','Mu_i\n[kgf*m]','Pu_j\n[kgf]','Vuj\n[kgf]','Muj\n[kgf*m]']
    forc.index += 1 
    forc.index.rename('Element', inplace=True)
    
    with pd.ExcelWriter('src_calc/onefile/AnalysisResults.xlsx') as writer:

        vcg.to_excel(writer, sheet_name='GeneralizedLoads')
        matr.to_excel(writer, sheet_name='RigidMatrixGlobal')
        desp.to_excel(writer, sheet_name='Displacements')
        rb.to_excel(writer, sheet_name='Reactions')
        forc.to_excel(writer, sheet_name='Forces')

    print('')    
    print(188*'=')
    print('\n','Structural Design [LRFD]')   
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



    compresion = pd.DataFrame({'kl/r_Design':KLR_diseno_listas[:len(ingreso_datos)],'λf':lamb_f_lista[:len(ingreso_datos)],
                               'λrf':lamb_rf_lista[:len(ingreso_datos)], 'Slenderness Flange':Ala_C_lista[:len(ingreso_datos)], 
                               'λw':lamb_w_lista[:len(ingreso_datos)],'λrw':lamb_rw_lista[:len(ingreso_datos)], 'Slenderness Web':Alma_C_lista[:len(ingreso_datos)],
                               'Type Section':TipoSeccion_Compresion_lista[:len(ingreso_datos)], 'Fe\n[kgf/m2]':Fe_lista[:len(ingreso_datos)], 'Bourder Le':O1_lista[:len(ingreso_datos)],
                               'Qs\nSlender Unstiffened Elements':Qs_lista[:len(ingreso_datos)],'f\nFcr_Y - Nonslender\n[kgf/m2]':f_lista[:len(ingreso_datos)],'be\nSlender Unstiffened Elements\n[m]':be_lista[:len(ingreso_datos)],
                               'Ae\nSlender Unstiffened Elements\n[m2]':Ae_lista[:len(ingreso_datos)],'Q\nSlender Sections':Q_lista[:len(ingreso_datos)], 'Buckling Type':FormaPandeo_Compresion_lista[:len(ingreso_datos)],
                               'Fcr - FB\nFlexural Buckling\n[kgf/m2]':Fcr_FB_lista[:len(ingreso_datos)], 'Pn - FB\nFlexural Buckling\n[kgf]':Pn_FB_lista[:len(ingreso_datos)], 'Fez\n[kgf/m2]':Fez_lista[:len(ingreso_datos)],
                               'FCR - FTB\nFlexural - Torsional Buckling\n[kgf/m2]':Fcr_FTB_lista[:len(ingreso_datos)], 'Pn - FTB\nFlexural - Torsional Buckling\n[kgf]':Pn_FTB_lista[:len(ingreso_datos)], 
                               'Pn\n[kgf]':Pn_lista[:len(ingreso_datos)], 'ΦPn [LRFD]\n[kgf]':Fhi_Pn_demo[:len(ingreso_datos)]})
    compresion.index += 1 
    compresion.index.rename('Element', inplace=True)


        

    flexionx = pd.DataFrame({'λf':lamb_f_lista[:len(ingreso_datos)], 'λpf':lamb_pf_lista[:len(ingreso_datos)],'λprf':lamb_prf_lista[:len(ingreso_datos)], 
                               'Slenderness Flange':Ala_F_lista[:len(ingreso_datos)], 'λw':lamb_w_lista[:len(ingreso_datos)],'λpw':lamb_pw_lista[:len(ingreso_datos)],
                               'λprw':lamb_prw_lista[:len(ingreso_datos)], 'Slenderness Web':Alma_F_lista[:len(ingreso_datos)], 'Type Section':TipoSeccion_Flexion_lista[:len(ingreso_datos)], 
                               'Lp\n[m]':Lp_lista[:len(ingreso_datos)], 'Lr':Lr_lista[:len(ingreso_datos)], 'Flexural buckling zone':ZonaPandeo_Flexion_lista[:len(ingreso_datos)],
                               'Mpx\n[kgf*m]':Mpx_lista[:len(ingreso_datos)],'Mnx - Y\nYielding\n[kgf*m]':Mnx_Y_lista[:len(ingreso_datos)], 'Cb':Cb_lista[:len(ingreso_datos)],
                               'Fcrx - LTB\nLateral - Torsional Buckling\n[kgf/m2]':Fcrx_LTB_lista[:len(ingreso_datos)], 'Mnx - LTB\nLateral - Torsional Buckling\n[kgf*m]':Mnx_LTB_lista[:len(ingreso_datos)],
                               'kc - FLB\nFlange Local Buckling':kc_lista[:len(ingreso_datos)], 'Mnx\nFlange Local Buckling\n[kgf*m]':Mnx_FLB_lista[:len(ingreso_datos)], 
                               'Mnx\n[kgf*m]':Mnx_lista[:len(ingreso_datos)],'ΦMn [LRFD]\n[kgf*m]':Fhi_Mnx_demo[:len(ingreso_datos)]})   

    flexionx.index += 1 
    flexionx.index.rename('Element', inplace=True)   




    flexiony = pd.DataFrame({'Type Section':TipoSeccion_Flexion_Y_lista[:len(ingreso_datos)],'Mpy\n[kgf*m]':Mpy_lista[:len(ingreso_datos)],'Mny - Y\nYielding\n[kgf*m]':Mny_Y_lista[:len(ingreso_datos)], 
                             'Fcry - FLB\nFlange Local Buckling\n[kgf/m2]':Fcr_FLB_lista[:len(ingreso_datos)], 'Mny\nFlange Local Buckling\n[kgf*m]':Mny_FLB_lista[:len(ingreso_datos)], 
                               'Mny\n[kgf*m]':Mny_lista[:len(ingreso_datos)],'ΦMn [LRFD]\n[kgf*m]':Fhi_Mny_demo[:len(ingreso_datos)]})   

    flexiony.index += 1 
    flexiony.index.rename('Element', inplace=True)  

    
#    print('\n','Sumario de diseño LRFD: ','\n')
    print('Instructions:','\n',' * While D/C is closer to 1 by the left, more optimal is the design..','\n')
    print('Element',7*' ','Type Element',3*' ','Cross Section Specific',6*' ','Weight',5*' ','Length',4*' ',
          'Element weight',1*' ','Verification Type',40*' ','Pu',25*' ','Mux',20*' ','Muy',15*' ','Fhi_Pn',20*' ','Fhi_Mnx',16*' ',
          'Fhi_Mny',10*' ','Ratio D/C')

    print('        ',1*' ','    ',14*' ','       ',48*' ','[kgf/m]',6*' ','[m]',13*' ',
          '[kgf]',72*' ',' ',1*'','[kgf]',20*' ','[kgf.m]',16*' ','[kgf.m]',13*' ','[kgf]',22*' ','[kgf.m]',18*' ',
          '[kgf.m]',1*' ','            ')


    for i in range(len(ingreso_datos)): 

        print(f"{i+1:>2} {ingreso_datos[i][1]:>26} {ingreso_datos[i][13]:>24} {ingreso_datos[i][14]:>8}" 
                f"{'%.3f'%Decimal(peso_elemento_lista[i]):>22} {Longitudes[i]:>13} {'%.3f'%Decimal(PesoTotalElemento_lista[i]):>20} {Verificacion_lista[i]:>45}" 
                f"{max(abs(F_elementos[i][0]), abs(F_elementos[i][3])):>18}" 
                f"{max(abs(F_elementos[i][2]), abs(F_elementos[i][5])):>28}" 
                f"{Muy_lista[i]:>21} {Fhi_Pn_demo[i]:>26} {Fhi_Mnx_demo[i]:>26} {Fhi_Mny_demo[i]:>26} {Restriccion_Demanda_Capacidades[i]:>20}")  


    diseo = pd.DataFrame({'Type Element':tipoelementos[:len(ingreso_datos)],'Cross Section Specific':seccions[:len(ingreso_datos)],'Weight per unit\n[kgf/m]':peso_elemento_lista[:len(ingreso_datos)], 
                          'Length\n[m]':Longitudes[:len(ingreso_datos)], 'Weight\n[kgf]':PesoTotalElemento_lista[:len(ingreso_datos)], 
                          'Verification Type\nDesign':Verificacion_lista[:len(ingreso_datos)],'ΦPn [LRFD]\n[kgf]':Fhi_Pn_demo[:len(ingreso_datos)],
                          'ΦMnx [LRFD]\n[kgf*m]':Fhi_Mnx_demo[:len(ingreso_datos)], 'ΦMny [LRFD]\n[kgf*m]':Fhi_Mny_demo[:len(ingreso_datos)], 'Ratio Demand/Capacity':Restriccion_Demanda_Capacidades[:len(ingreso_datos)]})   

    diseo.index += 1 
    diseo.index.rename('Element', inplace=True)  

    with pd.ExcelWriter('src_calc/onefile/DesignRestrictionResult.xlsx') as writer:

        compresion.to_excel(writer, sheet_name='CompressionDesign')
        flexionx.to_excel(writer, sheet_name='FlexuralDesign_X')
        flexiony.to_excel(writer, sheet_name='FlexuralDesign_Y')
        diseo.to_excel(writer, sheet_name='Ratio_DC')


    print('\n','Total structure weight is: ',round(PesoEstructural,3),' kgf')
    
    print('Average demand/capacity: ', promedio_DC)

    print('')    
    print(188*'=')
    print('\n','Correct criterion of assembly in the joints') 
    print(' ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    print('\n',' Instructions:','\n',' * Values less than or equal to 0 indicate a correct assembly')

    (validate, Restriccion_VigaColumna, Restriccion_C2C1_h, Restriccion_C2C1_b, 
     pares_VigaColumna, pares_ColumnaColumna, l, pcv2, m, pcc2,
     Restriccion_VigaColumnas, Restriccion_C2C1_hs, Restriccion_C2C1_bs) = unionesVC(ingreso_datos, D_optimizator, perfiles_aprobados, ExcelPrincipal)
    
    print('')
    print('Restrictions for column-beam connections (Flange)', '\n')   

    for l in range(len(pcv2)): 

        print(f"{[pares_VigaColumna[l][0], pares_VigaColumna[l][1]]} {Restriccion_VigaColumnas[l]:>27}")  

    uvc = pd.DataFrame({'Beam - Column Pairs\nFlange':pares_VigaColumna[:len(pcv2)], 'Validation':Restriccion_VigaColumnas})   

    uvc.index += 1 
    uvc.index.rename('Joint', inplace=True)  

    if len(pcc2) > 0:
        print('\n')
        print('Restrictions for Column-Column connections (Depth)')
        for m in range(len(pcc2)): 
            print(f"{[pares_ColumnaColumna[m][0], pares_ColumnaColumna[m][1]]}  {Restriccion_C2C1_hs[m]:>27} ")   
            
        print('\n')
        print('Restrictions for Column-Column connections (Flange)')  
        for m in range(len(pcc2)): 
            print(f"{[pares_ColumnaColumna[m][0], pares_ColumnaColumna[m][1]]}  {Restriccion_C2C1_bs[m]:>27} ")  

        ucc_h = pd.DataFrame({'Column - Column Pairs\nDepth':pares_VigaColumna[:len(pcc2)], 'Validation':Restriccion_C2C1_hs})   
        ucc_h.index += 1 
        ucc_h.index.rename('Joint', inplace=True)  
        
        ucc_b = pd.DataFrame({'Column - Column Pairs\nFlange':pares_VigaColumna[:len(pcc2)], 'Validation':Restriccion_C2C1_bs})   
        ucc_b.index += 1 
        ucc_b.index.rename('Joint', inplace=True)  
 
        with pd.ExcelWriter('src_calc/onefile/JointRestrictionResults.xlsx') as writer:

            uvc.to_excel(writer, sheet_name='BeamColJoint')
            ucc_h.to_excel(writer, sheet_name='ColColJoint_Depth')
            ucc_b.to_excel(writer, sheet_name='ColColJoint_Flange')            

    else:
        Restriccion_C2C1_h = 0
        Restriccion_C2C1_b = 0
        m = 0
        pcc2 = 0
        ucc_h = [0,0]
        ucc_b = [0,0]
        print('Restrictions for Column-Column connections - Does not apply')
        print(f"None {Restriccion_C2C1_h:>27} ")   
        print(f"None {Restriccion_C2C1_b:>27} ")    
        
        ucc_b = pd.DataFrame({'Column - Column Pairs\nFlange':[0], 'Validation':[0]})   
        ucc_h = pd.DataFrame({'Column - Column Pairs\nFlange':[0], 'Validation':[0]})   

        with pd.ExcelWriter('src_calc/onefile/JointRestrictionResults.xlsx') as writer:

            uvc.to_excel(writer, sheet_name='BeamColJoint')
            ucc_h.to_excel(writer, sheet_name='ColColJoint_Depth')
            ucc_b.to_excel(writer, sheet_name='ColColJoint_Flange')  
#        print(f"{pares_ColumnaColumna, pares_ColumnaColumna}  {Restriccion_C2C1_h:>24} {Restriccion_C2C1_b:>63}")  

    print('')    
    print(188*'=')
    print('\n','Criterion of members to efficient compression in both axes')   
    print(' ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')  
    print('\n',' Instructions:','\n',' * Values greater than or equal to 0.35 indicate a behavior in both axes due to their geometric relationship')  
    Restriccion_MiembroCompresion, Restriccion_MiembroCompresiones = Comp_Eficc(ExcelPrincipal, ingreso_datos, perfiles_aprobados, D_optimizator)      
 
    print('')
    print('Element a',5*' ','Ratio Ry/Rx') 
    print('Compression') 

    
    for i in range(len(ingreso_datos)): 
        if ingreso_datos[i][1] == 'Column':
            print(f"{i+1:02} {Restriccion_MiembroCompresiones[i]:>31}")            

    
    rmc = pd.DataFrame({'Ratio Ry/Rx':Restriccion_MiembroCompresiones[:len(Restriccion_MiembroCompresiones)]})   
    rmc.index += 1 
    rmc.index.rename('Compression\nMembers', inplace=True)  

    with pd.ExcelWriter('src_calc/onefile/CompEficRestrictionResults.xlsx') as writer:

        rmc.to_excel(writer, sheet_name='CEE.BothAxes')          
    

    my_console.close()

#    sys.stdout = orig_stdout
#    f.close()
        

#    elif D_criterio == 0:
#        print('\n','Esta restricción no aplica en base al cumplimiento que se quiere satisfacer','\n') 



















































def detallado_a(lista_los_mejores, ExcelPrincipal, lista_final_pv_bajo, ingreso_datos_a, D_optimizator, perfiles_aprobados,  D_nodos_totales, D_nodos_restringidos, D_criterio, lista_minimo_peso_variabilidad):
   
    my_console = Logger('src_calc/files/detailed_a.txt') 
    
    if (len(lista_los_mejores)) != 0:    

        print('GENERAL DETAIL OF RESULTS','\n')

        print('Note: It is possible that there is only one option, in any case it seeks to minimize the structural weight.','\n')

        print("Option with the lowest construction complexity index of all the most optimal options:")
        print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯','\n')    


        
        lista_detalle = lista_final_pv_bajo
        
        for lista_final_pv_bajo in lista_minimo_peso_variabilidad: # ================================================ 3.
            
            if len(lista_detalle) != 0:
                for i in range(0,len(ingreso_datos_a)):
                    if ingreso_datos_a[i][1] == 'Beam':
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
            desp.index.rename('nGDLT_Free', inplace=True)
        
                
            rb = pd.DataFrame(Qnc_estructura)
            rb.columns = ['Qnc\n[kgf]']
            rb.index += nGDL_libres
            rb.index.rename('nGDLT_Restrained', inplace=True)
        
            print('Forces at the elements are: ','\n') 
            print('Element',7*' ','Type Element',10*' ','Pu_i',16*' ','Vu_i',18*' ','Mu_i',18*' ','Pu_j',18*' ','Vu_j',18*' ','Mu_j')             
            print('                ',1*' ','    ',27*' ','[kgf]',16*' ','[kgf]',15*' ','[kgf.m]',16*' ','[kgf]',18*' ','[kgf]',16*' ','[kgf.m]')            
        
            for i in range(len(ingreso_datos_a)): #--> Para cada fila en el rango de 'ingreso de DatosPrincipales'[i]...
                
                print(f"{i+1:>2} {ingreso_datos_a[i][1]:>26} {F_elementos[i][0]:>25} {F_elementos[i][1]:>20}" 
                        f"{F_elementos[i][2]:>22} {F_elementos[i][3]:>23} {F_elementos[i][4]:>23}" 
                        f"{F_elementos[i][5]:>24}")         
        
            forc = pd.DataFrame(F_elementos)
            forc.columns = ['Pu_i\n[kgf]','Vui\n[kgf]','Mu_i\n[kgf*m]','Pu_j\n[kgf]','Vuj\n[kgf]','Muj\n[kgf*m]']
            forc.index += 1 
            forc.index.rename('Element', inplace=True)
            
            with pd.ExcelWriter('src_calc/files/A_AnalysisResults.xlsx') as writer:
        
                vcg.to_excel(writer, sheet_name='GeneralizedLoads')
                matr.to_excel(writer, sheet_name='RigidMatrixGlobal')
                desp.to_excel(writer, sheet_name='Displacements')
                rb.to_excel(writer, sheet_name='Reactions')
                forc.to_excel(writer, sheet_name='Forces')
        
            print('')    
            print(188*'=')
            print('\n','Structural Design [LRFD]')   
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
        
        
        
        
            compresion = pd.DataFrame({'kl/r_Design':KLR_diseno_listas[:len(ingreso_datos_a)],'λf':lamb_f_lista[:len(ingreso_datos_a)],
                                       'λrf':lamb_rf_lista[:len(ingreso_datos_a)], 'Slenderness Flange':Ala_C_lista[:len(ingreso_datos_a)], 
                                       'λw':lamb_w_lista[:len(ingreso_datos_a)],'λrw':lamb_rw_lista[:len(ingreso_datos_a)], 'Slenderness Web':Alma_C_lista[:len(ingreso_datos_a)],
                                       'Type Section':TipoSeccion_Compresion_lista[:len(ingreso_datos_a)], 'Fe\n[kgf/m2]':Fe_lista[:len(ingreso_datos_a)], 'Bourder Le':O1_lista[:len(ingreso_datos_a)],
                                       'Qs\nSlender Unstiffened Elements':Qs_lista[:len(ingreso_datos_a)],'f\nFcr_Y - Nonslender\n[kgf/m2]':f_lista[:len(ingreso_datos_a)],'be\nSlender Unstiffened Elements\n[m]':be_lista[:len(ingreso_datos_a)],
                                       'Ae\nSlender Unstiffened Elements\n[m2]':Ae_lista[:len(ingreso_datos_a)],'Q\nSlender Sections':Q_lista[:len(ingreso_datos_a)], 'Buckling Type':FormaPandeo_Compresion_lista[:len(ingreso_datos_a)],
                                       'Fcr - FB\nFlexural Buckling\n[kgf/m2]':Fcr_FB_lista[:len(ingreso_datos_a)], 'Pn - FB\nFlexural Buckling\n[kgf]':Pn_FB_lista[:len(ingreso_datos_a)], 'Fez\n[kgf/m2]':Fez_lista[:len(ingreso_datos_a)],
                                       'FCR - FTB\nFlexural - Torsional Buckling\n[kgf/m2]':Fcr_FTB_lista[:len(ingreso_datos_a)], 'Pn - FTB\nFlexural - Torsional Buckling\n[kgf]':Pn_FTB_lista[:len(ingreso_datos_a)], 
                                       'Pn\n[kgf]':Pn_lista[:len(ingreso_datos_a)], 'ΦPn [LRFD]\n[kgf]':Fhi_Pn_demo[:len(ingreso_datos_a)]})
            compresion.index += 1 
            compresion.index.rename('Element', inplace=True)
        
        
                
        
            flexionx = pd.DataFrame({'λf':lamb_f_lista[:len(ingreso_datos_a)], 'λpf':lamb_pf_lista[:len(ingreso_datos_a)],'λprf':lamb_prf_lista[:len(ingreso_datos_a)], 
                                       'Slenderness Flange':Ala_F_lista[:len(ingreso_datos_a)], 'λw':lamb_w_lista[:len(ingreso_datos_a)],'λpw':lamb_pw_lista[:len(ingreso_datos_a)],
                                       'λprw':lamb_prw_lista[:len(ingreso_datos_a)], 'Slenderness Web':Alma_F_lista[:len(ingreso_datos_a)], 'Type Section':TipoSeccion_Flexion_lista[:len(ingreso_datos_a)], 
                                       'Lp\n[m]':Lp_lista[:len(ingreso_datos_a)], 'Lr':Lr_lista[:len(ingreso_datos_a)], 'Flexural buckling zone':ZonaPandeo_Flexion_lista[:len(ingreso_datos_a)],
                                       'Mpx\n[kgf*m]':Mpx_lista[:len(ingreso_datos_a)],'Mnx - Y\nYielding\n[kgf*m]':Mnx_Y_lista[:len(ingreso_datos_a)], 'Cb':Cb_lista[:len(ingreso_datos_a)],
                                       'Fcrx - LTB\nLateral - Torsional Buckling\n[kgf/m2]':Fcrx_LTB_lista[:len(ingreso_datos_a)], 'Mnx - LTB\nLateral - Torsional Buckling\n[kgf*m]':Mnx_LTB_lista[:len(ingreso_datos_a)],
                                       'kc - FLB\nFlange Local Buckling':kc_lista[:len(ingreso_datos_a)], 'Mnx\nFlange Local Buckling\n[kgf*m]':Mnx_FLB_lista[:len(ingreso_datos_a)], 
                                       'Mnx\n[kgf*m]':Mnx_lista[:len(ingreso_datos_a)],'ΦMn [LRFD]\n[kgf*m]':Fhi_Mnx_demo[:len(ingreso_datos_a)]})   
        
            flexionx.index += 1 
            flexionx.index.rename('Element', inplace=True)   
        
        
        
        
            flexiony = pd.DataFrame({'Type Section':TipoSeccion_Flexion_Y_lista[:len(ingreso_datos_a)],'Mpy\n[kgf*m]':Mpy_lista[:len(ingreso_datos_a)],'Mny - Y\nYielding\n[kgf*m]':Mny_Y_lista[:len(ingreso_datos_a)], 
                                     'Fcry - FLB\nFlange Local Buckling\n[kgf/m2]':Fcr_FLB_lista[:len(ingreso_datos_a)], 'Mny\nFlange Local Buckling\n[kgf*m]':Mny_FLB_lista[:len(ingreso_datos_a)], 
                                       'Mny\n[kgf*m]':Mny_lista[:len(ingreso_datos_a)],'ΦMn [LRFD]\n[kgf*m]':Fhi_Mny_demo[:len(ingreso_datos_a)]})   
        
            flexiony.index += 1 
            flexiony.index.rename('Element', inplace=True)  
        
            
            print('Instructions:','\n',' * While D/C is closer to 1 by the left, more optimal is the design..','\n')
            print('Element',7*' ','Type Element',3*' ','Cross Section Specific',6*' ','Weight',5*' ','Length',4*' ',
                  'Element weight',1*' ','Verification Type',40*' ','Pu',25*' ','Mux',20*' ','Muy',15*' ','Fhi_Pn',20*' ','Fhi_Mnx',16*' ',
                  'Fhi_Mny',10*' ','Ratio D/C')
        
            print('        ',1*' ','    ',14*' ','       ',48*' ','[kgf/m]',6*' ','[m]',13*' ',
                  '[kgf]',72*' ',' ',1*'','[kgf]',20*' ','[kgf.m]',16*' ','[kgf.m]',13*' ','[kgf]',22*' ','[kgf.m]',18*' ',
                  '[kgf.m]',1*' ','            ')
        
        
            for i in range(len(ingreso_datos_a)): 
        
                print(f"{i+1:>2} {ingreso_datos_a[i][1]:>26} {ingreso_datos_a[i][13]:>24} {ingreso_datos_a[i][14]:>8}" 
                        f"{'%.3f'%Decimal(peso_elemento_lista[i]):>22} {Longitudes[i]:>13} {'%.3f'%Decimal(PesoTotalElemento_lista[i]):>20} {Verificacion_lista[i]:>45}" 
                        f"{max(abs(F_elementos[i][0]), abs(F_elementos[i][3])):>18}" 
                        f"{max(abs(F_elementos[i][2]), abs(F_elementos[i][5])):>28}" 
                        f"{Muy_lista[i]:>21} {Fhi_Pn_demo[i]:>26} {Fhi_Mnx_demo[i]:>26} {Fhi_Mny_demo[i]:>26} {Restriccion_Demanda_Capacidades[i]:>20}") 
        
        
            diseo = pd.DataFrame({'Type Element':tipoelementos[:len(ingreso_datos_a)],'Cross Section Specific':seccions[:len(ingreso_datos_a)],'Weight per unit\n[kgf/m]':peso_elemento_lista[:len(ingreso_datos_a)], 
                                  'Length\n[m]':Longitudes[:len(ingreso_datos_a)], 'Weight\n[kgf]':PesoTotalElemento_lista[:len(ingreso_datos_a)], 
                                  'Verification Type\nDesign':Verificacion_lista[:len(ingreso_datos_a)],'ΦPn [LRFD]\n[kgf]':Fhi_Pn_demo[:len(ingreso_datos_a)],
                                  'ΦMnx [LRFD]\n[kgf*m]':Fhi_Mnx_demo[:len(ingreso_datos_a)], 'ΦMny [LRFD]\n[kgf*m]':Fhi_Mny_demo[:len(ingreso_datos_a)], 'Ratio Demand/Capacity':Restriccion_Demanda_Capacidades[:len(ingreso_datos_a)]})   
        
            diseo.index += 1 
            diseo.index.rename('Element', inplace=True)  
        
            with pd.ExcelWriter('src_calc/files/A_DesignRestrictionResult.xlsx') as writer:
        
                compresion.to_excel(writer, sheet_name='CompressionDesign')
                flexionx.to_excel(writer, sheet_name='FlexuralDesign_X')
                flexiony.to_excel(writer, sheet_name='FlexuralDesign_Y')
                diseo.to_excel(writer, sheet_name='Ratio_DC')
        
        
            print('\n','Total structure weight is: ',round(PesoEstructural,3),' kgf')
            
            print('Average demand/capacity: ', promedio_DC)
        
            print('')    
            print(188*'=')
            print('\n','Correct criterion of assembly in the joints') 
            print(' ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
            print('\n',' Instructions:','\n',' * Values less than or equal to 0 indicate a correct assembly')
        
        
            (validate, Restriccion_VigaColumna, Restriccion_C2C1_h, Restriccion_C2C1_b, 
             pares_VigaColumna, pares_ColumnaColumna, l, pcv2, m, pcc2,
             Restriccion_VigaColumnas, Restriccion_C2C1_hs, Restriccion_C2C1_bs) = unionesVC(ingreso_datos_a, D_optimizator, perfiles_aprobados, ExcelPrincipal)
            
            print('')
            print('Restrictions for column-beam connections (Flange)', '\n')   
        
            for l in range(len(pcv2)): 
        
                print(f"{[pares_VigaColumna[l][0], pares_VigaColumna[l][1]]} {Restriccion_VigaColumnas[l]:>27}")  
        
        
            uvc = pd.DataFrame({'Beam - Column Pairs\nFlange':pares_VigaColumna[:len(pcv2)], 'Validation':Restriccion_VigaColumnas})   
        
            uvc.index += 1 
            uvc.index.rename('Joint', inplace=True)  
        
            if len(pcc2) > 0:
                print('\n')
                print('Restrictions for Column-Column connections (Depth)')
                for m in range(len(pcc2)): 
                    print(f"{[pares_ColumnaColumna[m][0], pares_ColumnaColumna[m][1]]}  {Restriccion_C2C1_hs[m]:>27} ")   
                    
                print('\n')
                print('Restrictions for Column-Column connections (Flange)')  
                for m in range(len(pcc2)): 
                    print(f"{[pares_ColumnaColumna[m][0], pares_ColumnaColumna[m][1]]}  {Restriccion_C2C1_bs[m]:>27} ")  
                    

                ucc_h = pd.DataFrame({'Column - Column Pairs\nDepth':pares_VigaColumna[:len(pcc2)], 'Validation':Restriccion_C2C1_hs})   
                ucc_h.index += 1 
                ucc_h.index.rename('Joint', inplace=True)  
                
                ucc_b = pd.DataFrame({'Column - Column Pairs\nFlange':pares_VigaColumna[:len(pcc2)], 'Validation':Restriccion_C2C1_bs})   
                ucc_b.index += 1 
                ucc_b.index.rename('Joint', inplace=True)  
         
                with pd.ExcelWriter('src_calc/files/A_JointRestrictionResults.xlsx') as writer:
        
                    uvc.to_excel(writer, sheet_name='BeamColJoint')
                    ucc_h.to_excel(writer, sheet_name='ColColJoint_Depth')
                    ucc_b.to_excel(writer, sheet_name='ColColJoint_Flange')       

         
            else:
                Restriccion_C2C1_h = 0
                Restriccion_C2C1_b = 0
                m = 0
                pcc2 = 0
                ucc_h = [0,0]
                ucc_b = [0,0]
                print('Restrictions for Column-Column connections - Does not apply')
                print(f"None {Restriccion_C2C1_h:>27} ")   
                print(f"None {Restriccion_C2C1_b:>27} ")   
                
                ucc_b = pd.DataFrame({'Column - Column Pairs\nFlange':[0], 'Validation':[0]})   
                ucc_h = pd.DataFrame({'Column - Column Pairs\nFlange':[0], 'Validation':[0]})   
        
                with pd.ExcelWriter('src_calc/files/A_JointRestrictionResults.xlsx') as writer:
        
                    uvc.to_excel(writer, sheet_name='BeamColJoint')
                    ucc_h.to_excel(writer, sheet_name='ColColJoint_Depth')
                    ucc_b.to_excel(writer, sheet_name='ColColJoint_Flange')  

        #        print(f"{pares_ColumnaColumna, pares_ColumnaColumna}  {Restriccion_C2C1_h:>24} {Restriccion_C2C1_b:>63}")  
        
            print('')    
            print(188*'=')
            print('\n','Criterion of members to efficient compression in both axes')   
            print(' ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')  
            print('\n',' Instructions:','\n',' * Values greater than or equal to 0.35 indicate a behavior in both axes due to their geometric relationship')  
            Restriccion_MiembroCompresion, Restriccion_MiembroCompresiones = Comp_Eficc(ExcelPrincipal, ingreso_datos_a, perfiles_aprobados, D_optimizator)      
        
            print('')
            print('Element a',5*' ','Ratio Ry/Rx') 
            print('Compression') 
        
            
            for i in range(len(ingreso_datos_a)): 
                if ingreso_datos_a[i][1] == 'Column':
                    print(f"{i+1:02} {Restriccion_MiembroCompresiones[i]:>31}")            
        
            
            rmc = pd.DataFrame({'Ratio Ry/Rx':Restriccion_MiembroCompresiones[:len(Restriccion_MiembroCompresiones)]})   
            rmc.index += 1 
            rmc.index.rename('Compression\nMembers', inplace=True)  
        
            with pd.ExcelWriter('src_calc/files/A_CompEficRestrictionResults.xlsx') as writer:
        
                rmc.to_excel(writer, sheet_name='CEE.BothAxes')          
            

    my_console.close()
            






























































def detallado_b(lista_los_mejores, ExcelPrincipal, lista_final_p_bajo, ingreso_datos_b, D_optimizator, perfiles_aprobados,  D_nodos_totales, D_nodos_restringidos, D_criterio, Opcion_pesominimo):

    my_console = Logger('src_calc/files/detailed_b.txt') 
    
    if (len(lista_los_mejores)) != 0:    
        print('GENERAL DETAIL OF RESULTS','\n')

        print('Note: It is possible that there is only one option, in any case it seeks to minimize the structural weight.','\n')

        print("Opción con el peso estructural más bajo de todas las opciones más óptimas:")
        print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯','\n')    
        
        lista_detalle = lista_final_p_bajo
        
        for lista_final_p_bajo in Opcion_pesominimo: # ================================================ 3.

            if len(lista_detalle) != 0:
                for i in range(0,len(ingreso_datos_b)):
                    if ingreso_datos_b[i][1] == 'Beam':
                        ingreso_datos_b[i][14]= lista_detalle[0][(len(lista_detalle[0])//2)+ingreso_datos_b[i][2]-1]
                    else:
                        ingreso_datos_b[i][14]=lista_detalle[0][ingreso_datos_b[i][2]-1]

            ingreso_datos_b, DatosPrincipales_actualizados = DatosPrograma(D_criterio, ingreso_datos_b, ExcelPrincipal)  
            
            print(188*'=')
            print('\n','Structural Analysis')  
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
            desp.index.rename('nGDLT_Free', inplace=True)
        
                
            rb = pd.DataFrame(Qnc_estructura)
            rb.columns = ['Qnc\n[kgf]']
            rb.index += nGDL_libres
            rb.index.rename('nGDLT_Restrained', inplace=True)
        
            print('Forces at the elements are: ','\n') 
            print('Element',7*' ','Type Element',10*' ','Pu_i',16*' ','Vu_i',18*' ','Mu_i',18*' ','Pu_j',18*' ','Vu_j',18*' ','Mu_j')             
            print('                ',1*' ','    ',27*' ','[kgf]',16*' ','[kgf]',15*' ','[kgf.m]',16*' ','[kgf]',18*' ','[kgf]',16*' ','[kgf.m]')             
        
            for i in range(len(ingreso_datos_b)): #--> Para cada fila en el rango de 'ingreso de DatosPrincipales'[i]...
                
                print(f"{i+1:>2} {ingreso_datos_b[i][1]:>26} {F_elementos[i][0]:>25} {F_elementos[i][1]:>20}" 
                        f"{F_elementos[i][2]:>22} {F_elementos[i][3]:>23} {F_elementos[i][4]:>23}" 
                        f"{F_elementos[i][5]:>24}")          
        
            forc = pd.DataFrame(F_elementos)
            forc.columns = ['Pu_i\n[kgf]','Vui\n[kgf]','Mu_i\n[kgf*m]','Pu_j\n[kgf]','Vuj\n[kgf]','Muj\n[kgf*m]']
            forc.index += 1 
            forc.index.rename('Element', inplace=True)
            
            with pd.ExcelWriter('src_calc/files/B_AnalysisResults.xlsx') as writer:
        
                vcg.to_excel(writer, sheet_name='GeneralizedLoads')
                matr.to_excel(writer, sheet_name='RigidMatrixGlobal')
                desp.to_excel(writer, sheet_name='Displacements')
                rb.to_excel(writer, sheet_name='Reactions')
                forc.to_excel(writer, sheet_name='Forces')
        
            print('')    
            print(188*'=')
            print('\n','Structural Design [LRFD]')   
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
        
        
        
            compresion = pd.DataFrame({'kl/r_Design':KLR_diseno_listas[:len(ingreso_datos_b)],'λf':lamb_f_lista[:len(ingreso_datos_b)],
                                       'λrf':lamb_rf_lista[:len(ingreso_datos_b)], 'Slenderness Flange':Ala_C_lista[:len(ingreso_datos_b)], 
                                       'λw':lamb_w_lista[:len(ingreso_datos_b)],'λrw':lamb_rw_lista[:len(ingreso_datos_b)], 'Slenderness Web':Alma_C_lista[:len(ingreso_datos_b)],
                                       'Type Section':TipoSeccion_Compresion_lista[:len(ingreso_datos_b)], 'Fe\n[kgf/m2]':Fe_lista[:len(ingreso_datos_b)], 'Bourder Le':O1_lista[:len(ingreso_datos_b)],
                                       'Qs\nSlender Unstiffened Elements':Qs_lista[:len(ingreso_datos_b)],'f\nFcr_Y - Nonslender\n[kgf/m2]':f_lista[:len(ingreso_datos_b)],'be\nSlender Unstiffened Elements\n[m]':be_lista[:len(ingreso_datos_b)],
                                       'Ae\nSlender Unstiffened Elements\n[m2]':Ae_lista[:len(ingreso_datos_b)],'Q\nSlender Sections':Q_lista[:len(ingreso_datos_b)], 'Buckling Type':FormaPandeo_Compresion_lista[:len(ingreso_datos_b)],
                                       'Fcr - FB\nFlexural Buckling\n[kgf/m2]':Fcr_FB_lista[:len(ingreso_datos_b)], 'Pn - FB\nFlexural Buckling\n[kgf]':Pn_FB_lista[:len(ingreso_datos_b)], 'Fez\n[kgf/m2]':Fez_lista[:len(ingreso_datos_b)],
                                       'FCR - FTB\nFlexural - Torsional Buckling\n[kgf/m2]':Fcr_FTB_lista[:len(ingreso_datos_b)], 'Pn - FTB\nFlexural - Torsional Buckling\n[kgf]':Pn_FTB_lista[:len(ingreso_datos_b)], 
                                       'Pn\n[kgf]':Pn_lista[:len(ingreso_datos_b)], 'ΦPn [LRFD]\n[kgf]':Fhi_Pn_demo[:len(ingreso_datos_b)]})
            compresion.index += 1 
            compresion.index.rename('Element', inplace=True)
        
        
                
        
            flexionx = pd.DataFrame({'λf':lamb_f_lista[:len(ingreso_datos_b)], 'λpf':lamb_pf_lista[:len(ingreso_datos_b)],'λprf':lamb_prf_lista[:len(ingreso_datos_b)], 
                                       'Slenderness Flange':Ala_F_lista[:len(ingreso_datos_b)], 'λw':lamb_w_lista[:len(ingreso_datos_b)],'λpw':lamb_pw_lista[:len(ingreso_datos_b)],
                                       'λprw':lamb_prw_lista[:len(ingreso_datos_b)], 'Slenderness Web':Alma_F_lista[:len(ingreso_datos_b)], 'Type Section':TipoSeccion_Flexion_lista[:len(ingreso_datos_b)], 
                                       'Lp\n[m]':Lp_lista[:len(ingreso_datos_b)], 'Lr':Lr_lista[:len(ingreso_datos_b)], 'Flexural buckling zone':ZonaPandeo_Flexion_lista[:len(ingreso_datos_b)],
                                       'Mpx\n[kgf*m]':Mpx_lista[:len(ingreso_datos_b)],'Mnx - Y\nYielding\n[kgf*m]':Mnx_Y_lista[:len(ingreso_datos_b)], 'Cb':Cb_lista[:len(ingreso_datos_b)],
                                       'Fcrx - LTB\nLateral - Torsional Buckling\n[kgf/m2]':Fcrx_LTB_lista[:len(ingreso_datos_b)], 'Mnx - LTB\nLateral - Torsional Buckling\n[kgf*m]':Mnx_LTB_lista[:len(ingreso_datos_b)],
                                       'kc - FLB\nFlange Local Buckling':kc_lista[:len(ingreso_datos_b)], 'Mnx\nFlange Local Buckling\n[kgf*m]':Mnx_FLB_lista[:len(ingreso_datos_b)], 
                                       'Mnx\n[kgf*m]':Mnx_lista[:len(ingreso_datos_b)],'ΦMn [LRFD]\n[kgf*m]':Fhi_Mnx_demo[:len(ingreso_datos_b)]})   
        
            flexionx.index += 1 
            flexionx.index.rename('Element', inplace=True)   
        
        
        
            flexiony = pd.DataFrame({'Type Section':TipoSeccion_Flexion_Y_lista[:len(ingreso_datos_b)],'Mpy\n[kgf*m]':Mpy_lista[:len(ingreso_datos_b)],'Mny - Y\nYielding\n[kgf*m]':Mny_Y_lista[:len(ingreso_datos_b)], 
                                     'Fcry - FLB\nFlange Local Buckling\n[kgf/m2]':Fcr_FLB_lista[:len(ingreso_datos_b)], 'Mny\nFlange Local Buckling\n[kgf*m]':Mny_FLB_lista[:len(ingreso_datos_b)], 
                                       'Mny\n[kgf*m]':Mny_lista[:len(ingreso_datos_b)],'ΦMn [LRFD]\n[kgf*m]':Fhi_Mny_demo[:len(ingreso_datos_b)]})   
        
            flexiony.index += 1 
            flexiony.index.rename('Element', inplace=True)  
        
            
        #    print('\n','Sumario de diseño LRFD: ','\n')
            print('Instructions:','\n',' * While D/C is closer to 1 by the left, more optimal is the design..','\n')
            print('Element',7*' ','Type Element',3*' ','Cross Section Specific',6*' ','Weight',5*' ','Length',4*' ',
                  'Element weight',1*' ','Verification Type',40*' ','Pu',25*' ','Mux',20*' ','Muy',15*' ','Fhi_Pn',20*' ','Fhi_Mnx',16*' ',
                  'Fhi_Mny',10*' ','Ratio D/C')
        
            print('        ',1*' ','    ',14*' ','       ',48*' ','[kgf/m]',6*' ','[m]',13*' ',
                  '[kgf]',72*' ',' ',1*'','[kgf]',20*' ','[kgf.m]',16*' ','[kgf.m]',13*' ','[kgf]',22*' ','[kgf.m]',18*' ',
                  '[kgf.m]',1*' ','            ')
        
        
            for i in range(len(ingreso_datos_b)): 
        
                print(f"{i+1:>2} {ingreso_datos_b[i][1]:>26} {ingreso_datos_b[i][13]:>24} {ingreso_datos_b[i][14]:>8}" 
                        f"{'%.3f'%Decimal(peso_elemento_lista[i]):>22} {Longitudes[i]:>13} {'%.3f'%Decimal(PesoTotalElemento_lista[i]):>20} {Verificacion_lista[i]:>45}" 
                        f"{max(abs(F_elementos[i][0]), abs(F_elementos[i][3])):>18}" 
                        f"{max(abs(F_elementos[i][2]), abs(F_elementos[i][5])):>28}" 
                        f"{Muy_lista[i]:>21} {Fhi_Pn_demo[i]:>26} {Fhi_Mnx_demo[i]:>26} {Fhi_Mny_demo[i]:>26} {Restriccion_Demanda_Capacidades[i]:>20}")  
        
        
            diseo = pd.DataFrame({'Type Element':tipoelementos[:len(ingreso_datos_b)],'Cross Section Specific':seccions[:len(ingreso_datos_b)],'Weight per unit\n[kgf/m]':peso_elemento_lista[:len(ingreso_datos_b)], 
                                  'Length\n[m]':Longitudes[:len(ingreso_datos_b)], 'Weight\n[kgf]':PesoTotalElemento_lista[:len(ingreso_datos_b)], 
                                  'Verification Type\nDesign':Verificacion_lista[:len(ingreso_datos_b)],'ΦPn [LRFD]\n[kgf]':Fhi_Pn_demo[:len(ingreso_datos_b)],
                                  'ΦMnx [LRFD]\n[kgf*m]':Fhi_Mnx_demo[:len(ingreso_datos_b)], 'ΦMny [LRFD]\n[kgf*m]':Fhi_Mny_demo[:len(ingreso_datos_b)], 'Ratio Demand/Capacity':Restriccion_Demanda_Capacidades[:len(ingreso_datos_b)]})   
        
            diseo.index += 1 
            diseo.index.rename('Element', inplace=True)  
        
            with pd.ExcelWriter('src_calc/files/B_DesignRestrictionResult.xlsx') as writer:
        
                compresion.to_excel(writer, sheet_name='CompressionDesign')
                flexionx.to_excel(writer, sheet_name='FlexuralDesign_X')
                flexiony.to_excel(writer, sheet_name='FlexuralDesign_Y')
                diseo.to_excel(writer, sheet_name='Ratio_DC')
        
        
            print('\n','Total structure weight is: ',round(PesoEstructural,3),' kgf')
            
            print('Average demand/capacity: ', promedio_DC)
        
            print('')    
            print(188*'=')
            print('\n','Correct criterion of assembly in the joints') 
            print(' ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
            print('\n',' Instructions:','\n',' * Values less than or equal to 0 indicate a correct assembly')
        
            (validate, Restriccion_VigaColumna, Restriccion_C2C1_h, Restriccion_C2C1_b, 
             pares_VigaColumna, pares_ColumnaColumna, l, pcv2, m, pcc2,
             Restriccion_VigaColumnas, Restriccion_C2C1_hs, Restriccion_C2C1_bs) = unionesVC(ingreso_datos_b, D_optimizator, perfiles_aprobados, ExcelPrincipal)
            
            print('')
            print('Restrictions for column-beam connections (Flange)', '\n')   
        
            for l in range(len(pcv2)): 
        
                print(f"{[pares_VigaColumna[l][0], pares_VigaColumna[l][1]]} {Restriccion_VigaColumnas[l]:>27}")  
        
            uvc = pd.DataFrame({'Beam - Column Pairs\nFlange':pares_VigaColumna[:len(pcv2)], 'Validation':Restriccion_VigaColumnas})   
        
            uvc.index += 1 
            uvc.index.rename('Joint', inplace=True)  
        
            if len(pcc2) > 0:
                print('\n')
                print('Restrictions for Column-Column connections (Depth)')
                for m in range(len(pcc2)): 
                    print(f"{[pares_ColumnaColumna[m][0], pares_ColumnaColumna[m][1]]}  {Restriccion_C2C1_hs[m]:>27} ")   
                    
                print('\n')
                print('Restrictions for Column-Column connections (Flange)')  
                for m in range(len(pcc2)): 
                    print(f"{[pares_ColumnaColumna[m][0], pares_ColumnaColumna[m][1]]}  {Restriccion_C2C1_bs[m]:>27} ")  

                ucc_h = pd.DataFrame({'Column - Column Pairs\nDepth':pares_VigaColumna[:len(pcc2)], 'Validation':Restriccion_C2C1_hs})   
                ucc_h.index += 1 
                ucc_h.index.rename('Joint', inplace=True)  
                
                ucc_b = pd.DataFrame({'Column - Column Pairs\nFlange':pares_VigaColumna[:len(pcc2)], 'Validation':Restriccion_C2C1_bs})   
                ucc_b.index += 1 
                ucc_b.index.rename('Joint', inplace=True)  
         
                with pd.ExcelWriter('src_calc/files/B_JointRestrictionResults.xlsx') as writer:
        
                    uvc.to_excel(writer, sheet_name='BeamColJoint')
                    ucc_h.to_excel(writer, sheet_name='ColColJoint_Depth')
                    ucc_b.to_excel(writer, sheet_name='ColColJoint_Flange')     
                    
        
            else:
                Restriccion_C2C1_h = 0
                Restriccion_C2C1_b = 0
                m = 0
                pcc2 = 0
                ucc_h = [0,0]
                ucc_b = [0,0]
                print('Restrictions for Column-Column connections - Does not apply')
                print(f"None {Restriccion_C2C1_h:>27} ")   
                print(f"None {Restriccion_C2C1_b:>27} ")   
                

                ucc_b = pd.DataFrame({'Column - Column Pairs\nFlange':[0], 'Validation':[0]})   
                ucc_h = pd.DataFrame({'Column - Column Pairs\nFlange':[0], 'Validation':[0]})   
        
                with pd.ExcelWriter('src_calc/files/B_JointRestrictionResults.xlsx') as writer:
        
                    uvc.to_excel(writer, sheet_name='BeamColJoint')
                    ucc_h.to_excel(writer, sheet_name='ColColJoint_Depth')
                    ucc_b.to_excel(writer, sheet_name='ColColJoint_Flange')  

        #        print(f"{pares_ColumnaColumna, pares_ColumnaColumna}  {Restriccion_C2C1_h:>24} {Restriccion_C2C1_b:>63}")  
        
            print('')    
            print(188*'=')
            print('\n','Criterion of members to efficient compression in both axes')   
            print(' ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')  
            print('\n',' Instructions:','\n',' * Values greater than or equal to 0.35 indicate a behavior in both axes due to their geometric relationship')  
            Restriccion_MiembroCompresion, Restriccion_MiembroCompresiones = Comp_Eficc(ExcelPrincipal, ingreso_datos_b, perfiles_aprobados, D_optimizator)      
        
            print('')
            print('Element a',5*' ','Ratio Ry/Rx') 
            print('Compression') 
        
            
            for i in range(len(ingreso_datos_b)): 
                if ingreso_datos_b[i][1] == 'Column':
                    print(f"{i+1:02} {Restriccion_MiembroCompresiones[i]:>31}")            
        
            
            rmc = pd.DataFrame({'Ratio Ry/Rx':Restriccion_MiembroCompresiones[:len(Restriccion_MiembroCompresiones)]})   
            rmc.index += 1 
            rmc.index.rename('Compression\nMembers', inplace=True)  
        
            with pd.ExcelWriter('src_calc/files/B_CompEficRestrictionResults.xlsx') as writer:
        
                rmc.to_excel(writer, sheet_name='CEE.BothAxes')         
            

    my_console.close()
            


















     