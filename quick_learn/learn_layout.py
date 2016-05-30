#!/usr/bin/env python
# -*- coding: utf-8 -*- \#
"""
@author = 'liangzb'
@date = '2016/5/25 0025'

"""

import sys
from PyQt5.QtWidgets import *


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.button_ok = QPushButton("OK")
        self.button_cancer = QPushButton("Cancel")

        # self.init_box_layout()
        self.init_grid_layout()

        self.resize(300, 150)
        self.setWindowTitle("Test Layout")
        self.show()

    def init_box_layout(self):
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.button_ok)
        hbox.addWidget(self.button_cancer)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def init_grid_layout(self):
        grid = QGridLayout()

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
        for position, name in zip(positions, names):
            if name:
                button = QPushButton(name)
                grid.addWidget(button, *position)

        self.setLayout(grid)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    sys.exit(app.exec_())
