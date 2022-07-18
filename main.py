from Function.load_save_image import *
from Function.Process_Image import *
import numpy as np
from matplotlib import pyplot as plt
#from scipy import ndimage

#Introduzione e scelta filtro 
print("Progetto Photo Sketching\n")

#Carico l'Immagine

print("Selezionare il numero relativo all'immagine che vogliamo modificare")
print("1 - auto")
print("2 - auto_2")
print("3 - città")
print("4 - città_2")
print("5 - ponte")

auto = load_image("Data/Input/auto.jpg")
auto_2 = load_image("Data/Input/auto2.jpg")
citta = load_image("Data/Input/citta.jpg")
citta_2 = load_image("Data/Input/citta2.jpg")
ponte = load_image("Data/Input/ponte.jpg")


plt.subplot(1,5,1)
plt.imshow(auto)

plt.subplot(1,5,2)
plt.imshow(auto_2)

plt.subplot(1,5,3)
plt.imshow(citta)

plt.subplot(1,5,4)
plt.imshow(citta_2)

plt.subplot(1,5,5)
plt.imshow(ponte)

plt.show()

selezione = str(input())


if selezione == '1':
    nomeImmagine = 'auto'
if selezione == '2':
    nomeImmagine = 'auto2'
if selezione == '3':
    nomeImmagine = 'citta'
if selezione == '4':
    nomeImmagine = 'citta2'
if selezione == '5':
    nomeImmagine = 'ponte'



image = load_image("Data/Input/" + nomeImmagine + ".jpg")

#Photo sketching

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
    
blurred_img = convolve_gray_image(inverted_image, Gaussian_Filter)
    
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
    
save_gray_image(sketched_image, "Data/Output_Photo_Sketching/" + nomeImmagine)
    
print("Salvataggio completatoa")
    
print("Photo sketching completato, la foto è stata salvata in Data/Output_Photo_Sketching")


