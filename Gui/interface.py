# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import cv2
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QLabel


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1342, 979)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1311, 941))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textLatih = QtWidgets.QTextEdit(self.frame)
        self.textLatih.setGeometry(QtCore.QRect(40, 100, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textLatih.setFont(font)
        self.textLatih.setObjectName("textLatih")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(310, 20, 711, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btnLoadLatih = QtWidgets.QPushButton(self.frame)
        self.btnLoadLatih.setGeometry(QtCore.QRect(350, 100, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnLoadLatih.setFont(font)
        self.btnLoadLatih.setObjectName("btnLoadLatih")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(1130, 110, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(140, 500, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(790, 500, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(440, 500, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(1100, 500, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textUji = QtWidgets.QTextEdit(self.frame)
        self.textUji.setGeometry(QtCore.QRect(40, 550, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.textUji.setFont(font)
        self.textUji.setObjectName("textUji")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(40, 530, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 550, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(510, 550, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(40, 620, 1231, 301))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.view_original = QtWidgets.QGraphicsView(self.frame)
        self.view_original.setGeometry(QtCore.QRect(40, 180, 300, 300))
        self.view_original.setObjectName("view_original")
        self.view_gray = QtWidgets.QGraphicsView(self.frame)
        self.view_gray.setGeometry(QtCore.QRect(350, 180, 300, 300))
        self.view_gray.setObjectName("view_gray")
        self.view_roi = QtWidgets.QGraphicsView(self.frame)
        self.view_roi.setGeometry(QtCore.QRect(660, 180, 300, 300))
        self.view_roi.setObjectName("view_roi")
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_4.setGeometry(QtCore.QRect(970, 180, 300, 300))
        self.graphicsView_4.setObjectName("graphicsView_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1342, 21))
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
        self.label_2.setText(_translate("MainWindow", "Load Data Latih"))
        self.btnLoadLatih.setText(_translate("MainWindow", "Load"))
        self.pushButton_4.setText(_translate("MainWindow", "Tampilkan"))
        self.label_3.setText(_translate("MainWindow", "Citra Asli"))
        self.label_4.setText(_translate("MainWindow", "ROI"))
        self.label_5.setText(_translate("MainWindow", "Grayscale"))
        self.label_6.setText(_translate("MainWindow", "Eigenface"))
        self.label_7.setText(_translate("MainWindow", "Load Data Uji"))
        self.pushButton_2.setText(_translate("MainWindow", "Load"))
        self.pushButton_3.setText(_translate("MainWindow", "Proses"))
        self.menuHome.setTitle(_translate("MainWindow", "Home"))
        self.actionexit.setText(_translate("MainWindow", "exit"))


        self.btnLoadLatih.clicked.connect(lambda: self.loadPathTrain())

        self.pushButton_4.clicked.connect(lambda : self.preprosImage())

    def loadPathTrain(self):
        file_path = str(QFileDialog.getExistingDirectory(None, "Select Directory"))
        self.textLatih.setText(file_path)
        print("File path : {}".format(file_path))

    def preprosImage(self):
        get_path = self.textLatih.toPlainText()
        for folder in os.listdir(get_path):
            path = os.path.join(get_path, folder)
            for i in range(2):
                for img in os.listdir(path):
                    dir_img = (os.path.join(path, img))

                    img_gui = QtGui.QImage(dir_img)
                    pixmap  = QtGui.QPixmap.fromImage(img_gui)

                    self.label_3.setPixmap(pixmap)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

