import xml.sax
from parse.search_namemn_nap import Search_Namemn_Nap
from parse.search_namemn_nap import get_mas_all, get_mas_all_id
from parse.delete_dom import DeleteElementByID
from add_new_data import get_res_search_data, del_search_el
from tabulate import tabulate

def del_namemn_nap(search_el):
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    handler = Search_Namemn_Nap()
    handler.set_input_search(search_el)
    parser.setContentHandler(handler)
    parser.parse("D:/Programs/PyCharm Community Edition 2021.2.3/Project/PPVIS2/Data.xml")
    if len(get_mas_all_id()) == 0 and len(get_res_search_data(search_el)) == 0:
        a = "Не были найдены элементы"
    else:
        for i in get_res_search_data(search_el):
            get_mas_all().append(i)
        del_search_el(search_el)
        head = ["Название товара", "Название производителя", "УНП товара",
                "Количество товара", "Адрес склада"]
        data = get_mas_all()
        a = "Были удалены следующие элементы:\n"
        a += tabulate(data, headers=head, tablefmt="grid", stralign='center')
        delete = DeleteElementByID()
        for i in get_mas_all_id():
            delete.init(i)
            delete.delete_element()
        get_mas_all().clear()
        get_mas_all_id().clear()
    return a
