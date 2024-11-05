import cv2
import sys
import os
import glob

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout,
    QGroupBox, QWidget, QLineEdit, QSpinBox
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('cvdlhw1.ui - Sören Petersen')
        self.setGeometry(100, 100, 1600, 1000)

        layout = QGridLayout()


app = QApplication([])
label = QLabel('Hello PyQt5!')
label.show()
cv2.destroyAllWindows()
app.exec_()