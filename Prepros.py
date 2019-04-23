import os
import cv2
import numpy as np
from PIL import Image

url_class = 'Dataset/Face/'
classes = os.listdir(url_class)

print("Jumlah Kelas : {}".format(len(classes)))
print("Nama Kelas : {}".format(classes))

for category in classes:
    path = os.path.join(url_class, category)
    print(category)
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path, img))

        # Add contras image
        contrast_img = cv2.addWeighted(img_array, 1.5, np.zeros(img_array.shape, img_array.dtype), 0, 0)

        # Face Detection library
        face_casecade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

        faces = face_casecade.detectMultiScale(contrast_img, 1.3, 1)

        for (x, y, w, h) in faces:
            cv2.rectangle(contrast_img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = contrast_img[y:y + h, x:x + w]
            roi_color = contrast_img[y:y + h, x:x + w]

        # # crop - get center
        # height, width = roi_color.shape[0:2]
        # startRow = int(height * .15)
        # startCol = int(width * .15)
        # endRow = int(height * .90)
        # endCol = int(width * .90)
        # croppedImage = roi_color[startRow:endRow, startCol:endCol]


        # Preprocessing
        gaussian = cv2.GaussianBlur(roi_color, (3, 3), 3)

        gray = cv2.cvtColor(gaussian, cv2.COLOR_BGR2GRAY)
        lapl = cv2.Laplacian(gray, cv2.CV_16S, 5)

        abs_dst = cv2.convertScaleAbs(lapl)

        dim = (300, 300)
        resized_lapl = cv2.resize(abs_dst, dim, interpolation=cv2.INTER_AREA)
        resized_gray = cv2.resize(gray, dim, interpolation=cv2.INTER_AREA)

        cv2.imshow("grayscale",gray)
        cv2.imshow("laplacian", resized_lapl)

        cv2.waitKey(0)

        # Save Image
        # ROI with Laplacian
        hasil = url_class + category + '/ROI_LAPL_{}_{}.jpg'.format(category, img)
        cv2.imwrite(hasil, resized_lapl)
        print("{} gambar {} tersimpan".format(category,img))

        # ROI grayscale
        hasil = url_class + category + '/ROI_GRAY_{}_{}.jpg'.format(category, img)
        cv2.imwrite(hasil, resized_gray)
        print("{} gambar {} tersimpan".format(category, img))