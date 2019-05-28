import numpy as np
from scipy.fftpack import *
import imageio
import matplotlib.pyplot as plt


def low_pass(radius, final_shape, debug=False):
    filt = np.zeros((radius, radius))

    # TODO: enhance later
    for x in range(radius):
        for y in range(radius):
            if (radius//2 - x)**2 + (radius//2 - y)**2 < (radius//2)**2:
                filt[x][y] = 1

    # calculate padding shape
    # TODO: fix even/odd cases
    pad_rows = ((final_shape[0] - filt.shape[0])//2, \
                (final_shape[0] - filt.shape[0])//2)

    pad_cols = ((final_shape[1] - filt.shape[1])//2, \
                (final_shape[1] - filt.shape[1])//2)

    pad_shape = (pad_rows, pad_cols)

    # padding
    filt = np.pad(filt, pad_shape, 'constant', constant_values=0)

    if debug:
        plt.imshow(filt)
        plt.show()

    return filt


def high_pass(radius, debug=False):
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
