# -*- coding: utf-8 -*-
"""
Created on Wed Jan 01 20:00:29 2020 

@author: Ing. Daniel Villarreal
"""

import numpy as np # Creación de matrices
import numbers # Esta la uso para evitar el problema de coger el mínimo de valores e ignorar textos.

def disenioLRFD(ExcelPrincipal, ingreso_datos, F_elementos, D_optimizator, perfiles_aprobados):

        
    Fhi_b = 0.9
    Fhi_c = 0.9
    
    
    kx = 1
    ky = 1
    kz = 1
    
    Cbc = 2.17
    Cbb = 1.32
    
    c = 1

    caracteristicas = []
    peso_elemento_lista = []
    
    tipoelementos = []
    seccions = []
    for i in range(len(ingreso_datos)): #--> Para cada fila en el rango de 'ingreso de DatosPrincipales'[i]...
        
        if D_optimizator == 1:
            Perfil_Data = perfiles_aprobados
            
        elif D_optimizator == 0:
            Perfil_Data = ExcelPrincipal.parse('W')   
            
        tipoelementos.append(ingreso_datos[i][1])
        seccions.append(['W '+str(ingreso_datos[i][14])])
            
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

        peso_elemento = caracteristicas[i][7]
        peso_elemento_lista.append(peso_elemento)
    
    G = caracteristicas [i][29]/(2*(1+caracteristicas [i][30]))                   # Módulo de Corte 

    
    KLR_diseno_listas = []
    lamb_f_lista = []
    lamb_rf_lista = []
    Ala_C_lista = []
    lamb_w_lista = []
    lamb_rw_lista = []
    Alma_C_lista = []
    TipoSeccion_Compresion_lista = []
    Fe_lista = []
    O1_lista = []
    Qs_lista = []
    f_lista = []
    be_lista = []
    Ae_lista = []
    Q_lista = []
    O2_lista = []
    FormaPandeo_Compresion_lista = []
    Fcr_FB_lista = []
    Pn_FB_lista = []
    Fez_lista = []
    Fcr_FTB_lista = []
    Pn_FTB_lista = []
    Pn_lista = []
    

    Fhi_Pn_demo = []
    Longitudes = []
    
    for i in range(len(ingreso_datos)):

        xi = ingreso_datos[i][9]
        yi = ingreso_datos[i][10]
        xf = ingreso_datos[i][11]
        yf = ingreso_datos[i][12]    
        
        L = round(np.sqrt((xf-xi)**2+(yf-yi)**2),3)
        Longitudes.append(L)        
        
    
        KLR_x = round(kx*Longitudes[i]/caracteristicas [i][9],2)     
        KLR_y = round(ky*Longitudes[i]/caracteristicas [i][15],2)  
        KLR_diseno = max(KLR_x, KLR_y)
        KLR_diseno_listas.append(KLR_diseno)
        
        
        Fe = round((np.pi**2)*caracteristicas [i][29]/(KLR_diseno**2),2)
        Fe_lista.append(Fe)
        
        O1 = round(4.71*np.sqrt(caracteristicas [i][29]/caracteristicas [i][28]),2)
        O1_lista.append(O1)
        
        Fez = round(((((np.pi**2)*caracteristicas [i][29]*caracteristicas [i][26])/(kz*Longitudes[i])**2)+G*caracteristicas [i][24])
                    *(1/(caracteristicas [i][6]*(caracteristicas [i][22]**2))),2)
        Fez_lista.append(Fez)
        
    
        lamb_f = round(caracteristicas [i][1]/(2*caracteristicas [i][2]),2)
        lamb_f_lista.append(lamb_f)
        
        lamb_rf = round(0.56*np.sqrt(caracteristicas [i][29]/caracteristicas [i][28]),2)
        lamb_rf_lista.append(lamb_rf)
    
        if lamb_f < lamb_rf:
            Ala_C = 'Non Slender Flange'
        
        else:
            Ala_C = 'Slender     Flange'
        Ala_C_lista.append(Ala_C)
        
    
        lamb_w = round(caracteristicas [i][4]/caracteristicas [i][3],2)
        lamb_w_lista.append(lamb_w)
        
        lamb_rw = round(1.49*np.sqrt(caracteristicas [i][29]/caracteristicas [i][28]),2)
        lamb_rw_lista.append(lamb_rw)
        
        if lamb_w < lamb_rw:
            Alma_C = 'Non Slender    Web'
        
        else:
            Alma_C = 'Slender        Web'
        Alma_C_lista.append(Alma_C)
            
        
        f1 = 0.56*np.sqrt(caracteristicas [i][29]/caracteristicas [i][28])
        f2 = 1.03*np.sqrt(caracteristicas [i][29]/caracteristicas [i][28]) 
        
        Qs = 0
        if lamb_f <= f1:
            Qs = 1
        elif f1 < lamb_f < f2:
            Qs = 1.415-0.74*lamb_f*np.sqrt(caracteristicas [i][28]/caracteristicas [i][29])
        else:
            Qs = (0.69/lamb_f**2)*(caracteristicas [i][29]/caracteristicas [i][28])
        Qs_lista.append(Qs)
            
            
        f = 0
        if KLR_diseno <= 4.71*np.sqrt(caracteristicas [i][29]/caracteristicas [i][28]):
            f = round((0.658**(caracteristicas [i][28]/Fe))*caracteristicas [i][28],2)
        else:
            f = round(0.877*Fe,2)
        f_lista.append(f)
            
            
        be = round(1.92*caracteristicas [i][3]*np.sqrt(caracteristicas [i][29]/f)*(1-(0.34/(caracteristicas [i][4]/caracteristicas [i][3])) 
        *np.sqrt(caracteristicas [i][29]/f)),2)
        be_lista.append(be)
        
        
        Ae = round(caracteristicas [i][6] - (caracteristicas [i][4]-be)*caracteristicas [i][3],2)
        Ae_lista.append(Ae)
        
        Qa = round(Ae/caracteristicas [i][6],2)
    
        
        if Ala_C == 'Slender     Flange' and Alma_C == 'Non Slender    Web':
            Q = 1
        elif Ala_C == 'Non Slender Flange' and Alma_C == 'Slender        Web':
            Q = 1
        elif Ala_C == 'Non Slender Flange' and Alma_C == 'Non Slender    Web':
            Q = 1
        else:
            Q = round(Qs*Qa,2)
        Q_lista.append(Q)
        
        
        # -------------------------------------------------------------------------@
        
        O2 = round(4.71*np.sqrt(caracteristicas [i][29]/(Q*caracteristicas [i][28])),2)
        O2_lista.append(O2)
    
        Fcr_FB = 0  
        Fcr_FTB = 0
        Pn_FB = 0
        Pn_FTB = 0
    
            
        if Ala_C == 'Non Slender Flange' and Alma_C == 'Non Slender    Web':
            
            TipoSeccion_Compresion = 'Non slender-element section'
            
            if KLR_diseno <= 4.71*np.sqrt(caracteristicas [i][29]/(caracteristicas [i][28])):
                
                FormaPandeo_Compresion = 'Inelastic Buckling Non-Slender Sections'
                
                
                Fcr_FB = round(0.658**(caracteristicas [i][28]/Fe)*caracteristicas [i][28],2) #--> Esfuerzo crítico de pandeo flexional
                Pn_FB = round(Fcr_FB*caracteristicas [i][6],2)
                
                
                Fcr_FTB = round(0.658**(caracteristicas [i][28]/Fez)*caracteristicas [i][28],2) #--> Esfuerzo crítico de pandeo flexotorsional
                Pn_FTB = round(Fcr_FTB*caracteristicas [i][6],2) 
                
            else:            
                FormaPandeo_Compresion = 'Elastic Buckling Non-Slender   Sections'
                
                
                Fcr_FB = round(0.877*Fe,2) #--> Esfuerzo crítico de pandeo flexional
                Pn_FB = round(Fcr_FB*caracteristicas [i][6],2)
                
                
                Fcr_FTB = round(0.877*Fez,2) #--> Esfuerzo crítico de pandeo flexional
                Pn_FTB = round(Fcr_FTB*caracteristicas [i][6],2) 
                           
        else:
            TipoSeccion_Compresion = 'Slender-element     section'
            
            if KLR_diseno <= 4.71*np.sqrt(caracteristicas [i][29]/(Q*caracteristicas [i][28])):
                
                FormaPandeo_Compresion = 'Inelastic Buckling Slender     Sections'
                
        
                Fcr_FB = round((Q*0.658**((Q*caracteristicas [i][28])/Fe))*caracteristicas [i][28],2) #--> Esfuerzo crítico de pandeo flexional
                Pn_FB = round(Fcr_FB*caracteristicas [i][6],2)
                
                
                Fcr_FTB = round((Q*0.658**((Q*caracteristicas [i][28])/Fez))*caracteristicas [i][28],2) #--> Esfuerzo crítico de pandeo flexotorsional
                Pn_FTB = round(Fcr_FTB*caracteristicas [i][6],2) 
                
                
            else:
                FormaPandeo_Compresion = 'Elastic Buckling Slender       Sections'
                
                
                Fcr_FB = round(0.877*Fe,2) #--> Esfuerzo crítico de pandeo flexional
                Pn_FB = round(Fcr_FB*caracteristicas [i][6],2)
                
                
                Fcr_FTB = round(0.877*Fez,2) #--> Esfuerzo crítico de pandeo flexotorsional
                Pn_FTB = round(Fcr_FTB*caracteristicas [i][6],2)        
        
        Fcr_FB_lista.append(Fcr_FB)
        Fcr_FTB_lista.append(Fcr_FTB)
        
        Pn_FB_lista.append(Pn_FB)
        Pn_FTB_lista.append(Pn_FTB)

                
        FormaPandeo_Compresion_lista.append(FormaPandeo_Compresion)
        TipoSeccion_Compresion_lista.append(TipoSeccion_Compresion)
        
        Pn = round(min(Pn_FB, Pn_FTB),2) 
        Pn_lista.append(Pn)
        
        Fhi_Pn = round(Fhi_c*Pn,2)        
        Fhi_Pn_demo.append(Fhi_Pn)

    
    lamb_pf_lista = []
    lamb_prf_lista = []
    Ala_F_lista = []
    lamb_pw_lista = []
    lamb_prw_lista = []
    Alma_F_lista = []
    TipoSeccion_Flexion_lista = []
    Lp_lista = []
    Lr_lista = []
    ZonaPandeo_Flexion_lista = []
    Mpx_lista = []
    Mnx_Y_lista = []
    Cb_lista = []
    Fcrx_LTB_lista = []
    Mnx_LTB_lista = []
    ff1_lista = []
    
    kc_lista = []
    Mnx_FLB_lista = []
    Mnx_lista = []
    
    
    Fhi_Mnx_demo = []
    
    for i in range(len(ingreso_datos)):
        
        
        Mpx = round(caracteristicas [i][28]*caracteristicas [i][12],2)
        Mpx_lista.append(Mpx)
    
        
        Lp = round(1.76*caracteristicas [i][15]*np.sqrt(caracteristicas [i][29]/caracteristicas [i][28]),2)
        Lp_lista.append(Lp)
        
        Lr = round((1.95*caracteristicas [i][27]*(caracteristicas [i][29]/(0.7*caracteristicas [i][28])))
        *np.sqrt(((caracteristicas [i][24]*c)/(caracteristicas [i][10]*caracteristicas [i][25])) 
        + np.sqrt((((caracteristicas [i][24]*c)/(caracteristicas [i][10]*caracteristicas [i][25]))**2) 
        + (6.76*(((0.7*caracteristicas [i][28])/caracteristicas [i][29])**2)))),2)
        Lr_lista.append(Lr)
    
    
        Cb = 0
        
        if ingreso_datos[i][1] == 'Column':
            Cb = Cbc
            
        else:
            Cb = Cbb
        Cb_lista.append(Cb)
            
        Fcrx_LTB = round(((Cb*(np.pi**2)*caracteristicas [i][29])/((Longitudes[i]/caracteristicas [i][27])**2))
        *(np.sqrt(1+0.078*((caracteristicas [i][24]*c)/(caracteristicas [i][10]*caracteristicas [i][25]))*((Longitudes[i]/caracteristicas [i][27])**2))),2)
        Fcrx_LTB_lista.append(Fcrx_LTB)
        
        ff1 = round(4/np.sqrt(caracteristicas [i][4]/caracteristicas [i][3]),2)
        ff1_lista.append(ff1)
        
        kc = 0
        
        if ff1 < 0.35:
            kc = 0.35
        
        elif 0.35 < ff1 < 0.76:
            kc = round(ff1,2)
        
        else:
            kc = 0.76
        kc_lista.append(kc)
    
        
        lamb_f = round(caracteristicas [i][1]/(2*caracteristicas [i][2]),2)
        
        lamb_pf = round(0.38*np.sqrt(caracteristicas [i][29]/caracteristicas [i][28]),2)
        lamb_pf_lista.append(lamb_pf)
        
        lamb_prf = round(1*np.sqrt(caracteristicas [i][29]/caracteristicas [i][28]),2)
        lamb_prf_lista.append(lamb_prf)
        
        if lamb_f < lamb_pf:
            Ala_F = 'Compact     Flange'
            
        elif lamb_f < lamb_prf and lamb_f > lamb_pf:
            Ala_F = 'Non Compact Flange'
            
        elif lamb_f > lamb_prf:
            Ala_F = 'Slender     Flange'  
        Ala_F_lista.append(Ala_F)    
        
        
        lamb_w = round(caracteristicas [i][4]/caracteristicas [i][3],2)
        
        lamb_pw = round(3.76*np.sqrt(caracteristicas [i][29]/caracteristicas [i][28]),2)
        lamb_pw_lista.append(lamb_pw)
        
        lamb_prw = round(5.70*np.sqrt(caracteristicas [i][29]/caracteristicas [i][28]),2)   
        lamb_prw_lista.append(lamb_prw)
        
        if lamb_w < lamb_pw:
            Alma_F = 'Compact       Web'
            
        elif lamb_w < lamb_prw and lamb_w > lamb_pw:
            Alma_F = 'Non Compact   Web'
            
        elif lamb_w > lamb_prw:
            Alma_F = 'Slender       Web'
        
        else:
            Alma_F = 0
        Alma_F_lista.append(Alma_F)
            
        TipoSeccion_Flexion = 0
        ZonaPandeo_Flexion = 0
        Mnx_Y = 0
        Mnx_LTB = 0
        Mnx_FLB = 0
            
        
        if Ala_F == 'Compact     Flange' and Alma_F == 'Compact       Web':
            
            TipoSeccion_Flexion = 'Compact    section    in    flange    and    web'
            
            
            Mnx_Y = round(Mpx,2) 
            
            
            if Longitudes[i] <= Lp:
                ZonaPandeo_Flexion = 'Buckling By Total Plastic Moment     (Zone 1)'
                
                Mnx_LTB = 'No Aplica'
                
            elif Lp < Longitudes[i] < Lr:
                ZonaPandeo_Flexion = 'Lateral Torsional Inelastic Buckling (Zone 2)'
                
                Mnx_LTB = round(Cb*(Mpx-(Mpx-0.7*caracteristicas [i][28]*caracteristicas [i][10])*((Longitudes[i]-Lp)/(Lr-Lp))),2)
                    
            elif Longitudes[i] >= Lr:
                ZonaPandeo_Flexion = 'Lateral Torsional elastic Buckling   (Zone 3)'
                
                Mnx_LTB = round(Fcrx_LTB*caracteristicas [i][10],2)
                
            else:
                Mnx_LTB = 0
                
            
            Mnx_FLB = 'No Aplica'
            
        elif Ala_F == 'Non Compact Flange' and Alma_F == 'Compact       Web':
            
            TipoSeccion_Flexion = 'Non compact section in flange and compact in web' 
            
            
            Mnx_Y = 'No Aplica'
        
        
            if Longitudes[i] <= Lp:
                ZonaPandeo_Flexion = 'Buckling By Total Plastic Moment     (Zone 1)'
                
                Mnx_LTB = 'No Aplica'            
                
            elif Lp < Longitudes[i] < Lr:
                ZonaPandeo_Flexion = 'Lateral Torsional Inelastic Buckling (Zone 2)'
                
                Mnx_LTB = round(Cb*(Mpx-(Mpx-0.7*caracteristicas [i][28]*caracteristicas [i][10])*((Longitudes[i]-Lp)/(Lr-Lp))),2)
                    
            elif Longitudes[i] >= Lr:
                ZonaPandeo_Flexion = 'Lateral Torsional elastic Buckling   (Zone 3)'
                
                Mnx_LTB = round(Fcrx_LTB*caracteristicas [i][10],2)
                
            else:
                Mnx_LTB = 0
                
        
            Mnx_FLB = round(Mpx-(Mpx - 0.7*caracteristicas [i][28]*caracteristicas [i][10])*((lamb_f-lamb_pf)/(lamb_prf-lamb_pf)),2)   
            
        elif Ala_F == 'Slender     Flange' and Alma_F == 'Compact       Web':
            
            TipoSeccion_Flexion = 'Slender section  in  flange  and  compact in web'
            
            Mnx_Y = 'No Aplica'
                    
            
            if Longitudes[i] <= Lp:
                ZonaPandeo_Flexion = 'Buckling By Total Plastic Moment     (Zone 1)'
                
                Mnx_LTB = 'No Aplica'  
                
            elif Lp < Longitudes[i] < Lr:
                ZonaPandeo_Flexion = 'Lateral Torsional Inelastic Buckling (Zone 2)'
                
                Mnx_LTB = round(Cb*(Mpx-(Mpx-0.7*caracteristicas [i][28]*caracteristicas [i][10])*((Longitudes[i]-Lp)/(Lr-Lp))),2)
                    
            elif Longitudes[i] >= Lr:
                ZonaPandeo_Flexion = 'Lateral Torsional elastic Buckling   (Zone 3)'
                
                Mnx_LTB = round(Fcrx_LTB*caracteristicas [i][10],2)
                
            else:
                Mnx_LTB = 0
                
            
            Mnx_FLB = round((0.9*caracteristicas [i][29]*kc*caracteristicas [i][10])/(lamb_f**2),2)    
            
        TipoSeccion_Flexion_lista.append(TipoSeccion_Flexion)
        ZonaPandeo_Flexion_lista.append(ZonaPandeo_Flexion)
        Mnx_Y_lista.append(Mnx_Y)
        Mnx_LTB_lista.append(Mnx_LTB)
        Mnx_FLB_lista.append(Mnx_FLB)
        
        Mnx = 0
        
        if TipoSeccion_Flexion == 'Compact    section    in    flange    and    web':
            Mnx = [Mnx_Y, Mnx_LTB]
            Mnx = min(item for item in Mnx if isinstance(item, numbers.Number))
            
        elif TipoSeccion_Flexion == 'Non compact section in flange and compact in web':
            Mnx = [Mnx_LTB, Mnx_FLB]       
            Mnx = min(item for item in Mnx if isinstance(item, numbers.Number))
            
        elif TipoSeccion_Flexion == 'Slender section  in  flange  and  compact in web':
            Mnx = [Mnx_LTB, Mnx_FLB]    
            Mnx = min(item for item in Mnx if isinstance(item, numbers.Number))
                
        
        Mnx_lista.append(Mnx)
        
        Fhi_Mnx = round(Fhi_b*Mnx,2)
        Fhi_Mnx_demo.append(Fhi_Mnx)

        
    TipoSeccion_Flexion_Y_lista = []
    Mpy_lista = []
    Mny_Y_lista = []
    Fcr_FLB_lista = []
    Mny_FLB_lista = []
    Mny_lista = []
    
    Fhi_Mny_demo = [] 
    
    for i in range(len(ingreso_datos)):
    
        Mpy = round(caracteristicas [i][28]*caracteristicas [i][18],2)
        Mpy_lista.append(Mpy)
               
        
        lamb_f = caracteristicas [i][1]/(2*caracteristicas [i][2])
        lamb_pf = round(0.38*np.sqrt(caracteristicas [i][29]/caracteristicas [i][28]),2)
        lamb_prf = round(1*np.sqrt(caracteristicas [i][29]/caracteristicas [i][28]),2)
        
        Fcr_FLB = round((0.69*caracteristicas [i][29])/(lamb_f**2),2) 
        Fcr_FLB_lista.append(Fcr_FLB)
        
        Mny_Y = 0
        Mny_FLB = 0
        if lamb_f < lamb_pf:
            Ala_F = 'Compact     Flange'
            
        elif lamb_f < lamb_prf and lamb_f > lamb_pf:
            Ala_F = 'Non Compact Flange'
            
        elif lamb_f > lamb_prf:
            Ala_F = 'Slender     Flange'   
                    
        
        if Ala_F == 'Compact     Flange':
            
            TipoSeccion_Flexion_Y = 'Compact section in flange     (Web is not considered)'
            
            Mny_Y = round(Mpy,2)
            Mny_FLB = 'No Aplica'
            
        elif Ala_F =='Non Compact Flange':
            
            TipoSeccion_Flexion_Y = 'Non compact section in flange (Web is not considered)'    
            Mny_Y = round(Mpy,2)
            Mny_FLB = round(Mpy-(Mpy-(0.7*caracteristicas [i][29]*caracteristicas [i][16]))*((lamb_f-lamb_pf)/(lamb_rf-lamb_pf)),2)
            
        elif Ala_F =='Slender     Flange':
            
            TipoSeccion_Flexion_Y = 'Slender section in flange     (Web is not considered)'
            Mny_Y = round(Mpy,2)
            Mny_FLB = round(Fcr_FLB*caracteristicas [i][16],2)
    
        else:
            TipoSeccion_Flexion_Y = 0
            
        Mny_Y_lista.append(Mny_Y)
        Mny_FLB_lista.append(Mny_FLB)
        TipoSeccion_Flexion_Y_lista.append(TipoSeccion_Flexion_Y)
        
        
        Mny = 0
        
        if (TipoSeccion_Flexion_Y == 'Compact section in flange     (Web is not considered)' or 
            TipoSeccion_Flexion_Y == 'Non compact section in flange (Web is not considered)' or 
            TipoSeccion_Flexion_Y == 'Slender section in flange     (Web is not considered)'):
            
            Mny = round(Mny_Y,2)
        else:
            Mny = round(Mny_FLB,2)
            
        Mny_lista.append(Mny)
        
        Fhi_Mny = round(Fhi_b*Mny,2)
        Fhi_Mny_demo.append(Fhi_Mny)

    
    PesoTotalElemento_lista = []
    Verificacion_lista = []
    Muy_lista = []
    
    
    PesoEstructural = 0
    Restriccion_Demanda_Capacidades = []
    for i in range(len(ingreso_datos)):
    
        Muy = 0
        
        if ingreso_datos[i][1] == 'Column':
            
            Verificacion = 'Combined forces, (flexure and axial)'
            Demanda_Capacidad = 0
            
            if (F_elementos[i][0]/Fhi_Pn_demo[i]) >= 0.2:
                
                Demanda_Capacidad = round(((max(abs(F_elementos[i][0]), abs(F_elementos[i][3])))/Fhi_Pn_demo[i])+(8/9)*
                                          (((max(abs(F_elementos[i][2]), abs(F_elementos[i][5])))/Fhi_Mnx_demo[i])+(Muy/Fhi_Mny_demo[i])),3)
            else:           
                Demanda_Capacidad = round(((max(abs(F_elementos[i][0]), abs(F_elementos[i][3])))/(2*Fhi_Pn_demo[i]))+
                                          (((max(abs(F_elementos[i][2]), abs(F_elementos[i][5])))/Fhi_Mnx_demo[i])+(Muy/Fhi_Mny_demo[i])),3)
            
        elif ingreso_datos[i][1] == 'Beam':
            
            Verificacion = 'Members  subject  to  flexure forces'
            Demanda_Capacidad = round((max(abs(F_elementos[i][2]), abs(F_elementos[i][5])))/Fhi_Mnx_demo[i],3)
            
        else:        
            Verificacion = 0
            Demanda_Capacidad = 0
            
        Verificacion_lista.append(Verificacion)
        
        Muy_lista.append(Muy)
        
        Restriccion_Demanda_Capacidades.append(Demanda_Capacidad)
        promedio_DC = round(np.mean(Restriccion_Demanda_Capacidades),3)
        
        PesoTotalElemento = Longitudes[i]*peso_elemento_lista[i]
        PesoTotalElemento_lista.append(PesoTotalElemento)
        
        PesoEstructural += round(PesoTotalElemento,3) 
        

    return (Restriccion_Demanda_Capacidades, promedio_DC, PesoEstructural, 
             
             KLR_diseno_listas, lamb_f_lista, lamb_rf_lista, Ala_C_lista,lamb_w_lista, lamb_rw_lista, Alma_C_lista, 
             TipoSeccion_Compresion_lista, Fe_lista, O1_lista, Qs_lista, f_lista, be_lista, Ae_lista, Q_lista, O2_lista, 
             FormaPandeo_Compresion_lista, Fcr_FB_lista, Pn_FB_lista, Fez_lista, Fcr_FTB_lista, Pn_FTB_lista, Pn_lista, Fhi_Pn_demo,
             
             lamb_pf_lista, lamb_prf_lista, Ala_F_lista, lamb_pw_lista, lamb_prw_lista, Alma_F_lista, TipoSeccion_Flexion_lista,
             Lp_lista, Lr_lista, ZonaPandeo_Flexion_lista, Mpx_lista, Mnx_Y_lista, Cb_lista, Fcrx_LTB_lista, Mnx_LTB_lista, ff1_lista,
             kc_lista, Mnx_FLB_lista, Mnx_lista, Fhi_Mnx_demo,
             
             TipoSeccion_Flexion_Y_lista, Mpy_lista, Mny_Y_lista, Fcr_FLB_lista, Mny_FLB_lista, Mny_lista, Fhi_Mny_demo,
             
             peso_elemento_lista, Longitudes, PesoTotalElemento_lista, Verificacion_lista, Muy_lista,
             
             tipoelementos, seccions)