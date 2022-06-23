from Function.load_save_image import *
from Function.Process_Image import *
import cv2
import numpy as np
from scipy import ndimage

image = load_image("Data/Input/paesaggio.jpg")

width = image.shape[0]
height = image.shape[1]
channels = image.shape[2]

gray = RGB_TO_GRAY(image)

Filter = Create_Gaussian_Filter(1)
blurred_gray = ndimage.convolve(gray,Filter)

gx = sobel_filters(blurred_gray, 'x')
gx = Normalize(gx)
gy = sobel_filters(blurred_gray, 'y')
gy = Normalize(gy)

Mag = np.hypot(gx,gy)

Mag = Mag * 255

Grad = np.degrees(np.arctan2(gy,gx))

#Non Maximum supression
img_con_Nms = NonMaxSup(Mag, Grad)

#THresHolding

Thresh_img = thresholding(img_con_Nms,8, 43, 255, 50)

afterIsteresi = isteresi(Thresh_img, 255, 50)

save_gray_image(afterIsteresi, "Isteresi")

bilateral = cv2.bilateralFilter(image, d=7, sigmaColor=200,sigmaSpace=200)

save_image(bilateral, "Bilateral")



#Fase finale

final_image = Final_Cartoon(bilateral, afterIsteresi)
save_image(final_image, "cartoon")