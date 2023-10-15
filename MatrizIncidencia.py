import pandas as pd
import numpy as np


def MatrizIncidencia(matriz_csv):
    """
    Devuelve un archivo CSV con las incidencias del grafo ingresado
    
    Parámetro
    ----------
    matriz_csv : debe ser un archivo csv que contenga la matriz 
    de adyacencia de un grafo.   
    """
    matriz_adyacencia = np.genfromtxt(matriz_csv,delimiter=',')
    n = len(matriz_adyacencia[1][:])
    salidas = []
    entradas = []
    
    for i in range(n):
        for j in range(n):
            if (matriz_adyacencia[i][j] == 1):
                salidas.append(i+1)
                entradas.append(j+1)
                
    DF = pd.DataFrame(list(zip(salidas, entradas)), columns=["salidas", "entradas"])
    DF.to_csv("MatIncidencia.csv", index=False)

MatrizIncidencia("graph.csv")
