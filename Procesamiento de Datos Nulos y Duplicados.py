# Kattherine Guadalupe Marina Cazares 951 28/Agosto/2023

import pandas as pd

alumnos = [{'Nombre': 'Juan', 'Edad': 25, 'Colegiatura': 1234}, {'Nombre': 'María', 'Edad': 30, 'Colegiatura': None},\
          {'Nombre': 'Pedro', 'Edad': 25, 'Colegiatura': 5678}, {'Nombre': 'Ana', 'Edad': None, 'Colegiatura': 9012},\
          {'Nombre': 'Juan', 'Edad': 28, 'Colegiatura': 1234}, {'Nombre': 'Luis', 'Edad': 30, 'Colegiatura': 3456},\
          {'Nombre': 'Ana', 'Edad': 25, 'Colegiatura': 7890}, {'Nombre': 'Elena', 'Edad': 28, 'Colegiatura': None},\
          {'Nombre': 'Pedro', 'Edad': 30, 'Colegiatura': 5678}, {'Nombre': 'Sara', 'Edad': None, 'Colegiatura': 9012},\
          {'Nombre': 'Juan', 'Edad': 25, 'Colegiatura': 1234}, {'Nombre': 'María', 'Edad': 30, 'Colegiatura': 3456},\
          {'Nombre': 'Carlos', 'Edad': None, 'Colegiatura': None}, {'Nombre': 'Ana', 'Edad': 25, 'Colegiatura': 5678},
           {'Nombre': 'Luis', 'Edad': 28, 'Colegiatura': 7890}, {'Nombre': 'Ana', 'Edad': 25, 'Colegiatura': 5678},
           {'Nombre': 'Pedro', 'Edad': 30, 'Colegiatura': 5678} ]
df = pd.DataFrame(alumnos)
print(df)

# Realizar una función que reciba como parámetro un DataFrame y  retorne el porcentaje de valores nulos de cada columna

def porcentaje_nulos(df):
    porcentaje = df.isnull().mean() * 100
    df = pd.DataFrame({
        'Columna': porcentaje.index,
        'Porcentaje de Nulos': porcentaje.values
    })
    print(df)

# Realizar una función que reciba como parámetro un DataFrame y retorne el número de renglones duplicados

def renglones_duplicados(df):
    duplicados = df[df.duplicated()]
    print(duplicados)

# Realizar una función que reciba como parámetro un DataFrame y un máximo porcentaje. Este debe eliminar todas las
# columnas que superen o igualen el máximo porcentaje de valores nulos establecidos en el DataFrame Original. Retornar
# la lista nombres de columnas eliminadas.  Validar que el porcentaje máximo esté entre 0 y 1.
def eliminar_nulos(df):
    porcentaje = 0.80
    if 0 <= porcentaje <= 1:
        entero = round(len(df) * porcentaje)
        nuevo_data = df.dropna(axis="columns", thresh=entero)
        eliminados = list(set(df.columns) - set(nuevo_data.columns))
        return f"Lista de columna(s) eliminada(s) porque no cuentan con el mínimo de {porcentaje}% de valores NO nulos: {eliminados}"
    else:
        return "El porcentaje debe estar entre 0 y 1."

print(eliminar_nulos(df))

# Realizar una función que reciba como parámetro un DataFrame, una lista con los nombres de las columnas a verificar y una cadena. La cadena solo puede ser mean, bfill o ffill, en caso contrario lanzar una excepción. Debe sustituir los valores nulos por el método especificado y retornar el DataFrame modificado.
def sustitucion(data, list, cadena):
    if cadena not in ['mean', 'bfill', 'ffill']:
        raise ValueError("El método debe ser 'mean', 'bfill' o 'ffill'.")
    if cadena == "mean":
        if pd.api.types.is_numeric_dtype(data[alumnos]):
            new_data = data[list].mean()
        else:
            raise ValueError(f"La columna '{alumnos}' no es numérica, por lo que no se puede usar 'mean'.")
    elif cadena == "bfill":
        new_data = data[list].bfill()
    else:
        new_data = data[list].ffill()
    return new_data

data = df
alumnos = ["Nombre", "Edad", "Colegiatura"]
cadena = "ffill"

# Realizar una función que reciba como parámetro un DataFrame y elimine los renglones repetidos en el DataFrame Original. Debe retornar la cantidad de renglones eliminados.
def repetidos(df):
    drop_duplicates = df.drop_duplicates()
    eliminados = len(df) - len(drop_duplicates)
    return f"La cantidad de renglones eliminados es: {eliminados}"
    print(df)

porcentaje_nulos(df)
renglones_duplicados(df)
eliminar_nulos(df)
sustitucion(df)
repetidos(df)