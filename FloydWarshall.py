import MatrizAdy as MA

def FloydWarshall(graph):
    """
    Devuelve una matriz con la distancia entre cada par de vértices.
   
    Parámetro
    ----------
    graph : debe ser la ruta de donde proviene el archivo CSV. El archivo CSV debe 
    contener una columna de entradas y otra de salidas.
    """
    MatDistGraph = MA.MatrizAdyacencia(graph)
    cn = len(MatDistGraph[1][:])
 
    for k in range(cn):
        for i in range(cn):
            for j in range(cn):
                dt = MatDistGraph[i][k] + MatDistGraph[k][j]
                if(MatDistGraph[i][j] > dt):
                    MatDistGraph[i][j] = dt
                    
    return MatDistGraph

FloydWarshall("graph.csv")
