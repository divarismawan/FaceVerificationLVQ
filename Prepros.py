import os
import cv2

url_class = 'Dataset/Face/'
classes = os.listdir(url_class)

print("Jumlah Kelas : {}".format(len(classes)))
print("Nama Kelas : {}".format(classes))

for category in classes:
    path = os.path.join(url_class, category)
    print(category)
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path, img))

        grey = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)

        # Face Detection
        face_casecade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

        faces = face_casecade.detectMultiScale(img_array, 1.3, 1)

        for (x, y, w, h) in faces:
            cv2.rectangle(grey, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = grey[y:y + h, x:x + w]
            roi_color = grey[y:y + h, x:x + w]

        # cv2.imshow('img', grey)

        # cv2.imshow('roi',roi_color)

        # Preprocessing
        gaussian = cv2.GaussianBlur(roi_gray, (3, 3), 1)

        lapl = cv2.Laplacian(gaussian, cv2.CV_16S, 10)

        abs_dst = cv2.convertScaleAbs(lapl)

        # detected_faces = detect_faces(abs_dst)

        # cv2.imshow("grayscale",img_array)
        # cv2.imshow("hasil grayscale",gaussian)
        cv2.imshow("hasil laplacian", abs_dst)
        # cv2.imshow("hasil laplacian", detected_faces)

        cv2.waitKey(0)
