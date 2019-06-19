import numpy as np
from scipy.fftpack import fft2, ifft2, fftshift
import imageio
import matplotlib.pyplot as plt
from skimage.util import random_noise
from matplotlib.colors import LogNorm


def diagonal_noise(img, gap):
    """
    Create lines for diagonal moiré pattern

    gap: number of pixels between black pixels
    """
    img_noise = np.copy(img)

    for x in range(img_noise.shape[0]):
        for y in range(img_noise.shape[1]):
            if( (x*img_noise.shape[0]+y) % gap == 0):
                img_noise[x,y] = 0

    return img_noise


def horizontal_noise(img, gap):
    """
    Create black lines for horizontal moiré pattern

    gap: number of rows between black rows
    """
    img_noise = np.copy(img)

    # black out a row in every [gap]
    for x in range(0, img_noise.shape[0], gap):
        for y in range(img_noise.shape[1]):
            img_noise[x,y] = 0

    return img_noise


def vertical_noise(img, gap):
    """
    Create lines for vertical moiré pattern

    gap: number of cols between black cols
    """
    img_noise = np.copy(img)

    # black out a column in every [gap]
    for x in range(img_noise.shape[0]):
        for y in range(0, img_noise.shape[1], gap):
            img_noise[x,y] = 0

    return img_noise


