import numpy as np
import PIL

#Dato in input un immagine (array) restituisce la versione disegnata a matita

def Photo_Sketching(Image):
    return



#Converto in immagine bianco e nero

def RGB_TO_GRAY(Image):
    width = Image.shape[0]
    height = Image.shape[1]
    gray_image = np.zeros((Image.shape[0],Image.shape[1]))
    
    for x in range(0,width):
        for y in range(0,height):
            gray_image[x,y] = 0.299 * Image[x,y,0] + 0.587 * Image[x,y,1] + 0.114 * Image[x,y,2]
    
    gray_image = np.floor(gray_image)
    
    return gray_image  

#Resitituisce l'Immagine invertita di quella in scala di grigi 

def Invert_Image(gray_image):
    width = gray_image.shape[0]
    height = gray_image.shape[1]
    inverted_image = np.zeros((gray_image.shape[0],gray_image.shape[1]))
    
    for x in range(0,width):
        for y in range(0,height):
            inverted_image[x,y] = 255 - gray_image[x,y]
    
    inverted_image = np.floor(inverted_image)
    
    return inverted_image
