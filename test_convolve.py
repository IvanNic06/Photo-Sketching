from Function.load_save_image import *
from Function.Process_Image import *
import cv2
import numpy as np
#from scipy import ndimage

image = load_image("Data/Input/paesaggio.jpg")

width = image.shape[0]
height = image.shape[1]
channels = image.shape[2]

gray = RGB_TO_GRAY(image)

Filter = Create_Gaussian_Filter(1)
blurred_mio = convolve_gray_image(gray, Filter)
#blurred_software = ndimage.convolve(gray, Filter)

save_gray_image(blurred_mio, "Gray_Blurred_mio")
#save_gray_image(blurred_software,"Gray_Blurred_software")


gx = sobel_filters(blurred_mio, 'x')
save_gray_image(gx,"Direzione x")
gx = Normalize(gx)
gy = sobel_filters(blurred_mio, 'y')
save_gray_image(gy,"Direzione y")
gy = Normalize(gy)

Mag = np.hypot(gx,gy)

Mag = Mag * 255

Grad = np.degrees(np.arctan2(gy,gx))

#Non Maximum supression
img_con_Nms = NonMaxSup(Mag, Grad)

save_gray_image(img_con_Nms, "MIO NON MAXIMUM SUPRESSION")



# from Function.load_save_image import *
# from Function.Process_Image import *
# import cv2
# import numpy as np
# from scipy import ndimage

# image = load_image("Data/Input/paesaggio.jpg")

# width = image.shape[0]
# height = image.shape[1]
# channels = image.shape[2]

# gray = RGB_TO_GRAY(image)

# Filter = Create_Gaussian_Filter(1)
# blurred_gray = convolve_gray_image(gray,Filter)

# gx = sobel_filters(blurred_gray, 'x')
# gx = Normalize(gx)
# gy = sobel_filters(blurred_gray, 'y')
# gy = Normalize(gy)

# Mag = np.hypot(gx,gy)

# Mag = Mag * 255

# Grad = np.degrees(np.arctan2(gy,gx))

# #Non Maximum supression
# img_con_Nms = NonMaxSup(Mag, Grad)

# #THresHolding

# Thresh_img = thresholding(img_con_Nms,8, 43, 255, 50)

# afterIsteresi = isteresi(Thresh_img, 255, 50)

# save_gray_image(afterIsteresi, "NUOVA Isteresi")

# bilateral = cv2.bilateralFilter(image, d=7, sigmaColor=200,sigmaSpace=200)

# save_image(bilateral, "NUOVA Bilateral")



# #Fase finale

# final_image = Final_Cartoon(bilateral, afterIsteresi)
# save_image(final_image, "NUOVA CARTOON")