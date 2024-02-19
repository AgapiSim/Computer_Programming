#1.2_Approximate the volume of a d-dimensional hypersphere

'''
A program that uses a Monte Carlo approximation of
the volume Vd (r) for a d-dimensional hypersphere radius r. A hypersphere is a generaliza-
tion of the circle and sphere to higher dimensions than two and three. The program should
have two arguments, n which is the number of random points to generate, and d which is
the number of dimensions. One can assume r = 1 and the center of the hypersphere is the
origin.

'''

import math
import random
import numpy as np
from time import perf_counter as pc
import concurrent.futures as future

random.seed(45) # reproducability 


#Generate random points between -1,1 in d dimensions
def random_points(n,d):
	return np.random.uniform(-1, 1, size=(n, d))



#function that returns T/F for filtering
def in_hyp_sphere(point):
    return np.sum(point**2) <= 1



def vol_hyp_sphere(points,d):

	# iteratively filters all rows (d dim points) and keeps only those that are true 
	nsp = list(filter(in_hyp_sphere, points))

	#calculate approximation of volume
	vol_appr = (len(nsp) / len(points)) * (2**d)
	
	return vol_appr



def main():
    points_to_test = [(10000000, 11)]

    start = pc()
    #Tact everything into a dict si that the printing is easier
    all_vol_approx = map(lambda x: {
        'dim': x[1],
        'vol_appr': vol_hyp_sphere(random_points(x[0], x[1]), x[1]),
        'act_vol': math.pi**(x[1]/2) / math.gamma(x[1]/2 + 1)
    }, points_to_test)

    #Extract all necessary info from the dict ti print
    for results in all_vol_approx:
        print(f"Dimensions: {results['dim']}")
        print(f"Volume Approximation: {results['vol_appr']}")
        print(f"Actual Volume: {results['act_vol']}\n")

    end = pc()
    print(f"Process took {round(end-start, 2)} seconds")




if __name__ == '__main__':
    main()



'''
Notes on Monte Carlo approximation of the volume:

	*Calculate how many points in d space belong to the hypersphere (percentage)
	*Calculate volume of a cube that contains this sphere (2**d where d is the number of dimensions - 2 is due to -1,1 range of selection of points)
	*Multiply the percentage with volume to find the volume

'''	

'''
Results:

For points_to_test = [(10000000, 11)]:

	Dimensions: 11
	Volume Approximation: 1.8825216
	Actual Volume: 1.8841038793898994

	Process took 36.88 seconds


'''
