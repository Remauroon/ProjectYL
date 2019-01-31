from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QTableWidget, QPushButton
from PyQt5.QtWidgets import QLineEdit, QLabel, QMainWindow, QDialog, QComboBox, QSpinBox
import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
import csv


class EnterInf(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('add_member.ui', self)
        self.addmember.clicked.connect(self.add_member)

    def add_member(self):
        months = {
            'January': '01',
            'February': '02',
            'March': '03',
            'April': '04',
            'May': '05',
            'June': '06',
            'July': '07',
            'August': '08',
            'September': '09',
            'October': '10',
            'November': '11',
            'December': '12'
        }
        with open('list.csv', newline='', mode='a', encoding='utf8') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            birth = '0' * (2 - len(str(self.day.value()))) + str(self.day.value()) + '.' + \
                    months[self.month.currentText()] + '.' + \
                    '0' * (4 - len(str(self.year.value()))) + str(self.year.value())
            fl = 0
            if self.do_show.isChecked():
                fl = 1
            writer.writerow([self.namedit.text(), self.surnamedit.text(), self.sex_select.currentText(),
                             birth, self.seriaedit.text(), self.passport_numedit.text(),
                             self.lineEdit.text(), self.phone_edit.text(), self.mail_edit.text(), fl])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EnterInf()
    ex.show()
    sys.exit(app.exec())
