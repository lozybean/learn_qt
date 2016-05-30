#!/usr/bin/env python
# -*- coding: utf-8 -*- \#
"""
@author = 'liangzb'
@date = '2016/5/25 0025'

"""

import sys
from time import strftime
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.lcd = QLCDNumber(self)
        self.lcd.move(0, 30)

        self.timer = QTimer(self)
        self.init_timer()

        self.r1 = QRadioButton("Hide seconds", self)
        self.r2 = QRadioButton("Show secends", self)
        self.init_radio()

        self.setWindowTitle("simple clock")

        self.show()

    def init_timer(self):
        self.timer.timeout.connect(self.display)
        self.timer.start(1)

    def init_radio(self):
        self.r1.move(10, 0)
        self.r1.toggled.connect(self.display_without_sec)

        self.r2.move(150, 0)
        self.r2.toggled.connect(self.display_with_sec)

        self.r1.toggle()

    @pyqtSlot()
    def display(self):
        if self.with_sec:
            self.lcd.display(strftime("%H:%M:%S"))
        else:
            self.lcd.display(strftime("%H:%M"))

    @pyqtSlot()
    def display_with_sec(self):
        self.with_sec = True
        self.resize(375, 130)
        self.lcd.resize(375, 100)
        self.lcd.setDigitCount(8)

    @pyqtSlot()
    def display_without_sec(self):
        self.with_sec = False
        self.resize(250, 130)
        self.lcd.resize(250, 100)
        self.lcd.setDigitCount(5)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_window = MyMainWindow()
    sys.exit(app.exec_())
