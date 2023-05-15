from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
import re

class MyWindow(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setWindowTitle("калькулятор")
        self.resize(400, 500)

        self.screen = QtWidgets.QLabel('')
        self.btn = QtWidgets.QPushButton('0')
        self.btn1 = QtWidgets.QPushButton('1')
        self.btn2 = QtWidgets.QPushButton('2')
        self.btn3 = QtWidgets.QPushButton('3')
        self.btn4 = QtWidgets.QPushButton('4')
        self.btn5 = QtWidgets.QPushButton('5')
        self.btn6 = QtWidgets.QPushButton('6')
        self.btn7 = QtWidgets.QPushButton('7')
        self.btn8 = QtWidgets.QPushButton('8')
        self.btn9 = QtWidgets.QPushButton('9')
        self.dot = QtWidgets.QPushButton(',')
        self.equals = QtWidgets.QPushButton('=')
        self.plus = QtWidgets.QPushButton('+')
        self.minus = QtWidgets.QPushButton('-')
        self.multiply = QtWidgets.QPushButton('*')
        self.divide = QtWidgets.QPushButton('/')
        self.erase = QtWidgets.QPushButton('<-')
        self.percent = QtWidgets.QPushButton('+/-')
        self.clear = QtWidgets.QPushButton('C')
        self.expand = QtWidgets.QPushButton('ƒx')

        self.firsk = QtWidgets.QPushButton('(')
        self.secsk = QtWidgets.QPushButton(')')
        self.pi = QtWidgets.QPushButton('π')


        # self.btn.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        # self.btn1.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        # self.btn2.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        # self.btn3.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        # self.btn4.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        # self.btn5.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        # self.btn6.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        # self.btn7.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        # self.btn8.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        # self.btn9.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        # self.dot.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        # self.equals.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        # self.plus.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        # self.minus.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        # self.multiply.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        # self.divide.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        # self.erase.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        # self.percent.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        # self.clear.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        # self.expand.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        # self.screen.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        self.mainlayout = QtWidgets.QGridLayout()

        self.screenlayout = QtWidgets.QVBoxLayout()
        self.screenlayout.addWidget(self.screen)
        self.screenlayout.addLayout(self.mainlayout)

        self.mainlayout.addWidget(self.btn1, 2, 0)
        self.mainlayout.addWidget(self.btn2, 2, 1)
        self.mainlayout.addWidget(self.btn3, 2, 2)
        self.mainlayout.addWidget(self.btn4, 3, 0)
        self.mainlayout.addWidget(self.btn5, 3, 1)
        self.mainlayout.addWidget(self.btn6, 3, 2)
        self.mainlayout.addWidget(self.btn7, 4, 0)
        self.mainlayout.addWidget(self.btn8, 4, 1)
        self.mainlayout.addWidget(self.btn9, 4, 2)
        self.mainlayout.addWidget(self.expand, 5, 0)
        self.mainlayout.addWidget(self.btn, 5, 1)
        self.mainlayout.addWidget(self.dot, 5, 2)
        self.mainlayout.addWidget(self.equals, 5, 3)
        self.mainlayout.addWidget(self.plus, 4, 3)
        self.mainlayout.addWidget(self.minus, 3, 3)
        self.mainlayout.addWidget(self.multiply, 2, 3)
        self.mainlayout.addWidget(self.divide, 1, 3)
        self.mainlayout.addWidget(self.erase, 1, 2)
        self.mainlayout.addWidget(self.percent, 1, 1)
        self.mainlayout.addWidget(self.clear, 1, 0)

        self.btn.clicked.connect(self.zerobtn)
        self.btn1.clicked.connect(self.onebtn)
        self.btn2.clicked.connect(self.twobtn)
        self.btn3.clicked.connect(self.threebtn)
        self.btn4.clicked.connect(self.fourbtn)
        self.btn5.clicked.connect(self.fivebtn)
        self.btn6.clicked.connect(self.sixbtn)
        self.btn7.clicked.connect(self.sevenbtn)
        self.btn8.clicked.connect(self.eightbtn)
        self.btn9.clicked.connect(self.ninebtn)
        self.clear.clicked.connect(self.clearing)
        self.plus.clicked.connect(self.plusing)
        self.minus.clicked.connect(self.minusing)
        self.multiply.clicked.connect(self.multy)
        self.divide.clicked.connect(self.delit)
        #self.percent.clicked.connect(self.plusminus)
        self.dot.clicked.connect(self.dotq)
        self.erase.clicked.connect(self.erasing)
        self.equals.clicked.connect(self.ravno)
        self.expand.clicked.connect(self.inginer)

        self.setLayout(self.screenlayout)

    def inginer(self):
        self.mainlayout.addWidget(self.firsk, 1, 4)
        self.mainlayout.addWidget(self.secsk, 1, 5)

    

    def zerobtn(self):
        text = self.screen.text()
        self.screen.setText(text + '0')
        self.zerocheck()

    def onebtn(self):
        text = self.screen.text()
        self.screen.setText(text + '1')
        self.zerocheck()

    def twobtn(self):
        text = self.screen.text()
        self.screen.setText(text + '2')
        self.zerocheck()

    def threebtn(self):
        text = self.screen.text()
        self.screen.setText(text + '3')


    def fourbtn(self):
        text = self.screen.text()
        self.screen.setText(text + '4')
        self.zerocheck()

    def fivebtn(self):
        text = self.screen.text()
        self.screen.setText(text + '5')
        self.zerocheck()

    def sixbtn(self):
        text = self.screen.text()
        self.screen.setText(text + '6')
        self.zerocheck()

    def sevenbtn(self):
        text = self.screen.text()
        self.screen.setText(text + '7')
        self.zerocheck()

    def eightbtn(self):
        text = self.screen.text()
        self.screen.setText(text + '8')
        self.zerocheck()

    def ninebtn(self):
        text = self.screen.text()
        self.screen.setText(text + '9')
        self.zerocheck()

    def clearing(self):
        self.screen.setText('')

    def zerocheck(self):
        text = self.screen.text()
        podtext = re.split("[-/+*]", text)
        lenP = len(podtext)
        j = podtext[lenP - 1]
        if len(text) == 2:
            if (self.screen.text()[0] == '0') and (self.screen.text()[1] != '.'):
                i = self.screen.text().replace('0', '', 1)
                self.screen.setText(i)
        elif len(j) > 1:
            if (j[0] == '0') and (j[1] != '.'):
                self.screen.setText(text[:-1])

    def znakcheck(self):
        text = self.screen.text()
        if text.count('[+-/*]') > 1:
            if text[-1] in {'-', '+', '*', '/'}:
                i = text[:-1]
                self.screen.setText(i)

    def erasing(self):
        i = self.screen.text()
        self.screen.setText(i[:-1])

    def dotq(self):
        text = self.screen.text()
        if len(text) == 0:
            return None
        else:
            self.screen.setText(text + '.')
            self.dotcheck()

    def dotcheck(self):
        text = self.screen.text()
        podtext = re.split("[-/+*]", text)
        lenP = len(podtext) - 1
        j = podtext[lenP]
        if j.count('.') > 1:
            self.screen.setText(text[:-1])
        if len(text) >= 2 and text[-2] in {'-', '+', '*', '/'} and text[-1] == '.':
            self.screen.setText(text[:-1])
    def plusing(self):
        qwe = len(self.screen.text())
        if len(self.screen.text()) == 0:
            return
        elif self.screen.text()[qwe - 1] == '+':
            return
        else:
            text = self.screen.text()
            if len(text) >= 1 and text[-1] in {'-', '+', '*', '/'}:
                text = text[:-1]
            self.screen.setText(text + "+")

    def minusing(self):
        qwe = len(self.screen.text())
        if len(self.screen.text()) == 0:
            return
        elif self.screen.text()[qwe - 1] == "-":
            return
        else:
            text = self.screen.text()
            if len(text) >= 1 and text[-1] in {'-', '+', '*', '/'}:
                text = text[:-1]
            self.screen.setText(text + "-")

    def multy(self):
        qwe = len(self.screen.text())
        if len(self.screen.text()) == 0:
            return
        elif self.screen.text()[qwe - 1] == "*":
            return
        else:
            text = self.screen.text()
            if len(text) >= 1 and text[-1] in {'-', '+', '*', '/'}:
                text = text[:-1]
            self.screen.setText(text + "*")

    def delit(self):
        qwe = len(self.screen.text())
        if len(self.screen.text()) == 0:
            return
        elif self.screen.text()[qwe - 1] == "/":
            return
        else:
            text = self.screen.text()
            if len(text) >= 1 and text[-1] in {'-', '+', '*', '/'}:
                text = text[:-1]
            self.screen.setText(text + "/")

    def ravno(self):
        text = self.screen.text()
        if len(text) < 1:
            return
        elif text[-1] in {'-', '+', '*', '/'}:
            return
        self.screen.setText(str(eval(self.screen.text())))


if __name__ == "__main__":
    from sys import argv, exit
    app = QtWidgets.QApplication(argv)
    window = MyWindow()
    window.setObjectName("MainWindow")
    window.show()

    exit(app.exec_())
