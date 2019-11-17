import sys
import sqlite3
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidgetItem


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle('coffee')
        con = sqlite3.connect('coffee.db')
        cur = con.cursor()
        rows = cur.execute("""SELECT * FROM coffee""").fetchall()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах',
                                                    'описание вкуса', 'цена', 'объем упаковки'])
        for row in rows:
            inx = rows.index(row)
            self.tableWidget.insertRow(inx)
            for i in range(7):
                item = str(row[i])
                cellinfo = QTableWidgetItem(item)
                # Только для чтения
                cellinfo.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(inx, i, QTableWidgetItem(cellinfo))
        self.tableWidget.resizeColumnsToContents()
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec_())
