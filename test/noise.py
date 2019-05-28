import numpy as np
from scipy.fftpack import fft2, ifft2
import imageio
import matplotlib.pyplot as plt
from skimage.util import random_noise


img = imageio.imread('images/arara.png')
img_fft = fft2(img)
plt.imshow(np.abs(img_fft), cmap='gray')
# plt.imshow(np.abs(img_fft), cmap='gray')
plt.show()

"""
img_ifft= ifft2(img)

plt.imshow(img, cmap='gray')
plt.show()

"""



