import xml.sax
from parse.add_all_data import Add_All_Data
from parse.add_all_data import get_mas_all, get_mas_all_id
from add_new_data import get_res_data_all
from tabulate import tabulate

def add_all_data():
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    handler = Add_All_Data()
    parser.setContentHandler(handler)
    try:
        parser.parse("D:/Programs/PyCharm Community Edition 2021.2.3/Project/PPVIS2/Data.xml")
        head = ["Название товара", "Название производителя", "УНП товара",
                "Количество товара", "Адрес склада"]
        data = get_mas_all()
        a = tabulate(data, headers=head, tablefmt="grid", stralign='center')
        get_mas_all().clear()
    except xml.sax._exceptions.SAXParseException:
        a = "В xml файле есть грубая синтаксическая ошибка"
    return a

def update_data():
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    Handler = Add_All_Data()
    parser.setContentHandler(Handler)
    try:
        parser.parse("D:/Programs/PyCharm Community Edition 2021.2.3/Project/PPVIS2/Data.xml")
        head = ["Название товара", "Название производителя", "УНП товара",
                "Количество товара", "Адрес склада"]
        if get_res_data_all() != 0:
            for i in get_res_data_all():
                get_mas_all().append(i)
        data = get_mas_all()
        b = tabulate(data, headers=head, tablefmt="grid", stralign='center')
        get_mas_all().clear()
    except xml.sax._exceptions.SAXParseException:
        b = "В xml файле есть грубая синтаксическая ошибка"
    return b

def get_num_data():
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    handler = Add_All_Data()
    parser.setContentHandler(handler)
    try:
        parser.parse("D:/Programs/PyCharm Community Edition 2021.2.3/Project/PPVIS2/Data.xml")
        stroka = f"В базе данных {len(get_mas_all())} элемент"
        get_mas_all().clear()
    except xml.sax._exceptions.SAXParseException:
        stroka = "В xml файле есть грубая синтаксическая ошибка"
    return stroka

def print_all_id():
    v = ""
    for i in get_mas_all_id():
        v += i + "  "
    return v
