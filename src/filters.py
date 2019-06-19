import numpy as np
from scipy.fftpack import *
import imageio
import matplotlib.pyplot as plt


# TODO: implement image receival and fourier transformation
# OBS: no longer returns filter, but filtered image
def low_pass(img, radius=50, debug=False):
    """
    Filters image using low pass filter in Fourier domain
    Returns filtered image
    """

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


# TODO: implement (receive img return img)
def high_pass(img, debug=False):
    filt = np.ones((radius, radius))

    for x in range(radius):
        for y in range(radius):
            if (radius//2 - x)**2 + (radius//2 - y)**2 < (radius//2)**2:
                filt[x][y] = 0

    if debug:
        plt.imshow(filt)
        plt.show()

    return filt


def _median(img, x, y, k):
    """
    Computes median for k-neighborhood of img[x,y]
    """
    flat = img[x-k : x+k+1, y-k : y+k+1].flatten()
    flat.sort()
    res[x, y] = flat[len(flat)//2]


def median(img, k=3):
    """
    Changes every pixel to the median of its neighboors
    """
    res = np.copy(img)

    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            if (x-k >= 0 and x+k < m) and (y-k >= 0 and y+k < n):
                res[x, y] = _median(x, y, k)

    return res


def cut(img):
    """
    Applies central horizontal threshold in Fourier spectrum
    """

    # Apply fourier transform and shift
    img_fft = fftn(img)
    img_fft_shift = fftshift(img_fft)

    # Print spectrum before
    plt.imshow(np.abs(img_fft_shift), cmap='gray', norm=LogNorm(vmin=5))
    plt.show()

    # Filter image: remove upper and lower horizontal thirds (1/3)
    img_fft_shift_filtered = np.copy(img_fft_shift)
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            if( x < img.shape[0]//3 or x > img.shape[0]*2//3):
                img_fft_shift_filtered[x,y] = 0

    # Print spectrum after
    plt.imshow(np.abs(img_fft_shift_filtered), cmap='gray', norm=LogNorm(vmin=5))
    plt.show()

    # Return to space domain result image using inverse
    res = ifftn( fftshift(img_fft_shift_filtered) )

    return res


