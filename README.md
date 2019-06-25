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

## Moiré Patterns
A moiré pattern is an interference pattern created when an observer observes through two overlapping periodic structures, in our case it ocours when someone tries to take a picture of a screen or monitor.
For this project we have decided to remove horizontal and vertical Moiré patterns.

## Techniques

### Noising
Taking pictures containing Moiré patterns can be quite difficult, as it depends a lot on your camera and the refresh rate of your monitor. Because of that, the patterns will be artificially generated, adding black vertical, horizontal and/or diagonal lines in the image. It is important to notice that the images used will be in grayscale.

### Denoising (with example)
Removing the Moiré pattern from the image is based on changing the domain of the image using the Fast Fourier Transform. 

![Example image](https://user-images.githubusercontent.com/23103524/60060175-cdfacc00-96c5-11e9-9ca0-bb7cb03d0054.jpg)
![Example fourier](https://user-images.githubusercontent.com/23103524/60060476-28e0f300-96c7-11e9-8e31-9f5d30fbb73b.png)

Then, three options of filters can be chosen to denoise: a low-pass filter (used in the example), a bandstop filter using threshold and a simple cut on the noise spectre. One or more filters are applied on the shifted Fourier of the noisy image, removing noises, verified to appear on the edges of the shifted Fourier image. The filter and filtered image can be seen below.

![Low-pass filter](https://user-images.githubusercontent.com/23103524/60060167-bde2ec80-96c5-11e9-8a04-4ec8a5c96bef.jpg)
![Filtered fourier](https://user-images.githubusercontent.com/23103524/60060475-267e9900-96c7-11e9-9313-e55062442521.png)

The original image essential frequencies are kept, denoising it back to the original (almost).

![Denoised](https://user-images.githubusercontent.com/23103524/60060190-e10d9c00-96c5-11e9-97cb-03a1f6e396ec.jpg)

## Code
There is a step-by-step example on a [Jupyter Notebook](https://github.com/LTKills/silentMoire/blob/master/study.ipynb) inside this repo.
You can also run the all.py document to see some images and results.

## Run yourself
If you want to run the script yourself, simply execute
`python silent.py <INPUT IMAGE>`
on the project root folder e follow the steps to apply some noise and denoise the image. Images are shown to accompany you through the process.

## Images source
All the images used in this project were taken from [Pexels](https://www.pexels.com/) and [Unsplash](https://unsplash.com/).

## Authors

- Gabriel de Melo Cruz
- Murilo Baldi
- Rafael Amaro Rolfsen
