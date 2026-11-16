
'''
Ejercicio 2 — Crear diccionarios de productos

**Objetivo:** modelar un producto con claves y valores.


    **Desafíos:**

    * Agregar una marca.
    * Aumentar el stock en cinco unidades.
    * Mostrar una frase con el nombre y el precio actualizado.
    * Probar `producto.get("descuento", 0)` y explicar la diferencia frente a `producto["descuento"]`.

'''


producto = {
    "nombre": "Teclado mecánico",
    "precio": 85.50,
    "categoria": "Accesorios",
    "stock": 12,
}

print(producto["nombre"])
print(producto["precio"])

producto["precio"] = 79.99
producto["disponible"] = True

print(producto)

