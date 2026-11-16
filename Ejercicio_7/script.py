'''

Ejercicio 7 — Guardar y leer archivos TXT y JSON

**Objetivo:** persistir resultados y recuperarlos.


**Desafíos:**

* Abrir y leer el TXT línea por línea.
* Agregar una línea al TXT usando modo `a`.
* Confirmar que el JSON recuperado contiene la misma cantidad de productos.

'''


import json
from pathlib import Path

Path("datos").mkdir(exist_ok=True)

with open("datos/resumen.txt", "w", encoding="utf-8") as archivo:
    for producto in productos_limpios:
        archivo.write(f'{producto["nombre"]}: {producto["precio"]}\n')

with open("datos/productos.json", "w", encoding="utf-8") as archivo:
    json.dump(productos_limpios, archivo, ensure_ascii=False, indent=4)

with open("datos/productos.json", "r", encoding="utf-8") as archivo:
    datos_guardados = json.load(archivo)

print("Productos recuperados:", len(datos_guardados))