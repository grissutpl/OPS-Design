# -*- coding: utf-8 -*-
"""
Created on Wed Jan 01 20:00:29 2020 

@author: Ing. Daniel Villarreal
"""

import matplotlib.pyplot as plt # Ploteo de gráficas

def graph_objetive(lista_Peso_estructural):

    x = []
    y = []
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(1, 1, 1)

    ax.grid(which='both')
    
    x = range(1,len(lista_Peso_estructural)+1)
    y = lista_Peso_estructural

#    plt.title('Optimización Objetivo\n',fontsize=14, fontweight='bold')

#    plt.xlabel(r"$\bf{" + 'Número\,\,de\,\,iteraciones\,\,validadas\,\,(unit)' + "}$\n\n${Elaborado\,\,por:\,Daniel\,\,Villarreal\,\,Leiva}$")


    plt.xlabel('Number of validated iterations (unit)', fontweight='bold')
    plt.ylabel('Total Structure Weight (kgf)', fontweight='bold')
    plt.plot(x, y, color = '#EAAB00') 

    plt.show() # -------------------------------------------------------------@   