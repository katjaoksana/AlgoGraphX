import pandas as pd
import networkx as nx


def BronKerbosch(graph):
    """
    Devuelve una lista con todos los cliques maximales del grafo ingresado.
    
    Parámetro
    ----------
    graph : debe ser la ruta de donde proviene el archivo CSV. El archivo CSV debe 
    contener una columna de salidas y otra de entradas.
    
    """
    
    #Creación del grafo
    GrafoImportado = pd.read_csv(graph) 
    G= nx.from_pandas_edgelist(GrafoImportado, source="salidas", target="entradas")
    
    def bk(R,P,X):
        if P == set() and X == set():
            print (R, "es un clique")
        else:
            for v in P:
                bk(R.union({v}),P.intersection(set(G.neighbors(v))),X.intersection(set(G.neighbors(v))))
                P = P.difference({v})
                X = X.union({v})
                 
    
    R = set([])
    X = set([])
    P = set(G.nodes()) 
    
    bk(R,P,X) 

BronKerbosch("graph.csv")
