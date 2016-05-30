#!/usr/bin/env python
# -*- coding: utf-8 -*- \#
"""
@author = 'liangzb'
@date = '2016/5/25 0025'

"""
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.lcd = QLCDNumber(self)

        sld = QSlider(Qt.Horizontal, self)
        sld.setMinimum(0)
        sld.setMaximum(99999)
        sld.valueChanged.connect(self.lcd.display)
        self.sld = sld

        self.num = self.sld.minimum()

        self.lcd.display(self.num)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lcd)
        vbox.addWidget(self.sld)
        self.setLayout(vbox)

    def set_num(self, value):
        if value > self.sld.maximum():
            pass
        else:
            self.__num = value
            self.sld.setValue(value)

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, value):
        self.set_num(value)


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setCentralWidget(MyWidget())
        self.centralWidget().sld.sliderPressed.connect(self.slider_drags)
        self.centralWidget().sld.sliderMoved.connect(self.slider_move)
        self.centralWidget().sld.sliderReleased.connect(self.slider_release)

    def init_ui(self):
        self.resize(800, 600)
        self.setWindowTitle('Signal & Slot')
        self.statusBar().showMessage('请拖动滑条...')
        self.show()

    @pyqtSlot()
    def slider_drags(self):
        self.statusBar().showMessage('准备拖动...')

    @pyqtSlot()
    def slider_move(self):
        self.statusBar().showMessage('拖动中...')

    @pyqtSlot()
    def slider_release(self):
        self.statusBar().showMessage('请再次拖动滑条...')

    # rewrite event
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.centralWidget().num = 0
        if Qt.Key_0 <= e.key() <= Qt.Key_9:
            self.centralWidget().num *= 10
            self.centralWidget().num += int(chr(e.key()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyMainWindow()
    sys.exit(app.exec_())
