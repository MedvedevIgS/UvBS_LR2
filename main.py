from PyQt6 import uic, QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtGui import QIntValidator, QDoubleValidator
import sys
#import networkx as nx
#import matplotlib.pyplot as plt

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("FormApp.ui", self)
        self.kolV.setValidator(QIntValidator())
        self.MatrBut.clicked.connect(self.makeMatr)
        self.loadBut.clicked.connect(self.loadMatr)
        self.Error.setVisible(False)
        self.K=0

    def loadMatr(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'Data\ ', '(*.txt)')
        f = open(fname[0], 'r')
        Data = f.read()
        f.close()
        Data = Data.split('\n')
        for i in range(len(Data)):
            Data[i] = Data[i].split(' ')
        for i in Data:
            print(i)
        self.K=len(Data)
        print(self.K)
        self.kolV.setText(str(self.K))
        self.MatrA.setRowCount(self.K)
        self.MatrA.setColumnCount(self.K)
        h = 30 + 30 * self.K
        w = 26 + 52 * self.K
        self.MatrA.resize(QtCore.QSize(w, h))
        for i in range(self.K):
            self.MatrA.setColumnWidth(i, 1)
        for i in range(int(self.MatrA.rowCount())):
            for j in range(int(self.MatrA.columnCount())):
                LineA = QtWidgets.QLineEdit()
                if i == j:
                    LineA.setText('0')
                else:
                    LineA.setText('-')
                LineA.setValidator(QIntValidator())
                self.MatrA.setCellWidget(i, j, LineA)
        for i in range(self.K):
            for j in range(self.K):
                self.MatrA.cellWidget(i, j).setText(Data[i][j])



    def makeMatr(self):
        if self.kolV.text() != '':
            if int(self.kolV.text()) > 0:
                self.Error.setVisible(False)
                self.Error.setText('')
                self.K = int(self.kolV.text())
                self.MatrA.setRowCount(self.K)
                self.MatrA.setColumnCount(self.K)
                h = 30 + 30 * self.K
                w = 26 + 52 * self.K
                self.MatrA.resize(QtCore.QSize(w, h))
                for i in range(self.K):
                    self.MatrA.setColumnWidth(i, 1)
                for i in range(int(self.MatrA.rowCount())):
                    for j in range(int(self.MatrA.columnCount())):
                        LineA = QtWidgets.QLineEdit()
                        if i==j:
                            LineA.setText('0')
                        else:
                            LineA.setText('-')
                        LineA.setValidator(QIntValidator())
                        self.MatrA.setCellWidget(i, j, LineA)
            else:
                self.Error.setVisible(True)
                self.Error.setText('Введите число больше 0')
        else:
            self.Error.setVisible(True)
            self.Error.setText('Введите колличество вершин')

def application():
    app=QApplication(sys.argv)
    window=MainWindow()
    widget=QtWidgets.QStackedWidget()
    widget.addWidget(window)
    widget.setMinimumWidth(1050)
    widget.setMinimumHeight(680)
    widget.show()
    app.exec()

if __name__ == "__main__":
    application()