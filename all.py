
import numpy as np
import src.noises
from scipy.fftpack import fftn, ifftn, fftshift
import imageio
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

def cut(img):   #function for cut image into a block

    img_cut = np.copy(img)  #copy image to image_cut

    #for x in range(img.shape[0]):       # remove image parts to rest only the
    #    for y in range(img.shape[1]):   # 1/3 center of it in vertical and horizontal
    #        if( x < img.shape[0]//3 or x > img.shape[0]*2//3 \
    #        or y < img.shape[1]//3 or y > img.shape[1]*2//3):
    #            img_cut[x,y] = 0  

    for x in range(img.shape[0]):       # remove image parts to rest only the
        for y in range(img.shape[1]):   # 1/3 center of it in horizontal
            if( x < img.shape[0]//3 or x > img.shape[0]*2//3):
                img_cut[x,y] = 0 

    return img_cut  #return cut image

def low_pass(radius, final_shape, debug=False): # create low pass filter
    filt = np.zeros((radius, radius))   #create matrix for new filter

    # TODO: enhance later   
    for x in range(radius):     #create a circular area with values 1
        for y in range(radius): # this will be the pass region
            if (radius//2 - x)**2 + (radius//2 - y)**2 < (radius//2)**2:
                filt[x][y] = 1

    print(filt.shape)
    plt.imshow(filt, cmap='gray')
    plt.show()

    # calculate padding shape
    # TODO: fix even/odd cases
    aux1 = final_shape[0] - filt.shape[0]   #calculate the difference betwen
    if(aux1%2 == 0):                         #the circular filter and the real image
        pad_cols = ( (final_shape[0] - filt.shape[0])//2, \
                    (final_shape[0] - filt.shape[0])//2)
    else:                                   #verify size based on the difference
        pad_rows = ( (final_shape[0] - filt.shape[0])//2+1, \
                     (final_shape[0] - filt.shape[0])//2+1 )

    aux2 = final_shape[1] - filt.shape[1]   #calculate the difference betwen
    if(aux2%2 == 0):                        #the circular filter and the real image
        pad_cols = ( (final_shape[1] - filt.shape[1])//2, \
                     (final_shape[1] - filt.shape[1])//2)
    else:                                   #verify size based on the difference
        pad_cols = ( (final_shape[1] - filt.shape[1])//2+1, \
                     (final_shape[1] - filt.shape[1])//2+1)

    pad_shape = (pad_rows, pad_cols)

    # padding
    filt = np.pad(filt, pad_shape, 'constant', constant_values=0)
                                             #check for even numbers
    if(aux1%2 != 0 and aux2%2 != 0):         #if needed remove row and/or coluns
        filt = filt[0:filt.shape[0]-1, 0:filt.shape[1]-1]
    elif(aux1%2 != 0 and aux2%2 == 0):       
        filt = filt[0:filt.shape[0]-1, 0:filt.shape[1]]
    elif(aux1%2 == 0 and aux2%2 != 0):
        filt = filt[0:filt.shape[0], 0:filt.shape[1]-1]

    print(filt.shape)
    plt.imshow(filt, cmap='gray')
    plt.show()

    if debug:
        plt.imshow(filt)
        plt.show()

    return filt

def median_filter(img): # vai deixar esse?
    k = 3
    m, n = img.shape
    out = np.copy(img)
    for x in range(0, m):
        for y in range(0, n):
            if((x-k >= 0 and x+k < m) and (y-k >= 0 and y+k < n)):
                flat = img[x-k:x+k+1,y-k: y+k+1].flatten()
                flat.sort()
                out[x, y] = flat[len(flat)//2]
    return out


def rgb2gray(rgb):      # pass image from RGB to gray levels
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

#main
img = imageio.imread('images/cat_original.jpg')     #read original image
img = rgb2gray(img)                                 # pass image too grey levels

print(img.shape)                        #show image shape

plt.imshow(img, cmap='gray')            #show original image
plt.show()

print("Press 1 to horizontal noise:")
print("Press 2 to vertical noise:")
print("Press 3 to horizontal and vertical noise:")
print("Press 4 to diagonal noise:")
print("Press 5 to horizontal, vertical and diagonal noise:")

option = int(input())           #option for aply noises

if(option == 1):
    img = src.noises.horizontal(img, 3)

elif(option == 2):
    img = src.noises.vertical(img, 3)

elif(option == 3):
    img = src.noises.horizontal(img, 3)
    img = src.noises.vertical(img, 3)

elif(option == 4):
    img = src.noises.diagonal(img, 3)

elif(option == 5):
    img = src.noises.horizontal(img, 3)
    img = src.noises.vertical(img, 3)
    img = src.noises.diagonal(img, 3)

else:
    print("valor inválido")

plt.imshow(img, cmap='gray')            #show noise image
plt.show()

print("Press 1 to median filter:")
print("Press 2 to fourier cut filter:")
print("Press 3 to fourier low pass filter:")

option = int(input())           #option for filter

if(option == 1):
    img_filtered = median_filter(img)       #aply median filter
    plt.imshow(img_filtered, cmap='gray')   #show filtered image
    plt.show()

elif(option == 2):
    img_fft = fftn(img)                             #aply fourier transform
    img_fft_shift = fftshift(img_fft)               #aply shift into the fourier image
    plt.imshow(np.abs(img_fft_shift), cmap='gray', norm=LogNorm(vmin=5))
    plt.show()                                      #show the spectrum
    img_fft_shift_filtered = cut(img_fft_shift)     #cut the shifted image
    plt.imshow(np.abs(img_fft_shift_filtered), cmap='gray', norm=LogNorm(vmin=5))
    plt.show()                                      #show cut spectrum
    res = ifftn( fftshift(img_fft_shift_filtered) ) # create result image using inverse
    plt.imshow(np.abs(res), cmap='gray', norm=LogNorm(vmin=5))
    plt.show()                                      #show the result image

elif(option == 3):
    img_fft = fftn(img)                             #aply fourier transform
    img_fft_shift = fftshift(img_fft)               #aply shift into the fourier image
    plt.imshow(np.abs(img_fft_shift), cmap='gray', norm=LogNorm(vmin=5))
    plt.show()                                      #show the spectrum
    filt = low_pass(501, img.shape)                 #create low pass filter
    img_fft_shift_filtered = img_fft_shift * filt   #aply the filter in the fourier image
    plt.imshow(np.abs(img_fft_shift_filtered), cmap='gray', norm=LogNorm(vmin=5))
    plt.show()                                      #show low filter pass spectrum 
    res = ifftn( fftshift(img_fft_shift_filtered) ) # create result image using inverse
    plt.imshow(np.abs(res), cmap='gray', norm=LogNorm(vmin=5))
    plt.show()                                      #show the result image

else:
    print("valor inválido")

