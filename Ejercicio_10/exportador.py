import json
from pathlib import Path
import pandas as pd


def exportar_productos(productos, carpeta="datos"):
    destino = Path(carpeta)
    destino.mkdir(parents=True, exist_ok=True)

    with (destino / "productos.json").open("w", encoding="utf-8") as archivo:
        json.dump(productos, archivo, ensure_ascii=False, indent=4)

    with (destino / "resumen.txt").open("w", encoding="utf-8") as archivo:
        for producto in productos:
            archivo.write(f'{producto["nombre"]}: {producto["precio"]}\n')

    pd.DataFrame(productos).to_csv(
        destino / "productos.csv", index=False, encoding="utf-8-sig"
    )