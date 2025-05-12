# options.py

from app.utils.helper import capture_float, capture_int, capture_str


def get_add_product(inventory):
    """Adds a product to the database."""
    product_inventory: str = capture_str("Ingrese el nombre del producto: ")
    product_price = capture_float("Ingrese el precio del producto: ")
    product_lot = capture_int("Ingrese la cantidad de unidades de producto: ")
    inventory.add_product(product_inventory, product_price, product_lot)


def get_show_products(inventory):
    """Shows the products in the database."""
    match capture_str(
        "Opciónes de mostrar productos:\n"
        "[1]. Todos los productos.\n"
        "[2]. Un producto específico.\n"
        "Ingrese una opción: "
    ):
        case "1":
            print(inventory.show_all_products())
        case "2":
            print(
                inventory.show_product(capture_str("Ingrese el nombre del producto: "))
            )
        case _:
            print("Error: No identificado.")


def get_update_product(inventory):
    """Updates the name of a product."""
    match capture_str(
        "Opciónes de actualizar productos:\n"
        "[1]. Nombre del producto.\n"
        "[2]. Precio del producto.\n"
        "[3]. Cantidad de unidades del producto.\n"
        "Ingrese una opción: "
    ):
        case "1":
            print(
                inventory.update_product(
                    capture_str("Ingrese el nombre del producto: "),
                    capture_str("Ingrese el nuevo nombre del producto: "),
                )
            )
        case "2":
            print(
                inventory.udpate_price(
                    capture_str("Ingrese el nombre del producto: "),
                    capture_float("Ingrese el nuevo precio del producto: "),
                )
            )
        case "3":
            print(
                inventory.udpate_lot(
                    capture_str("Ingrese el nombre del producto: "),
                    capture_int("Ingrese la nueva cantidad de unidades del producto: "),
                )
            )
        case _:
            print("Error: No identificado.")


def get_delete_product(inventory):
    """Deletes a product from the database."""
    inventory.delete_product(capture_str("Ingrese el nombre del producto a eliminar: "))


def get_total_inventario(inventory):
    """Returns the total value of the inventory."""

    print(f"El valor total del inventario: {inventory.total_inventario()}$")
