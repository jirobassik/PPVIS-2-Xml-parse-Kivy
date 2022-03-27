import xml.sax
from parse.search_namemn_nap import Search_Namemn_Nap
from parse.search_namemn_nap import get_mas_all
from tabulate import tabulate

def search_namemn_nap(search_el):
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    handler = Search_Namemn_Nap()
    handler.set_input_search(search_el)
    parser.setContentHandler(handler)
    parser.parse("D:/Programs/PyCharm Community Edition 2021.2.3/Project/PPVIS2/Data.xml")
    if len(get_mas_all()) == 0:
        a = "Не были найдены элементы"
    else:
        head = ["Название товара", "Название производителя", "УНП товара",
                "Количество товара", "Адрес склада"]
        data = get_mas_all()
        a = tabulate(data, headers=head, tablefmt="grid", stralign='center')
        get_mas_all().clear()
    return a
