#Libraries
import matplotlib.pyplot as plt
import numpy as np
from numpy import sqrt, sin, cos, pi

#from scipy.optimize import curve_fit
#from scipy import special
#from scipy.special import erf

import matplotlib.pylab as pylab
import math

# Plot Formatting

pylab.rcParams['figure.figsize'] = 7,7/1.62
pylab.rcParams['figure.autolayout'] = False
pylab.rcParams.update({'axes.labelsize': 20})
pylab.rcParams.update({'xtick.labelsize': 12})
pylab.rcParams.update({'ytick.labelsize': 12})
pylab.rcParams.update({'lines.linewidth': 1.0})
pylab.rcParams.update({'axes.titlesize': 20.0})

pylab.rcParams.update({'ytick.direction': 'in'}) 
pylab.rcParams.update({'xtick.major.size': 7})   
pylab.rcParams.update({'xtick.direction': 'in'}) 
pylab.rcParams.update({'xtick.top': True}) 
pylab.rcParams.update({'xtick.minor.bottom': True}) 
plt.xlabel('Time After Explosion  (ms)',fontsize=12)
plt.ylabel('Radius of the Explosion (m)', fontsize=12)
plt.title('First Atomic Bomb Explosion Radius over Time',fontsize=12)

# Data
T = np.array([0.10,0.24,0.38,0.52,0.66,
              0.80,0.94,1.08,1.22,1.36,
              1.50,1.65,1.79,1.93,3.26,
              3.53,3.80,4.07,4.34,4.61,
              15.0,25.0,34.0,53.0,62.0])
R = np.array([11.1,19.9,25.4,28.8,31.9,
              34.2,36.3,38.9,41.0,42.8,
              44.4,46.0,46.9,48.7,59.0,
              61.1,62.9,64.3,65.6,67.3,
              106.5,130.0,145.0,175.0,185.0])


plt.plot(T,R,'r.')
plt.show()
