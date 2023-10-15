import pandas as pd
import networkx as nx
import numpy as np
import CliquesKgrafo as CKG 

def KCliqueCover(graph, k):
    """
    Devuelve una cubierta del k-clique ingresado.
    
    Parámetros
    ----------
    graph : debe ser la ruta de donde proviene el archivo CSV. El archivo CSV debe 
    contener una columna de salidas y otra de entradas.
    
    k : distancia máxima entre cada par de vértices. 
    ----------   
    """    
############# Definición del k-grafo y su matriz de adyacencia ##################
    GrafoImportado = pd.read_csv(graph) 
    G = nx.from_pandas_edgelist(GrafoImportado, source="salidas", target="entradas")
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos)
    V = list(G.nodes())
    vertices = len(V)
    cliques = CKG.CliquesKGrafo(graph,k)
    columnas = len(cliques)
    
    Matrix_cover = np.zeros((len(V),len(cliques)))
 
    for i in range(vertices):
       for j in range(columnas):
           if (V[i] in cliques[j]):
               Matrix_cover[i][j] = 1
    R = Matrix_cover.copy()
             
############## Vector de costos #################################         
    SV = []
    filas_visitadas = []
    columnas_visitadas = []
    
############# Elección de la fila ###########################
    for k in range(vertices):
        sum_rowNV = list(np.zeros(vertices))          
        for i in range(vertices):
            if i in filas_visitadas:
                sum_rowNV[i] = 1e100000
            else:
                sum_rowNV[i] = R[i][:].sum()

        posicion_fila_min = sum_rowNV.index(min(sum_rowNV))    
        filas_visitadas.append(posicion_fila_min)
        
############# Elección de la columna que cubre mejor la fila ##############    
        clique_Vmax = list(np.zeros(columnas))
        for j in range(columnas):
            if j in columnas_visitadas:
                clique_Vmax[j] = -1
            else:
                if R[posicion_fila_min][j] == 1:
                    clique_Vmax[j] = R[:,j].sum()
       
        posicion_col_max = clique_Vmax.index(max(clique_Vmax))
        columnas_visitadas.append(posicion_col_max)
        SV.append(cliques[posicion_col_max])
        
        if len(filas_visitadas) == vertices or len(columnas_visitadas)==columnas:
            break

############## Cubiertas suficientes para cubrir el grafo
    S = SV.copy()
    for x in SV:
        subconjunto = set()
        cliquesminusX = S.copy()
        cliquesminusX.remove(x)
     
        for y in cliquesminusX:
            subconjunto.update(y)
        if set(x).issubset(subconjunto):
            S.remove(x)
    print(S)
            
         
KCliqueCover("graph.csv", 2) 
