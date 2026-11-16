from scraper import obtener_productos
from utilidades import transformar_productos
from exportador import exportar_productos


def main():
    originales = obtener_productos(limite=10)
    productos = transformar_productos(originales)
    exportar_productos(productos)
    print(f"Se exportaron {len(productos)} productos")


if __name__ == "__main__":
    main()