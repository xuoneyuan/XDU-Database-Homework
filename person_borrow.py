import psycopg2
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
import sys

class LibraryApp(QWidget):

    def __init__(self, parent=None):
        super(LibraryApp, self).__init__(parent)
        self.setWindowTitle('图书馆借还书系统')
        self.resize(300, 200)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.internalStaffIDLineEdit = QLineEdit()
        self.internalStaffNameLineEdit = QLineEdit()
        self.externalStaffIDLineEdit = QLineEdit()
        self.externalStaffNameLineEdit = QLineEdit()
        self.internalStaffInsertButton = QPushButton('插入内部人员')
        self.internalStaffDeleteButton = QPushButton('删除内部人员')
        self.externalStaffRegisterButton = QPushButton('登记外部人员')

        layout.addWidget(QLabel('内部人员信息'))
        layout.addWidget(QLabel('ID Number:'))
        layout.addWidget(self.internalStaffIDLineEdit)
        layout.addWidget(QLabel('Full Name:'))
        layout.addWidget(self.internalStaffNameLineEdit)
        layout.addWidget(self.internalStaffInsertButton)
        layout.addWidget(self.internalStaffDeleteButton)
        layout.addWidget(QLabel('外部人员信息'))
        layout.addWidget(QLabel('ID Number:'))
        layout.addWidget(self.externalStaffIDLineEdit)
        layout.addWidget(QLabel('Full Name:'))
        layout.addWidget(self.externalStaffNameLineEdit)
        layout.addWidget(self.externalStaffRegisterButton)

        self.setLayout(layout)

        self.internalStaffInsertButton.clicked.connect(self.insertInternalStaff)
        self.internalStaffDeleteButton.clicked.connect(self.deleteInternalStaff)
        self.externalStaffRegisterButton.clicked.connect(self.registerExternalStaff)

    def insertInternalStaff(self):
        id_number = self.internalStaffIDLineEdit.text()
        full_name = self.internalStaffNameLineEdit.text()

        if id_number and full_name:
            gConn = psycopg2.connect(host="127.0.0.1", port="54321", user="system", password="123", database="test")

            if gConn:
                print("Connected to the database")

            cur = gConn.cursor()
            cur.execute(f"INSERT INTO internal_staff (ID_number, full_name) VALUES ('{id_number}', '{full_name}')")
            gConn.commit()

            cur.close()
            gConn.close()

            self.internalStaffIDLineEdit.clear()
            self.internalStaffNameLineEdit.clear()

    def deleteInternalStaff(self):
        id_number = self.internalStaffIDLineEdit.text()

        if id_number:
            gConn = psycopg2.connect(host="127.0.0.1", port="54321", user="system", password="123", database="test")

            if gConn:
                print("Connected to the database")

            cur = gConn.cursor()
            cur.execute(f"DELETE FROM internal_staff WHERE ID_number = '{id_number}'")
            gConn.commit()

            cur.close()
            gConn.close()

            self.internalStaffIDLineEdit.clear()

    def registerExternalStaff(self):
        id_number = self.externalStaffIDLineEdit.text()
        full_name = self.externalStaffNameLineEdit.text()

        if id_number and full_name:
            gConn = psycopg2.connect(host="127.0.0.1", port="54321", user="system", password="123", database="test")

            if gConn:
                print("Connected to the database")

            cur = gConn.cursor()
            cur.execute(f"INSERT INTO external_staff (ID_number, full_name) VALUES ('{id_number}', '{full_name}')")
            gConn.commit()

            cur.close()
            gConn.close()

            self.externalStaffIDLineEdit.clear()
            self.externalStaffNameLineEdit.clear()

if __name__ == '__main__':
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    win = LibraryApp()
    win.show()

    sys.exit(app.exec_())
