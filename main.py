# main.py

from datetime import datetime as time

from pandas import read_excel

from app.utils.helper import capture_path_file, check_file
from app.utils.inventary import Inventory
from app.utils.options import get_add_product, get_show_products

file_path: str = capture_path_file()
check_file(file_path)
invent = Inventory(read_excel(file_path), file_path)
while True:
    match option := input(
        f"Fecha: {time.now().date}\nSistema de gestion de inventario.\n\n"
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
            print("You chose 2")
            get_show_products(invent)

        case "3":
            print("You chose 3")

        case "4":
            print("You chose 4")

        case "5":
            print("You chose 5")

        case "6":
            print("You chose 6")
            break

        case _:
            print("Error: Ingreso de opción inválida.\n")
