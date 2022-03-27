class Warehause:

    def __init__(self):
        self._quantity = None
        self._address = None

    def set_quantity(self, quantity: int) -> None:
        self._quantity = quantity

    def get_quantity(self) -> int:
        return self._quantity

    def set_address(self, address: str) -> None:
        self._address = address

    def get_address(self) -> str:
        return self._address
