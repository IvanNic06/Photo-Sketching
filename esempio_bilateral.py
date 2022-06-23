from Function.load_save_image import *
from Function.Process_Image import *
import cv2
import numpy as np
from scipy import ndimage

image = load_image("Data/Input/Photo1.jpg")

width = image.shape[0]
height = image.shape[1]
channels = image.shape[2]

bilater = bilateral_filter(image, 1, 1)