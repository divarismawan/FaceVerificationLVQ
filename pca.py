from __future__ import print_function

import numpy as np
from time import time
import logging
import matplotlib.pyplot as plt
import os
import cv2
from sklearn.utils import Bunch

from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import fetch_lfw_people
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

PATH = "D:/0TUGAS TI/FaceVerificationLVQ/Grayscale"
cats = [cats for cats in os.listdir(PATH+"\\.")]
    

def append_feature():

    images = []
    target = []
    flatten_images = []

    for i, dir_images in zip(range(10),os.listdir(PATH)):
        for file in os.listdir(PATH+"\\{}".format(dir_images)):
            dir = os.path.join(PATH+"\\{}".format(dir_images),file)
            #get images
            img = cv2.imread(dir,0)
            # tambahkan preprocessing
            flatten_images.append(img.flatten())
            images.append(img)
            target.append(i)

    flatten_images = np.array(flatten_images)
    images = np.array(images)
    target = np.array(target)

    return Bunch(data = flatten_images,
                target = target,
                target_names = cats,
                images = images,
                descr = "deskripsi"
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
    image_dataset = append_feature()
    print("success")

    n_samples, h, w = image_dataset.images.shape

    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(image_dataset.data, image_dataset.target, test_size=0.1)

    print(type(X_train))

    n_components = 40

    pca = PCA(n_components=n_components).fit(X_train)

    eigenfaces = pca.components_.reshape((n_components, h, w))

    print("Projecting the input data on the eigenfaces orthonormal basis")
    X_train_pca = pca.transform(X_train)
    X_test_pca = pca.transform(X_test)
    print(X_train_pca)

    # k = 5
    # knn_model = KNeighborsClassifier(n_neighbors=k)
    # knn_model.fit(X_train_pca, y_train)
    #
    # y_predict = knn_model.predict(X_test_pca)


    eigenface_titles = ["eigenface %d" % i for i in range(eigenfaces.shape[0])]
    plot_gallery(eigenfaces, eigenface_titles, h, w)

    plt.show()


if __name__ == "__main__":
    main()
    pass
