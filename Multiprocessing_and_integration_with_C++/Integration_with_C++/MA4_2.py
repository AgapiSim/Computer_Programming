#!/usr/bin/env python3

import time
import matplotlib.pyplot as plt
from person import Person  # Import the Person class from your Python interface


# Python fibonacci recursion                                                                                                                                 
def fib_py(n):
    if n <= 1:
        return n
    else:
        return fib_py(n - 1) + fib_py(n - 2)



# Numba fibonacci                                                                                                                                            
from numba import njit

@njit
def fib_numba(n):
    if n <= 1:
        return n
    else:
        return fib_numba(n - 1) + fib_numba(n - 2)
        
        

# measure execution time for a given function                                                                                                                
def measure_time(func):
    start_time = time.perf_counter()
    result = func()
    end_time = time.perf_counter()
    return result, end_time - start_time



def main():
    f = Person(10)
    print(f.get())
    #f.set(10)                                                                                                                                               
    #print(f.get())                                                                                                                                          
    fibonacci = f.fib()

    # set the values to be examined                                                                                                                            
    n_values = [10, 15, 20, 25, 30, 35, 40, 47]
    execution_times = {
        "Python": [],
        "Numba": [],
        "C++": []
    }

    for n in n_values:
            result, exec_time = measure_time(lambda: fib_py(n)) #necessary as fib_py() requires s variable
            execution_times["Python"].append(exec_time)
            
            result, exec_time = measure_time(lambda: fib_numba(n)) #necessary as fib_numba(n) requires s variable
            execution_times["Numba"].append(exec_time)
            
            f = Person(n)
            result, exec_time = measure_time(f.fib)
            execution_times["C++"].append(exec_time)

            #print(result)
    # Plot and save the execution times to a figure
    plt.plot(n_values, execution_times["Python"], label="Python")
    plt.plot(n_values, execution_times["Numba"], label="Numba")
    plt.plot(n_values, execution_times["C++"], label="C++")
    plt.xlabel("n")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.savefig("fibonacci_execution_times.png")
    plt.show()



if __name__== "__main__":
        main()




'''
Running C++ for n=47 I get: -1323752223

That due to the integer overflow. In C++ i have to state the type of data and here I have stated that it is int. Apparrently getting a negative number
means that the value is more positions/digits than the default of the system (16, 32 or 64). Also an integer overflow can cause the value to wrap and 
become negative, which could justify the number we get.

'''
