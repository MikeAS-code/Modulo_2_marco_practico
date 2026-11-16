'''
Ejercicio 9 — Exportar y volver a leer CSV

**Objetivo:** generar un archivo interoperable con hojas de cálculo.


**Desafíos:**

* Crear `datos/productos_caros.csv` con precios mayores que 50.
* Crear `datos/productos_por_rating.csv` ordenado por valoración.
* Explicar por qué se usa `index=False`.



'''

from pathlib import Path
import pandas as pd

Path("datos").mkdir(exist_ok=True)

df.to_csv("datos/productos.csv", index=False, encoding="utf-8-sig")

leidos = pd.read_csv("datos/productos.csv")
print(leidos.head())