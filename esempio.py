from Function.load_save_image import *
from Function.Photo_Sketching import *

image = load_image("Data/Input/Photo1.jpg")

width = image.shape[0]
height = image.shape[1]
channels = image.shape[2]

print("L'immagine ha una risoluzione di " + str(width) + "*" + str(height) + " per " + str(channels) + " canali")

print(np.zeros((5,5)))

gray_image = RGB_TO_GRAY(image)

inverted_image = Invert_Image(gray_image)

save_gray_image(inverted_image, "Photo3 modificata")