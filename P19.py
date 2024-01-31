import networkx as nx
import matplotlib as matp
import matplotlib.pyplot as plt


A = {1,2,3,4,5} # Conjunto de nodos
R = [(1,1), (2,2), (3,3), (3,1), (5,4)] # Conjunto de relaciones

GDa = nx.DiGraph()  # Creacion del digrafo
GDa.add_nodes_from(A) # Agregado de los nodos al digrafo
GDa.add_edges_from(R) # Agregado de los arcos al digrafo

def ciclos_long_1(dif):
  result = list(nx.selfloop_edges(dif)) # Variable guarda en lista los ciclos de longitud 1
  

  return result # Se retorna la variable
   
ciclos = ciclos_long_1(GDa) # guardado en variable el resultado del llamado de la funcion

print("Relaciones en el digrafo: ") # Impresion de los resultados
print(R)

print("Ciclos de longitud 1 encontrados: ")
for i in ciclos:
  print(i)






