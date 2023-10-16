import networkx as nx
import pandas as pd

def BronKerboschPivote(graph):
    
    """
    Devuelve una lista con todos los cliques maximales del grafo ingresado.
    
    Parámetro
    ----------
    graph : debe ser la ruta de donde proviene el archivo CSV. El archivo CSV debe 
    contener una columna de salidas y otra de entradas.
    
    """
    GrafoImportado = pd.read_csv(graph) 
    G= nx.from_pandas_edgelist(GrafoImportado, source="salidas", target="entradas")
    clanes=[]
    
    def BK(R,P,X):
        if P==X and P==set():
            clanes.append(R)
        else:
            for u in P.union(X):
                for v in (P.difference(set(G.neighbors(u)))):
                     BK(R.union({v}), P.intersection(set(G.neighbors(v))), X.intersection(set(G.neighbors(v))))
                     P=P.difference({v})
                     X=X.union({v})

    R=set([])
    X=set([])
    P=set(G.nodes())
    
    BK(R,P,X)
    return clanes

BronKerboschPivote("graph.csv")
