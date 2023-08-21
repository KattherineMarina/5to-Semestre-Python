# SUMA DE DOS NUMEROS---------------------------------------------------------------------------------------------------
# Dado una lista de números enteros y un valor entero (target), retorna el índice de los dos números que sumados sean
# igual al target. Debe asumir que existe siempre una única solución, y que los elementos no se pueden usar dos veces.
# Debes retorna una tupla con los índices
nums=[2,7,11,15]
nums2=[3,2,4]
target=9

def sumaindice(nums,target):
    for w in range (len(nums)):
        for a in range (w+1, len(nums)):
            if nums[w]+nums[a] == target:
                return (w,a)
    return ("No se encontro la suma")
print(sumaindice(nums,target))
print(sumaindice(nums2,target))