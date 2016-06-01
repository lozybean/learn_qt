#!/usr/bin/env python
# -*- coding: utf-8 -*- \#
"""
@author = 'liangzb'
@date = '2016/5/25 0025'

"""

import sys
from decimal import Decimal
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Screen(QLCDNumber):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setDigitCount(12)


class KeyBoard(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.value = None
        grid = QGridLayout()
        grid.setSpacing(1)
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']
        positions = [
            (i, j)
            for i in range(5)
            for j in range(4)
            ]
        self.buttons = {}
        for position, name in zip(positions, names):
            if name:
                button = QPushButton(name)
                self.buttons[name] = button
                grid.addWidget(button, *position)
        self.setLayout(grid)

    def value_increase(self, num):
        value = Decimal(str(self.value))
        value_int = int(value)
        value_fractional = value - value_int
        if self.int_part:
            value_int *= 10
            value_int += num
            value = value_int + value_fractional
            self.value = value
        else:
            value_fractional += Decimal(10) ** (int(value_fractional.log10()) - Decimal(2)) * num
            value = value_int + value_fractional
            self.value = value

    def slots(self, keyname):
        def slot():
            try:
                n = int(keyname)
                self.value_increase(n)
            except ValueError:
                if keyname == '.':
                    self.int_part = False

        return slot


class CentralWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)
        grid = QGridLayout()
        grid.setSpacing(10)
        # self.parent = parent
        self.screen = Screen(self)
        self.screen.resize(400, 50)
        self.screen.move(0, 0)
        grid.addWidget(self.screen, 0, 0, 1, 0)

        self.keyboard = KeyBoard(self)
        self.keyboard.resize(400, 350)
        self.keyboard.move(0, 50)
        grid.addWidget(self.keyboard, 1, 0, 5, 0)

        self.setLayout(grid)
        self.resize(400, 400)
        self.show()

    def display(self):
        self.screen.display(self.parent().num)


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.num = 0
        self.setCentralWidget(CentralWidget(self))
        self.resize(self.centralWidget().width(),
                    self.centralWidget().height())
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    sys.exit(app.exec_())
