from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
import sys

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("checklist.ui", self)
        to_do_lists = ["First", "Second", "Third", "Fourth"]
        for todo in to_do_lists:
            item = QListWidgetItem(todo)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            self.todo_listWidget.addItem(item)
        self.toggle_all_button.clicked.connect(self.toggle_all)

    def toggle_all(self):
        for i in range(self.todo_listWidget.count()):
            item = self.todo_listWidget.item(i)
            if item.checkState() == Qt.Checked:
                item.setCheckState(Qt.Unchecked)
            else:
                item.setCheckState(Qt.Checked)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()