import os
import cv2
import numpy as np
from PIL import Image

def check_folder(folder_name):
    if os.path.isdir("Grayscale/train/"+folder_name) is False:
        os.mkdir("Grayscale/gabung/"+folder_name) #create folder
        os.mkdir('Grayscale/test/'+folder_name) #create folder
        os.mkdir("Grayscale/train/"+folder_name) #create folder
    pass



count_file = 0

url_sumber = 'Dataset/tes/'

url_tujuan = 'Grayscale/test/'
url_gabung = 'Grayscale/gabung/'

classes = os.listdir(url_sumber)

gray_class =  os.listdir(url_tujuan)

print("Jumlah Kelas : {}".format(len(classes)))
print("Jumlah Kelas : {}".format(len(url_gabung)))
print("Nama Kelas : {}".format(classes))


for folder in classes:
    count_file += 1
    # Cek if file already exist
    if(count_file > 42 and count_file <100):
        if(folder in gray_class):

            # check_folder(folder)

            # print("Test")

            path = os.path.join(url_sumber, folder)
            print(folder)
            for img in os.listdir(path):
                img_array = cv2.imread(os.path.join(path, img))

                # Add contras image
                contrast_img = cv2.addWeighted(img_array, 1.5, np.zeros(img_array.shape, img_array.dtype), 0, 0)

                # Face Detection library
                face_casecade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
                eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

                faces = face_casecade.detectMultiScale(contrast_img, 1.3, 1)

                print(faces)

                for (x, y, w, h) in faces:
                    cv2.rectangle(contrast_img, (x, y), (x + w, y + h), (255, 0, 0), 0)
                    roi_gray = contrast_img[y:y + h, x:x + w]
                    roi_color = contrast_img[y:y + h, x:x + w]

                dim = (300, 300)
                gray = cv2.cvtColor(roi_color, cv2.COLOR_BGR2GRAY)
                resized_gray = cv2.resize(gray, dim, interpolation=cv2.INTER_AREA)

                # cv2.imshow("grayscale", gray)
                # cv2.waitKey(0)

                hasil  = url_tujuan + folder + '/ROI_GRAY_{}_{}.jpg'.format(folder, img)
                hasil2 = url_gabung + folder + '/ROI_GRAY_{}_{}.jpg'.format(folder, img)
                cv2.imwrite(hasil, resized_gray)
                cv2.imwrite(hasil2, resized_gray)

            print("{} gambar {} tersimpan".format(folder, img))



# #Edit
#         # # crop - get center
#         # height, width = roi_color.shape[0:2]
#         # startRow = int(height * .15)
#         # startCol = int(width * .15)
#         # endRow = int(height * .90)
#         # endCol = int(width * .90)
#         # croppedImage = roi_color[startRow:endRow, startCol:endCol]
#
#
#         # Preprocessing
#         gaussian = cv2.GaussianBlur(roi_color, (3, 3), 3)
#
#         gray = cv2.cvtColor(gaussian, cv2.COLOR_BGR2GRAY)
#         lapl = cv2.Laplacian(gray, cv2.CV_16S, 5)
#
#         abs_dst = cv2.convertScaleAbs(lapl)
#
#         dim = (300, 300)
#         resized_lapl = cv2.resize(abs_dst, dim, interpolation=cv2.INTER_AREA)
#         resized_gray = cv2.resize(gray, dim, interpolation=cv2.INTER_AREA)
#
#         cv2.imshow("grayscale",gray)
#         cv2.imshow("laplacian", resized_lapl)
#
#         cv2.waitKey(0)
#
#         # Save Image
#         # ROI with Laplacian
#         hasil = url_class + folder + '/ROI_LAPL_{}_{}.jpg'.format(folder, img)
#         cv2.imwrite(hasil, resized_lapl)
#         print("{} gambar {} tersimpan".format(folder,img))
#
#         # ROI grayscale
#         hasil = url_class + folder + '/ROI_GRAY_{}_{}.jpg'.format(folder, img)
#         cv2.imwrite(hasil, resized_gray)
#         print("{} gambar {} tersimpan".format(folder, img))
#
# # End