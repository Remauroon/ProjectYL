from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QTableWidget, QPushButton
from PyQt5.QtWidgets import QLineEdit, QLabel, QMainWindow, QDialog
import sys
from PyQt5 import uic
import add_member, view_list


class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main_menu.ui', self)
        self.setWindowTitle('Information Base')
        self.addmember.clicked.connect(self.add)
        self.memberslist.clicked.connect(self.view)

    def add(self):
        window = add_member.EnterInf()
        window.setWindowTitle('Add to list')
        window.show()
        window.exec_()

    def view(self):
        window = view_list.ViewWindow()
        window.setWindowTitle('List viewer')
        window.show()
        window.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainView()
    ex.show()
    sys.exit(app.exec())
