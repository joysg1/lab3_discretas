import networkx as nx
import matplotlib as matp
import matplotlib.pyplot as plt

A = {1,2,3,4,5,6,7}

R = [(1, 1), (1, 2), (2, 2), (1, 3), (3, 3), (1, 4), 
 (2, 4), (4, 4), (1, 5), (5, 5), 
 (1, 6), (2, 6), (3, 6), (6, 6), (1, 7), (7, 7)]    #Resultados de la relacion (P.6d)

GD = nx.DiGraph() # Creacion del digrafo
GD.add_nodes_from(A) # Agregado de los nodos al digrafo 
GD.add_edges_from(R) # Agregado de los arcos al digrafo

GD.clear_edges() # Eliminacion de los arcos del digrafo

R2 = {(1, 2), (1, 6), (2, 3), (3, 3), (3, 4), (4, 3), (4, 1),
(4, 5), (6, 4), (1, 7), (7, 2)}

GD.add_edges_from(R2) # Agregado de los arcos representados en R2

nx.draw(GD, arrows=True, arrowstyle = "->", 
        connectionstyle = 'arc3, rad = 0.3', with_labels = True)

plt.show()