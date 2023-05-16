from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
from qt_material import apply_stylesheet
import re
import math

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
        self.fact = QtWidgets.QPushButton('n!')
        self.step = QtWidgets.QPushButton('x^y')
        self.eee = QtWidgets.QPushButton('e')
        self.tenX = QtWidgets.QPushButton('10^x')
        self.viktor = QtWidgets.QPushButton('√x')
        self.modul = QtWidgets.QPushButton('|x|')
        self.ln = QtWidgets.QPushButton('ln')

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
        self.dot.clicked.connect(self.dotq)
        self.erase.clicked.connect(self.erasing)
        self.equals.clicked.connect(self.ravno)
        self.expand.clicked.connect(self.inginer)

        self.firsk.clicked.connect(self.skob1)
        self.secsk.clicked.connect(self.skob2)
        self.fact.clicked.connect(self.fakt)
        self.step.clicked.connect(self.stepen)
        self.pi.clicked.connect(self.ps)
        self.eee.clicked.connect(self.eeee)
        self.tenX.clicked.connect(self.tenstep)
        self.viktor.clicked.connect(self.koren)
        self.modul.clicked.connect(self.moduul)
        self.ln.clicked.connect(self.lnn)

        self.setLayout(self.screenlayout)

    def inginer(self):
        self.mainlayout.addWidget(self.firsk, 1, 4)
        self.mainlayout.addWidget(self.secsk, 1, 5)
        self.mainlayout.addWidget(self.fact, 2, 4)
        self.mainlayout.addWidget(self.step, 2, 5)
        self.mainlayout.addWidget(self.pi, 3, 4)
        self.mainlayout.addWidget(self.eee, 3, 5)
        self.mainlayout.addWidget(self.tenX, 4, 4)
        self.mainlayout.addWidget(self.viktor, 4, 5)
        self.mainlayout.addWidget(self.modul, 5, 4)
        self.mainlayout.addWidget(self.ln, 5, 5)

    def lnn(self):
        i = float(self.screen.text())
        j = math.log(i, 2.7182818284)
        self.screen.setText(str(j))

    def moduul(self):
        i = float(self.screen.text())
        if i <= -1:
            i *= -1
            self.screen.setText(str(i))
        else:
            return

    def koren(self):
        i = float(self.screen.text())
        j = math.sqrt(i)
        self.screen.setText(str(j))

    def tenstep(self):
        if len(self.screen.text()) < 1:
            return
        else:
            i = float(self.screen.text())
            j = i**10
            self.screen.setText(str(j))


    def eeee(self):
        self.screen.setText('2.7182818284')

    def ps(self):
        i = str(math.pi)
        self.screen.setText(i)

    def stepen(self):
        if len(self.screen.text()) < 1:
            return
        else:
            self.screen.setText(self.screen.text() + "**")

    def skob1(self):
        self.screen.setText(self.screen.text() + '(')

    def skob2(self):
        self.screen.setText(self.screen.text() + ')')

    def fakt(self):
        if len(self.screen.text()) < 1:
            return
        try:
            i = int(self.screen.text())
            i = math.factorial(i)
            self.screen.setText(str(i))
        except ValueError:
            QtWidgets.QMessageBox.about(QtWidgets.QWidget(), "Ошибка", "невозможно высчитать факториал")
            return
        except OverflowError:
            QtWidgets.QMessageBox.about(QtWidgets.QWidget(), "Ошибка", "число слишком большое, калькулятору плохо")

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
            self.screen.setText("-")
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
        elif text.count('(') != text.count(')'):
            QtWidgets.QMessageBox.about(QtWidgets.QWidget(), "Ошибка", "Имеется незакрытая скобка")
            return
        try:
            self.screen.setText(str(eval(self.screen.text())))
        except ZeroDivisionError:
            QtWidgets.QMessageBox.about(QtWidgets.QWidget(), "Ошибка", "деление на ноль невозможно")
            return

if __name__ == "__main__":
    from sys import argv, exit
    app = QtWidgets.QApplication(argv)
    apply_stylesheet(app, theme='dark_cyan.xml')
    window = MyWindow()
    window.setObjectName("MainWindow")
    window.show()

    exit(app.exec_())
