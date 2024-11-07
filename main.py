import cv2
import sys
import os
import glob

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from imageLoader import ImageLoading
from calibration import Calibration


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #### Layout
        self.setWindowTitle('cvdlhw1.ui - Sören Petersen')
        self.setGeometry(100, 100, 1600, 1000)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        layout = QGridLayout(centralWidget)
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)

        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        #### Load Image
        self.loadImage = ImageLoading()
        layout.addWidget(self.loadImage, 0, 0)

        #### 1. Calibration
        self.calibration = Calibration()
        self.calibration.setFont(QFont())
        layout.addWidget(self.calibration, 0, 0) 

        #### 2. Augmented Reality
        """  self.AR = LoadImage()
        self.AR.setFont(QFont())
        layout.addWidget(self.AR, 0, 0)

        #### 3. Stereo Disparity Map
        self.load_image_widget = LoadImage()
        self.load_image_widget.setFont(QFont())
        layout.addWidget(self.load_image_widget, 0, 0)

        #### 4. SIFT
        self.load_image_widget = LoadImage()
        self.load_image_widget.setFont(QFont())
        layout.addWidget(self.load_image_widget, 0, 0) """



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()