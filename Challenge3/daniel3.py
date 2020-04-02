# John Daniel
# Challenge 3: I'm a little pyplot, gaussian!  Here is my half with, half maximum!
# This script is called along with a temperature in Kelvin and plots the Gaussian form of the transition that results.

import matplotlib.pyplot as plt
import numpy as np
import sys


# constants
kb = 1.38064852e-23 # m^2*kg*s^-2*K^-1
amu = 1.6605402e-27 # kg/amu
m = 62 * amu # kg, AlCl mass
c = 299792458 # m/s, speed of light
f0 = 1146.331050e12 # THz, line transition

try:
	T = np.float(sys.argv[1])
except:
	T = np.float(input('Temperature (K):'))

fmin = -500
fmax = 500
nf = 1000
f = np.linspace(fmin,fmax,nf)*1e6 + f0

sigma = np.sqrt(kb*T/(m*c**2))*f0

A = 1/(sigma*np.sqrt(2*np.pi))

Abs = A*np.exp(-(f-f0)**2/(2*sigma**2))

plt.figure()
plt.plot(f,Abs)
plt.show()