import numpy as np
from scipy.fftpack import fft2, ifft2, fftshift
import imageio
import matplotlib.pyplot as plt
from skimage.util import random_noise
from matplotlib.colors import LogNorm


def median_filter(img):
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




def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])



img = imageio.imread('images/cat_horizontal.jpg')
img = rgb2gray(img)
img_fft = fft2(img)
img_fft_shift = fftshift(img_fft)
#img_fft_shift_filtered = median_filter(img_fft_shift)


#res = ifft2(img_fft_shift)
res = ifft2(img_fft)
#plt.imshow(np.abs(img_fft_shift_filtered), cmap='gray', norm=LogNorm(vmin=5))
plt.imshow(np.abs(res), cmap='gray')
plt.show()



