#
#
#
#  NOISE GENERATION FUNCTIONS
#
# take image, return image with noise
#
import numpy as np
from scipy.fftpack import fft2, ifft2, fftshift
import imageio, math
import matplotlib.pyplot as plt
from skimage.util import random_noise
from matplotlib.colors import LogNorm


def diagonal(img, gap):
    """
    Create lines for diagonal moiré pattern

    gap: number of pixels between black pixels
    """
    img_noise = np.copy(img)

    for x in range(img_noise.shape[0]):
        for y in range(0, img_noise.shape[1], gap):
            img_noise[x,(y+x) % img_noise.shape[1]] = 0

    return img_noise


def horizontal(img, gap):
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


def vertical(img, gap):
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



def _general(grid_size, inter_grid_angle):
    pass


def general(img, grid_size=1, inter_grid_angle=4):
    """
    Interesting grid sizes and angles (respectively)
    (50, 30)
    (1, 13)
    """

    lambd = int(math.sqrt(2) * grid_size * \
                math.sqrt(1 + math.cos(math.radians(inter_grid_angle))) * \
                1/math.sin(math.radians(inter_grid_angle)))

    print('lambda = ', lambd)

    noise = img.flatten()

    noise[::lambd] = 0

    return noise.reshape(img.shape)
