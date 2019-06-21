
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
    print("Choose up to three options (e.g. 3 2):")
    print("(1) Horizontal noise")
    print("(2) Vertical noise")
    print("(3) Diagonal noise")

    options = [int(opt) for opt in input().split()]

    return options


def filter_menu():
    print(" Choose up to three filter options (e.g. 2 1)")
    print("(1) Median filter")
    print("(2) Cut filter")
    print("(3) Low pass filter")

    options = [int(opt) for opt in input().split()]

    return options


if __name__ == '__main__':

    if len(sys.argv) != 2:
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

    # Choose and apply filter functions
    filter_options = filter_menu()

    filters = {
        1: src.filters.median,
        2: src.filters.cut,
        3: src.filters.low_pass,
    }

    # Apply chosen noises
    img_gray_noisy = np.copy(img_gray)
    for noise_opt in noise_options:
        img_gray_noisy = noises[noise_opt](img_gray_noisy, 3)
        plt.imshow(img_gray_noisy, cmap='gray')
        plt.show()

    # Apply chosen filters
    img_gray_filtered = np.copy(img_gray_noisy)
    for filter_opt in filter_options:
        img_gray_filtered = filters[filter_opt](img_gray_filtered)
        plt.imshow(img_gray_filtered, cmap='gray')
        plt.show()
