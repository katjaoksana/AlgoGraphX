import networkx as nx
import pandas as pd
import numpy as np


def MatrizAdyacencia(graph):
    
    """
    Devuelve la matriz de adyacencia del grafo ingresado.
    En caso de que no exista un arista entre un par de vértices la entrada será "inf".
    
    Parámetro
    ----------
    graph : debe ser la ruta de donde proviene el archivo CSV. El archivo CSV debe 
    contener una columna de salidas y otra de entradas.
    """
    
    GrafoImportado = pd.read_csv(graph)
    G = nx.from_pandas_edgelist(GrafoImportado, source="salidas", target="entradas")
    
    salidas = GrafoImportado["salidas"]
    entradas = GrafoImportado["entradas"]
    n = len(nx.nodes(G))
    m = len(salidas)
     
    MatAdy = np.ones((n,n))*1e1000
    
    for i in range(m):
    
        x = int(salidas[i])-1
        y = int(entradas[i])-1
        
        MatAdy[x][y] = MatAdy[y][x] = 1 
        MatAdy[x][x] = MatAdy[y][y] = 0
    
    return MatAdy


MatrizAdyacencia("graph.csv")
