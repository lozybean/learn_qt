#!/usr/bin/env python
# -*- coding: utf-8 -*- \#
"""
@author = 'liangzb'
@date = '2016/5/30 0030'

"""

import sys
from pymongo import MongoClient
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from search_exon.main import Ui_MainWindow

client = MongoClient('192.168.6.4', 27018)
db = client.reference
db.authenticate(name='reference', password='123')
mRNA_info = db.mRNA_info
exon_info = db.exon_info


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.show_search_result)

    def show_search_result(self):
        gene_name = self.lineEdit.text()
        search_result = list(self.search(gene_name))
        self.init_table(4, len(search_result))
        for index, value in enumerate(search_result):
            (gene_name, transcript_id, exon_length, exon_num) = value
            self.tableWidget.setItem(index, 0, QTableWidgetItem(gene_name))
            self.tableWidget.setItem(index, 1, QTableWidgetItem(transcript_id))
            self.tableWidget.setItem(index, 2, QTableWidgetItem(str(exon_length)))
            self.tableWidget.setItem(index, 3, QTableWidgetItem(str(exon_num)))

    def init_table(self, col, row):
        self.tableWidget.setColumnCount(col)
        self.tableWidget.setRowCount(row)
        self.tableWidget.setHorizontalHeaderLabels(['gene_name', 'transcript_id',
                                                    'exon_length', 'exon_num'])
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 100)

    def search(self, gene_name):
        cursor_mRNA = mRNA_info.find({'gene': gene_name}, {'Name': 1, '_id': 0})
        for q in cursor_mRNA:
            mRNA = q['Name']
            exon_length = 0
            exon_num = 0
            cursor_exon = exon_info.find({'transcript_id': mRNA},
                                         {'start': 1, 'end': 1})
            for q in cursor_exon:
                exon_length += q['end'] - q['start'] + 1
                exon_num += 1
            yield gene_name, mRNA, exon_length, exon_num


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
