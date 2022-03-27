import xml.sax
import copy
from model.manufacturer import Manufacturer
from model.product import Product
from model.warehause import Warehause

mas_all = []
mas = []
mas_all_id = []

def get_mas_all() -> list:
    return mas_all

def get_mas_all_id() -> list:
    return mas_all_id

class Search_Address(xml.sax.ContentHandler):
    search_el = ""
    mas_products = []
    id = None

    def __init__(self):
        self.manufacturer = Manufacturer()
        self.warehouse = Warehause()
        self.name = ""
        self.product = Product()
        self.namemn = ""
        self.nap = ""
        self.quantity = ""
        self.address = ""
        self.check = False

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "productid":
            name2 = attributes["id"]
            self.id = name2
        if tag == "prname":
            name = attributes["name"]
            self.mas_products.append(name)

    # Call when an elements ends
    def endElement(self, tag):
        if self.CurrentData == "namemn":
            self.mas_products.append(self.namemn)
        elif self.CurrentData == "nap":
            self.mas_products.append(self.nap)
        elif self.CurrentData == "quantity":
            self.mas_products.append(self.quantity)
        elif self.CurrentData == "address":
            self.mas_products.append(self.address)
        self.CurrentData = ""
        if tag == "productid":
            if len(self.mas_products) == 5 and self.check:
                self.product.set_name_pr(self.mas_products[0])
                self.product.set_manufacturer(self.manufacturer)
                self.manufacturer.set_name_mn(self.mas_products[1])
                self.manufacturer.set_pan(self.mas_products[2])
                self.product.set_manufacturer(self.manufacturer)
                self.warehouse.set_quantity(self.mas_products[3])
                self.warehouse.set_address(self.mas_products[4])
                self.product.set_warehouse(self.warehouse)
                mas = copy.copy(self.mas_products)
                t = copy.copy(self.id)
                mas_all_id.append(t)
                mas_all.append(mas)
                self.check = False
                self.mas_products.clear()
            elif len(self.mas_products) == 5 and not self.check:
                self.mas_products.clear()
            elif len(self.mas_products) < 5:
                self.mas_products.clear()
                self.check = False

    def characters(self, content):
        if self.CurrentData == "namemn":
            self.namemn = content
        elif self.CurrentData == "nap":
            self.nap = content
        elif self.CurrentData == "quantity":
            self.quantity = content
        elif self.CurrentData == "address":
            self.address = content
            if content == self.search_el:
                self.check = True

    def get_product(self) -> Product:
        return self.product

    def set_input_search(self, search_el):
        self.search_el = search_el

