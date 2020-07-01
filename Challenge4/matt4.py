import numpy as np 
import matplotlib.pyplot as plt
import lmfit
from lmfit import Minimizer, Parameters, report_fit

def read_in(f_file = 'freq_file.txt', y_file = 'data_file.txt'):
	freq = np.genfromtxt(f_file)
	data = np.genfromtxt(y_file)

	return freq, data

def fxn(params, f, data, plot_fit = False):
	
	amu = 1.6605402e-27 #kg/amu
	m = 62*amu #kg
	c = 299792458 #m/s
	k = 1.38064852e-23 #(kg(m/s)**2)/K

	A = params['A']
	y0 = params['y0']
	f0 = params['f0']
	T = params['T']

	sigma = ((k*T)/(m*(c**2)))**(1/2)*f0

	if plot_fit == False:
		model = A * np.exp((-(f-f0)**2)/(2*sigma**2)) + y0

		return np.array(model - data)

	else:
		f_plot = np.linspace(np.min(f), np.max(f), 200)
		model = A * np.exp((-(f_plot-f0)**2)/(2*sigma**2)) + y0

		return f_plot,np.array(model)

def fit(x,y):

	params = Parameters()
	params.add('A', value = np.max(y), min = np.min(y)*.1, max = np.max(y)*2)
	params.add('f0', value = (np.max(x)-np.min(x))/2, min = np.min(x), max = np.max(x))
	params.add('y0', value = 0, min = -np.exp(-8), max = np.exp(-8))
	params.add('T', value = 20, min = 0, max = 100)
	minner = Minimizer(fxn, params, fcn_args = (x,y))
	result = minner.minimize()
	con_report = lmfit.fit_report(result.params)

	(x_plot, model) = fxn(result.params, x, y, plot_fit = True)

	return x_plot, model, result.params, con_report

if __name__ == '__main__':

	f, data = read_in()

	x, y, params, con_report = fit(f, data)

	print('Temp: {} K' .format(params['T'].value))
	print('Line Center: {} THz'.format(np.float(params['f0'].value)*1e-12))

	plt.figure()
	plt.scatter(f,data)
	plt.plot(x,y)
	plt.show()



