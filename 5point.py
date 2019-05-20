
# calculate a 5-number summary
from numpy import percentile
from numpy.random import rand
import numpy

def load_uptimes(file):
    uptimes = []
    with open(file, 'r') as f:
        for line in f:
            try:
                uptimes.append(float(line))
            except:
                None #  Literally do nothing

    return uptimes
   


filename = 'results/HISTOGRAM.txt'

#data = generate_uptimes_for_histogram(10000)
#save_uptimes(data , filename)
data = load_uptimes(filename)


