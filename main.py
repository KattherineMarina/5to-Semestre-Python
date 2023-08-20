# DUPLICADOS------------------------------------------------------------------------------------------------------------
# Dada una lista de números enteros, retorna True si al menos un valor aparece dos veces, y Falso si todos los elementos
# son distintos.
lista1=[1,2,3,4,5,1,2,3]
lista2=[1,2,3,4,5]

print(len(lista1))
print(len(lista2))
print(lista1.count(2))

def duplicados (lista):
    for a in range (len(lista)):
        for i in range (a+1, len(lista)):
            if lista[a]==lista[i]:
                return True
        return False
print(duplicados(lista1))
print(duplicados(lista2))

def duplicados2 (lista):
    return len(lista) != len(set(lista))
resultado= duplicados2(lista2)
print(resultado)