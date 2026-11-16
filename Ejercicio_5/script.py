'''


Ejercicio 5 — Extraer y transformar datos

**Objetivo:** seleccionar campos útiles y normalizar los registros.

Partiendo de `productos` obtenido en el ejercicio anterior:


**Desafíos:**

* Incorporar `discountPercentage`.
* Calcular `precio_con_descuento` según el precio y porcentaje de descuento.
* Decidir qué hacer si falta la marca.

'''


productos_limpios = []

for producto in productos:
    item = {
        "nombre": producto["title"],
        "precio": float(producto["price"]),
        "categoria": producto.get("category"),
        "marca": producto.get("brand", "Sin marca"),
        "rating": producto.get("rating"),
    }
    productos_limpios.append(item)

print(productos_limpios)