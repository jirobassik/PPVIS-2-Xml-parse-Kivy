from xml.dom import minidom

class DeleteElementByID:

    def init(self, product_id: str):
        self._product_id = product_id

    def delete_element(self) -> bool:
        xml = minidom.parse("D:/Programs/PyCharm Community Edition 2021.2.3/Project/PPVIS2/Data.xml")
        group = xml.documentElement
        product = group.getElementsByTagName('productid')
        for products in product:
            if str(products.getAttribute('id')) == str(self._product_id):
                products.parentNode.removeChild(products)
        xml.writexml(open('D:/Programs/PyCharm Community Edition 2021.2.3/Project/PPVIS2/Data.xml', 'w', encoding="UTF-8"), encoding="UTF-8")
        return True
