def verf_rel(X, Y, W):    #Declaracion de la funcion
    for el1 in X:         # Ciclos repetitivos para recorrer los elementos de X y Y
        for el2 in Y:
            if (el1, el2) in W: # Validar si los elementos de X y Y estan en W
                return True     # Retorno de true de encontrar coincidencia
    return False # Retorno de false al salir de los ciclos de repeticion

A = {1, 2, 3, 4, 5, 6, 7}                           # Asignacion de valores a los conjuntos
B = {'a', 'b'}
C = {(1, 'a'), (2, 'b'), (3, 'a')}
D = {(1,'h'), (2,'s')}


resultado = verf_rel(A, B, C)  # Guardado de la ejecucion de la funcion en variables

resultado2 = verf_rel(A, B, D)

print(resultado) # Impresion de los resultados
print(resultado2)



