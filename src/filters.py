import numpy as np
from scipy.fftpack import *
import imageio
import matplotlib.pyplot as plt


def low_pass(img, debug=False): # create low pass filter
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


def high_pass(img, debug=False):
    filt = np.ones((radius, radius))

    # TODO: enhance later
    for x in range(radius):
        for y in range(radius):
            if (radius//2 - x)**2 + (radius//2 - y)**2 < (radius//2)**2:
                filt[x][y] = 1

    if debug:
        plt.imshow(filt)
        plt.show()

    return filt


def median(img): # vai deixar esse?
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


