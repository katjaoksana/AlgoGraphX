import pandas as pd
import numpy as np
import MatrizKgrafo as MKG
import MatrizIncidencia as MI
import BronKerboschPivote as BK


def CliquesKGrafo(graph,k):
    """
    Devuelve los k-cliques del grafo ingresado.
    
    Parámetros
    ----------
    graph : debe ser la ruta de donde proviene el archivo CSV. El archivo CSV debe 
    contener una columna de salidas y otra de entradas.
    
    k : distancia máxima entre cada par de vértices. 
    ----------   
    """
    
    MatKgraph = MKG.Matrizkclique(graph,k)

    DF = pd.DataFrame(np.array(MatKgraph))
    DF.to_csv("matrizkgraph.csv", index = False, header=False)
    MatInKgraph = MI.MatrizIncidencia("matrizkgraph.csv")

    DF1 = pd.DataFrame(np.array(MatInKgraph)).T
    DF1.columns = ["salidas","entradas"]
    DF1.to_csv("incidenciaskgraph.csv", index = False)
    
    return BK.BronKerboschPivote("incidenciaskgraph.csv")

CliquesKGrafo("graph.csv", 2)
