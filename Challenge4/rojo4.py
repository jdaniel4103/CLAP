import numpy as np
import matplotlib.pyplot as plt
import lmfit
from lmfit import Minimizer, Parameters, report_fit


# model - gaussian bell curve
#parameters - f0, sd, f- frequency
# frequency and data(absorption) are the actual values

def find_minimum(params, frequency, data):
    f0 = params['f0']
    T = params['T'] 
    A = params['A']
    y0 = params['y0']

    
    m = 62 * (1.6605402*pow(10,-27)) #unit = kg (m*amu)
    c = 299792458 #m/s
    k = 1.38064852*pow(10,-23)
    sigma =  np.sqrt((k*T)/(m*c**2))*f0  

    model_gaussian = A*np.exp(-np.power(frequency-f0,2)/(2*sigma**2)) + y0
    
    return np.array(model_gaussian - data) # gives back residual

    
def fitted_plot_gaussian(params, x, data):  
    f0 = params['f0']
    T = params['T']
    A = params['A']
    y0 = params['y0']
    
    m = 62 * (1.6605402*pow(10,-27)) #unit = kg (m*amu)
    c = 299792458 #m/s
    k = 1.38064852*pow(10,-23)
    sigma =  np.sqrt((k*T)/((m)*pow(c,2)))*f0  

    x_plot = np.linspace(np.min(x), np.max(x), 200)
    model_gaussian = A*np.exp(-np.power(x_plot-f0,2)/(2*sigma**2)) +y0
    return x_plot, np.array(model_gaussian)


def gauss_fit(x,y):  
    params = Parameters()
    params.add('f0', value = (np.max(x)+np.min(x))/2.0, min = np.min(x), max = np.max(x))
    params.add('T', value =12.0, min = 0.0 , max = 50.0) #Kelvin
    params.add('y0', value = 0.0)
    params.add('A', value = np.max(y), min = np.max(y)*0.1, max = np.max(y)*2.0)

    result = Minimizer(find_minimum, params, fcn_args = (x,y)) #analogy - numbers for which you get the least chi-square value
    out = result.minimize()
    
    
    optimization_report = report_fit(out)

    (x_plot, model) = fitted_plot_gaussian(out.params, x, y)

    return x_plot, model, params, optimization_report




def main():

    x = np.genfromtxt('freq_file.txt')    
    y = np.genfromtxt("data_file.txt")

    freq, data, parameter, optimization_report = gauss_fit(x,y)

    print('Report: ',optimization_report)
    print ('Line Center: {} Thz'.format(np.float(parameter['f0'].value)*1e-12))



    plt.figure()
    plt.scatter(x,y)
    plt.plot(freq,data)
    plt.show()




if __name__ == '__main__':
    main()