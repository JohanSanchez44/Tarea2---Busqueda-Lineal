# Tarea 2 Busqueda Líneal 

def Busqueda(lista, piv):   # S(n) = 1
    i = 1   # T(n) = 1   S(n) = 1
    for x in lista:   # T(n) = n   S(n) = 1
        if x == piv:   # T(n) = 1
            return True, i   # T(n) = 1
        else: 
            i += 1   # T(n) = 1
    return False, None   # T(n) = 1

arreglo = [1, 2, 3, 4, 5, 6, 7, 8, 56, 78, 9, 0, 23, 65, 36, 5]   # T(n) = n   S(n) = n
num = 67   # T(n) = 1   S(n) = 1

encontrado, numI = Busqueda(arreglo, num)   # T(n) = 1   S(n) = 2

if encontrado: # T(n) = 1
    print(f"El numero {num} fue encontrado dentro del arreglo :) \nEl numero de comparaciones fue: {numI}")   # T(n) = 1
else: 
    print(f"El numero {num} no ha sido encontrado :(")   # T(n) = 1

# T(n) = 1 + n + 1 + 1 + 1 + n + 1 + 1 + 1 + 1 = [2n + 8]
# S(n) = 1 + 1 + 1 + n + 1 + 2 = [n + 6]
