import networkx as nx
import matplotlib as matp
import matplotlib.pyplot as plt

A = {1,2,3,4,5,6,7}

R2 = {(1, 2), (1, 6), (2, 3), (3, 3), (3, 4), (4, 3), (4, 1),
(4, 5), (6, 4), (1, 7), (7, 2)}

GD = nx.DiGraph() # Creacion del digrafo
GD.add_nodes_from(A) # Agregado de los nodos al digrafo 
GD.add_edges_from(R2) # Agregado de los arcos representados en R2

pos = {}       # Posicionamiento de los nodos
pos[1] = (0,7) 
pos[2] = (0,9)
pos[3] = (9,7)
pos[4] = (5,7)
pos[5] = (3,8)
pos[6] = (3,6)
pos[7] = (2,5)


nx.draw_networkx_nodes(GD, pos, nodelist = [1,2,3,4], node_color="purple")    # Dibujo de los nodos
nx.draw_networkx_nodes(GD, pos, nodelist = [5,6,7], node_color="yellow")
nx.draw_networkx_edges(GD, pos, edgelist = [(1,2), (3,4)], edge_color="blue", # Dibujo de los arcos
                       width=3.0, connectionstyle = 'arc3, rad = 0.3')
nx.draw_networkx_edges(GD, pos, edgelist = [(4,1), (2,3)], edge_color="blue", 
                       width=3.0, connectionstyle = 'arc3, rad = 0.3')

nx.draw_networkx_edges(GD, pos, edgelist = [(1,6)], edge_color="orange", 
                       width=1.5, connectionstyle = 'arc3, rad = 0.3')
nx.draw_networkx_edges(GD, pos, edgelist = [(3,3), (4,3)], edge_color="orange", 
                       width=1.5, connectionstyle = 'arc3, rad = 0.3')
nx.draw_networkx_edges(GD, pos, edgelist = [(4,5)], edge_color="orange", 
                       width=1.5, connectionstyle = 'arc3, rad = 0.3')
nx.draw_networkx_edges(GD, pos, edgelist = [(6,4), (1,7)], edge_color="orange", 
                       width=1.5, connectionstyle = 'arc3, rad = 0.3')
nx.draw_networkx_edges(GD, pos, edgelist = [(7,2)], edge_color="orange", 
                       width=1.5, connectionstyle = 'arc3, rad = 0.3')


nx.draw_networkx_labels(GD, pos, font_size=14, font_color="white") # Dibujo de los labels

plt.show() # Muestra del dibujo final