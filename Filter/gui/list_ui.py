# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/Toda/Udacity/VisualizationP4/PipelineHelper/gui/list.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_List(object):
    def setupUi(self, List):
        List.setObjectName("List")
        List.resize(203, 165)
        List.setAcceptDrops(True)
        self.gridLayout = QtWidgets.QGridLayout(List)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.infoLabel = QtWidgets.QLabel(List)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.infoLabel.setFont(font)
        self.infoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infoLabel.setObjectName("infoLabel")
        self.verticalLayout.addWidget(self.infoLabel)
        self.container = QtWidgets.QListWidget(List)
        self.container.setMinimumSize(QtCore.QSize(0, 0))
        self.container.setAcceptDrops(True)
        self.container.setObjectName("container")
        self.verticalLayout.addWidget(self.container)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.clearPb = QtWidgets.QPushButton(List)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearPb.sizePolicy().hasHeightForWidth())
        self.clearPb.setSizePolicy(sizePolicy)
        self.clearPb.setMinimumSize(QtCore.QSize(110, 41))
        self.clearPb.setMaximumSize(QtCore.QSize(110, 41))
        self.clearPb.setObjectName("clearPb")
        self.horizontalLayout.addWidget(self.clearPb)
        spacerItem = QtWidgets.QSpacerItem(258, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(List)
        QtCore.QMetaObject.connectSlotsByName(List)

    def retranslateUi(self, List):
        _translate = QtCore.QCoreApplication.translate
        List.setWindowTitle(_translate("List", "Form"))
        self.infoLabel.setText(_translate("List", "Please Drag images below"))
        self.clearPb.setText(_translate("List", "Clear List"))

