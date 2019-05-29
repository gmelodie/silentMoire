# silentMoire

Moiré pattern denoiser for scanned photos


## The problem (or Abstract)

Whenever you try to take a picture of a screen or monitor they always end up with some weird patterns. These patterns, the Moiré patterns, can be removed by using image restoration techniques. The aim of this project is to create an application that allows you to easily denoise your scanned pictures in order to remove this types of patterns.


## In other words...

You are too lazy to take a proper screenshot of your screen. You see your phone nearby and decide to do the most stupid thing ever: take a pic of your screen with your phone. You end up with this:

![Noisy photo](https://user-images.githubusercontent.com/23103524/57874836-d8cd6180-77e7-11e9-8cda-cdf32e0b2f82.png)

We've all been there, enter silentMoire: using silentMoire you should be able to restore the image back to something more like the original picture:

![Restored photo](https://user-images.githubusercontent.com/23103524/57874787-c6ebbe80-77e7-11e9-899e-c72f5756e1df.png)

(Example images are inside the images folder)

## Techniques

### Pre-processing
Taking pictures containing Moiré patterns can be quite difficult, as it depends a lot on your camera and the refresh rate of your monitor. Because of that, the patterns will be artificially generated, adding black vertical, horizontal and/or diagonal lines in the image. It is important to notice that the images used will be in grayscale.

### Denoising
Removing the Moiré pattern from the image is based on changing the domain of the image using the Fast Fourier Transform. Then, a low-pass filter is applied on the shifted Fourier of the noisy image, removing the high frequency noises, verified to appear on the edges of the shifted Fourier image, keeping the image essential frequencies, denoising it back to the original (almost).

## Code
There is a step-by-step example on a [Jupyter Notebook](https://github.com/LTKills/silentMoire/blob/master/study.ipynb) inside this repo.
You can alsu run the all.py documment to see some images and results.

## Moiré Patterns
[description about Moire Patterns]
A moiré pattern is an interference pattern created when an observer observes through two overlapping periodic structures, in our case it ocours when someone try to take a picture of a screen or monitor.
For this work we decided to solve patterns that create lines at the noisy image, these lines being horizontal, vertical and diagonal.


## Authors

- Gabriel de Melo Cruz
- Murilo Baldi 
- Rafael Amaro Rolfsen
