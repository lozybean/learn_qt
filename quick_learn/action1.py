#!/usr/bin/env python
# -*- coding: utf-8 -*- \#
"""
@author = 'liangzb'
@date = '2016/5/20 0020'

"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 800)
        self.center()
        self.setWindowTitle('myapp')
        self.setToolTip('看啥子看^_^')
        QToolTip.setFont(QFont('微软雅黑', 12))

    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self, '伤心',
                                     '你真的不爱我了吗?',
                                     QMessageBox.Yes,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(800, 600)
        self.center()
        self.setWindowTitle('myapp')
        self.setToolTip('看啥子看^_^')
        QToolTip.setFont(QFont('微软雅黑', 12))
        self.init_menu()
        self.statusBar().showMessage('程序已就绪...')
        self.set_btn()

    def set_btn(self):
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(100, 100)
        btn.clicked.connect(self.btn_clicked)


    @pyqtSlot()
    def btn_clicked(self):
        self.statusBar().showMessage('按下按钮')

    def init_menu(self):
        menu_control = self.menuBar().addMenu('Control')
        act_quit = menu_control.addAction('quit')
        act_quit.triggered.connect(self.close)

        menu_help = self.menuBar().addMenu('Help')
        act_about = menu_help.addAction('about...')
        act_about.triggered.connect(self.about)
        act_aboutqt = menu_help.addAction('aboutqt')
        act_aboutqt.triggered.connect(self.aboutqt)

    @pyqtSlot()
    def about(self):
        self.statusBar().showMessage('关于...')
        QMessageBox.about(self, "about this software",
                          "wise system")

    @pyqtSlot()
    def aboutqt(self):
        self.statusBar().showMessage('关于...')
        QMessageBox.aboutQt(self)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '信息',
                                     '你确定要退出吗?',
                                     QMessageBox.Yes,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # my_widget = MyWidget()
    # my_widget.show()
    my_window = MyWindow()
    my_window.show()
    sys.exit(app.exec_())
