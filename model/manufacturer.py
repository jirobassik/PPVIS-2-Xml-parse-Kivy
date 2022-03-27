class Manufacturer:

    def __init__(self):
        self._name_mn = ""
        self._pan = None

    def set_name_mn(self, name: str) -> None:
        self._name_mn = name

    def get_name_mn(self) -> str:
        return self._name_mn

    def set_pan(self, pan: int) -> None:
        self._pan = pan

    def get_pan(self) -> int:
        return self._pan
