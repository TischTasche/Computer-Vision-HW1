import cv2
import sys
import os
import glob

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ImageLoading(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        #### Box Layout 
        self.loadImageBox = QGroupBox('Load Image')
        self.loadImageLayout = QVBoxLayout()
        

        #### Load Folder Button
        self.loadFolderButton = QPushButton("Load Folder")
        self.loadFolderButton.clicked.connect(self.loadFolder)
        self.loadImageLayout.addWidget(self.loadFolderButton)

        #### Load Image Left Button
        self.loadImageLButton = QPushButton("Load Image_L")
        self.loadImageLButton.clicked.connect(self.loadImageL)
        self.loadImageLayout.addWidget(self.loadImageLButton)
        self.imageL = ""

        #### Load Image Right Button
        self.loadImageRButton = QPushButton("Load Image_R")
        self.loadImageRButton.clicked.connect(self.loadImageR)
        self.loadImageLayout.addWidget(self.loadImageRButton)
        self.imageR = ""

        #### Finishing Layout
        self.loadImageBox.setLayout(self.loadImageLayout)
        self.layout.addWidget(self.loadImageBox)

        self.setLayout(self.layout)

        self.imageDict = {}


    #### Load Folder and images 
    def loadFolder(self):
        folderPath = QFileDialog.getExistingDirectory(self, "Select a folder")
        if folderPath:
            imageFiles = glob.glob(os.path.join(folderPath, '*.png')) + \
                         glob.glob(os.path.join(folderPath, '*.jpg')) + \
                         glob.glob(os.path.join(folderPath, '*.jpeg')) + \
                         glob.glob(os.path.join(folderPath, '*.bmp'))
            if imageFiles:
                self.loadImage(imageFiles)
            else: 
                self.label.setText("No images available in the selected folder")

    def loadImage(self, imageFiles):
        for imageFile in imageFiles:
            image = cv2.imread(imageFile)
            if image is not None:
                self.imageDict[imageFile] = image
            else:
                self.label.setText("Failed to load image: {imageFile}")


#### Load Image Left and Right

    def loadImageL(self, imageFile):
        imagePath = QFileDialog.getOpenFileName(self, "Select an image file")[0]
        if imagePath: 
            self.imageL = cv2.imread(imagePath)
            if self.imageL is not None:
                self.label.setText("Loaded Image_L")
            else:
                self.label.setText("Loading Image_L failed")

    def loadImageR(self, imageFile):
        imagePath = QFileDialog.getOpenFileName(self, "Select an image file")[0]
        if imagePath: 
            self.imageR = cv2.imread(imagePath)
            if self.imageR is not None:
                self.label.setText("Loaded Image_R")
            else:
                self.label.setText("Loading Image_R failed")



