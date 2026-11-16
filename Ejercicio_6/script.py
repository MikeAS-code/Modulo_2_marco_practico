'''

Ejercicio 6 — Filtrar y calcular

**Objetivo:** aplicar condiciones y cálculos a datos extraídos.


**Desafíos:**

* Encontrar el más barato.
* Calcular el promedio de precios.
* Mostrar cuántos productos pertenecen a cada categoría.
* Comparar el descuento fijo del 10 % con el descuento informado por la API.

'''


productos_caros = [
    producto
    for producto in productos_limpios
    if producto["precio"] > 50
]

mas_caro = max(productos_limpios, key=lambda p: p["precio"])

for producto in productos_limpios:
    producto["precio_promocional"] = round(producto["precio"] * 0.90, 2)

print("Productos caros:", len(productos_caros))
print("Más caro:", mas_caro["nombre"])