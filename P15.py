def tray_long_n (lista_tray, n):
    n_trayec = []   #Lista vacia para guardar las trayectorias
    for i in lista_tray: # Ciclo para recorrer las posiciones
        if len(i) - 1 == n: # Determinar si la longitud es igual a n
            n_trayec.append(i) # Se agrega la trayectoria a la lista
    return n_trayec # Se retorna la lista


t = [['A', 'B'], ['A', 'D'], ['A', 'C', 'D'], ['B', 'C', 'D']]

# Lista de trayectorias


rest = tray_long_n(t,1) # Guardado de las trayectorias de longitud 1
rest2 = tray_long_n(t,2) # Guardado de las trayectorias de longitud 2

for i in rest: # Impresion de las trayectorias de longitud 1
    print("Trayectoria de longitud 1 (2 vertices 1 arco): ", i)

for i in rest2: # Impresion de las trayectorias de logitud 2
    print("Trayectoria de longitud 2 (3 vertices 2 arcos): ", i)    