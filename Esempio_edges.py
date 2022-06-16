from Function.load_save_image import *
from Function.Process_Image import *
import cv2

image = load_image("Data/Input/Photo1.jpg")

width = image.shape[0]
height = image.shape[1]
channels = image.shape[2]

gray = RGB_TO_GRAY(image)

Filter = Create_Gaussian_Filter(1)
blurred_gray = convolve_Image(gray,Filter)

img_n = cv2.normalize(blurred_gray, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
edges = cv2.Canny(img_n,100,200)


color = cv2.bilateralFilter(image,9,250,250)
cartoon = cv2.bitwise_and(color,color,mask=edges)

save_gray_image(cartoon, "Y")
