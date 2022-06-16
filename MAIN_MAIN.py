from Function.load_save_image import *
from Function.Process_Image import *
import cv2

#Introduzione e scelta filtro 
print("Progetto Image Transformation\n")
print("Selezionare il tipo di effetto da voler applicare all'immagine")
print("Per selezionare il relativo filtro digitare:")
print("1 - Photo sketching")
print("2 - Photo Cartoonifying")
print("3 - Colorize Sobel")

selezione = '1'

#Carico l'Immagine

Numero_immagine = '1'
image = load_image("Data/Input/Photo"+Numero_immagine+".jpg")


#Photo sketching
if selezione == '1':
    print("Hai selezionato Photo sketching")
    
    #Passo 1: Trasformo l'immagine in bianco e nero
    
    print("Fase 1: RGB TO GRAY")
    
    gray_image = RGB_TO_GRAY(image)
    
    print("Fase 1 COMPLETATA\n")
    
    #Passo 2: Inverto l'intensità dei pixel dell'immagine in bianco e nero 
    
    print("Fase 2: INVERT IMAGE")
    
    inverted_image = Invert_Image(gray_image)
    
    print("Fase 2 COMPLETATA\n")
    
    #Passo 3: Applico una sfocatura Gaussiana
    
    print("Fase 3: GAUSSIAN BLUR")
    
    Gaussian_Filter = Create_Gaussian_Filter(1)
    
    blurred_img = convolve_Image(inverted_image, Gaussian_Filter)
    
    print("Fase 3 COMPLETATA\n")
    
    #Passo 4: Inverto la foto dopo aver applicato la sfocatura
    
    print("Fase 4: INVERT BLURRED IMAGE")
    
    inverted_blurred_img = Invert_Image(blurred_img)
    
    print("Fase 4 COMPLETATA\n")
    
    #Passo 5: Procedo con lo sketching dell'immagine
    
    print("Fase 5: IMAGE DIVISION")
    
    sketched_image = Image_Division(gray_image, inverted_blurred_img, 255)
    
    print("Fase 5 COMPLETATA\n")
    
    
    #Passo 6: Salvataggio della foto
    
    print("Salvataggio della foto in corso")
    
    save_gray_image(sketched_image, "Photo"+Numero_immagine+" modificata")
    
    print("Salvataggio completatoa")
    
    print("Photo sketching completato, la foto è stata salvata in Data/Output")
    
elif selezione == '2':
    print("Hai selezionato Photo Cartoonifying")
    
    #Passo 1: Trasformo l'immagine in bianco e nero
    
    print("Fase 1: RGB TO GRAY")
    
    gray_image = RGB_TO_GRAY(image)
    
    print("Fase 1 COMPLETATA\n")
    
    #Passo 2: Riduco il rumore applicando la sfocatura gaussiana
    
    print("Fase 2: GAUSSIAN BLUR")
    
    Gaussian_Filter = Create_Gaussian_Filter(1)
    
    blurred_img = convolve_Image(inverted_image, Gaussian_Filter)
    
    print("Fase 2 COMPLETATA\n")
    
    