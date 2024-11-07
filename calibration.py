import cv2
import sys
import os
import glob

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Calibration(QWidget):
    def __init__(self):
        super().__init__("calibration")

        self.layout = QVBoxLayout()

        #### 1.1 Find Corners
        self.findCornersButton = QPushButton("1.1 Find Corners")
        self.findCornersButton.clicked.connect(self.findCorners)
        self.layout.addWidget(self.findCornersButton)

        #### 1.2 Find Intrinsics
        self.findIntrinsicButton = QPushButton("1.2 Find Intrinsics")
        self.findIntrinsicButton.clicked.connect(self.findIntrinsic)
        self.layout.addWidget(self.findIntrinsicButton)

        #### 1.3 Find Extrinsic
        self.findExtrinsicBox = QGroupBox("1.3 Find Extrinsic")
        self.findExtrinsicLayout = QHBoxLayout()

        self.spinBox = QSpinBox()
        self.spinBox.setMinimum(0)
        self.spinBox.setValue(1)
        self.spinBox.setSingleStep(1)
        self.findExtrinsicLayout.addWidget(self.spinBox)

        self.findExtrinsicButton = QPushButton("1.3 Find Extrinsics")
        self.findExtrinsicButton.clicked.connect(self.findExtrinsic)
        self.findExtrinsicLayout.addWidget(self.findExtrinsicButton)

        #### 1.4 Find Distortion
        self.findDistortionButton = QPushButton("1.4 Find Distortion")
        self.findDistortionButton.clicked.connect(self.findDistortion)
        self.layout.addWidget(self.findDistortionButton)

        #### 1.5 Show Result
        self.showResultButton = QPushButton("1.5 Show Result")
        self.showResultButton.clicked.connect(self.showResult)
        self.layout.addWidget(self.showResultButton)

        self.setLayout(self.layout)