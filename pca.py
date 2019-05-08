from __future__ import print_function

import pickle


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
from sklearn.metrics import classification_report, accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

TRAIN_PATH = "Grayscale/train"
TEST_PATH = "Grayscale/test"
# cats = [cats for cats in os.listdir(PATH+"\\.")]
    

def append_feature(PATH):

    images = []
    target = []
    flatten_images = []

    for i, dir_images in zip(range(25),os.listdir(PATH)):
        for file in os.listdir(PATH+"\\{}".format(dir_images)):
            dir = os.path.join(PATH+"\\{}".format(dir_images),file)
            #get images
            img = cv2.imread(dir,0)
            # tambahkan preprocessing
            flatten_images.append(img.flatten())
            images.append(img)
            target.append(dir_images)

    flatten_images = np.array(flatten_images)
    images = np.array(images)
    target = np.array(target)

    return Bunch(data = flatten_images,
                target = target,
                target_names = target,
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

def doPCA(image_set, h, w):
    n_components = 20
    pca = PCA(n_components=n_components).fit(image_set)
    eigenfaces = pca.components_.reshape((n_components, h, w))


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


    n_components = 22
    pca = PCA(n_components=n_components).fit(X_train)
    eigenfaces = pca.components_.reshape((n_components, h, w))

    print("Projecting the input data on the eigenfaces orthonormal basis")
    X_train_pca = pca.transform(X_train)
    X_test_pca = pca.transform(X_test)


    # ni paling banyak benarnya dari 1-10 k nya

    k=1
    knn_model = KNeighborsClassifier(n_neighbors=k)
    model_save = knn_model.fit(X_train_pca, y_train)
    saved_model = pickle.dumps(model_save)
    knn_from_pickle = pickle.loads(saved_model)

    # print(model_save)


    y_predict = knn_from_pickle.predict(X_test_pca)
    # print(accuracy_score(y_test, y_predict))
    salah = 0
    # print("target: "+str(k))
    for i in range(0,len(y_predict)):
        print(str(i)+". "+str(y_test[i]))
        # print("uji: "+str(k))
        print(str(i)+". "+str(y_predict[i]))
        print("\n")
        if (y_test[i]!=y_predict[i]):
            salah+=1

    benar = len(y_predict) - salah
    akurasi = benar/len(y_predict) * 100
    print("jumlah ="+str(len(y_predict)))
    print("salah ="+str(salah))
    print("benar ="+str(benar))
    print("akurasi ="+str(akurasi))
    # print(confusion_matrix(y_test, y_predict))
    print(classification_report(y_test, y_predict))

    eigenface_titles = ["eigenface %d" % i for i in range(eigenfaces.shape[0])]
    plot_gallery(eigenfaces, eigenface_titles, h, w)

    # plt.show()


if __name__ == "__main__":
    main()
    pass
