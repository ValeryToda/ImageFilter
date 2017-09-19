#!/usr/bin/python3
import numpy as np
import matplotlib.image as mpimg
from PyQt5.QtCore import (Qt, QEvent, QSize)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import cv2
import matplotlib.pyplot as plt
from .utils import *
from math import pi
from .common import *

class Frame(QFrame):
    """
    Class Frame implementation
    """
    def __init__(self, parent=None):
        super(Frame, self).__init__(parent)
        self.thresh_min = 0
        self.thresh_max = 255
        self.currentImageData = None
        self.image = None
        self.renderMethod = None
        self.filename = None

    def loadImageData(self, filename, method):
        self.filename = filename
        self.currentImageData = mpimg.imread(filename)
        self.updateGeometry()
        self.renderMethod = method  
        self.renderRSelect()

    def sizeHint(self):
        if self.image is None:
            return super().sizeHint()
        else:
            return QSize(self.currentImageData.shape[1], self.currentImageData.shape[0])

    def setMinThreshold(self, value):
        self.thresh_min = value
        self.renderRSelect()

    def setMaxThreshold(self, value):
        self.thresh_max = value
        self.renderRSelect()
        

    def renderRSelect(self):
        if self.renderMethod == ORIGINAL:
            self.image = QImage(self.filename)  
            self.repaint()
            return
        elif self.renderMethod == L_SELECT:
            binary_output = l_select(self.currentImageData, thresh=(self.thresh_min,
                                                                    self.thresh_max))
        
        elif self.renderMethod == S_SELECT:
            binary_output = s_select(self.currentImageData, thresh=(self.thresh_min, 
                                                                    self.thresh_max))
        
        elif self.renderMethod == DIR_GRADIENT:
            #scaling values between 0 and 255 to values between 0 and 1.57(== pi/2)
            # Formula: Result := ((Input - InputLow) / (InputHigh - InputLow)) * (OutputHigh - OutputLow) + OutputLow
            thresh_min = (self.thresh_min / 255) * (pi / 2)
            thresh_max = (self.thresh_max / 255) * (pi / 2)
            #print ("min: {}".format(thresh_min))
            #print ("max: {}".format(thresh_max))
            binary_output = dir_thresh(self.currentImageData, thresh=(thresh_min, thresh_max))
        
        elif self.renderMethod == MAGNITUDE:
            binary_output = mag_thresh(self.currentImageData, mag_thresh=(self.thresh_min, self.thresh_max))
        elif self.renderMethod == X_DIRECTION:
            binary_output = soebel_filter(self.currentImageData, direction='x', thresh_min=self.thresh_min, 
                                                            thresh_max=self.thresh_max)
        elif self.renderMethod == Y_DIRECTION:
            binary_output = soebel_filter(self.currentImageData, direction='y', thresh_min=self.thresh_min, 
                                                            thresh_max=self.thresh_max)
        elif self.renderMethod == H_SELECT:
            binary_output = h_select(self.currentImageData, thresh=(self.thresh_min,
                                                                    self.thresh_max))
        elif self.renderMethod == LAPLACIAN:
            binary_output = laplacian(self.currentImageData, thresh=(self.thresh_min,
                                                                    self.thresh_max))

        else:
            #print("unknown rendering Method")
            #print(self.renderMethod)
            return

        height, width = binary_output.shape
        gray_color_table = [~((i + (i<<8) + (i<<16))) for i in range(255,-1,-1)]
        img_result = QImage(binary_output.data, width, height, QImage.Format_Indexed8)
        img_result.setColorTable(gray_color_table)
        img_result.ndarray = binary_output

        self.image = img_result
        self.repaint()
        

    def paintEvent(self, event):
        if self.currentImageData is not None and self.image is not None:
            p = QPainter(self)
            p.setRenderHint(QPainter.Antialiasing, True)
            rect = p.viewport()
            p.setViewport(rect.x(), rect.y(), self.size().width(), self.size().height())
            p.setWindow(self.image.rect())
            p.drawImage(0, 0, self.image)
            #p.drawPixmap(0, 0, QPixmap.fromImage(self.image))
