tup1 = (1,2)   #Asignacion de valores a las tuplas
tup2 = (1,2)
tup3 = ("a","b")



def verf_tup(t1,t2): #Funcion con las condiciones de evaluacion
    
    if t1 == t2:   # Retorno de true si ambas tuplas son iguales
       return True
    else:
        return False # Retorno de false si las tuplas son diferentes
   
    
    
    
print(verf_tup(tup1,tup2))  # Impresiones del llamado de la funcion

print(verf_tup(tup3, tup1))  