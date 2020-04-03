# Tristan Rojo
# Challenge 2: Doppler Broadened Spectral Line
# The script shows a Doppler Broadened Spectral Line of Al27Cl35 via using Gaussian Nomral Distribution Function

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

def sd(temperature):

	f0 = 1146.331050 # Tetrahertz
	m = 62 * (1.6605402*pow(10,-27)) #unit = kg (m*amu)
	c = 299792458 #m/s
	k = 1.38064852*pow(10,-23)


	st = math.sqrt((k*temperature)/((m)*pow(c,2)))*f0
	return st  
    

def gaussian(sd): #+-500 MhZ from f0
    
    f0 = 1146.331050 
    f = np.linspace(f0-0.0005,f0+0.0005,100)
    absorption = 1/(sd*np.sqrt(2*math.pi))*np.exp(-np.power(f-f0,2)/(2*sd**2))
    plt.figure
    plt.plot(f,absorption, label = "$Al^27Cl^35$")
    plt.xlabel ("Frequency (THz)")
    plt.ylabel ("Absorption")
    plt.title ("Doppler Broadened Spectral Line- Absorption Signal")
    plt.legend()
    plt.grid()
    plt.show() 

def main():

    temperature = int(sys.argv[1])
    
    x = sd(temperature)
    print ("working")
    print ("Temperature =", int(sys.argv[1]), "K", end= ', ')
    print("sigma =", x)
    gaussian(x)

if __name__ == "__main__":
    main() 

