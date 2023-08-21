# ESTADISTICA BASICA
# Cree una clase llamada Estadística que contiene como atributo una lista de números naturales la cual puede contener
# repetidos. Debe contener los siguientes métodos:
class Estadistica:
    def __init__(self, numeros_naturales):
        self.numeros_naturales = numeros_naturales

# a) Frecuencia de Números.
# Dada la lista, devuelve un diccionario con el número de veces que aparece cada número en la lista.
    def frecuencia(self):
        frecuencia={}
        for n in self.numeros_naturales:
            if n in frecuencia:
                frecuencia[n]=frecuencia[n]+1
            else:
                frecuencia[n]=1
        return frecuencia

# b) Moda.
# Dada la lista, devuelva la moda de la lista (el valor más repetido). Puedes usar la función anterior como ayuda.
    def moda(self):
        frecuencia = self.frecuencia()
        numerorepetido = 0
        for n, cantidad in frecuencia.items():
            if cantidad > numerorepetido:
                numerorepetido = cantidad
                moda = n
        return moda

# c) Histograma.
# Dada la lista, muestra el histograma de la lista. Puedes reusar los métodos anteriores.
    def histograma(self):
        frecuencia = self.frecuencia()
        for n in frecuencia:
            histo= '*' * frecuencia[n]
            print(f"{n} {histo}")

# Ejemplo: lista = ListaNumeros ([1, 3, 2, 4, 2, 2, 3, 2, 4, 1, 2, 1, 2, 3, 1, 3, 1])
# lista.histograma()
# Salida: 1 ***** 2 ****** 3 **** 4 *
listanumeros = [1, 3, 2, 4, 2, 2, 3, 2, 4, 1, 2, 1, 2, 3, 1, 3, 1]

e1= Estadistica(listanumeros)

print("Frecuencia:", e1.frecuencia())
print("Moda:", e1.moda())
print("Histograma:") #aqui no se pone el ,e1.histograma ya que te regresa un none como resultado.
e1.histograma()