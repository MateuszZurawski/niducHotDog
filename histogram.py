import matplotlib.pyplot as plt

import simulator

import numpy as np
import sklearn.mixture
from scipy.optimize import curve_fit


def gauss(x,a,x0,sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

def generate_uptimes_for_histogram(number_of_times):
    s = simulator.Simulator()
    uptimes = s.uptimes_for_histogram(number_of_times)

    return uptimes

def test_gauss():
    plt.plot([x for x in np.arange(-3, 3, 0.01)], [gauss(x, 1, 1, 1) for x in np.arange(-3, 3, 0.01)])
    plt.show()

def save_uptimes(uptimes, output_file):
    with open(output_file, 'w') as f:
        for item in uptimes:
            f.write(f"{item}\n")

def load_uptimes(file):
    uptimes = []
    with open(file, 'r') as f:
        for line in f:
            try:
                uptimes.append(float(line))
            except:
                None #  Literally do nothing

    return uptimes
            
def generate_histogram(uptimes):
    #histogram = plt.hist(uptimes, 100)

    hist, bin_edges = np.histogram(uptimes, density=True, bins=100)
    bin_centres = (bin_edges[:-1] + bin_edges[1:])/2


    # Mediana w średniej niezawodności
    p0 = [1., 90., 1.]
    #coeff = p0

    coeff, var_matrix = curve_fit(gauss, bin_centres, hist, p0=p0)
    #print(coeff)
    # Get the fitted curve
    hist_fit = gauss(bin_centres, *coeff)
    
    plt.legend(loc='best')
    plt.plot(bin_centres, hist_fit, label='Fitted data', color='red')
    
    plt.bar(bin_centres, hist, label='Fitted data')
    print([gauss(x, *coeff) for x in range(80,90)])
    
    #plt.hist(uptimes, )
    
    # Finally, lets get the fitting parameters, i.e. the mean and standard deviation:
    print ('Fitted mean = ', coeff[1])
    print ('Fitted standard deviation = ', coeff[2])


    plt.show()
        


#test_gauss()
#exit()


filename = 'results/HISTOGRAM.txt'

#data = generate_uptimes_for_histogram(10000)
#save_uptimes(data , filename)
uptimes = load_uptimes(filename)

generate_histogram(uptimes)

