# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
import os

import cv2
import numpy as np

import Prepros


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1576, 979)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Image = QtWidgets.QFrame(self.centralwidget)
        self.Image.setGeometry(QtCore.QRect(10, 10, 1551, 941))
        self.Image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Image.setObjectName("Image")
        self.label = QtWidgets.QLabel(self.Image)
        self.label.setGeometry(QtCore.QRect(460, 20, 711, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnLoadData = QtWidgets.QPushButton(self.Image)
        self.btnLoadData.setGeometry(QtCore.QRect(630, 100, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnLoadData.setFont(font)
        self.btnLoadData.setObjectName("btnLoadData")
        self.btnProses = QtWidgets.QPushButton(self.Image)
        self.btnProses.setGeometry(QtCore.QRect(1150, 100, 141, 41))

        self.btnLoadData.clicked.connect (self.loadPathTrain)

        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnProses.setFont(font)
        self.btnProses.setObjectName("btnProses")
        self.label_3 = QtWidgets.QLabel(self.Image)
        self.label_3.setGeometry(QtCore.QRect(140, 500, 91, 16))

        self.btnProses.clicked.connect (self.preprosImage)

        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.Image)
        self.label_4.setGeometry(QtCore.QRect(460, 500, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.Image)
        self.label_5.setGeometry(QtCore.QRect(760, 500, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.Image)
        self.label_6.setGeometry(QtCore.QRect(1160, 840, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setTextFormat(QtCore.Qt.RichText)
        self.label_6.setObjectName("label_6")
        self.inputDataUji = QtWidgets.QTextEdit(self.Image)
        self.inputDataUji.setGeometry(QtCore.QRect(40, 100, 571, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.inputDataUji.setFont(font)
        self.inputDataUji.setObjectName("inputDataUji")
        self.label_7 = QtWidgets.QLabel(self.Image)
        self.label_7.setGeometry(QtCore.QRect(50, 70, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.linePengujian = QtWidgets.QLineEdit(self.Image)
        self.linePengujian.setGeometry(QtCore.QRect(40, 620, 841, 301))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.linePengujian.setFont(font)
        self.linePengujian.setObjectName("linePengujian")
        self.label_2 = QtWidgets.QLabel(self.Image)
        self.label_2.setGeometry(QtCore.QRect(40, 560, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_asli = QtWidgets.QLabel(self.Image)
        self.label_asli.setGeometry(QtCore.QRect(40, 180, 300, 300))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_asli.setFont(font)
        self.label_asli.setObjectName("label_asli")
        self.label_roi = QtWidgets.QLabel(self.Image)
        self.label_roi.setGeometry(QtCore.QRect(340, 190, 300, 300))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_roi.setFont(font)
        self.label_roi.setObjectName("label_roi")
        self.label_gray = QtWidgets.QLabel(self.Image)
        self.label_gray.setGeometry(QtCore.QRect(660, 200, 300, 300))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_gray.setFont(font)
        self.label_gray.setObjectName("label_gray")
        self.label_eigen = QtWidgets.QLabel(self.Image)
        self.label_eigen.setGeometry(QtCore.QRect(920, 210, 600, 600))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_eigen.setFont(font)
        self.label_eigen.setObjectName("label_eigen")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1576, 21))
        self.menubar.setObjectName("menubar")
        self.menuHome = QtWidgets.QMenu(self.menubar)
        self.menuHome.setObjectName("menuHome")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.menuHome.addAction(self.actionexit)
        self.menubar.addAction(self.menuHome.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Interface Program"))
        self.label.setText(_translate("MainWindow", "KLASIFIKASI WAJAH MENGGUNAKAN K-NN"))
        self.btnLoadData.setText(_translate("MainWindow", "Load"))
        self.btnProses.setText(_translate("MainWindow", "Proses"))
        self.label_3.setText(_translate("MainWindow", "Citra Asli"))
        self.label_4.setText(_translate("MainWindow", "ROI"))
        self.label_5.setText(_translate("MainWindow", "Grayscale"))
        self.label_6.setText(_translate("MainWindow", "Eigenface"))
        self.label_7.setText(_translate("MainWindow", "Load Data Uji"))
        self.label_2.setText(_translate("MainWindow", "Pengujian"))
        self.label_asli.setText(_translate("MainWindow", "Image ?"))
        self.label_roi.setText(_translate("MainWindow", "Image ?"))
        self.label_gray.setText(_translate("MainWindow", "Image ?"))
        self.label_eigen.setText(_translate("MainWindow", "Image ?"))
        self.menuHome.setTitle(_translate("MainWindow", "Home"))
        self.actionexit.setText(_translate("MainWindow", "exit"))

    def loadPathTrain(self):
        file_path = str(QFileDialog.getExistingDirectory(None, "Select Directory"))

        self.inputDataUji.setText(file_path)
        # print("File path : {}".format(file_path))

    def preprosImage(self):
        get_path = self.inputDataUji.toPlainText()
        for folder in os.listdir(get_path):
            path = os.path.join(get_path, folder)
            for i in range(2):
                for img in os.listdir(path):
                    print(img)
                    path_image = (os.path.join(path, img))
                    # Citra Asli
                    img_gui = QtGui.QImage(path_image)
                    pixmap = QtGui.QPixmap.fromImage(img_gui)

                    self.label_asli.setPixmap(pixmap)

                    # ROI
                    img_roi = Prepros.roi_img(path_image)

                    print(img_roi.shape)
                    height, width, channel = img_roi.shape
                    bytesPerLine = 3 * width
                    qImg = QImage(img_roi.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
                    roi_map = QPixmap(qImg)
                    self.label_roi.setPixmap(roi_map)

                    # Grayscale
                    img_gray = Prepros.imgGray(img_roi)
                    height, width = img_gray.shape
                    img_gray = QtGui.QImage(img_gray, width, height, QtGui.QImage.Format_Grayscale8)
                    img = QtGui.QPixmap.fromImage(img_gray)
                    self.label_gray.setPixmap(img)

                    #Eigenface





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

