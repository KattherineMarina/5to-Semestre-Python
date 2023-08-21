# DESENCRIPTAR----------------------------------------------------------------------------------------------------------
# Diseña una funcion desencripta(s,clave) que realice la funcion inversa a la funcion anterior, es decir, reciba un
# string s y una clave y realice la desencripcion del mensaje en el string devolviendo la cadena desencriptada.

m= "milk"
chocolate= "riok 1 mtfmfbidk"
abecedario= "abcdefghijklmnopqrstuvwxyz"
clave= "ixmrklstnuzbowfaqejdcpvhyg"
s= "cafe"
s2= "dame 1 chocolate"
print(s.isalpha())
print(s2.isalpha())

def desencriptar(m,clave):
    final= []
    for i in m:
        if i == "":
            pass
        else:
            index= clave.index(i)
            letter= abecedario[index]
            final += letter
    return "".join(final)
print(desencriptar(m,clave))

diccionario = {}
def desencriptar2(chocolate, diccionario):
    final2 = []
    for x in chocolate:
        if x == " ":
            final2.append("")
        else:
            letter = diccionario.get(x,x)
            final2.append(letter)
    return "".join(final2)
resultado = desencriptar2(chocolate,diccionario)
print(resultado)