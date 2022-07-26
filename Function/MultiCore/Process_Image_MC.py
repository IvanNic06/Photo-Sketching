import numpy as np
import PIL
import math
from threading import Thread
#Converto in immagine bianco e nero

def convolve_multi_core(Filter,starty,endy):
    Image = np.load("Image.npy","r+")
    filter_offset = math.floor(Filter.shape[0] / 2)
    Ret_Image = 0
    #Per ogni pixel dell'immagine
    for i in range(0,Image.shape[0]):
       for j in range(starty,endy):
            somma = 0
            for l in range(-filter_offset,filter_offset+1):
                for m in range(-filter_offset,filter_offset+1):
                   a = clamped_pixel_gray(Image, i-l, j-m)
                   b = Filter[filter_offset-l,filter_offset-m]
                   somma = somma + (a * b)
            Image[i,j] = somma
    return Ret_Image


def clamped_pixel_gray(Image,x,y):
    x = int(x)
    y = int(y)
    if (x < 0):
        x = 0
    if (x >= Image.shape[0]):
        x = Image.shape[0] - 1
    if (y < 0):
        y = 0
    if (y >= Image.shape[1]):
        y = Image.shape[1] - 1
    return Image[x,y]


def convolve_multi_core_2(Filter,starty,endy):
    image = np.load("Image.npy","r+")
    filterSize = Filter.shape[0]              #DImensione del filtro
    print(filterSize)
    filterOffset = math.floor(filterSize/2)   #Dimensione metà filtro escluso il centro
    print(filterOffset)

    imageWithPadding = np.zeros((image.shape[0] + filterSize - 1, image.shape[1] + filterSize - 1))     #Aggiungo padding all'immagine dato in input per poter utilizzare il filtro sui pixel del bordo
    imageWithPadding[filterOffset:-filterOffset, filterOffset:-filterOffset] = image

    for i in range(starty,endy):
        for j in range(image.shape[0]):
            #Effettuo il prodotto elemento per elemento delle 2 matrici e poi sommo tutti gli elementi della matrice
            image[j, i] = (Filter * imageWithPadding[j: j+filterSize, i: i+filterSize]).sum()
    return image
    
    
            
            