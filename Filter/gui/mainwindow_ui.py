# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/Toda/Udacity/VisualizationP4/PipelineHelper/gui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1054, 804)
        MainWindow.setWindowTitle("")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_4 = QtWidgets.QSplitter(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_4.sizePolicy().hasHeightForWidth())
        self.splitter_4.setSizePolicy(sizePolicy)
        self.splitter_4.setMinimumSize(QtCore.QSize(1030, 780))
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.splitter = QtWidgets.QSplitter(self.splitter_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.listgb = QtWidgets.QGroupBox(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listgb.sizePolicy().hasHeightForWidth())
        self.listgb.setSizePolicy(sizePolicy)
        self.listgb.setMinimumSize(QtCore.QSize(0, 0))
        self.listgb.setTitle("")
        self.listgb.setObjectName("listgb")
        self.upMiddleGb = QtWidgets.QGroupBox(self.splitter)
        self.upMiddleGb.setMinimumSize(QtCore.QSize(0, 0))
        self.upMiddleGb.setTitle("")
        self.upMiddleGb.setObjectName("upMiddleGb")
        self.upRightGb = QtWidgets.QGroupBox(self.splitter)
        self.upRightGb.setMinimumSize(QtCore.QSize(0, 0))
        self.upRightGb.setTitle("")
        self.upRightGb.setObjectName("upRightGb")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.midLeftGb = QtWidgets.QGroupBox(self.splitter_2)
        self.midLeftGb.setMinimumSize(QtCore.QSize(0, 0))
        self.midLeftGb.setTitle("")
        self.midLeftGb.setObjectName("midLeftGb")
        self.midMiddleGb = QtWidgets.QGroupBox(self.splitter_2)
        self.midMiddleGb.setMinimumSize(QtCore.QSize(0, 0))
        self.midMiddleGb.setTitle("")
        self.midMiddleGb.setObjectName("midMiddleGb")
        self.midRightGb = QtWidgets.QGroupBox(self.splitter_2)
        self.midRightGb.setMinimumSize(QtCore.QSize(0, 0))
        self.midRightGb.setTitle("")
        self.midRightGb.setObjectName("midRightGb")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_3.sizePolicy().hasHeightForWidth())
        self.splitter_3.setSizePolicy(sizePolicy)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.dowLeftGb = QtWidgets.QGroupBox(self.splitter_3)
        self.dowLeftGb.setMinimumSize(QtCore.QSize(0, 0))
        self.dowLeftGb.setTitle("")
        self.dowLeftGb.setObjectName("dowLeftGb")
        self.dowMiddleGb = QtWidgets.QGroupBox(self.splitter_3)
        self.dowMiddleGb.setMinimumSize(QtCore.QSize(0, 0))
        self.dowMiddleGb.setTitle("")
        self.dowMiddleGb.setObjectName("dowMiddleGb")
        self.dowRightGb = QtWidgets.QGroupBox(self.splitter_3)
        self.dowRightGb.setMinimumSize(QtCore.QSize(0, 0))
        self.dowRightGb.setTitle("")
        self.dowRightGb.setObjectName("dowRightGb")
        self.gridLayout.addWidget(self.splitter_4, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass
