# main.py

from datetime import datetime

from pandas import read_excel

from app.utils.helper import capture_path_file, check_file
from app.utils.inventary import Inventory
from app.utils.options import (
    get_add_product,
    get_delete_product,
    get_show_products,
    get_total_inventario,
    get_update_product,
)

file_path: str = check_file(capture_path_file())  # type: ignore
invent = Inventory(read_excel(file_path), file_path)

while True:
    match option := input(
        f"Fecha: {datetime.now().date()}\nSistema de gestion de inventario.\n\n"
        "[1]. Añadir producto.\n"
        "[2]. Consultar productos.\n"
        "[3]. Actualizar producto.\n"
        "[4]. Eliminar producto.\n"
        "[5]. Valor total del inventario.\n"
        "[6]. Salir del sistema.\n\n"
        "Ingrese una opción: "
    ):
        case "1":
            get_add_product(invent)

        case "2":
            get_show_products(invent)
        case "3":
            get_update_product(invent)
        case "4":
            get_delete_product(invent)
        case "5":
            get_total_inventario(invent)
        case "6":
            break

        case _:
            print("Error: Ingreso de opción inválida.\n")
