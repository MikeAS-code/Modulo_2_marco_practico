import requests


def obtener_productos(limite=10):
    url = "https://dummyjson.com/products"
    respuesta = requests.get(url, params={"limit": limite}, timeout=15)
    respuesta.raise_for_status()
    return respuesta.json()["products"]