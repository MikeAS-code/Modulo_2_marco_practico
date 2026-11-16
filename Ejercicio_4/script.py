'''
Ejercicio 4 — Consultar una API con requests

**Objetivo:** realizar una petición HTTP GET y convertir la respuesta JSON en objetos Python.


**Desafíos:**

* Cambiar `limit=10` por `limit=20`.
* Imprimir el número de productos recibidos.
* Inspeccionar las claves del primer producto usando `.keys()`.




'''

import requests

url = "https://dummyjson.com/products?limit=10"

response = requests.get(url, timeout=15)
response.raise_for_status()

data = response.json()
productos = data["products"]

for producto in productos:
    print(producto["title"], producto["price"])