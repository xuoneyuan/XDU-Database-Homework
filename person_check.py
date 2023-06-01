import psycopg2
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextBrowser
import sys

class LibraryApp(QWidget):

    def __init__(self, parent=None):
        super(LibraryApp, self).__init__(parent)
        self.setWindowTitle('图书馆借还书系统')
        self.resize(500, 400)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.internalStaffSearchButton = QPushButton('查询内部人员')
        self.externalStaffSearchButton = QPushButton('查询外部人员')

        self.internalStaffResult = QTextBrowser()
        self.externalStaffResult = QTextBrowser()

        layout.addWidget(QLabel('查询内部人员信息'))
        layout.addWidget(self.internalStaffSearchButton)
        layout.addWidget(self.internalStaffResult)

        layout.addWidget(QLabel('查询外部人员信息'))
        layout.addWidget(self.externalStaffSearchButton)
        layout.addWidget(self.externalStaffResult)

        self.setLayout(layout)

        self.internalStaffSearchButton.clicked.connect(self.searchInternalStaff)
        self.externalStaffSearchButton.clicked.connect(self.searchExternalStaff)

    def searchInternalStaff(self):
        gConn = psycopg2.connect(host="127.0.0.1", port="54321", user="system", password="123", database="test")

        if gConn:
            print("Connected to the database")

        cur = gConn.cursor()
        cur.execute("SELECT * FROM internal_staff")
        rows = cur.fetchall()

        result = ""
        for row in rows:
            result += f"ID Number: {row[0]}, Full Name: {row[1]}, Number of Books Borrowed: {row[2]}, Overdue: {row[3]}\n"

        self.internalStaffResult.setText(result)

        cur.close()
        gConn.close()

    def searchExternalStaff(self):
        gConn = psycopg2.connect(host="127.0.0.1", port="54321", user="system", password="123", database="test")

        if gConn:
            print("Connected to the database")

        cur = gConn.cursor()
        cur.execute("SELECT * FROM external_staff")
        rows = cur.fetchall()

        result = ""
        for row in rows:
            result += f"ID Number: {row[0]}, Full Name: {row[1]}, Number of Books Borrowed: {row[2]}, Overdue: {row[3]}\n"

        self.externalStaffResult.setText(result)

        cur.close()
        gConn.close()

if __name__ == '__main__':
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    win = LibraryApp()
    win.show()

    sys.exit(app.exec_())
