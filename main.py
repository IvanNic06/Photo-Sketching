from Function.load_save_image import *
from Function.Photo_Sketching import *

#Introduzione e scelta filtro 
print("Progetto Image Transformation\n")
print("Selezionare il tipo di effetto da voler applicare all'immagine")
print("Per selezionare il relativo filtro digitare:")
print("1 - Photo sketching")
print("2 - ")
print("3 - ")

#Carico l'Immagine
image = load_image("Data/Input/Photo1.jpg")
width = image.shape[0]
height = image.shape[1]
channels = image.shape[2]

selezione = str(input())

#Photo sketching
if selezione == '1':
    print("Hai selezionato Photo sketching")
    
    #Passo 1: Trasformo l'immagine in bianco e nero
    
    gray_image = RGB_TO_GRAY(image)
    
    
    #Passo 2: Inverto l'intensità dei pixel dell'immagine in bianco e nero 
    
    inverted_image = Invert_Image(gray_image)
    
    
    #Passo 3: Applico una sfocatura Gaussiana
    
    
    
    
    
    