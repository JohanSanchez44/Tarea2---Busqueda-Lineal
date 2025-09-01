# Tarea 2 Busqueda Líneal 

def Busqueda(lista, piv):
    i = 1   # T(n) = 1
    for x in lista:   
        if x == piv:
            return True, i   # T(n) = 1
        else: 
            i += 1   # T(n) = n
    return False, None   # T(n) = 1

arreglo = [1, 2, 3, 4, 5, 6, 7, 8, 56, 78, 9, 0, 23, 65, 36, 5]   # T(n) = n
num = 67   # T(n) = 1

encontrado, numI = Busqueda(arreglo, num)   # T(n) = 1

if encontrado: 
    print(f"El numero {num} fue encontrado dentro del arreglo :) \nEl numero de comparaciones fue: {numI}")   # T(n) = 1
else: 
    print(f"El numero {num} no ha sido encontrado :(")   # T(n) = 1
