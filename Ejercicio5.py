# GESTION DE PENSIONISTAS-----------------------------------------------------------------------------------------------
# Crear una clase llamada GrupoPensionistas la cual tendrá un único atributo la cual es una lista o diccionario de
# objetos de tipo Pensionista (Elija a conveniencia si una lista o diccionario). Cada objeto de Pensionista tiene los
# siguientes atributos: identificador del pensionista (string), un entero que indica la edad y una serie de gastos
# mensuales que se guardan (lista de enteros). El número de gastos mensuales puede variar entre pensionistas.
# Por ejemplo, el pensionista con identificador '1111A' se llama 'Carlos' tiene 68 años y tiene 3 gastos mensuales de
# 640, 589 y 573.

class Pensionistas():
    def __init__(self,matricula,nombre,edad,gastos):
        self.matricula=matricula
        self.nombre=nombre
        self.edad=edad
        self.gastos=gastos

    def promediodegastos(self):
        return sum(self.gastos)/len(self.gastos)

class GrupoPensionistas():
    def __init__(self,pensionistas):
        self.pensionistas=pensionistas

# La clase GrupoPensionistas debe tener los siguientes métodos:
# a) mediaGastos(identificador), dado el identificador o indice de un pensionista, devuelva el promedio de los gastos.
    def promediodegastos(self, matricula):
        for x in self.pensionistas:
            if x.matricula==matricula:
                return x.promediodegastos()
        return ("No esta en la base de datos este registro")

# b) mediaEdad(), dado todos los pensionados, devuelve el promedio de las edades.
    def mediaEdad(self):
        edades= sum(x.edad for x in self.pensionistas)
        return edades/len(self.pensionistas)

# c) edadesExtremas(), dado todos los pensionados, devuelva al pensionado con menor y mayor edad en una tupla.
    def edadesExtremas(self, edad):
        if len(edad)>0:
            menor=edad[0]
            mayor=[0]
            for n in edad:
                if n<menor:
                    menor=n
                if n>mayor:
                    mayor=n
            return print(menor,mayor)
        else:
            return ("No se puede hacer una comparacion con una lista vacia")

# d) sumaPromedio(), dado todos los pensionados, devuelva la suma del promedio de los gastos de todos los pensionistas
# de la lista.
    def sumaPromdio(self):
        gastospromedio= 0
        for x in self.pensionistas:
            gastospromedio += x.promediodegastos
        return gastospromedio

# e) mediaMaxima(), dado todos los pensionistas, retorne el mayor promedio de los gastos entre todos los pensionistas de
# la lista, su nombre e identificador.
    def mediaMaxima(self):
        listamaximo= sum(self.pensionistas[0].gastos)/len(self.pensionistas[0].gastos)
        listapensionistas= self.pensionistas[0]
        for x in range (1,len(self.pensionistas)):
            w= self.pensionistas[x]
            promediO=sum(x.gastos)/len(x.gastos)
            if promedi0>listamaximo:
                listamaximo=promediO
                listapensionistas=x
        return (listamaximo,listapensionistas.nombre, listapensionistas.matricula)

# f) gastoPromedio(lst), dado todos los pensionistas, devuelve una lista con el gasto promedio de cada persona. La lista
# resultante debe estar ordenada de forma ascendente.
    def gastoPromedio(self):
        lista3=[]
        for x in self.pensionistas:
            lista3.append(x.promediodegastos())
        lista3.sort()
        return lista3

pensionista1=Pensionistas(1291656, 'Carlos', 68, [640,589,573])
pensionista2=Pensionistas(1298369, 'Miguel', 30, [600,599,873])
pensionista3=Pensionistas(8926418, 'Carmelo', 28, [400,899,1073])

GPENSIONISTAS=GrupoPensionistas([pensionista1,pensionista2,pensionista3])

print(GPENSIONISTAS.medidaGastos(1291656))
print(GPENSIONISTAS.mediaEdad())
print(GPENSIONISTAS.edadesExtremas())
print(GPENSIONISTAS.sumaPromdio())
print(GPENSIONISTAS.mediaMaxima())
print(GPENSIONISTAS.gastoPromedio())