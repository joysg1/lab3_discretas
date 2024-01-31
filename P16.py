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

pos = {}       # Posicionamiento de los nodos
pos[1] = (0,7) 
pos[2] = (0,9)
pos[3] = (9,7)
pos[4] = (5,7)
pos[5] = (3,8)
pos[6] = (3,6)
pos[7] = (2,5)



nx.draw_networkx_nodes(GD, pos, nodelist = [1,2,3,4], node_color="red")    # Dibujo de los nodos
nx.draw_networkx_nodes(GD, pos, nodelist = [5,6,7], node_color="blue")
nx.draw_networkx_edges(GD, pos, edgelist = [(1,4), (1,6)],  # Dibujo de los arcos
                       width = 3.0, edge_color = "yellow", 
                       connectionstyle = 'arc3, rad = 0.3')
nx.draw_networkx_edges(GD, pos, edgelist = [(1,1), (1,2)], 
                        edge_color = "black", connectionstyle = 'arc3, rad = 0.3')
nx.draw_networkx_edges(GD, pos, edgelist = [(2,2), (1,3)], 
                        edge_color = "black", connectionstyle = 'arc3, rad = 0.3')
nx.draw_networkx_edges(GD, pos, edgelist = [(3,3), (2,4)], 
                        edge_color = "black", connectionstyle = 'arc3, rad = 0.3')
nx.draw_networkx_edges(GD, pos, edgelist = [(4,4), (1,5)], 
                        edge_color = "black", connectionstyle = 'arc3, rad = 0.3')
nx.draw_networkx_edges(GD, pos, edgelist = [(5,5), (2,6)], 
                        edge_color = "black", connectionstyle = 'arc3, rad = 0.3')
nx.draw_networkx_edges(GD, pos, edgelist = [(3,6), (6,6)], 
                        edge_color = "black", connectionstyle = 'arc3, rad = 0.3')
nx.draw_networkx_edges(GD, pos, edgelist = [(1,7), (7,7)], 
                        edge_color = "black", connectionstyle = 'arc3, rad = 0.3')

nx.draw_networkx_labels(GD, pos, font_size=14, font_color="white") # Dibujo de los labels

plt.show()