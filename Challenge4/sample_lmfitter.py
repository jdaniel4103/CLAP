import numpy as np
import matplotlib.pyplot as plt
import lmfit
from lmfit import Minimizer, Parameters, report_fit


# function to run through minimizer
def fcn2min(params, x, data, plot_fit = False):
	A = params['A']
	x0 = params['x0']
	y0 = params['y0']

	if plot_fit == False:
		model = A * (x-x0)**2 + y0
		return np.array(model - data)

	else:
		x_plot = np.linspace(np.min(x), np.max(x), 200)
		model = A * (x_plot-x0)**2 + y0
		return x_plot,np.array(model)

def do_fit(x,y):
	params = Parameters()
	params.add('A', value = 1, min = -5, max = 5, vary = True)
	params.add('x0', value = 0, min = -5, max = 5, vary = True)
	params.add('y0', value = 0, min = -5, max = 5, vary = True)
	minner = Minimizer(fcn2min, params, fcn_args = (x,y))
	result = minner.minimize()
	con_report = lmfit.fit_report(result.params)

	(x_plot, model) = fcn2min(result.params, x, y, plot_fit = True)

	return x_plot, model, params, con_report


if __name__ == '__main__':
	# generating sample data
	X = np.linspace(-5,5,25)
	Y = np.zeros(len(X))
	for i in range(len(X)):
		Y[i] = 2.34*(X[i]-0.12)**2 + (2.0*np.random.ranf() - 1.0)
	


	x, y, par, con = do_fit(X,Y)
	
	print('Con Report: ',con)


	plt.figure()
	plt.scatter(X,Y)
	plt.plot(x,y)
	plt.show()