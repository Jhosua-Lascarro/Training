# helper.py

from datetime import datetime
from pathlib import Path

from openpyxl import Workbook


# manejo de la ubicacion de la database
def check_file(path_file: str) -> str | None:
    """Creates the database file if it doesn't exist."""
    file_path: str = path_file + "database.xlsx"

    if Path(path_file).exists():
        print("Database cargada...")
        return file_path
    Path(path_file).mkdir(parents=True)
    book = Workbook()
    book.active.append(["Producto", "Precio", "Cantidad"])  # type: ignore
    book.save(file_path)
    return file_path


def capture_path_file() -> str:
    """Retorna la ruta de la base de datos segun la fecha."""
    date: datetime = datetime.now()
    return rf"./app/data/{date.year}/{date.month}/"


# funciones manejo de entrada de datos
def capture_error(func):
    "decorador para manejo de errores."

    def value_func(txt: str) -> str:
        while True:
            try:
                return func(txt)
            except ValueError as e:
                print(f"Error: {e}.")

    return value_func


@capture_error
def capture_str(txt: str) -> str:
    "Captura y comprueba si la entrada esta vacia."

    if not (value := input(txt)):
        raise ValueError("El valor no puede ser vacío.")
    return value


@capture_error
def capture_int(txt: str) -> int:
    "Captura y comprueba si la entrada esta vacia o si es numerica."

    if not (value := input(txt)):
        raise ValueError("El valor no puede ser vacío.")
    elif not int(value):
        raise ValueError("Ingreso de valor de númerico entero.")
    return int(value)


@capture_error
def capture_float(txt: str) -> float:
    "Captura y comprueba si la entrada esta vacia o si es numerica."

    if not (value := input(txt)):
        raise ValueError("El valor no puede ser vacío.")
    elif not float(value):
        raise ValueError("El valor no es númerico")
    return float(value)
