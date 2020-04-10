import numpy as np
import matplotlib.pyplot as plt
import lmfit
from lmfit import minimize, Parameters, report_fit


# model - gaussian bell curve
#parameters - f0, sd, f- frequency
# frequency and data(absorption) are the actual values

def find_minimum(params, frequency, data):
    f0 = params['f0'].value
    m = params['m'].value
    c = params['c'].value
    k = params['k'].value
    amu = params['amu'].value
    T = params['T'].value # from a given temperature; not varied
    A = params['A'].value
    
    m = m * amu
    sigma =  np.sqrt((k*T)/((m)*pow(c,2)))*f0  

    model_gaussian = A*np.exp(-np.power(frequency-f0,2)/(2*sigma**2))
    
    return model_gaussian - data # gives back residual

    
def fitted_plot_gaussian(params, x, data):  
    x_plot = np.linspace(np.min(x), np.max(x), 500)
    model_gaussian = A*np.exp(-np.power(frequency-f0,2)/(2*sigma**2))
    return x_plot, model_gaussian


def gauss_fit(x,y):  
    params = Parameters()
    params.add('f0', value = 1, vary = True)
    params.add('m', value = 62, vary = False)
    params.add('c', value = 299792458, vary = False)
    params.add('k', value = 1.38064852e-23, vary = False) 
    params.add('amu', value = 1.6605402e-27,vary = False)
    params.add('T', vary = True) #Kelvin
    params.add('x0',min = np.min(x), max=np.max(x), vary = True)
    params.add('y0', vary = True)
    params.add('A', vary = True)
    result = minimize(find_minimum, params, args= (x,y)) #analogy - numbers for which you get the least chi-square value
    print (result)
    
    optimization_report = report_fit(result)

    (x_plot, model) = fitted_plot_gaussian(result.params, x, y)

    return x_plot, model, params, optimization_report




def main():

	x = np.genfromtxt('freq_file.txt')    
	y = np.genfromtxt("data_file.txt")

	x, y, parameter, optimization_report = gauss_fit(x,y)
	
	print('Report: ',optimization_report)


	plt.figure()
	plt.scatter(x,y)
	plt.plot(freq,data)
	plt.show()




if __name__ == '__main__':
    main()