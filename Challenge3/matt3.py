import matplotlib.pyplot as plt
import numpy as np
import sys
import math 

f0 = 1146.331050
f = np.linspace(-500, 500, 1000) + f0
m = 62
c = 299792458
k = 1.38064852e-23
amu = 1.6605402e-27
T = float(sys.argv[1])

sigma = ((k*T)/((m*c)**2))**(1/2)*f0
print(sigma)

Abs = (1/(sigma*((2*math.pi)**(1/2))))*np.exp((-(f-f0)**2)/(2*(sigma**2)))
print(Abs)

plt.figure()
plt.title('Dopper-Broadened Gaussian at ' + str(T) + ' K for Al^27Cl^35')
plt.xlabel('Freq. (THz)')
plt.ylabel('Absorption')
plt.plot(f, Abs)
plt.show()
