# John Daniel
# Challenge 4: 
# This script reads in data from a file and uses lmfit to get the temperature and the line center.

import matplotlib.pyplot as plt
import numpy as np
import lmfit
from lmfit import Minimizer, Parameters, report_fit

# function to run through minimizer
def fcn2min(params, x, data, plot_fit = False):
	A = params['A']
	f0 = params['f0']
	y0 = params['y0']
	T = params['T']

	# constants
	kb = 1.38064852e-23 # m^2*kg*s^-2*K^-1
	amu = 1.6605402e-27 # kg/amu
	m = 62 * amu # kg, AlCl mass
	c = 299792458 # m/s, speed of light
	sigma = np.sqrt(kb*T/(m*c**2))*f0

	if plot_fit == False:
		model = A*np.exp(-(x-f0)**2/(2*sigma**2)) + y0 # Doppler broadened line
		return np.array(model - data)

	else:
		x_plot = np.linspace(np.min(x), np.max(x), 200)
		model = A*np.exp(-(x_plot-f0)**2/(2*sigma**2)) + y0 # Doppler broadened line
		return x_plot,np.array(model)


def do_fit(x,y):
	params = Parameters()
	params.add('A', value = np.max(y), min = np.max(y)*0.1, max = np.max(y)*2.0)
	params.add('f0', value = (np.max(x)+np.min(x))/2.0, min = np.min(x), max = np.max(x))
	params.add('y0', value = 0.0, min = -1.0e-8, max = 1.0e-8)
	params.add('T', value = 20.0, min = 0.0, max = 100.0)
	
	minner = Minimizer(fcn2min, params, fcn_args = (x,y))
	result = minner.minimize()
	con_report = lmfit.fit_report(result.params)

	(x_plot, model) = fcn2min(result.params, x, y, plot_fit = True)

	return x_plot, model, result.params, con_report


def read_in_data(x_file = 'freq_file.txt', y_file = 'data_file.txt'):

	freqs = np.genfromtxt(x_file)
	data = np.genfromtxt(y_file)

	return freqs, data


if __name__ == '__main__':

	f,a = read_in_data()

	x, y, par, con = do_fit(f,a)

	print('Temperature: {} K'.format(par['T'].value))
	print('Line Center: {} THz'.format(np.float(par['f0'].value)*1e-12))

	# Make plot
	plt.figure()
	plt.scatter(f,a)
	plt.plot(x,y)
	plt.xlabel('Frequency (THz)')
	plt.ylabel('Absorption (arb.)')
	plt.title('Doppler Broadened AlCl Line at {}K'.format(par['T'].value))
	plt.show()

