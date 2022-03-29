from parse.func_parse.func_search_address import search_address
from parse.func_parse.func_search_namemn_nap import search_namemn_nap
from parse.func_parse.func_search_namepr_quantity import search_name_quantity
from parse.func_parse.func_add_all_data import add_all_data, get_mas_all_id, get_num_data
from parse.func_parse.func_add_all_data import update_data, print_all_id
from parse.func_del.func_del_address import del_address
from parse.func_del.func_del_namemn_nap import del_namemn_nap
from parse.func_del.func_del_name_product_quantity import del_name_product_quantity
from add_new_data import Add_data
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Window.fullscreen = 'auto'


class MainWindow(Screen):
    main_labels = StringProperty()
    second_labels = StringProperty()
    num_labels = StringProperty()

    def __init__(self, **kw):
        super(MainWindow, self).__init__(**kw)
        self.main_labels = add_all_data()
        if len(get_mas_all_id()) > 0:
            self.second_labels = f"В xml файле есть незаполненное поле. Это данные со следующими id:" \
                                 f" {print_all_id()}"
        self.num_labels = get_num_data()

    def update_data(self):
        self.main_labels = update_data()
        self.num_labels = get_num_data()

class AddWindow(Screen):

    def add_data(self):
        add = Add_data()
        if add.add_new_data(self.input_1.text, self.input_2.text, self.input_3.text, self.input_4.text,
                            self.input_5.text):
            self.label_1.text = "Есть неверное поле или такие данные уже есть, пожалуйста исправьте его"
        else:
            self.label_1.text = "Элемент был успешно добавлен!"

    def clear(self):
        self.input_1.text = ""
        self.input_2.text = ""
        self.input_3.text = ""
        self.input_4.text = ""
        self.input_5.text = ""
        self.label_1.text = ""

class SecondWindow(Screen):
    pass


class SecondWindow_1(Screen):
    def delete_address(self):
        self.mylabel.text = del_address(self.del_input.text)

    def clear(self):
        self.mylabel.text = ""
        self.del_input.text = ""


class SecondWindow_2(Screen):
    def delete_namemn_nap(self):
        self.mylabel.text = del_namemn_nap(self.del_input.text)

    def clear(self):
        self.mylabel.text = ""
        self.del_input.text = ""

class SecondWindow_3(Screen):
    def delete_namepr_quantity(self):
        self.mylabel.text = del_name_product_quantity(self.del_input.text)

    def clear(self):
        self.mylabel.text = ""
        self.del_input.text = ""

class ThirdWindow(Screen):
    pass


class ThirdWindow_1(Screen):
    def search_pr1(self):
        self.search_label.text = search_address(self.search_input.text)

    def clear(self):
        self.search_label.text = ""
        self.search_input.text = ""


class ThirdWindow_2(Screen):
    def search_pr2(self):
        self.search_label.text = search_namemn_nap(self.search_input.text)

    def clear(self):
        self.search_label.text = ""
        self.search_input.text = ""

class ThirdWindow_3(Screen):
    def search_pr3(self):
        self.search_label.text = search_name_quantity(self.search_input.text)

    def clear(self):
        self.search_label.text = ""
        self.search_input.text = ""

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("main.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()
