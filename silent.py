
import numpy as np
import src.noises, src.filters
from scipy.fftpack import fftn, ifftn, fftshift
import imageio
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import sys



def rgb2gray(rgb):      # pass image from RGB to gray levels
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])


def noise_menu():
    print("Choose three options (e.g. 3 2 0):")
    print("(0) No noise")
    print("(1) Horizontal noise")
    print("(2) Vertical noise")
    print("(3) Diagonal noise")

    options = [int(opt) for opt in input().split()]

    return options


def filter_menu():
    print(" Choose four filter options (e.g. 2 1 3 0)")
    print("(0) No filter")
    print("(1) Median filter")
    print("(2) Cut filter")
    print("(3) Low pass filter")
    print("(4) High pass filter")

    options = [int(opt) for opt in input().split()]

    return options


if __name__ == '__main__':

    if sys.argc != 2:
        print('usage: python silent.py <INPUT IMAGE>')
        exit(0)

    img_orig = imageio.imread(sys.argv[1])

    # Convert image to gray levels
    img_gray = rgb2gray(img_orig)

    print('Image dimensions:')
    print(img_gray.shape)

    # Show original grayscale image
    plt.imshow(img_gray, cmap='gray')
    plt.show()

    # Choose and apply noise functions
    noise_options = noise_menu()

    noises = {
        1: src.noises.horizontal,
        2: src.noises.vertical,
        3: src.noises.diagonal,
    }

    img_gray_noisy = np.copy(img_gray)

    for noise_opt in noise_options:
        img_gray_noisy = noises[noise_opt](img_gray_noisy, 3)
        plt.imshow(img_gray_noisy, cmap='gray')
        plt.show()

    # Choose and apply filter functions
    filter_options = filter_menu()
    filters = {
        1: src.filters.median,
        2: src.filters.cut,
        3: src.filters.low_pass,
        4: src.filters.high_pass,
    }

    # Apply chosen noises
    img_gray_filtered = np.copy(img_gray_noisy)

    for filter_opt in filter_options:
        img_gray_noisy = filters[filter_opt](img_gray_filtered)
        plt.imshow(img_filtered, cmap='gray')
        plt.show()


    # TODO: RELOCATE THIS PART OF THE CODE
    if(option == 1):
        img_filtered = median_filter(img)       #aply median filter

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

