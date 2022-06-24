from Function.load_save_image import *
from Function.Process_Image import *
import cv2
import numpy as np
#from scipy import ndimage

image = load_image("Data/Input/paesaggio.jpg")

print("Fase 4: BILATERAL FILTER")
 
 
#bilateral = cv2.bilateralFilter(image, d=7, sigmaColor=200,sigmaSpace=200)
bilateral=bilateralFilter(image, 1, 0.3)
 
print("Fase 4 COMPLETATA\n")