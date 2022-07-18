import numpy as np
import PIL
import math
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


def clamped_pixel(Image,x,y,c):
    x = math.floor(x)
    y = math.floor(y)
    c = math.floor(c)
    if (x < 0):
        x = 0
    if (x >= Image.shape[0]):
        x = Image.shape[0] - 1
    if (y < 0):
        y = 0
    if (y >= Image.shape[1]):
        y = Image.shape[1] - 1
    if (c < 0):
        c = 0
    if (c >= Image.shape[2]):
        c = Image.shape[2] - 1    
    return int(Image[x,y,c])

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



def compute_gaussian(x,y,sigma):
    sigma2 = sigma*sigma
    return 1.0/(2*np.pi*sigma2)*np.exp(-(x*x+y*y)/(2*sigma2))


def l1_normalize(Image):
    somma = 0
    for i in range(0,Image.shape[0]):
        for j in range(0,Image.shape[1]):
            somma = somma + Image[i,j]
    for i in range(0,Image.shape[0]):
        for j in range(0,Image.shape[1]):
            Image[i,j] = Image[i,j] / somma
    return

#Funzione che crea un filtro gaussiano

def Create_Gaussian_Filter(sigma):
    Range = int(sigma*3)
    size = Range * 2 + 1
    
    
    Filter = np.zeros((size,size))
    for l in range(0,size):
        for m in range(0,size):
            Filter[l,m] = compute_gaussian(l - Range, m - Range, sigma)
          
    l1_normalize(Filter)
    return Filter
            
#Effettua convoluzione per immagini in gray scale

def convolve_gray_image(Image,Filter):
    filter_offset = math.floor(Filter.shape[0] / 2)
    Ret_Image = np.zeros(Image.shape)

        
        
    #Per ogni pixel dell'immagine
    for i in range(0,Image.shape[0]):
       for j in range(0,Image.shape[1]):
            somma = 0
            for l in range(-filter_offset,filter_offset+1):
                for m in range(-filter_offset,filter_offset+1):
                   a = clamped_pixel_gray(Image, i-l, j-m)
                   b = Filter[filter_offset-l,filter_offset-m]
                   somma = somma + (a * b)
            Ret_Image[i,j] = somma
    return Ret_Image
 

#Effettua convoluzione per immagini a colori

def convolve_image(Image,Filter):
    filter_offset = int(Filter.shape[0] / 2)
    Ret_Image = np.zeros(Image.shape)

        
        
    #Per ogni pixel dell'immagine
    for k in range(0,Image.shape[2]):
        for i in range(0,Image.shape[0]):
            for j in range(0,Image.shape[1]):
                somma = 0
                for l in range(-filter_offset,filter_offset+1):
                    for m in range(-filter_offset,filter_offset+1):
                       a = clamped_pixel(Image, i-l, j-m, k)
                       b = Filter[filter_offset-l,filter_offset-m]
                       somma = somma + a * b
                Ret_Image[i,j,k] = somma
    return Ret_Image

#Funzione che effetua la divisione dei valori dei pixel tra 2 immagini 

def Image_Division(Image1,Image2,scale):
    Final_Image = np.zeros((Image1.shape[0],Image1.shape[1]))
    for x in range(0,Image1.shape[0]):
        for y in range(0,Image1.shape[1]):
            if Image2[x,y] == 0:
                Final_Image[x,y] = Image1[x,y] * 255 / (Image2[x,y] + 1)
            else:
                Final_Image[x,y] = Image1[x,y] * 255 / Image2[x,y]
    return Final_Image





    




    
    
            
            