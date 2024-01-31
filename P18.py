import networkx as nx
import matplotlib as matp
import matplotlib.pyplot as plt

A2 = {0,1,2} # Conjunto con los nodos 
R2 = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 0), (2, 1), (2, 2)] # Conjunto con las relaciones

GDb = nx.DiGraph() # Creacion del digrafo

GDb.add_nodes_from(A2) # Agregado de los nodos al digrafo
GDb.add_edges_from(R2) # Agregado de los arcos al digrafo

pos = {}        # lista para asignar posiciones a los nodos
pos[0] = (0,0)
pos[1] = (3,5)
pos[2] = (2,3)

nx.draw(GDb, pos, arrows=True, arrowstyle = "->",  # Dibujo del digrafo
        connectionstyle = 'arc3, rad = 0.3', with_labels = True)

def ciclos_simples(dif):  
    result = list(nx.simple_cycles(dif)) # Variable guarda en lista los ciclos simples
    return result # Retorno de la variable


cic_s = ciclos_simples(GDb) # Variable guarda el resultado de llamar a la funcion


print("Ciclos simples encontrados: ") 
for i in cic_s: # Impresion del contenido de la variable mediante un for
    print(i)

plt.show() # Se muestra el dibujo del digrafo para corroborar las respuestas