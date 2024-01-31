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

plt.show()

