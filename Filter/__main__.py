#!/usr/bin/python3
import sys
from PyQt5.QtWidgets import *
from .gui.mainwindow_ui import Ui_MainWindow
from .box import *
from .list import *
from PyQt5.QtCore import *
from .common import *


class MainWindow(QMainWindow, Ui_MainWindow):
    listSelectionChanged = pyqtSignal(str)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.liw = List(self.listgb)
        self.gl1 = QGridLayout(self.listgb)
        self.gl1.setContentsMargins(0, 0, 0, 0)
        self.gl1.setSpacing(5)
        self.gl1.addWidget(self.liw, 0, 0)
        
        self.ow = Box(method=ORIGINAL, parent=self.upMiddleGb)
        self.gl2 = QGridLayout(self.upMiddleGb)
        self.gl2.setContentsMargins(0, 0, 0, 0)
        self.gl2.setSpacing(5)
        self.gl2.addWidget(self.ow, 0, 0)

        self.sw = Box(method=S_SELECT, parent=self.dowLeftGb)
        self.gl3 = QGridLayout(self.dowLeftGb)
        self.gl3.setContentsMargins(0, 0, 0, 0)
        self.gl3.setSpacing(5)
        self.gl3.addWidget(self.sw, 0, 0)

        self.lw = Box(method=L_SELECT, parent=self.midLeftGb)
        self.gl4 = QGridLayout(self.midLeftGb)
        self.gl4.setContentsMargins(0, 0, 0, 0)
        self.gl4.setSpacing(5)
        self.gl4.addWidget(self.lw, 0, 0)

        self.gw = Box(method=DIR_GRADIENT, parent=self.midMiddleGb)
        self.gl5 = QGridLayout(self.midMiddleGb)
        self.gl5.setContentsMargins(0, 0, 0, 0)
        self.gl5.setSpacing(5)
        self.gl5.addWidget(self.gw, 0, 0)

        self.mw = Box(method=MAGNITUDE, parent=self.midRightGb)
        self.gl6 = QGridLayout(self.midRightGb)
        self.gl6.setContentsMargins(0, 0, 0, 0)
        self.gl6.setSpacing(5)
        self.gl6.addWidget(self.mw, 0, 0)

        self.yw = Box(method=Y_DIRECTION, parent=self.dowMiddleGb)
        self.gl7 = QGridLayout(self.dowMiddleGb)
        self.gl7.setContentsMargins(0, 0, 0, 0)
        self.gl7.setSpacing(5)
        self.gl7.addWidget(self.yw, 0, 0)

        self.xw = Box(method=X_DIRECTION, parent=self.dowRightGb)
        self.gl8 = QGridLayout(self.dowRightGb)
        self.gl8.setContentsMargins(0, 0, 0, 0)
        self.gl8.setSpacing(5)
        self.gl8.addWidget(self.xw, 0, 0)

        self.hsw = Box(method=H_SELECT, parent=self.upRightGb)
        self.gl9 = QGridLayout(self.upRightGb)
        self.gl9.setContentsMargins(0, 0, 0, 0)
        self.gl9.setSpacing(5)
        self.gl9.addWidget(self.hsw, 0, 0)
        
        self.liw.container.itemClicked.connect(self.getItemAbsFilename)
        self.liw.container.itemSelectionChanged.connect(self.getItemInfos)
        self.listSelectionChanged.connect(self.xw.loadImage)
        self.listSelectionChanged.connect(self.lw.loadImage)
        self.listSelectionChanged.connect(self.sw.loadImage)
        self.listSelectionChanged.connect(self.mw.loadImage)
        self.listSelectionChanged.connect(self.gw.loadImage)
        self.listSelectionChanged.connect(self.ow.loadImage)
        self.listSelectionChanged.connect(self.yw.loadImage)
        self.listSelectionChanged.connect(self.hsw.loadImage)

    def getItemInfos(self):
        try:
            row = self.liw.container.currentRow()
            if self.liw.container.count() > 0:
                self.listSelectionChanged.emit(self.liw.data[row])
        except IndexError:
            pass
    
    def getItemAbsFilename(self, item):
        try:
            row = self.liw.container.currentRow()
            if self.liw.container.count() > 0:
                self.listSelectionChanged.emit(self.liw.data[row])
        except IndexError:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
    app.deleteLater()
    sys.exit()