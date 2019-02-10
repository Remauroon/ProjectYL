from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QTableWidget, QPushButton
from PyQt5.QtWidgets import QLineEdit, QLabel, QMainWindow, QDialog
import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
import csv


PASSWORD = "projectYL"


class ViewWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('view_list.ui', self)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setSortingEnabled(True)
        n = 1
        self.tableWidget.setHorizontalHeaderLabels(["Name", "Surname", "Sex", "Date of birth", "Passport series",
                                                    "Passport №", "Place of registration", "Phone number", "E-mail"])
        for i in range(9):
            self.tableWidget.resizeColumnToContents(i)
        csvfile = open('list.csv', encoding='utf8', mode='r')
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')
        self.view = [0]
        for index, row in enumerate(reader):
            if index > 0:
                if index > 1:
                    self.view.append(0)
                    self.tableWidget.setRowCount(n + 1)
                    n += 1
                for i in range(9):
                    if row[-1] == '1' or i in [0, 1, 2, 3] or self.showflag.isChecked():
                        if row[i] != '' and not (i == 7 and row[i] == '+7'):
                            self.tableWidget.setItem(index - 1, i, QTableWidgetItem(row[i]))
                        else:
                            self.tableWidget.setItem(index - 1, i, QTableWidgetItem('unspecified'))
                    else:
                        if row[i] != '' and not (i == 7 and row[i] == '+7'):
                            self.tableWidget.setItem(index - 1, i, QTableWidgetItem('specified'))
                        else:
                            self.tableWidget.setItem(index - 1, i, QTableWidgetItem('unspecified'))
                    self.tableWidget.resizeColumnToContents(i)
        self.Search.clicked.connect(self.change_view)
        self.current = ''
        self.showflag.stateChanged.connect(self.control)

        self.remove.clicked.connect(self.remove_member)
        self.lable9 = QLabel(self)
        self.lable9.setText('')

    def change_view(self):
        charge = {
            'Name': 0,
            'Surname': 1,
            'Sex': 2,
            'Date of birth': 3,
            'Passport series': 4,
            'Passport №': 5,
            'Place of registration': 6,
            'Phone number': 7,
            'E-mail': 8
        }
        k = 0
        self.tableWidget.setRowCount(0)
        n = 0
        csvfile = open('list.csv', encoding='utf8')
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')
        m = 1
        for index, row in enumerate(reader):
            print(self.current)
            if index > 0 and (row[charge[self.vars.currentText()]] == str(self.entername.text())
                              or self.entername.text() == ''):
                self.tableWidget.setRowCount(n + 1)
                n += 1
                if not self.view[index - 1]:
                    for i in range(9):
                        if row[-1] == '1' or i in [0, 1, 2, 3] or self.showflag.isChecked():
                            if row[i] != '' and not (i == 7 and row[i] == '+7'):
                                self.tableWidget.setItem(index - 1, i, QTableWidgetItem(row[i]))
                            else:
                                self.tableWidget.setItem(index - 1, i, QTableWidgetItem('unspecified'))
                        else:
                            if row[i] != '' and not (i == 7 and row[i] == '+7'):
                                self.tableWidget.setItem(m - 1, i, QTableWidgetItem('specified'))
                            else:
                                self.tableWidget.setItem(m - 1, i, QTableWidgetItem('unspecified'))
                        self.tableWidget.resizeColumnToContents(i)
                    m += 1
        self.tableWidget.setRowCount(m - 1)

    def setvalue(self, text):
        self.current = text

    def control(self, state):
        if state == Qt.Checked:
            password = PasswordRequest()
            password.show()
            password.exec_()
            if not password.exit():
                self.showflag.toggle()
                self.showflag.setCheckState(Qt.Unchecked)
            else:
                pass

    def remove_member(self):
        password = PasswordRequest()
        password.show()
        password.exec_()
        if password.exit():
            self.lable9.setText('')
            print(self.view)
            indices = self.tableWidget.selectionModel().selectedRows()
            for i in sorted(indices):
                self.view[i.row()] = 1
                self.tableWidget.removeRow(i.row())
        else:
            self.lable9.setText('Access is denied.')
            self.lable9.resize(self.lable9.sizeHint())
            self.lable9.move(670, 600)


class PasswordRequest(QDialog):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(820, 500, 230, 70)
        self.setWindowTitle('Enter password:')
        self.setWindowModality(Qt.ApplicationModal)

        self.line = QLineEdit(self)
        self.line.move(50, 10)

        self.but = QPushButton('OK', self)
        self.but.move(80, 40)
        self.but.resize(self.but.sizeHint())
        self.but.clicked.connect(self.exit)

    def exit(self):
        if self.line.text() == PASSWORD:
            print(1)
            self.close()
            print(1)
            return 1
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ViewWindow()
    ex.show()
    sys.exit(app.exec())
