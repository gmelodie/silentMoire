import numpy as np
from scipy.fftpack import fft2, ifft2, fftshift
import imageio
import matplotlib.pyplot as plt
from skimage.util import random_noise
from matplotlib.colors import LogNorm




def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])



img = imageio.imread('images/cat_original.jpg')
img = rgb2gray(img)
img_fft = fft2(img)
img_fft_shift = fftshift(img_fft)
plt.imshow(np.abs(img_fft_shift), cmap='gray', norm=LogNorm(vmin=5))
plt.show()

"""
img_ifft= ifft2(img)

plt.imshow(img, cmap='gray')
plt.show()

"""



