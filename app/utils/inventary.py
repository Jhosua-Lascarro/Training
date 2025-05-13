# inventary.py

from dataclasses import dataclass

from pandas import DataFrame


@dataclass
class Inventory:
    _data: DataFrame
    _path_data_file: str

    def add_product(self, product: str, price: float, lot: int) -> bool:
        """Adds a product to the database."""

        if product in self._data["Producto"].values:
            raise ValueError(f"El producto '{product}' ya existe en el inventario.")
        self._data.loc[len(self._data)] = [product, price, lot]
        self._data.to_excel(self._path_data_file, index=False)
        return True

    def show_product(self, product: str) -> DataFrame:
        """Returns a list of products."""
        if product not in self._data["Producto"].values:
            raise ValueError(f"El producto '{product}' no existe en el inventario.")

        return self._data[self._data["Producto"] == product]

    def show_all_products(self) -> DataFrame:
        """Returns a list of all products."""
        if self._data.empty:
            raise ValueError("El inventario está vacío.")

        return self._data

    def update_product(self, product: str, new_name_product: str):
        """Updates the name of a product."""
        if product not in self._data["Producto"].values:
            raise ValueError(f"El producto '{product}' no existe en el inventario.")

        self._data.loc[self._data["Producto"] == product, "Producto"] = new_name_product
        self._data.to_excel(self._path_data_file, index=False)

    def udpate_price(self, product: str, new_price: float):
        """Updates the price of a product."""
        if product not in self._data["Producto"].values:
            raise ValueError(f"El producto '{product}' no existe en el inventario.")

        self._data.loc[self._data["Producto"] == product, "Precio"] = new_price
        self._data.to_excel(self._path_data_file, index=False)

    def udpate_lot(self, product: str, new_lot: int) -> bool:
        """Updates the lot of a product."""
        if product not in self._data["Producto"].values:
            raise ValueError(f"El producto '{product}' no existe en el inventario.")

        self._data.loc[self._data["Producto"] == product, "Cantidad"] = new_lot
        self._data.to_excel(self._path_data_file, index=False)
        return True

    def delete_product(self, product: str) -> bool:
        """Deletes a product from the database."""
        if product not in self._data["Producto"].values:
            raise ValueError(f"El producto '{product}' no existe en el inventario.")

        self._data = self._data[self._data["Producto"] != product]
        self._data.to_excel(self._path_data_file, index=False)
        return True

    def total_inventario(self) -> float:
        """Returns the total value of the inventory."""

        if self._data.empty:
            raise ValueError("El inventario está vacío.")

        return float(self._data["Precio"].sum() * self._data["Cantidad"].sum())
