#1.1_Monte Carlo approximation of π

'''
A program that has n, the number of random points that should be generated,
as an argument and produces the following output:

1. Print the number of points nc that are inside the circle.
2. Print the approximation of π ≈ 4nc /n.
3. Print the builtin constant π (math.pi) of Python.
4. Produce a png file that shows all points inside the circle as red dots and points outside
   the circle as blue dots
'''

import matplotlib.pyplot as plt
import math
import random


random.seed(47) # reproducability 


#Generate random points between -1,1
def random_points(n):
	return [(random.uniform(-1,1),random.uniform(-1,1)) for x in range(n)]



def mc_pi_appr(points):
	
	#Find the points inside the circ;e and outside
	nc=[]
	ns=[]
	for x,y in points:
		if x**2+y**2<=1:
			nc.append((x,y))
		else:
			ns.append((x,y))

	print(f"The number of point in circle are: {len(nc)}")

	#calculate π
	pi_appr = 4*(len(nc)/len(points))

	print(f"For {len(points)} points the π approximation is: {pi_appr}")
	print(f"The π is: {math.pi}")
	

	return {"nc": nc, "ns": ns, "pi_appr": pi_appr}


def main():

	num_points={1000, 10000, 100000}

	all_points ={ }

	#save all results in a dict
	for n in num_points:
		points = random_points(n)
		all_points[n]=mc_pi_appr(points)
	

	#iterate through the dict to plot the points based on where they belong
	for num, results in all_points.items():
		
		#unpacking the elements of nc,ns tuples iterably into 2 lists each with
		nc_x, nc_y = zip(*results['nc'])
		ns_x, ns_y = zip(*results['ns'])

		#plotting
		plt.scatter(nc_x, nc_y, color='red', label='Points Inside Circle') 
		plt.scatter(ns_x, ns_y , color='blue', label='Points Outside Circle')
		plt.title(f'Monte Carlo π Approximation (n = {num}): {results["pi_appr"]}')
		plt.legend()
		plt.grid(True)
		#plt.savefig(f'monte_carlo_pi_{num}.png')
		plt.show()


if __name__=='__main__':
	main()




