#!/usr/bin/python3
from PyQt5.QtCore import (Qt, QEvent)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from .gui.box_ui import Ui_Box
from .frame import *
from math import pi


class Box(QWidget, Ui_Box):
    """
    Class Box implementation
    """
    def __init__(self, method=S_SELECT, parent=None):
        super(Box, self).__init__(parent)
        self.setupUi(self)
        self.setAcceptDrops(True)
        self.contentFrame = Frame(self.frameGroupBox)
        self.gridLayout_cf = QGridLayout(self.frameGroupBox)
        self.gridLayout_cf.setContentsMargins(0, 0, 0, 0)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.contentFrame.setSizePolicy(sizePolicy)
        self.contentFrame.setFrameShape(QFrame.StyledPanel)
        self.contentFrame.setFrameShadow(QFrame.Plain)
        self.gridLayout_cf.addWidget(self.contentFrame, 0, 0)

        self.min2maxSlider.valueChanged.connect(self.contentFrame.setMinThreshold)
        self.max2minSlider.valueChanged.connect(self.contentFrame.setMaxThreshold)
        self.setTitle(method)
        self.renderMethod = method
        if method == ORIGINAL:
            self.max2minLcdNumber.hide()
            self.min2maxLcdNumber.hide()
            self.min2maxSlider.hide()
            self.max2minSlider.hide()
        if method == DIR_GRADIENT:
            palette = self.max2minLcdNumber.palette()
            palette.setColor(palette.WindowText, QColor(0, 0, 0))
            self.max2minLcdNumber.setSmallDecimalPoint(True)
            self.min2maxLcdNumber.setSmallDecimalPoint(True)
            self.min2maxLcdNumber.setPalette(palette)
            self.max2minLcdNumber.setPalette(palette)
            self.max2minLcdNumber.setSegmentStyle(1)
            self.max2minLcdNumber.display(pi/2)
            self.min2maxLcdNumber.setSegmentStyle(1)
            self.min2maxLcdNumber.display(0)
            self.min2maxSlider.valueChanged.connect(self.scaleMin2MacLcd)
            self.max2minSlider.valueChanged.connect(self.scaleMax2MinLcd)
        
        # Set default values for sliders
        if method == S_SELECT:
            self.min2maxSlider.setValue(162)
            self.max2minSlider.setValue(255)
        elif method == L_SELECT:
            self.min2maxSlider.setValue(122)
            self.max2minSlider.setValue(161)
        elif method == MAGNITUDE:
            self.min2maxSlider.setValue(68)
            self.max2minSlider.setValue(168)
        elif method == X_DIRECTION:
            self.min2maxSlider.setValue(48)
            self.max2minSlider.setValue(145)
        elif method == Y_DIRECTION:
            self.min2maxSlider.setValue(68)
            self.max2minSlider.setValue(180)
        elif method == DIR_GRADIENT:
            self.min2maxSlider.setValue(15)
            self.max2minSlider.setValue(161)
        elif method ==H_SELECT:
            self.min2maxSlider.setValue(16)
            self.max2minSlider.setValue(31)
        elif method ==LAPLACIAN:
            self.min2maxSlider.setValue(16)
            self.max2minSlider.setValue(31)

    def scaleMax2MinLcd(self, value):
        # only for floating representation (0, np.pi/2)
        scaled_max_value = (value / 255) * (pi / 2)
        self.max2minLcdNumber.setSegmentStyle(1)
        self.max2minLcdNumber.display(scaled_max_value)
        
    def scaleMin2MacLcd(self, value):
        # only for floating representation (0, np.pi/2)
        scaled_min_value = (value / 255) * (pi / 2)
        self.min2maxLcdNumber.setSegmentStyle(1)
        self.min2maxLcdNumber.display(scaled_min_value)

    def loadImage(self, filename):
        self.contentFrame.loadImageData(filename, self.renderMethod)

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        if e.mimeData().hasUrls():
            for url in e.mimeData().urls():
                if QImage().load(url.toLocalFile()):
                    self.loadImage(url.toLocalFile())
                    break

    def setTitle(self, method):
        if method == S_SELECT:
            newTitle = "Thresholded S Channel"    
        elif method == L_SELECT:
            newTitle = "Thresholded L Channel"
        elif method == DIR_GRADIENT:
            newTitle = "Thresholded Gradient Direction"
        elif method == MAGNITUDE:
            newTitle = "Thresholded Gradient Magnitude"
        elif method == X_DIRECTION:
            newTitle = "Thresholded Gradient X Direction"
        elif method == Y_DIRECTION:
            newTitle = "Thresholded Gradient Y Direction"
        elif method == ORIGINAL:
            newTitle = "Original"
        elif method == H_SELECT:
            newTitle = "Thresholded H Channel"
        elif method == LAPLACIAN:
            newTitle = "Laplacian of Gray"
        else:
            newTitle = "--"
        self.titleLabel.setText(newTitle)
