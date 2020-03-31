# Challenge 3: I'm a little pyplot, gaussian!  Here is my full width, half maximum!

Due: Apr 3, 2020

The purpose of this challenge is to learn the basics of the MatPlotLib.pyplot package.  This package is a powerful tool for plotting data.  Any time you see a plot from our lab, from scatter plots to color plots, they are all generated using the pyplot package.  For this script you will be creating a plot of a Doppler-broadened spectral line.

## Doppler Broadened Spectral Line

A spectral line always has some width to it, even as the sample approaches 0 K.  This is refered to as the "natural line width" of the transition.  In the case of a non-zero temperature, thermal effects of the sample lead to "Doppler Broadening".  As the temperature of the sample increases, you have atoms and molecules moving with a velocity according to their velocity distribution.  This means that you have some absorptions that are red-shifted and some that are blue-shifted, depending on whether the molecule that absorbed that photon was moving away from or towards the spectroscopy laser.  The absorption signal as a function of frequency is $$ Abs(f) = \frac{1}{\sigma \sqrt{2 \pi}} \exp{\frac{(f-f_0)^2}{2 \sigma^2}} $$ where $f_0$ is the line center and $\sigma$ is the standard deviation which is related to the temperature as $$ \sigma = \sqrt{\frac{kT}{mc^2}} f_0 $$ where $k$ is the Boltzman constant, $T$ is the temperature (in Kelvin), $m$ is the mass of the molecule, and $c$ is the speed of light.

## Challenge Tasks

Write a script that is called along with a temperature in Kelvin as a system argument.  The script will plot the doppler-broadened gaussian at that temperature using the matplotlib.pyplot package.  The line we will plot is the Q00 line of $Al^{27}Cl^{35}$.  The range we will look at is $\pm 500$ MHz around the center transition frequency of 1146.331050 THz.  For example, "script.py 12" would plot a doppler-broadened line for a temperature of 12 K.

## Useful Tips

1. For your import statement, using "import matplotlib.pyplot as plt" is a useful shortcut.
2. Use numpy arrays for the data instead of python lists.
3. Make sure to label axes and title your plot!
4. Pay attention to units!  Otherwise you fill find your gaussian looks more like either a delta function or a flat line instead of a gaussian!


## Constants

| Constant | Value                            |
| -------- | ------------------------------- :|
| f_0      | 1146.331050 THz                  |
| m        | 62 amu          				  |
| c        | 299792458 m/s                    |
| k        | 1.38064852e-23 m^2 * kg * s^-2 |
| amu      | 1.6605402e-27 kg                 |
