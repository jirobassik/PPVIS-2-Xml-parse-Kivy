import xml.sax
from parse.add_all_data import Add_All_Data
from parse.add_all_data import get_mas_all
import copy
import re
import collections

res_data_all = []

def get_res_data_all():
    return res_data_all

def data_to_mas():
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    Handler = Add_All_Data()
    parser.setContentHandler(Handler)
    parser.parse("D:/Programs/PyCharm Community Edition 2021.2.3/Project/PPVIS2/Data.xml")
    data = copy.copy(get_mas_all())
    get_mas_all().clear()
    return data

class Add_data:
    res_data = []

    def add_new_data(self, namepr, namemn, nap, quantity, address):
        match_nap = re.fullmatch(r"\d{9}", nap)
        match_quantity = re.fullmatch(r"^[1-9]{1}[0-9]{1,7}$", quantity)
        match_namepr = re.fullmatch(r"-[0-9]*|[0-9]*", namepr)
        match_namemn = re.fullmatch(r"-[0-9]*|[0-9]*", namemn)
        match_address = re.fullmatch(r"-[0-9]*|[0-9]*", address)
        if not namepr.strip() or not namemn.strip() or not nap.strip() or not quantity.strip() or not address.strip()\
                or not match_nap or not match_quantity or match_namepr or match_namemn or match_address:
            return True
        else:
            check = False
            new_data = [namepr, namemn, nap, quantity, address]
            for i in data_to_mas():
                if collections.Counter(i) == collections.Counter(new_data):
                    b = "Такие данные уже есть"
                    check = True
                    return b
            if not check:
                Add_data.set_res_data(self, new_data)

    def set_res_data(self, copy_data):
        self.res_data = copy.copy(copy_data)
        r = copy.copy(self.res_data)
        res_data_all.append(r)
