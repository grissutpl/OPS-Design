# -*- coding: utf-8 -*-
"""
Created on Wed Jan 01 20:00:29 2020 

@author: Ing. Daniel Villarreal
"""

import numpy as np # Creación de matrices
import matplotlib.pyplot as plt # Ploteo de gráficas


def frame(ingreso_datos):
    
    x = []
    y = []
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(1, 1, 1)

    for i in range(len(ingreso_datos)): 

        xi = ingreso_datos[i][9]
        yi = ingreso_datos[i][10]
        xf = ingreso_datos[i][11]
        yf = ingreso_datos[i][12]
        
        wd_height = 0
        if abs(ingreso_datos[i][15])/10000 > 1:
            wd_height = abs(ingreso_datos[i][15])/100000
     
        elif abs(ingreso_datos[i][15])/10000 > 10:
            wd_height = abs(ingreso_datos[i][15])/1000000
    
        elif abs(ingreso_datos[i][15])/10000 < 0.1:
            wd_height = abs(ingreso_datos[i][15])/1000
        else:
            wd_height = abs(ingreso_datos[i][15])/10000         
            
        p_height = abs(ingreso_datos[i][16])/10000
        
        lateral_height = abs(ingreso_datos[i][21])/1000
        
        space = 1
    
        slope = 0
        if ingreso_datos[i][1] == 'Vig':
            slope = (yf-yi)/(xf-xi)


        x.append(ingreso_datos[i][11])
        y.append(ingreso_datos[i][12])
        AreaRejilla = max(max(x), max(y))
    
        major_ticks = np.arange(-30, AreaRejilla+20, 1)
        minor_ticks = np.arange(-30, AreaRejilla+20, 0.25)
        
        ax.set_xticks(major_ticks)
        ax.set_xticks(minor_ticks, minor=True)
        ax.set_yticks(major_ticks)
        ax.set_yticks(minor_ticks, minor=True)
        
        ax.grid(which='both')
        
        ax.grid(which='minor', alpha=0.2)
        ax.grid(which='major', alpha=0.5)
        
        plt.title('Gráfica del Pórtico analizado\n',fontsize=14, fontweight='bold')

        plt.xlabel(r"$\bf{" + 'Longitud\,(m)' + "}$\n\n${Elaborado\,\,por:\,Daniel\,\,Villarreal\,\,Leiva}$")

        plt.ylabel('Altura (m)', fontweight='bold')
        plt.axis('equal')
    
        plt.plot((xi, xf), (yi, yf), color='#003F72' if ingreso_datos[i][1] == "Col" else "#A71930", linewidth=4) 
    
        anotations = plt.annotate(f"Elemento: {ingreso_datos[i][1]} {ingreso_datos[i][0]}\nPerfil {ingreso_datos[i][13]} - {ingreso_datos[i][14]}",
                     xy=(xi + (xf - xi) / 2, yi + (yf - yi) / 2), #--> Mis anotaciones estarán en medio de la línea
                     textcoords="offset points", #--> Junto con la línea anterior, me ubica en medio de la línea
                     xytext= (0, -15) if ingreso_datos[i][1] == "Vig" else (5, 0), #--> Ajusta la ubicación del texto
                     ha='center' if ingreso_datos[i][1] == "Vig" else "left", 
                     va="center")
        anotations.set_fontsize(9)
    
        if slope == 0:
    
            if ingreso_datos[i][1] == 'Vig' and abs(ingreso_datos[i][15]) > 0:
                plt.plot((xi, xf), (yi+wd_height, yf+wd_height), color='green', linewidth=1) 
        
                for xj in np.arange(xi, xf + 1e-9, space):
                    plt.arrow(xj, yi + wd_height, 0, -wd_height, color='green', linewidth=1,
                              length_includes_head=True, head_width=0.1, head_length=0.1)
        
                anotations = plt.annotate(f"WD = {ingreso_datos[i][15]} kgf/m", xy=(xi + (xf - xi) / 2, yi + wd_height + (yf + wd_height - yi) / 2), 
                             textcoords="offset points", xytext= (0, 0), ha='center', va="center")

                anotations.set_fontsize(9)
                
            if ingreso_datos[i][1] == 'Vig' and abs(ingreso_datos[i][21]) > 0:
                anotations = plt.annotate(f"SX = {round(ingreso_datos[i][21],3)} kgf", xy=(xi,yi), 
                             textcoords="offset points", xytext= (-60, -10), ha='center', va="center")        
  
                anotations.set_fontsize(9)
              
                plt.arrow(xi-lateral_height, yi, lateral_height, 0,color='red', linewidth=1, 
                          length_includes_head=True, head_width=0.1, head_length=0.1)  
        
            if ingreso_datos[i][1] == 'Vig' and abs(ingreso_datos[i][16]) > 0:
        
                plt.arrow((xj-xi)/2, yi + p_height, 0, -p_height, color='magenta', linewidth=2, length_includes_head=True, head_width=0.1, head_length=0.1)    
        
                anotations = plt.annotate(f"P = {ingreso_datos[i][16]} kgf", xy=(xi + (xf - xi) / 2, yi + wd_height + (yf + wd_height - yi) / 2), 
                             textcoords="offset points", xytext= (0, 10), ha='center', va="center")  

                anotations.set_fontsize(9)                
        else:
            None
    plt.show() # -------------------------------------------------------------@





def frame_a(ingreso_datos_a):
    
    x = []
    y = []
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(1, 1, 1)


    for i in range(len(ingreso_datos_a)): 

        xi = ingreso_datos_a[i][9]
        yi = ingreso_datos_a[i][10]
        xf = ingreso_datos_a[i][11]
        yf = ingreso_datos_a[i][12]
        
        wd_height = 0
        if abs(ingreso_datos_a[i][15])/10000 > 1:
            wd_height = abs(ingreso_datos_a[i][15])/100000
     
        elif abs(ingreso_datos_a[i][15])/10000 > 10:
            wd_height = abs(ingreso_datos_a[i][15])/1000000
    
        elif abs(ingreso_datos_a[i][15])/10000 < 0.1:
            wd_height = abs(ingreso_datos_a[i][15])/1000
        else:
            wd_height = abs(ingreso_datos_a[i][15])/10000         
            
        p_height = abs(ingreso_datos_a[i][16])/10000
        
        lateral_height = abs(ingreso_datos_a[i][21])/1000
        
        space = 1
    
        slope = 0
        if ingreso_datos_a[i][1] == 'Vig':
            slope = (yf-yi)/(xf-xi)


        x.append(ingreso_datos_a[i][11])
        y.append(ingreso_datos_a[i][12])
        AreaRejilla = max(max(x), max(y))
    
        major_ticks = np.arange(-30, AreaRejilla+20, 1)
        minor_ticks = np.arange(-30, AreaRejilla+20, 0.25)
        
        ax.set_xticks(major_ticks)
        ax.set_xticks(minor_ticks, minor=True)
        ax.set_yticks(major_ticks)
        ax.set_yticks(minor_ticks, minor=True)
        
        ax.grid(which='both')
        
        ax.grid(which='minor', alpha=0.2)
        ax.grid(which='major', alpha=0.5)
        
        plt.title('Gráfica del Pórtico\nOpción con el índice de complejidad mas bajo posible\n',fontsize=14, fontweight='bold')
        plt.xlabel(r"$\bf{" + 'Longitud\,(m)' + "}$\n\n${Elaborado\,\,por:\,Daniel\,\,Villarreal\,\,Leiva}$")

        plt.ylabel('Altura (m)', fontweight='bold')
        plt.axis('equal')
    
        plt.plot((xi, xf), (yi, yf), color='#003F72' if ingreso_datos_a[i][1] == "Col" else "#A71930", linewidth=4) 
    
        anotations = plt.annotate(f"Elemento: {ingreso_datos_a[i][1]} {ingreso_datos_a[i][0]}\nPerfil {ingreso_datos_a[i][13]} - {ingreso_datos_a[i][14]}",
                     xy=(xi + (xf - xi) / 2, yi + (yf - yi) / 2), #--> Mis anotaciones estarán en medio de la línea
                     textcoords="offset points", #--> Junto con la línea anterior, me ubica en medio de la línea
                     xytext= (0, -15) if ingreso_datos_a[i][1] == "Vig" else (5, 0), #--> Ajusta la ubicación del texto
                     ha='center' if ingreso_datos_a[i][1] == "Vig" else "left", 
                     va="center")
        anotations.set_fontsize(9)
    
        if slope == 0:
    
            if ingreso_datos_a[i][1] == 'Vig' and abs(ingreso_datos_a[i][15]) > 0:
                plt.plot((xi, xf), (yi+wd_height, yf+wd_height), color='green', linewidth=1) 
        
                for xj in np.arange(xi, xf + 1e-9, space):
                    plt.arrow(xj, yi + wd_height, 0, -wd_height, color='green', linewidth=1,
                              length_includes_head=True, head_width=0.1, head_length=0.1)
        
                anotations = plt.annotate(f"WD = {ingreso_datos_a[i][15]} kgf/m", xy=(xi + (xf - xi) / 2, yi + wd_height + (yf + wd_height - yi) / 2), 
                             textcoords="offset points", xytext= (0, 0), ha='center', va="center")

                anotations.set_fontsize(9)
                
            if ingreso_datos_a[i][1] == 'Vig' and abs(ingreso_datos_a[i][21]) > 0:
                anotations = plt.annotate(f"SX = {round(ingreso_datos_a[i][21],3)} kgf", xy=(xi,yi), 
                             textcoords="offset points", xytext= (-60, -10), ha='center', va="center")        
  
                anotations.set_fontsize(9)
              
                plt.arrow(xi-lateral_height, yi, lateral_height, 0,color='red', linewidth=1, 
                          length_includes_head=True, head_width=0.1, head_length=0.1)  
        
            if ingreso_datos_a[i][1] == 'Vig' and abs(ingreso_datos_a[i][16]) > 0:
        
                plt.arrow((xj-xi)/2, yi + p_height, 0, -p_height, color='magenta', linewidth=2, length_includes_head=True, head_width=0.1, head_length=0.1)    
        
                anotations = plt.annotate(f"P = {ingreso_datos_a[i][16]} kgf", xy=(xi + (xf - xi) / 2, yi + wd_height + (yf + wd_height - yi) / 2), 
                             textcoords="offset points", xytext= (0, 10), ha='center', va="center")  

                anotations.set_fontsize(9)                
        else:
            None
    plt.show() # -------------------------------------------------------------@
        
    
    
    
    
    
def frame_b(ingreso_datos_b):
    
    x = []
    y = []
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(1, 1, 1)

    for i in range(len(ingreso_datos_b)): 

        xi = ingreso_datos_b[i][9]
        yi = ingreso_datos_b[i][10]
        xf = ingreso_datos_b[i][11]
        yf = ingreso_datos_b[i][12]
        
        wd_height = 0
        if abs(ingreso_datos_b[i][15])/10000 > 1:
            wd_height = abs(ingreso_datos_b[i][15])/100000
     
        elif abs(ingreso_datos_b[i][15])/10000 > 10:
            wd_height = abs(ingreso_datos_b[i][15])/1000000
    
        elif abs(ingreso_datos_b[i][15])/10000 < 0.1:
            wd_height = abs(ingreso_datos_b[i][15])/1000
        else:
            wd_height = abs(ingreso_datos_b[i][15])/10000         
            
        p_height = abs(ingreso_datos_b[i][16])/10000
        
        lateral_height = abs(ingreso_datos_b[i][21])/1000
        
        space = 1
    
        slope = 0
        if ingreso_datos_b[i][1] == 'Vig':
            slope = (yf-yi)/(xf-xi)

        x.append(ingreso_datos_b[i][11])
        y.append(ingreso_datos_b[i][12])
        AreaRejilla = max(max(x), max(y))
    
        major_ticks = np.arange(-30, AreaRejilla+20, 1)
        minor_ticks = np.arange(-30, AreaRejilla+20, 0.25)
        
        ax.set_xticks(major_ticks)
        ax.set_xticks(minor_ticks, minor=True)
        ax.set_yticks(major_ticks)
        ax.set_yticks(minor_ticks, minor=True)
        
        ax.grid(which='both')
        
        ax.grid(which='minor', alpha=0.2)
        ax.grid(which='major', alpha=0.5)
        
        plt.title('Gráfica del Pórtico\nOpción con el peso más bajo posible\n',fontsize=14, fontweight='bold')
        plt.xlabel(r"$\bf{" + 'Longitud\,(m)' + "}$\n\n${Elaborado\,\,por:\,Daniel\,\,Villarreal\,\,Leiva}$")

        plt.ylabel('Altura (m)', fontweight='bold')
        plt.axis('equal')
    
        plt.plot((xi, xf), (yi, yf), color='#003F72' if ingreso_datos_b[i][1] == "Col" else "#A71930", linewidth=4) 
    
        anotations = plt.annotate(f"Elemento: {ingreso_datos_b[i][1]} {ingreso_datos_b[i][0]}\nPerfil {ingreso_datos_b[i][13]} - {ingreso_datos_b[i][14]}",
                     xy=(xi + (xf - xi) / 2, yi + (yf - yi) / 2), #--> Mis anotaciones estarán en medio de la línea
                     textcoords="offset points", #--> Junto con la línea anterior, me ubica en medio de la línea
                     xytext= (0, -15) if ingreso_datos_b[i][1] == "Vig" else (5, 0), #--> Ajusta la ubicación del texto
                     ha='center' if ingreso_datos_b[i][1] == "Vig" else "left", 
                     va="center")
        anotations.set_fontsize(9)
    
        if slope == 0:
    
            if ingreso_datos_b[i][1] == 'Vig' and abs(ingreso_datos_b[i][15]) > 0:
                plt.plot((xi, xf), (yi+wd_height, yf+wd_height), color='green', linewidth=1) 
        
                for xj in np.arange(xi, xf + 1e-9, space):
                    plt.arrow(xj, yi + wd_height, 0, -wd_height, color='green', linewidth=1,
                              length_includes_head=True, head_width=0.1, head_length=0.1)
        
                anotations = plt.annotate(f"WD = {ingreso_datos_b[i][15]} kgf/m", xy=(xi + (xf - xi) / 2, yi + wd_height + (yf + wd_height - yi) / 2), 
                             textcoords="offset points", xytext= (0, 0), ha='center', va="center")

                anotations.set_fontsize(9)
                
            if ingreso_datos_b[i][1] == 'Vig' and abs(ingreso_datos_b[i][21]) > 0:
                anotations = plt.annotate(f"SX = {round(ingreso_datos_b[i][21],3)} kgf", xy=(xi,yi), 
                             textcoords="offset points", xytext= (-60, -10), ha='center', va="center")        
  
                anotations.set_fontsize(9)
              
                plt.arrow(xi-lateral_height, yi, lateral_height, 0,color='red', linewidth=1, 
                          length_includes_head=True, head_width=0.1, head_length=0.1)  
        
            if ingreso_datos_b[i][1] == 'Vig' and abs(ingreso_datos_b[i][16]) > 0:
        
                plt.arrow((xj-xi)/2, yi + p_height, 0, -p_height, color='magenta', linewidth=2, length_includes_head=True, head_width=0.1, head_length=0.1)    
        
                anotations = plt.annotate(f"P = {ingreso_datos_b[i][16]} kgf", xy=(xi + (xf - xi) / 2, yi + wd_height + (yf + wd_height - yi) / 2), 
                             textcoords="offset points", xytext= (0, 10), ha='center', va="center")  

                anotations.set_fontsize(9)                
        else:
            None
    plt.show() # -------------------------------------------------------------@