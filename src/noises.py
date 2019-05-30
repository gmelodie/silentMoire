#
#
#
#
#
#
#
#
#
#  NOISE GENERATION FUNCTIONS
#
# take image, return image with noise
#
import numpy as np
from math import cos, sin


def horizontal(img):
    pass


def vertical(img):
    pass


def diagonal(img):
    pass


def _general(grid_size, inter_grid_angle):
    pass


def general(img, grid_size=1, inter_grid_angle=4):
    """
    Interesting grid sizes and angles (respectively)
    (50, 30)
    (1, 13)
    """

    lmb = int(math.sqrt(2) * grid_size * math.sqrt(1 + math.cos(inter_grid_angle)) * \
            1/math.sin(inter_grid_angle))

    noise = img.flatten()

    noise[::lmb] = 1

    return noise.reshape(img.shape)
