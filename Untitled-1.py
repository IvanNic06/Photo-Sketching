from Function.load_save_image import *
from Function.Process_Image import *
import cv2
import numpy as np

Image = np.array([[[200,0,100],[20,10,128],[200,44,76],[200,0,100],[20,10,128],[200,44,76]],[[200,0,100],[20,10,128],[200,44,76],[200,0,100],[20,10,128],[200,44,76]],[[200,0,100],[20,10,128],[200,44,76],[200,0,100],[20,10,128],[200,44,76]]])

#bilateral = bilateralFilter(Image,0.5,0.3)
bilateral = cv2.bilateralFilter(Image, d=7, sigmaColor=200,sigmaSpace=200)

print(bilateral)