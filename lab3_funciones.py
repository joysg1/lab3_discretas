import networkx as nx
import matplotlib.pyplot as plt
import matplotlib as matp
from itertools import product

tup1 = (1,2)   #Asignacion de valores a las tuplas
tup2 = (1,2)
tup3 = ("a","b")


def verf_tup(t1,t2):

 #Funcion con las condiciones de evaluacion
    
    if t1 == t2:   # Retorno de true si ambas tuplas son iguales
       return True
    else:
        return False # Retorno de false si las tuplas son diferentes
   
    
    
    
# print(verf_tup(tup1,tup2))  # Impresiones del llamado de la funcion

# print(verf_tup(tup3, tup1)) 


def prod_cart(S1, S2):
    result = list(product(S1,S2)) # se declara result que recibe como lista 
                                  # el resultado de la funcion product
    
    return result   # se retorna result

# print(prod_cart(A,B)) # se imprime el llamado de la funcion prod_cart


def verf_rel(X, Y, W):
    for el1 in X:         # Ciclos repetitivos para recorrer los elementos de X y Y
        for el2 in Y:
            if (el1, el2) in W: # Validar si los elementos de X y Y estan en W
                return True     # Retorno de true de encontrar coincidencia
    return False # Retorno de false al salir de los ciclos de repeticion

A = {1, 2, 3}                           # Asignacion de valores a los conjuntos
B = {'a', 'b'}
C = {(1, 'a'), (2, 'b'), (3, 'a')}
D = {(1,'h'), (2,'s')}


resultado = verf_rel(A, B, C)  # Guardado de la ejecucion de la funcion en variables

resultado2 = verf_rel(A, B, D)

# print(resultado) # Impresion de los resultados
# print(resultado2)



A = {1,2,3,4,5,6,7}

R = [(1, 1), (1, 2), (2, 2), (1, 3), (3, 3), (1, 4), 
 (2, 4), (4, 4), (1, 5), (5, 5), 
 (1, 6), (2, 6), (3, 6), (6, 6), (1, 7), (7, 7)]    #Resultados de la relacion (P.6d)

GD = nx.DiGraph()
GD.add_nodes_from(A)
GD.add_edges_from(R)

nx.draw(GD, arrows=True, arrowstyle = "->", 
        connectionstyle = 'arc3, rad = 0.3', with_labels = True)


ruta="C:/test/figura.pdf"


def guardar_digrafo(r):
    
    plt.savefig(r)
    

guardar_digrafo(ruta)


def obtener_trayectorias(graf):
    trayec = [] # Lista vacia para almacenar las trayectorias
    nodos = list(graf.nodes) # Obtencion de los nodos del grafo
    for i in nodos: # Ciclos anidados para recorrer los pares del grafo
        for j in nodos:
            if i!=j:# Se agregan los pares a la lista trayec si i != j 
                trayec.extend(list(nx.all_simple_paths(graf,i,j)))

    return trayec # Se retorna trayec

res = obtener_trayectorias(GD)  # Guardado de las trayectorias

# print("Trayectorias simples de GD: ")
# for ta in res: # Uso de ciclo for para impresion de las trayectorias
   # print(ta)


def tray_long_n(lista_tray, n):
    n_trayec = []   #Lista vacia para guardar las trayectorias
    for i in lista_tray: # Ciclo para recorrer las posiciones
        if len(i) - 1 == n: # Determinar si la longitud es igual a n
            n_trayec.append(i) # Se agrega la trayectoria a la lista
    return n_trayec # Se retorna la lista


t = [['A', 'B'], ['A', 'D'], ['A', 'C', 'D'], ['B', 'C', 'D']]

# Lista de trayectorias


rest = tray_long_n(t,1) # Guardado de las trayectorias de longitud 1
rest2 = tray_long_n(t,2) # Guardado de las trayectorias de longitud 2

# for i in rest: # Impresion de las trayectorias de longitud 1
   # print("Trayectoria de longitud 1 (2 vertices 1 arco): ", i)

# for i in rest2: # Impresion de las trayectorias de logitud 2
  #  print("Trayectoria de longitud 2 (3 vertices 2 arcos): ", i)



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


# print("Ciclos simples encontrados: ") 
# for i in cic_s: # Impresion del contenido de la variable mediante un for
   # print(i)

# plt.show() # Se muestra el dibujo del digrafo para corroborar las respuestas  



A = {1,2,3,4,5} # Conjunto de nodos
R = [(1,1), (2,2), (3,3), (3,1), (5,4)] # Conjunto de relaciones

GDa = nx.DiGraph()  # Creacion del digrafo
GDa.add_nodes_from(A) # Agregado de los nodos al digrafo
GDa.add_edges_from(R) # Agregado de los arcos al digrafo

def ciclos_long_1(dif):
 result = list(nx.selfloop_edges(dif)) # Variable guarda en lista los ciclos de longitud 1
  

 return result # Se retorna la variable
   
ciclos = ciclos_long_1(GDa) # guardado en variable el resultado del llamado de la funcion

# print("Relaciones en el digrafo: ") # Impresion de los resultados
# print(R)

# print("Ciclos de longitud 1 encontrados: ")
# for i in ciclos:
  # print(i)