def transformar_productos(productos):
    resultado = []
    for producto in productos:
        resultado.append({
            "nombre": producto["title"],
            "precio": float(producto["price"]),
            "categoria": producto.get("category"),
            "marca": producto.get("brand") or "Sin marca",
            "rating": producto.get("rating"),
        })
    return resultado