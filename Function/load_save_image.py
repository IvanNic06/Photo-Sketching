from PIL import Image as pil
import numpy as np


#Carico un'immagine, la trasformo in un array di numpy e lo restituisco in output
def load_image(imagename):
    image = pil.open(imagename)
    data = np.asarray(image)
    return data



#Prendo in input un array e lo converto in un tipo PIL.Image in modo da poter salvare la foto 
def save_image(array,imagename):
    image = pil.fromarray(array.astype(np.uint8))
    image.save(imagename + ".png")
    return


#Prendo in input un array 2x2 e lo converto in un tipo PIL.Image in modo da poter salvare la foto 
def save_gray_image(array,imagename):
    image = pil.fromarray(array)
    image.convert("L").save(imagename + ".png")
    return


    