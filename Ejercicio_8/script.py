'''
Ejercicio 8 — Introducción a pandas

**Objetivo:** analizar una lista de diccionarios con un DataFrame.


**Desafíos:**

* Mostrar solo los productos con precio mayor que 50.
* Ordenar por valoración si la columna `rating` está disponible.
* Identificar el precio mínimo y máximo con `.min()` y `.max()`.

'''

import pandas as pd

df = pd.DataFrame(datos_guardados)

print(df.head())
print(df[["nombre", "precio"]])
print(df["precio"].mean())

ordenados = df.sort_values("precio", ascending=False)
print(ordenados[["nombre", "precio"]].head())