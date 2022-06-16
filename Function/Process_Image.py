import numpy as np
import PIL
import math
from scipy import ndimage
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
            
    
def convolve_Image(Image,Filter):
   
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
            Final_Image[x,y] = Image1[x,y] * 230 / Image2[x,y]
    return Final_Image

#Funzioni per colorize sobel   

def sobel_filters(image,direction):
    
    if (direction == "x"):
        Gx_Filter = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
        Ret_Image = ndimage.convolve(image,Gx_Filter)
    elif (direction == "y"):
         Gy_Filter = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
         Ret_Image = ndimage.convolve(image,Gy_Filter)

    return Ret_Image


def Normalize(Image):
    
    Nimg = Image / np.max(Image)
    
    return Nimg
    
def NonMaxSup(Mag, Grad):
    img = np.zeros(Mag.shape)
    for i in range(1, int(Mag.shape[0]) - 1):
        for j in range(1, int(Mag.shape[1]) - 1):
            if((Grad[i,j] >= -22.5 and Grad[i,j] <= 22.5) or (Grad[i,j] <= -157.5 and Grad[i,j] >= 157.5)):
                if((Mag[i,j] > Mag[i,j+1]) and (Mag[i,j] > Mag[i,j-1])):
                    img[i,j] = Mag[i,j]
                else:
                    img[i,j] = 0
            if((Grad[i,j] >= 22.5 and Grad[i,j] <= 67.5) or (Grad[i,j] <= -112.5 and Grad[i,j] >= -157.5)):
                if((Mag[i,j] > Mag[i+1,j+1]) and (Mag[i,j] > Mag[i-1,j-1])):
                    img[i,j] = Mag[i,j]
                else:
                    img[i,j] = 0
            if((Grad[i,j] >= 67.5 and Grad[i,j] <= 112.5) or (Grad[i,j] <= -67.5 and Grad[i,j] >= -112.5)):
                if((Mag[i,j] > Mag[i+1,j]) and (Mag[i,j] > Mag[i-1,j])):
                    img[i,j] = Mag[i,j]
                else:
                    img[i,j] = 0
            if((Grad[i,j] >= 112.5 and Grad[i,j] <= 157.5) or (Grad[i,j] <= -22.5 and Grad[i,j] >= -67.5)):
                if((Mag[i,j] > Mag[i+1,j-1]) and (Mag[i,j] > Mag[i-1,j+1])):
                    img[i,j] = Mag[i,j]
                else:
                    img[i,j] = 0

    return img
    

def thresholding(img,low,high,strong,weak):
    Ret_Image = np.zeros(img.shape)
    for x in range(0,img.shape[0]):
        for y in range(0,img.shape[1]):
            
            if img[x,y] >= high:
                Ret_Image[x,y] = strong
            elif img[x,y] < high and img[x,y] >= low:
                Ret_Image[x,y] = weak
            else:
                Ret_Image[x,y] = 0
    return Ret_Image

 

#def make_bilateral_filter(img)
           
    
# def bilateral_filter(img,sigma1,sigma2):
#     Filtro = Create_Gaussian_Filter(sigma1)
    
#     Ret_Image = np.zeros(img.shape)
    
         

    
    
    
    
    
    
    
    
    
    
    
            
            