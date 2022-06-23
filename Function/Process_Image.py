import numpy as np
import PIL
import math
#from scipy import ndimage
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
    x = int(x)
    y = int(y)
    c = int(c)
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
    return Image[x,y,c]

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

def Create_Gaussian_Filter(sigma):
    Range = int(sigma*3)
    size = Range * 2 + 1
    
    
    Filter = np.zeros((size,size))
    for l in range(0,size):
        for m in range(0,size):
            Filter[l,m] = compute_gaussian(l - Range, m - Range, sigma)
          
    l1_normalize(Filter)
    return Filter
            

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


def Image_Division(Image1,Image2,scale):
    Final_Image = np.zeros((Image1.shape[0],Image1.shape[1]))
    for x in range(0,Image1.shape[0]):
        for y in range(0,Image1.shape[1]):
            Final_Image[x,y] = Image1[x,y] * 230 / Image2[x,y]
    return Final_Image

#Funzioni per colorize sobel   

def sobel_filters(image,direction):
    Ret_Image = np.zeros(image.shape)
    if (direction == "x"):
        Gx_Filter = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
        #Ret_Image = ndimage.convolve(image,Gx_Filter)
        Ret_Image = convolve_gray_image(image,Gx_Filter)
    elif (direction == "y"):
         Gy_Filter = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
        # Ret_Image = ndimage.convolve(image,Gy_Filter)
         Ret_Image = convolve_gray_image(image,Gy_Filter)

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

 
def isteresi(img,strong,weak):
    Ret_Image = np.zeros(img.shape)
    for x in range(1,img.shape[0]):
        for y in range(1,img.shape[1]):
            if img[x,y] == strong:
                Ret_Image[x,y] = strong
            elif img[x,y] == weak:
                if ((img[x-1,y-1] == strong) or (img[x-1,y] == strong) or (img[x-1,y+1] == strong) or (img[x,y-1] == strong) or (img[x,y+1] == strong) or (img[x+1,y-1] == strong) or (img[x+1,y] == strong) or (img[x+1,y+1] == strong)):
                    Ret_Image[x,y] = strong
    return Ret_Image
    
    
def Create_bilateral_filter(image,gaussFilter,cx,cy,cc,sigma):
    
    Color_gaussian_filter = np.zeros(gaussFilter.shape)
    
    for x in range(0,gaussFilter.shape[0]):
        for y in range(0,gaussFilter.shape[1]):
            ax = cx - gaussFilter.shape[0]/2 + x
            ay = cy - gaussFilter.shape[1]/2 + y
            
            differenza = clamped_pixel(image, ax, ay, cc) - clamped_pixel(image, cx, cy, cc) 
            
            var = np.power(sigma,2)
            
            c = 2 * np.pi * var
            
            p = -(np.power(differenza,2)/(2*var))
            
            e = np.exp(p)
            
            val = e / c
            
            Color_gaussian_filter[x,y] = val
            
    bf = np.zeros(gaussFilter.shape)
    
    for x in range(0,bf.shape[0]):
        for y in range(0,bf.shape[1]):
            bf[x,y] = gaussFilter[x,y] * Color_gaussian_filter[x,y]
    
    l1_normalize(bf)
    
    return bf
    
def bilateral_filter(img,sigma1,sigma2):
   gaussian_filter = Create_Gaussian_Filter(sigma1)
   Ret_Image = np.zeros(img.shape)
   
   for c in range(0,img.shape[2]):
       for x in range(0,img.shape[0]):
           for y in range(0,img.shape[1]):
             bf = Create_bilateral_filter(img, gaussian_filter, x, y, c, sigma2)
             somma = 0
             
             for x2 in range(0,gaussian_filter.shape[0]):
                 for y2 in range(0,gaussian_filter.shape[1]):
                     
                     ax = x - bf.shape[0] / 2 + x2
                     ay = y - bf.shape[1] / 2 + y2
                     
                     somma = somma + 2 * clamped_pixel(img, ax, ay, c)
            
             Ret_Image[x,y,c] = somma

   return Ret_Image


def Final_Cartoon(Image_blurred,edge_mask):
    for x in range(0,edge_mask.shape[0]):
        for y in range(0,edge_mask.shape[1]):
            if edge_mask[x,y] == 255:
                Image_blurred[x,y,0] = 0
                Image_blurred[x,y,1] = 0
                Image_blurred[x,y,2] = 0
    return Image_blurred
                    
                

    
    
    
    
    
    
            
            