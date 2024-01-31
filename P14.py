import networkx as nx
import matplotlib as matp
import matplotlib.pyplot as plt

A = {1,2,3,4,5,6,7}

R = [(1, 1), (1, 2), (2, 2), (1, 3), (3, 3), (1, 4), 
 (2, 4), (4, 4), (1, 5), (5, 5), 
 (1, 6), (2, 6), (3, 6), (6, 6), (1, 7), (7, 7)]    #Resultados de la relacion (P.6d)

GD = nx.DiGraph()
GD.add_nodes_from(A)
GD.add_edges_from(R)

nx.draw(GD, arrows=True, arrowstyle = "->", 
        connectionstyle = 'arc3, rad = 0.3', with_labels = True)



def obtener_trayectorias(graf):

    trayec = [] # Lista vacia para almacenar las trayectorias
    nodos = list(graf.nodes) # Obtencion de los nodos del grafo
    for i in nodos: # Ciclos anidados para recorrer los pares del grafo
        for j in nodos:
            if i!=j:# Se agregan los pares a la lista trayec si i != j 
                trayec.extend(list(nx.all_simple_paths(graf,i,j)))

    return trayec # Se retorna trayec


res = obtener_trayectorias(GD) # Guardado de las trayectorias

print("Trayectorias simples de GD: ")
for ta in res: # Uso de ciclo for para impresion de las trayectorias
    print(ta)

