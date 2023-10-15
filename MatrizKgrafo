import FloydWarshall as FL

def Matrizkclique(graph,k=2):
    """
    Devuelve la matriz de adyacencia del k-distancia grafo.
    
    Parámetros
    ----------
    graph : debe ser la ruta de donde proviene el archivo CSV. El archivo CSV debe 
    contener una columna de entradas y otra de salidas.
    
    k : distancia máxima entre cada par de vértices. 
    ----------
    Nota : en caso de no ingresar el parámetro "k" se tomará k = 2.
    
    """

    MatKDist = FL.FloydWarshall(graph)
    n = len(MatKDist[1][:])
    for i in range(n):
        for j in range(n):
            if (0 < MatKDist[i][j] <= k):
                MatKDist[i][j] = MatKDist[j][i] = 1
            else:
                MatKDist[i][j] = MatKDist[j][i] = 0
                
    return MatKDist

Matrizkclique("graph.csv",2)
