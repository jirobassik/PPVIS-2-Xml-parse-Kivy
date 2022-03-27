from model.manufacturer import Manufacturer
from model.warehause import Warehause

class Product(Manufacturer, Warehause):

    def __init__(self):
        super().__init__()
        self._name = ""
        self._mas_all = []
        self._manufacturer = None
        self._warehouse = None

    def get_name_pr(self) -> str:
        return self._name

    def set_name_pr(self, name: str) -> None:
        self._name = name

    def set_manufacturer(self, manufacturer: Manufacturer) -> None:
        self._manufacturer = manufacturer

    def get_manufacturer(self) -> Manufacturer:
        return self._manufacturer

    def set_warehouse(self, warehause: Warehause) -> None:
        self._warehouse = warehause

    def get_warehouse(self) -> Warehause:
        return self._warehouse

    def set_mas_all(self, mas_all) -> None:
        self._mas_all.append(mas_all)

    def get_mas_all(self) -> list:
        return self._mas_all




