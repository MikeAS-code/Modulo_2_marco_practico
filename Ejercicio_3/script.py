'''

Ejercicio 3 — Trabajar con listas de diccionarios

**Objetivo:** recorrer un catálogo y calcular estadísticas básicas.

**Desafíos:**

* Mostrar solo productos con precio mayor que 50.
* Contar los productos que cumplen esa condición.
* Crear una nueva lista `productos_caros` sin modificar la original.
* Identificar el producto de menor precio.

'''


productos = [
    {"nombre": "Mouse", "precio": 25},
    {"nombre": "Teclado", "precio": 85},
    {"nombre": "Monitor", "precio": 210},
]

total = 0

for producto in productos:
    print(producto["nombre"], producto["precio"])
    total += producto["precio"]

promedio = total / len(productos)
print("Precio promedio:", promedio)


