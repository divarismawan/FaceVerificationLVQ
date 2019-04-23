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

PATH = "D:/TUGAS/FaceVerificationLVQ/LOG"

cats = [cats for cats in os.listdir(PATH+"\\.")]

# print(cats)
# print(class_folders)

def append_feature():

    images = []
    target = []
    flatten_images = []

    for i, dir_images in zip(range(10),os.listdir(PATH)):
        for file in os.listdir(PATH+"\\{}".format(dir_images)):
            dir = os.path.join(PATH+"\\{}".format(dir_images),file)
            #get images
            img = cv2.imread(dir)
            flatten_images.append(img.flatten())
            #append images
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


def main():

    print("add dataset into numpy array")
    image_dataset = append_feature()
    print("success")

    n_samples, h, w, n = image_dataset.images.shape

    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(image_dataset.data, image_dataset.target, test_size=0.1)

    print(X_test.shape)

    n_components = 6

    pca = PCA(n_components=n_components, svd_solver='randomized',
          whiten=True).fit(X_train)

    # eigenfaces = pca.components_.reshape((n_components, 10, 10))

    print("Projecting the input data on the eigenfaces orthonormal basis")
    X_train_pca = pca.transform(X_train)
    X_test_pca = pca.transform(X_test)
    print(X_train_pca)


if __name__ == "__main__":
    main()
    pass
