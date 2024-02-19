#1.3_Parallel programming in Python

'''
Modification of the code from Volume_d_dim_ hypersphere_1.2.py so that it can run in parallel, by using futures.ProcessPoolExecutor.
Timing the runtime of the code to compare with that of Volume_d_dim_ hypersphere_1.2.py.

'''

import math
import numpy as np
from time import perf_counter as pc
import concurrent.futures as future


#np.random.seed(45)  


#Generate random points between -1,1 in d dimensions
def random_points(n,d):
	return np.random.uniform(-1, 1, size=(n, d))



#function that returns T/F for filtering
def in_hyp_sphere(point):
    return np.sum(point**2) <= 1



def vol_hyp_sphere(inp):
    p, d = inp

    # Generate random points - in every process / calling
    points = random_points(p, d)

    # iteratively filter all rows (d dim points) and keep only those that are true
    nsp = list(filter(in_hyp_sphere, points))

    # Calculate the approximation of volume
    vol_appr = (len(nsp) / len(points)) * (2**d)
    
    return vol_appr



def main():
    points_to_test = [(10000000, 11)]
    n_processes = 10

    start = pc()

    for n, dims in points_to_test:
        with future.ProcessPoolExecutor(max_workers=n_processes) as ex:
            all_processes = [(n // n_processes, dims)] * n_processes
            results = list(ex.map(vol_hyp_sphere, all_processes))
  
            # Calculate the actual volume
            actual_volume = math.pi**(dims/2) / math.gamma(dims/2 + 1)

            print(f"Dimensions: {dims}")
            print(f"Volume Approximation: {sum(results) / len(results)}")
            print(f"Actual Volume: {actual_volume}\n")

    end = pc()
    print(f"Process took {round(end-start, 2)} seconds")


if __name__ == '__main__':
    main()

'''

Testing (10000000, 11):

RESULTS 1.2:

	Dimensions: 11
	Volume Approximation: 1.8972672
	Actual Volume: 1.8841038793898994

	Process took 32.97 seconds

RESULTS 1.3:

	Dimensions: 11
	Volume Approximation: 1.86368
	Actual Volume: 1.8841038793898994

	Process took 9.28 seconds


With multiprocessing (parallel running) the same calculations take place ~3.5X faster that when run serially (default via Python)
In general it is expected that multiprocessing is faster than the running all procedures in one process as more CPU cores are utilized
parallelly. However how faster it can get it varies with the CPU and the numbers of cores available and set to be employed.

'''
