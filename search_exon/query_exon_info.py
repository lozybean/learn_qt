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
        search_result = self.search(gene_name)
        self.textBrowser.setText(search_result)

    def search(self, gene_name):
        cursor_mRNA = mRNA_info.find({'gene': gene_name}, {'Name': 1, '_id': 0})
        string = ''
        for q in cursor_mRNA:
            mRNA = q['Name']
            exon_length = 0
            exon_num = 0
            cursor_exon = exon_info.find({'transcript_id': mRNA},
                                         {'start': 1, 'end': 1})
            for q in cursor_exon:
                exon_length += q['end'] - q['start'] + 1
                exon_num += 1
            string += '{gene_name}\t{mRNA}\t{exon_length}\t{exon_num}\n'.format_map(vars())
        return string


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
