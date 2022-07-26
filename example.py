if __name__ == "__main__":
    from Function.load_save_image import *
    from Function.Process_Image import *
    import numpy as np
    from matplotlib import pyplot as plt
    import cv2
    import time
    import multiprocessing as mp
    import os
    #from scipy import ndimage

    #Introduzione e scelta filtro 
    print("Progetto Photo Sketching\n")

    #Carico l'Immagine

    print("Selezionare il numero relativo all'immagine che vogliamo modificare")
    print("1 - Dog")
    print("2 - Iguana")
    print("3 - Auto")
    print("4 - Ponte")
    print("5 - Città")


    dog = load_image("Data/Input/dog.jpg")
    iguana = load_image("Data/Input/iguana.jpg")
    melisa = load_image("Data/Input/auto.jpg")
    ponte = load_image("Data/Input/ponte.jpg")
    citta = load_image("Data/Input/città.jpg")


    plt.subplot(1,5,1)
    plt.imshow(dog)
    plt.xlabel("Dog")
    plt.xticks([])
    plt.yticks([])

    plt.subplot(1,5,2)
    plt.imshow(iguana)
    plt.xlabel("Iguana")
    plt.xticks([])
    plt.yticks([])

    plt.subplot(1,5,3)
    plt.imshow(melisa)
    plt.xlabel("Auto")
    plt.xticks([])
    plt.yticks([])

    plt.subplot(1,5,4)
    plt.imshow(ponte)
    plt.xlabel("Ponte")
    plt.xticks([])
    plt.yticks([])

    plt.subplot(1,5,5)
    plt.imshow(citta)
    plt.xlabel("Città")
    plt.xticks([])
    plt.yticks([])


    plt.show()

    selezione = str(input())


    if selezione == '1':
        nomeImmagine = 'dog'
    if selezione == '2':
        nomeImmagine = 'iguana'
    if selezione == '3':
        nomeImmagine = 'auto'
    if selezione == '4':
        nomeImmagine = 'ponte'
    if selezione == '5':
        nomeImmagine = 'città'

    #image = load_image("Data/Input/" + nomeImmagine + ".jpg")
    image = load_image("Data/Input/" + nomeImmagine + ".jpg")
    #Photo sketching
    Multicore = str(input("Vuoi usare più core? "))

    if Multicore == "si":
        print("Hai a disposizione " + str(mp.cpu_count()) + " core")
        numero_core = int(input("Quanti core usare? "))

    
    
    print("Fase 1: RGB TO GRAY")

    gray = RGB_TO_GRAY(image)

    print("FASE 1 COMPLETATA")



    print("FASE 2: INVERT IMAGE")

    inverted_image = Invert_Image(gray)

    print("FASE 2 COMPLETATA")



    print("FASE 3: GAUSSIAN BLUR")

    Gaussian_Filter = Create_Gaussian_Filter(5)

    print(str(Gaussian_Filter.shape[0]) + " x " + str(Gaussian_Filter.shape[1]))

    #blurred = convolve2d(gray,Gaussian_Filter)
    blurred = convolve_image_2(inverted_image,Gaussian_Filter)

    print("FASE 3 COMPLETATA")



    print("FASE 4: INVERT BLURRED IMAGE")

    inverted_blurred_img = Invert_Image(blurred)

    print("FASE 4 COMPLETATA")



    print("FASE 5: SKETCH IMAGE")

    sketched_image = Image_Division(gray, inverted_blurred_img, 255)

    print("FASE 5 COMPLETATA")



    save_gray_image(sketched_image, "Data/Output/SKETCHED")
