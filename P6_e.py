A = [1,2,3,4,5,6,7]   #Asignacion de valores al conjunto A 
R = [] #Creacion del conjunto vacio R para la relacion
tup_aux = () #Creacion de tupla para guardar los pares de la relacion

for i in A:       #Ciclos for anidados para realizar los recorridos
    for j in A:
        if i%227 == j%227:   # Comparativa entre posiciones
            tup_aux = (j,i) # Uso de la tupla para guardar el par si i%227 == j%227
            R.append(tup_aux) # La tupla se agrega al conjunto R
        else:
            tup_aux = () # La tupla se limpia en caso de que i%227 == j%227 no sean iguales   
    

print(R) # Se imprime el conjunto R