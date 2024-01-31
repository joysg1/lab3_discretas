from itertools import product   # Importe de la funcion product de itertools


A = {1,2,3,4,5,6,7}  # Asignacion de valores a los conjuntos
B = {"a", "b"}


def prod_cart(S1,S2):  # Definicion de la funcion 
    
    result = list(product(S1,S2)) # se declara result que recibe como lista 
                                  # el resultado de la funcion product
    
    return result   # se retorna result
    
    
print(prod_cart(A,B)) # se imprime el llamado de la funcion prod_cart