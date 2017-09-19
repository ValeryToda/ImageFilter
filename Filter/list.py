#!/usr/bin/python3
from PyQt5.QtCore import (Qt, QFileInfo)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from .gui.list_ui import Ui_List

class List(QWidget, Ui_List):
    """
    Class Box implementation
    """
    def __init__(self, parent=None):
        super(List, self).__init__(parent)
        self.setupUi(self)
        #self.setAcceptDrops(True)
        #self.container.hide()
        self.data = []
        self.clearPb.clicked.connect(self.clearContainer)
        self.container.itemClicked.connect(self.getAbsFilenamefromItem)
        self.container.itemSelectionChanged.connect(self.showItemInfos)

    def showItemInfos(self):
        currentItem = self.container.currentItem()
        row = self.container.currentRow()
        #print(row)

    def getAbsFilenamefromItem(self, item):
        #print(item.text())
        currentItem = self.container.currentItem()
        #print(currentItem.text())
        row = self.container.currentRow()
        return self.data[row]
        #print(self.data[row])

    def clearContainer(self):
        self.data.clear()
        self.container.clear()
            
    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        if e.mimeData().hasUrls():
            for url in e.mimeData().urls():
                currentFileName = url.toLocalFile()
                if QImage().load(currentFileName):
                    self.data.append(currentFileName)
                    item = QListWidgetItem()
                    item.setTextAlignment(Qt.AlignLeft)
                    item.setFlags( Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                    item.setText(QFileInfo(currentFileName).fileName())
                    item.setToolTip(currentFileName)
                    self.container.addItem(item)
