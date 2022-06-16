from Function.load_save_image import *
from Function.Photo_Sketching import *

image = load_image("Data/Input/Photo3.jpg")

width = image.shape[0]
height = image.shape[1]
channels = image.shape[2]

print("L'immagine ha una risoluzione di " + str(width) + "*" + str(height) + " per " + str(channels) + " canali")


gray_image = RGB_TO_GRAY(image)

print("RGB TO GRAY OK")

inverted_image = Invert_Image(gray_image)

print("Invert_Image OK")

Gaussian_filter = Create_Gaussian_Filter(1)


Image_Example = 255 * np.random.rand(10,10)


Blurred_img = Blur_Image(Image_Example,Gaussian_filter)



blurred_image = Blur_Image(inverted_image,Gaussian_filter)

print("Blur_image OK")

invert_blurred_img = Invert_Image(blurred_image)

print("Invert_Image OK")

sketched_image = Image_Division(gray_image, invert_blurred_img,255)

print("Processo completato")


save_gray_image(sketched_image, "Photo3 modificata")