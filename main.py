import cv2
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout,
    QGroupBox, QWidget, QLineEdit, QSpinBox
)

""" class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('cvdlhw1.ui')
        self.layout = QVBoxLayout()
        self.layout.addWidget(QPushButton('Button')) """

app = QApplication([])
label = QLabel('Hello PyQt5!')
label.show()
cv2.destroyAllWindows()
app.exec_()