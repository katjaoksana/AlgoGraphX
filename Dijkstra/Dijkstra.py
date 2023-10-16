import networkx as nx
import pandas as pd

def Dijkstra(graph,s):
    """
    Devuelve la lista de la ruta más corta desde un vértice inicial a 
    todos los demás en el grafo.
    
    Parámetro
    ----------
    graph : debe ser la ruta de donde proviene el archivo CSV. El archivo CSV debe 
    contener una columna de salidas, una de entradas y una columna "A" que corresponda
    a los pesos asignados a las aristas.
    
    s : nodo inicial.
    """  
    #Creación del grafo.
    GrafoImportado = pd.read_csv(graph) 
    G = nx.from_pandas_edgelist(GrafoImportado, source="salidas", target="entradas", edge_attr="A")
    p = nx.get_edge_attributes(G,  "A")
    pesos = p.copy()
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos)
    nx.draw_networkx_edge_labels(G,pos, edge_labels=p)
    
    S = {s:0}
    P_tentativos = {s:0}

    for u in set(G.nodes).difference({s}):
        if u in G.neighbors(s):
            if (u,s) in pesos:
                P_tentativos[u] = pesos[(u,s)]
            else:
                P_tentativos[u] = pesos[(s,u)]
        else:
            P_tentativos[u] = 1e1000
            
    P_no_visitados = P_tentativos.copy()
    P_no_visitados.pop(s)

    while True:
        for v in P_no_visitados:         
            if P_no_visitados[v] == min(P_no_visitados.values()):
                v_min = v
        for v in set(G.neighbors(v_min)).difference(S):
            if (v_min,v) in pesos:
                if P_tentativos[v] > pesos[(v_min , v)] + P_no_visitados[v_min]:
                    P_tentativos[v] = pesos[(v_min ,v)] + P_no_visitados[v_min]          
            else:
                if P_tentativos[v] > pesos[(v,v_min)] + P_no_visitados[v_min]:
                    P_tentativos[v] = pesos[(v,v_min)] + P_no_visitados[v_min]

            if v in P_no_visitados:
                P_no_visitados[v] = P_tentativos[v]
                
        S[v_min] = min(P_no_visitados.values())
        P_no_visitados.pop(v_min)
              
        if P_no_visitados == {}:
            
            print(S)
            break
        
Dijkstra("Graph.csv",5) #Es necesario ingresar el archivo csv y el vértice inicial

