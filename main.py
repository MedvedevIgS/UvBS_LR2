from PyQt6 import uic, QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtGui import QIntValidator, QDoubleValidator, QPixmap
import sys
import os
#import networkx as nx
#import matplotlib.pyplot as plt
import graphviz as gr


def matrixTranspose(F):
    F_T = [[row[i] for row in F] for i in range(len(F[0]))]
    return F_T

class resWindow(QMainWindow):
    def __init__(self):
        super(resWindow, self).__init__()
        uic.loadUi("ResForm.ui", self)
        self.Graf1.setPixmap(QPixmap('Graf1.png'))
        self.Graf1.setScaledContents(True)
        self.Graf2.setPixmap(QPixmap('Graf2.png'))
        self.Graf2.setScaledContents(True)
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("FormApp.ui", self)
        self.kolV.setValidator(QIntValidator())
        self.MatrBut.clicked.connect(self.makeMatr)
        self.loadBut.clicked.connect(self.loadMatr)
        self.ResBut.clicked.connect(self.resMatr)
        self.AddBut.clicked.connect(self.addinMatr)
        self.DelBut.clicked.connect(self.delinMatr)
        self.Error.setVisible(False)
        self.K=0
        self.matrA_res=[]
        self.matrA_buf = []



    def addinMatr(self):
        if self.kolV.text()=='' or int(self.kolV.text())<0:
            self.kolV.setText('1')
        else:
            self.kolV.setText(str(int(self.kolV.text())+1))
        self.matrA_buf = self.zapisMatr(self.matrA_buf)
        self.makeMatr()

    def delinMatr(self):
        n=self.MatrA.currentRow()
        m = self.MatrA.currentColumn()
        if n == m or (n!=0 and m==0) or (m!=0 and n==0):
            self.Error.setVisible(False)
            self.Error.setText('')
            if m==0:
                print('Удаляем '+str(n))
                delV=n

            else:
                print('Удаляем ' + str(m))
                delV = m
            buf = []
            indB=0
            for i in range(len(self.matrA_buf)):
                if i != delV:
                    buf.append([])
                    for j in range(len(self.matrA_buf[i])):
                        if j!=delV:
                            buf[indB].append(self.matrA_buf[i][j])
                    indB += 1
            self.matrA_buf=buf
            self.K -= 1
            self.kolV.setText(str(self.K))
            self.makeMatr()

        else:
            self.Error.setVisible(True)
            self.Error.setText('Выделите одну вершину')

    def zapisMatr(self, matr):
        flag=True
        while flag:
            print(len(matr) < self.K)
            if len(matr) < self.K:
                for i in range(len(matr)):
                    matr[i].append('-')
                matr.append([])
                for i in range(len(matr)):
                    if i == len(matr) - 1:
                        matr[-1].append('0')
                    else:
                        matr[-1].append('-')
            else:
                flag = False
        for i in range(self.K):
            for j in range(self.K):
                matr[i][j]=self.MatrA.cellWidget(i, j).text()
        return matr

    def resMatr(self):
        self.matrA_res=[]
        for i in range(self.K):
            self.matrA_res.append([])
            for j in range(self.K):
                if i==j:
                    self.matrA_res[i].append('0')
                else:
                    self.matrA_res[i].append('-')
        self.matrA_res = self.zapisMatr(self.matrA_res)
        graf1='digraph G {\n'
        for i in range(self.K):
            for j in range(self.K):
                if self.matrA_res[i][j]!='0' and self.matrA_res[i][j]!='-':
                    graf1+=' '+str(i+1)+' -> '+str(j+1)+' [label="'+str(self.matrA_res[i][j])+'"];\n'
        graf1+='}'
        print(graf1)
        uprgraf= []
        for i in range(self.K):
            uprgraf.append({'name': str(i+1), 'input': [], 'output': [], 'level': 0})
        for i in range(self.K):
            out=[]
            for j in range(self.K):
                if self.matrA_res[i][j] != '0' and self.matrA_res[i][j] != '-':
                    out.append(j+1)
            uprgraf[i]['output']=out

        matrA_resT = matrixTranspose(self.matrA_res)

        for i in range(self.K):
            inp = []
            for j in range(self.K):
                if matrA_resT[i][j] != '0' and matrA_resT[i][j] != '-':
                    inp.append(j+1)
            uprgraf[i]['input'] = inp

        initV=[]
        level=0
        iV=1
        while iV <= self.K:
            initVi=[]
            for i in range(self.K):
                if set(uprgraf[i]['input']).issubset(initV) and not (i+1 in initV):
                    initVi.append(i+1)
                    uprgraf[i]['name']=str(iV)+'('+uprgraf[i]['name']+')'
                    uprgraf[i]['level']=level
                    iV+=1
            for i in range(len(initVi)):
                initV.append(initVi[i])
            level += 1

        graf2 = 'digraph G {\n'
        for i in range(self.K):
            graf2+=' v'+str(i)+' [label = "'+uprgraf[i]['name']+'"];\n'

        kolver=0
        level=0
        while kolver<len(uprgraf):
            graf2 += ' subgraph cluster_level'+str(level)+' {\n node [style=filled]\n'
            for i in range(self.K):
                if uprgraf[i]['level']==level:
                    graf2 += ' v'+str(i)+';'
                    kolver+=1
            graf2 += '\n label="Уровень '+str(level)+'";}\n'
            level+=1


        for i in range(self.K):
            for j in range(self.K):
                if self.matrA_res[i][j]!='0' and self.matrA_res[i][j]!='-':
                    graf2+=' v'+str(i)+' -> v'+str(j)+' [label="'+str(self.matrA_res[i][j])+'"];\n'
        graf2 += '}'
        print(graf1)
        os.remove('Graf1.png')
        os.remove('Graf2.png')
        grap1_view = gr.Source(graf1)
        grap1_view.render(filename='Graf1', format='png')
        grap2_view = gr.Source(graf2)
        grap2_view.render(filename='Graf2', format='png')
        os.remove('Graf1')
        os.remove('Graf2')
        global widget2
        Res = resWindow()
        widget2 = QtWidgets.QStackedWidget()
        widget2.addWidget(Res)
        widget2.setMinimumWidth(920)
        widget2.setMinimumHeight(690)
        widget2.show()
        for i in uprgraf:
            print(i)


    def loadMatr(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'Data\ ', '(*.txt)')
        if fname!=('', ''):
            f = open(fname[0], 'r')
            Data = f.read()
            f.close()
            self.loadMatr_1(Data)

    def loadMatr_1(self, Data):
        Data = Data.split('\n')
        for i in range(len(Data)):
            Data[i] = Data[i].split(' ')
        self.K=len(Data)
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
                LineA.setValidator(QIntValidator())
                self.MatrA.setCellWidget(i, j, LineA)
        for i in range(self.K):
            for j in range(self.K):
                self.MatrA.cellWidget(i, j).setText(Data[i][j])
        self.matrA_buf=self.zapisMatr(self.matrA_buf)



    def makeMatr(self):
        if self.kolV.text() != '':
            if int(self.kolV.text()) > 0:
                if self.matrA_buf!=[]:
                    flagBuf=True
                else:
                    flagBuf = False
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
                if not flagBuf:
                    for i in range(int(self.MatrA.rowCount())):
                        for j in range(int(self.MatrA.columnCount())):
                            LineA = QtWidgets.QLineEdit()
                            if i == j:
                                LineA.setText('0')
                            else:
                                LineA.setText('-')
                            LineA.setValidator(QIntValidator())
                            self.MatrA.setCellWidget(i, j, LineA)
                else:
                    for i in range(len(self.matrA_buf)):
                        for j in range(len(self.matrA_buf)):
                            LineA = QtWidgets.QLineEdit()
                            LineA.setText(self.matrA_buf[i][j])
                            LineA.setValidator(QIntValidator())
                            self.MatrA.setCellWidget(i, j, LineA)

                    for i in range(int(self.MatrA.rowCount())):
                        for j in range(int(self.MatrA.columnCount())):
                            if j>=len(self.matrA_buf) or i>=len(self.matrA_buf):
                                LineA = QtWidgets.QLineEdit()
                                if i == j:
                                    LineA.setText('0')
                                else:
                                    LineA.setText('-')
                                LineA.setValidator(QIntValidator())
                                self.MatrA.setCellWidget(i, j, LineA)
                self.matrA_buf = self.zapisMatr(self.matrA_buf)

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
    widget.setMinimumHeight(720)
    widget.show()
    app.exec()

if __name__ == "__main__":
    application()