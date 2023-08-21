# ENCRIPTAR-------------------------------------------------------------------------------------------------------------
# Diseñe una funcion encripta(s,clave), que reciba un strign s con un mensaje y un string con una clave de codificacion,
# y retorne el mensaje codificado segun la clave leida. Los signos de puntuacion y digitos que aparecen en el mensaje
# deben conservarse sin cambios.
abecedario= "abcdefghijklmnopqrstuvwxyz"
clave= "ixmrklstnuzbowfaqejdcpvhyg"
s= "cafe"
s2= "dame 1 chocolate"
s_modificada=[]
s_modificada2=[]
dic= {}
dic2= {}

def indices(s,clave):
    for m in range (26):
        dic[abecedario[m]]=clave[m]
    for x in s:
        if x in dic:
            s_modificada.append(dic[x])
        else:
            s_modificada.append(x)
    return "".join(s_modificada)
print(indices(s,clave))

def indices2(s2,clave):
    for m in range (26):
        dic2[abecedario[m]]=clave[m]
    for x in s2:
        if x in dic2:
            s_modificada2.append(dic[x])
        else:
            s_modificada2.append(x)
    return "".join(s_modificada2)
print(indices2(s2,clave))