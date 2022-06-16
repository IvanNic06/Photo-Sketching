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


def clamped_pixel(Image,x,y):
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

def Create_Gaussian_Filter(sigma):
    Range = int(sigma*3)
    size = Range * 2 + 1
    
    
    Filter = np.zeros((size,size))
    for l in range(0,size):
        for m in range(0,size):
            Filter[l,m] = compute_gaussian(l - Range, m - Range, sigma)
          
    l1_normalize(Filter)
    return Filter
            
    
def convolve_image(Image,Filter):
   
    filter_offset = int(Filter.shape[0] / 2)
    Image_ret = np.zeros((Image.shape[0],Image.shape[1]))    
    
    width = Image.shape[0]
    height = Image.shape[1]
    
    for i in range(0,width):
        for j in range(0,height):
            somma = 0
            for l in range(0-filter_offset,filter_offset):
                for m in range(0-filter_offset,filter_offset):
                    a = clamped_pixel(Image, i-l, j-m)
                    b = Filter[filter_offset-l,filter_offset-m]
                    somma = somma + a * b
            Image_ret[i,j] = somma
    return Image_ret
            
def Image_Division(Image1,Image2,scale):
    Final_Image = np.zeros((Image1.shape[0],Image1.shape[1]))
    for x in range(0,Image1.shape[0]):
        for y in range(0,Image1.shape[1]):
            Final_Image[x,y] = Image1[x,y] * 255 / Image2[x,y]
    return Final_Image
            
            
            
            
            
            