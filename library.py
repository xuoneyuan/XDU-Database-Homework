#导入了psycopg2用于与数据库进行交互
import psycopg2
from PyQt5.QtWidgets import QListWidget, QApplication, QLineEdit, QWidget, QFormLayout, QPushButton
import sys
#创建应用程序主窗口类 LibraryApp
class LibraryApp(QWidget):
    def __init__(self, parent=None):
        super(LibraryApp, self).__init__(parent)
        self.setWindowTitle('图书馆借还书系统')
        self.resize(800, 600)

        self.initUI()
#初始化界面
    def initUI(self):
        layout = QFormLayout()

        self.isbnLineEdit = QLineEdit()
        self.bookNameLineEdit = QLineEdit()
        self.pressLineEdit = QLineEdit()
        self.authorLineEdit = QLineEdit()
        self.classificationLineEdit = QLineEdit()
        self.yearLineEdit = QLineEdit()
        self.quantityLineEdit = QLineEdit()

        self.insertButton = QPushButton('插入图书')
        self.searchButton = QPushButton('查询图书')
        self.deleteButton = QPushButton('删除图书')

        self.bookList = QListWidget()

        self.insertButton.clicked.connect(self.insertBook)
        self.searchButton.clicked.connect(self.searchBooks)
        self.deleteButton.clicked.connect(self.deleteBook)

        layout.addRow('ISBN', self.isbnLineEdit)
        layout.addRow('图书名称', self.bookNameLineEdit)
        layout.addRow('出版社', self.pressLineEdit)
        layout.addRow('作者', self.authorLineEdit)
        layout.addRow('图书分类', self.classificationLineEdit)
        layout.addRow('出版年份', self.yearLineEdit)
        layout.addRow('剩余数量', self.quantityLineEdit)
        layout.addRow(self.insertButton)
        layout.addRow(self.searchButton)
        layout.addRow(self.deleteButton)
        layout.addRow('图书列表', self.bookList)

        self.setLayout(layout)
#查询图书函数
    def searchBooks(self):
        self.bookList.clear()

        gConn = psycopg2.connect(host="127.0.0.1", port="54321", user="system", password="123", database="test")

        if gConn:
            print("Connected to the database")

        cur = gConn.cursor()
        cur.execute("SELECT * FROM book")
        rows = cur.fetchall()
        for row in rows:
            self.bookList.addItem(f"ISBN: {row[0]}, BookName: {row[1]}, Publisher: {row[2]}, Author: {row[3]}, "
                                  f"Category: {row[4]}, PublicationYear: {row[5]}, RemainingQuantity: {row[6]}")
        cur.close()

        gConn.close()
#插入图书函数
    def insertBook(self):
        isbn = self.isbnLineEdit.text()
        book_name = self.bookNameLineEdit.text()
        press = self.pressLineEdit.text()
        author = self.authorLineEdit.text()
        classification = self.classificationLineEdit.text()
        year = self.yearLineEdit.text()
        quantity = self.quantityLineEdit.text()
        # 连接数据库，提交事务
        gConn = psycopg2.connect(host="127.0.0.1", port="54321", user="system", password="123", database="test")

        if gConn:
            print("Connected to the database")

        cur = gConn.cursor()
        cur.execute(f"INSERT INTO book (ISBN, book_name, press, author, book_classification, year_of_publication, remaining_quantity) "
                    f"VALUES ('{isbn}', '{book_name}', '{press}', '{author}', '{classification}', '{year}', {quantity})")
        gConn.commit()

        cur.close()
        gConn.close()

        self.isbnLineEdit.clear()
        self.bookNameLineEdit.clear()
        self.pressLineEdit.clear()
        self.authorLineEdit.clear()
        self.classificationLineEdit.clear()
        self.yearLineEdit.clear()
        self.quantityLineEdit.clear()

        self.searchBooks()
#删除图书函数
    def deleteBook(self):
        selected_item = self.bookList.currentItem()
        if selected_item is not None:
            book_info = selected_item.text()
            isbn = book_info.split("ISBN: ")[1].split(",")[0]

            gConn = psycopg2.connect(host="localhost", port="54321", user="system", password="123", database="test")

            if gConn:
                print("Connected to the database")

            cur = gConn.cursor()
            cur.execute(f"DELETE FROM book WHERE ISBN = '{isbn}'")
            gConn.commit()

            cur.close()
            gConn.close()

            self.bookList.takeItem(self.bookList.row(selected_item))
#主程序
if __name__ == '__main__':
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    win = LibraryApp()
    win.show()

    sys.exit(app.exec_())
