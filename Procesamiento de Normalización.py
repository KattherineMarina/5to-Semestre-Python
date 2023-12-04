# Kattherine Guadalupe Marina Cazares 951 28/Agosto/2023

import pandas as pd
casas = {"NDormitorios": [2, 1, 3, 2, 3, 4, 1, 2],
         "Tamaño": [85, 65, 150, 100, 240, 80, 105, 90]}
df = pd.DataFrame(casas)

#class Normalizacion():

# Realizar una función que normalice los datos usando min-max que reciba como parámetro un DataFrame y otro parámetro que
# sea una lista de columnas a normalizar. Retornar el DataFrame con los datos normalizados

def min_max(df):
    min_dormitorios = df.NDormitorios.min()
    max_dormitorios = df.NDormitorios.max()
    df["MinMax NºDormitorios"] = (df.NDormitorios - min_dormitorios) / (max_dormitorios - min_dormitorios)

    min_tamaño = df.Tamaño.min()
    max_tamaño = df.Tamaño.max()
    df["MinMax Tamaño"] = (df.Tamaño - min_tamaño) / (max_tamaño - min_tamaño)
    print(df)

# Realizar una función que normalice los datos usando Z-Score que reciba como parámetro un DataFrame y otro parámetro que
# sea una lista de columnas a normalizar. Retornar el DataFrame con los datos normalizados.

def z_score(df):
    prom_dormitorios = df.NDormitorios.mean()
    std_dormitorios = df.NDormitorios.std()
    df["Zscore NºDormitorios"] = (df.NDormitorios - prom_dormitorios) / std_dormitorios

    prom_tamaño = df.Tamaño.mean()
    std_tamaño = df.Tamaño.std()
    df["Zscore Tamaño"] = (df.Tamaño - prom_tamaño) / std_tamaño
    print(df)

# Realizar una función que normalice los datos usando escalado simple que reciba como parámetro un DataFrame y otro
# parámetro que sea una lista de columnas a normalizar. Retornar el DataFrame con los datos normalizados.
def escalado_simple(df):
    max_dormitorios = df.NDormitorios.max()
    max_tamaño = df.Tamaño.max()
    df["Escalado Simple NºDormitorios"] = df.NDormitorios / max_dormitorios
    df["Escalado Simple Tamaño"] = df.Tamaño / max_tamaño
    print(df)

min_max(df)
z_score(df)
escalado_simple(df)