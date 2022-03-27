from xml.dom import minidom

class DeleteByAverageMarkDomHandler:

    def init(self, student_id: str):
        self._student_id = student_id

    def delete_student_by_student_id(self) -> bool:
        xml = minidom.parse("D:/Programs/PyCharm Community Edition 2021.2.3/Project/PPVIS2/Data.xml")
        group = xml.documentElement
        students = group.getElementsByTagName('productid')
        for student in students:
            if str(student.getAttribute('id')) == str(self._student_id):
                student.parentNode.removeChild(student)
        xml.writexml(open('D:/Programs/PyCharm Community Edition 2021.2.3/Project/PPVIS2/Data.xml', 'w', encoding="UTF-8"), encoding="UTF-8")
        return True
