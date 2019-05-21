# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
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
from matplotlib.mlab import PCA
from sklearn.utils import Bunch
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier

import Prepros
from pca import *


TRAIN_PATH = "D:\kuliah\semester6\Biometrika\FaceVerificationLVQ\Grayscale/train"
TEST_PATH = "D:\kuliah\semester6\Biometrika\FaceVerificationLVQ\Grayscale/test"

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1322, 997)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Image = QtWidgets.QFrame(self.centralwidget)
        self.Image.setGeometry(QtCore.QRect(10, 10, 1311, 941))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Image.setFont(font)
        self.Image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Image.setObjectName("Image")
        self.label = QtWidgets.QLabel(self.Image)
        self.label.setGeometry(QtCore.QRect(240, 20, 711, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnLoadData = QtWidgets.QPushButton(self.Image)
        self.btnLoadData.setGeometry(QtCore.QRect(670, 100, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnLoadData.setFont(font)
        self.btnLoadData.setObjectName("btnLoadData")
        self.btnProses = QtWidgets.QPushButton(self.Image)
        self.btnProses.setGeometry(QtCore.QRect(820, 100, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnProses.setFont(font)
        self.btnProses.setObjectName("btnProses")
        self.label_3 = QtWidgets.QLabel(self.Image)
        self.label_3.setGeometry(QtCore.QRect(160, 510, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.Image)
        self.label_4.setGeometry(QtCore.QRect(600, 510, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.Image)
        self.label_5.setGeometry(QtCore.QRect(990, 510, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.inputDataUji = QtWidgets.QTextEdit(self.Image)
        self.inputDataUji.setGeometry(QtCore.QRect(40, 100, 601, 41))
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
        self.label_2 = QtWidgets.QLabel(self.Image)
        self.label_2.setGeometry(QtCore.QRect(40, 560, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_asli = QtWidgets.QLabel(self.Image)
        self.label_asli.setGeometry(QtCore.QRect(100, 160, 230, 320))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_asli.setFont(font)
        self.label_asli.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_asli.setText("")
        self.label_asli.setPixmap(QtGui.QPixmap(":/picture/11204-200.png"))
        self.label_asli.setAlignment(QtCore.Qt.AlignCenter)
        self.label_asli.setObjectName("label_asli")
        self.label_roi = QtWidgets.QLabel(self.Image)
        self.label_roi.setGeometry(QtCore.QRect(480, 180, 300, 300))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_roi.setFont(font)
        self.label_roi.setText("")
        self.label_roi.setPixmap(QtGui.QPixmap(":/picture/11204-200.png"))
        self.label_roi.setAlignment(QtCore.Qt.AlignCenter)
        self.label_roi.setObjectName("label_roi")
        self.label_gray = QtWidgets.QLabel(self.Image)
        self.label_gray.setGeometry(QtCore.QRect(890, 190, 300, 300))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_gray.setFont(font)
        self.label_gray.setText("")
        self.label_gray.setPixmap(QtGui.QPixmap(":/picture/11204-200.png"))
        self.label_gray.setAlignment(QtCore.Qt.AlignCenter)
        self.label_gray.setObjectName("label_gray")
        self.btnEigen = QtWidgets.QPushButton(self.Image)
        self.btnEigen.setGeometry(QtCore.QRect(970, 100, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnEigen.setFont(font)
        self.btnEigen.setObjectName("btnEigen")
        self.btnUji = QtWidgets.QPushButton(self.Image)
        self.btnUji.setGeometry(QtCore.QRect(1120, 100, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnUji.setFont(font)
        self.btnUji.setObjectName("btnUji")
        self.textUji = QtWidgets.QTextEdit(self.Image)
        self.textUji.setGeometry(QtCore.QRect(380, 580, 551, 331))
        self.textUji.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.textUji.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.textUji.setObjectName("textUji")
        self.label_6 = QtWidgets.QLabel(self.Image)
        self.label_6.setGeometry(QtCore.QRect(190, 720, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.Image)
        self.label_8.setGeometry(QtCore.QRect(140, 750, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.Image)
        self.label_9.setGeometry(QtCore.QRect(280, 700, 21, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.scrollArea = QtWidgets.QScrollArea(self.Image)
        self.scrollArea.setGeometry(QtCore.QRect(390, 590, 531, 311))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 529, 309))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 501, 291))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setText("")
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_10.setObjectName("label_10")
        self.scrollArea.setWidget(self.label_10)
        self.label_10.setAlignment(QtCore.Qt.AlignAbsolute)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1322, 21))
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
        self.label.setText(_translate("MainWindow", "IDENTIFIKASI WAJAH MENGGUNAKAN K-NN"))
        self.btnLoadData.setText(_translate("MainWindow", "Load"))
        self.btnProses.setText(_translate("MainWindow", "Proses"))
        self.label_3.setText(_translate("MainWindow", "Citra Asli"))
        self.label_4.setText(_translate("MainWindow", "ROI"))
        self.label_5.setText(_translate("MainWindow", "Grayscale"))
        self.label_7.setText(_translate("MainWindow", "Load Data Uji"))
        self.btnEigen.setText(_translate("MainWindow", "Eigen"))
        self.btnUji.setText(_translate("MainWindow", "Pengujian"))
        self.label_6.setText(_translate("MainWindow", "HASIL "))
        self.label_8.setText(_translate("MainWindow", "PENGUJIAN"))
        self.label_9.setText(_translate("MainWindow", ":"))
        self.menuHome.setTitle(_translate("MainWindow", "Home"))
        self.actionexit.setText(_translate("MainWindow", "exit"))



        self.btnProses.clicked.connect(self.preprosImage)
        self.btnLoadData.clicked.connect(self.loadPathTrain)
        self.btnEigen.clicked.connect(self.pca)

    def loadPathTrain(self):
        file_path = str(QFileDialog.getExistingDirectory(None, "Select Directory"))
        # print(file_path)
        self.inputDataUji.setText(file_path)
        # print("File path : {}".format(file_path))

    def preprosImage(self):
        get_path = self.inputDataUji.toPlainText()
        if(get_path !=''):
            for folder in os.listdir(get_path):
                path = os.path.join(get_path, folder)
                for i in range(2):
                    for img in os.listdir(path):
                        # print(img)
                        path_image = (os.path.join(path, img))
                        # Citra Asli
                        img_gui = QtGui.QImage(path_image)
                        pixmap = QtGui.QPixmap.fromImage(img_gui)

                        self.label_asli.setPixmap(pixmap)

                        # ROI
                        img_roi = Prepros.roi_img(path_image)

                        # print(img_roi.shape)
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



    def pca(self):
        if(self.inputDataUji.toPlainText() !=''):
            print("add dataset into numpy array")
            train_dataset = append_feature(TRAIN_PATH)
            print("train set created successfully")
            test_dataset = append_feature(TEST_PATH)
            print("train set created successfully")

            n_samples, h, w = train_dataset.images.shape

            X_train = train_dataset.data
            y_train = train_dataset.target

            X_test = test_dataset.data
            y_test = test_dataset.target

            n_components = 70
            pca = PCA(n_components=n_components).fit(X_train)
            eigenfaces = pca.components_.reshape((n_components, h, w))

            print("Projecting the input data on the eigenfaces orthonormal basis")
            X_train_pca = pca.transform(X_train)
            X_test_pca = pca.transform(X_test)

            eigenface_titles = ["eigenface %d" % i for i in range(eigenfaces.shape[0])]
            plot_gallery(eigenfaces, eigenface_titles, h, w)
            plt.show()

            k = 2
            knn_model = KNeighborsClassifier(n_neighbors=k)
            model_save = knn_model.fit(X_train_pca, y_train)
            saved_model = pickle.dumps(model_save)
            knn_from_pickle = pickle.loads(saved_model)

            # print(model_save)

            y_predict = knn_from_pickle.predict(X_test_pca)



            self.label_10.setText(classification_report(y_test, y_predict))

            # self.labelUji.append(line])


            # print(classification_report(y_test, y_predict))
            # salah = 0
            # print("target: "+str(k))
            # for i in range(0, len(y_predict)):
            # print(str(i) + ". " + str(y_test[i]))
            # print("uji: "+str(k))
            # print(str(i) + ". " + str(y_predict[i]))
            # print("\n")
            # if (y_test[i] != y_predict[i]):
            # salah += 1

    def append_feature(PATH):

        images = []
        target = []
        flatten_images = []

        for i, dir_images in zip(range(30), os.listdir(PATH)):
            for file in os.listdir(PATH + "\\{}".format(dir_images)):
                dir = os.path.join(PATH + "\\{}".format(dir_images), file)
                # get images
                img = cv2.imread(dir, 0)
                # tambahkan preprocessing
                flatten_images.append(img.flatten())
                images.append(img)
                target.append(dir_images)

        flatten_images = np.array(flatten_images)
        images = np.array(images)
        target = np.array(target)

        return Bunch(data=flatten_images,
                     target=target,
                     target_names=target,
                     images=images,
                     descr="deskripsi"
                     )
        pass

    def plot_gallery(images, titles, h, w, n_row=3, n_col=4):
        """Helper function to plot a gallery of portraits"""
        plt.figure(figsize=(1.8 * n_col, 2.4 * n_row))
        plt.subplots_adjust(bottom=0, left=.01, right=.99, top=.90, hspace=.35)
        for i in range(n_row * n_col):
            plt.subplot(n_row, n_col, i + 1)
            plt.imshow(images[i].reshape((h, w)), cmap=plt.cm.gray)
            plt.title(titles[i], size=12)
            plt.xticks(())
            plt.yticks(())

    def main():
        print("add dataset into numpy array")
        train_dataset = append_feature(TRAIN_PATH)
        print("train set created successfully")
        test_dataset = append_feature(TEST_PATH)
        print("train set created successfully")

        n_samples, h, w = train_dataset.images.shape

        # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
        # X_train, X_test, y_train, y_test = train_test_split(image_dataset.data, image_dataset.target, test_size=0.1)
        X_train = train_dataset.data
        y_train = train_dataset.target

        X_test = test_dataset.data
        y_test = test_dataset.target

        # print(y_train)
        # print(y_test)

        n_components = 70
        pca = PCA(n_components=n_components).fit(X_train)
        eigenfaces = pca.components_.reshape((n_components, h, w))

        print("Projecting the input data on the eigenfaces orthonormal basis")
        X_train_pca = pca.transform(X_train)
        X_test_pca = pca.transform(X_test)

        eigenface_titles = ["eigenface %d" % i for i in range(eigenfaces.shape[0])]
        # print(eigenfaces.shape[0])
        plot_gallery(eigenfaces, eigenface_titles, h, w)
        # plt.imshow(eigenfaces.shape[0])
        plt.show()

        k = 2
        knn_model = KNeighborsClassifier(n_neighbors=k)
        model_save = knn_model.fit(X_train_pca, y_train)
        saved_model = pickle.dumps(model_save)
        knn_from_pickle = pickle.loads(saved_model)

        # print(model_save)

        y_predict = knn_from_pickle.predict(X_test_pca)
        print(classification_report(y_test, y_predict))
        # salah = 0
        # print("target: "+str(k))
        # for i in range(0, len(y_predict)):
        #     print(str(i) + ". " + str(y_test[i]))
        #     # print("uji: "+str(k))
        #     print(str(i) + ". " + str(y_predict[i]))
        #     print("\n")
        #     if (y_test[i] != y_predict[i]):
        #         salah += 1
# import arrow_rc
# import note_rc
import picture_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

