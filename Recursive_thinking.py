"""
Student: Agapi Eleni Simaiaki
Reviewed date: 11/09/2023
Part of the course: Computer programming II (1TD722)
Uppsala University
"""
 
"""
Important notes: 
These examples are intended to practice RECURSIVE thinking. Thus, you may NOT 
use any loops nor built in functions like count, reverse, zip, math.pow etc.

"""


import time
import math

def power(x, n: int):                        # Optional
    """ Computes x**n using multiplications and/or division """
    if n==0:
        return 1
    elif n>0:
        return x*power(x,n-1)
    else:
        #n=-n 
        return 1 / (x*power(x,-n-1))
    pass


def multiply(m: int, n: int) -> int:         # Compulsory
    """ Computes m*n using additions"""
    if m==0 or n==0:
        return 0
    elif m>0 and n>0:
        if m<n:
            iterr=m
            num=n
        else:
            iterr=n
            num=m
        return num+multiply(num,iterr-1)
    else:
        print("Insert non-negative integers")
    pass



def divide(t: int, n: int) -> int:           # Optional
    """ Computes m*n using subtractions"""
    if t==n:
        return 1
    elif t>n:
        return 1+divide(t-n,n)
    else:
        return 0
    pass


def harmonic(n: int) -> float:                 # Compulsory
    """ Computes and returns the harmonc sum 1 + 1/2 + 1/3 + ... + 1/n"""
    if n==1:
        return 1
    else:
        return 1/n + harmonic(n-1)
    pass


def digit_sum(x: int, base=10) -> int:       # Optional
    """ Computes and returns the sum of the decimal (or other base) digits in x"""
    if base==2:
        x= get_binary(x)
    num=str(x)
    if len(num)==1:
        return int(num)
    else:
        return int(num[0])+int(digit_sum(num[1:]))
    pass


def get_binary(x: int) -> str:               # Compulsary
    """ Returns the binary representation of x """
    if x==0:
        return "0"
    elif x==1:
        return "1"
    elif x>1:
        return get_binary(x // 2) + str(x % 2)
    else:
        return '-' + get_binary(abs(x))
    pass


def reverse_string(s: str) -> str:           # Optional
    """ Returns the s reversed """
    if len(s) < 1:
        return "" 
    else:
        return s[-1]+reverse_string(s[:-1])
    pass


def largest(a: iter):                        # Compulsory
    """ Returns the largest element in a"""
    if len(a)==1:
        return a[0]
    else:
        maxv=a[0]
        a=largest(a[1:])
        if maxv > a:
            return maxv
        else:
            return a
    pass


def count(x, s: list) -> int:                # Compulsory
    """ Counts the number of occurences of x on all levels in s"""
    #Empty list return 0
    if not s:
        return 0
    counter = 0

    if x==s[0]:
        counter+=1

    #Check for all levels (only for lists checked here)
    elif type(s[0])==list:
        counter+=count(x,s[0])

    #Recursion adds each time that find x in first level
    counter+=count(x,s[1:])

    return counter
    pass


def zippa(l1: list, l2: list) -> list:       # Compulsory
    """ Returns a new list from the elements in l1 and l2 like the zip function"""
    #Check point
    if not l1 and not l2:
        return []
    
    new_list = []

    #Make sure it will work even with lists with different lengths
    if l1:
        new_list.append(l1[0])
    if l2:
        new_list.append(l2[0])

    rest = new_list + zippa(l1[1:], l2[1:]) 
    return rest
    pass


def bricklek(a: str, b: str, h: str, n: int) -> str:  # Compulsory
    """ Returns a string of instruction ow to move the tiles """
    #Check point
    if n==0:
        return []
    else:
        steps = bricklek(a, h, b, n-1) 
        steps.append(f"{a}->{b}") 
        steps+= bricklek(h, b ,a, n-1)
          
        return steps
    pass


def fib(n: int) -> int:                       # Compulsory
    """ Returns the n:th Fibonacci number """
    # You should verify that the time for this function grows approximately as
    # Theta(1.618^n) and also estimate how long time the call fib(100) would take.
    # The time estimate for fib(100) should be in reasonable units (most certainly
    # years) and, since it is just an estimate, with no more than two digits precision.
    #
    # Put your code at the end of the main function below!
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def main():
    print('\nCode that demonstates my implementations\n')
    
    n=30 #Randomly selected, large enough and feasible to run

    #Implementation of fib(n) for a set of n sequential numbers
    theta_observed=[]
    for i in range(1,n+1):
        tstart = time.perf_counter()
        fib(i)
        tstop = time.perf_counter()
        dif = tstop-tstart
        theta_observed.append(dif)


    #Calulation of theoritical expected additions for a set of n sequential numbers
    theta_expected=[(1.618**x) for x in range(1,n+1)]    

    print('\n\nCode for analysing fib\n')

    '''
    #Visual representation of the growth rate of fib(n) v.s. Θ(1.618^n)
    #Code is added as comment since matplotlib.pyplot is not in the advised packages
    import matplotlib.pyplot as plt

    #Plotting Observed
    import matplotlib.pyplot as plt

    x_values = list(range(1,n+1))
    y_values = theta_observed
    plt.plot(x_values, y_values, marker='o', linestyle='-', )
    plt.xlabel('Input Size n')
    plt.ylabel('Θ observed')
    plt.title('Exponential Growth Example (Observed)')
    plt.show()

    #Plotting EXpected
    x_values = list(range(1,n+1))
    y_values = theta_expected
    plt.plot(x_values, y_values, marker='o', linestyle='-', )
    plt.xlabel('Input Size n')
    plt.ylabel('Θ(1.618^n)')
    plt.title('Exponential Growth Example (Expected)')
    plt.show()
    '''

    print('\nBye!')


if __name__ == "__main__":
    main()

####################################################

"""
  Answers to the none-coding tasks
  ================================
  
  
  Theoretical exercise: Suppose you have a stack of 50 tiles and it takes 1 second to move one tile. How long will it take you to complete the entire transfer?
  
    secs = (2**50)-1
    minut = 60
    hours = 60
    days = 24 
    years = 365
    total_years = secs / (minut*hours*days*years)

    print("It would take",secs,"seconds or",total_years,"years in total to stack 50 tiles")

    Outcome: It would take 1125899906842623 seconds or 35702051.8405195 years in total to stack 50 tiles

    The calculation is based on the given mathematical equation of t(n)
    on Example 12: Analysis of the tile game. It is also obvious if run 
    the bricklek(a, b, h, n) function for n=1,2,3,4 etc and check the 
    length of the steps calculated. 
  
  
  
  
  Theoretical exercise:
       a) Verify by test runs that the time for the given Fibonacci algorithm grows as Θ(1.618n )
       b) Find out how long the calls fib(50) and fib(100) take (would take) on your compu-
          ter. Reply with appropriate units! (Seconds are not a suitable unit if it takes several
          hours. Hours are not a suitable unit if it takes several days or years.)

    a) To verify that the given Fibonacci algorithm grows as Θ(1.618^n) we have to run the fib(n) function
       for many different n and compare it to the expected number of additions 1.618^n (code provided in main() ).
       To make the comparison easier the results of the observed time response and the theoretical expect for the sample 
       n values were plotted (n=1-30). By looking into the plots (look at files: ex17_theta_expected.png, ex17_theta_observed.png)
       it is seen that although the numerical values are different their growth rates seem to be very similar. The numerical values 
       are expected to be different as in the observed results we are looking on the time calculated to execute the fib(n) function
       while on the other case we calculate the expected number of additions that will occur. In order for that number to be transformed 
       to time it should be multiplied with a constant c. That constant can differ in different PCs and based on their processing power. 
  

    b) Calculation of c constant & estimation of necessary time: 

        t(n) = c * 1.618^n
        c = t(n) / 1.618^n

        
        Calculate the observed time for a relatively high n. I selected n=30 as it's quite big and also fast to be calculated
        in my laptop:

        #Code

        n=30
        tstart = time.perf_counter()
        fib(n)
        tstop = time.perf_counter()
        time_dif = tstop-tstart

        c = time_dif / (1.618**n) 

        print(c) 
        # Outcome: 1.0728354523974806e-07


      Calculation of expected time for my laptop to calculate the fib(50) & fib(100):
        
        #Fib(50)

            print(c * (1.618**50)/60)

        Outcome: ~50 minutes (50.26986628067395)


        #Fib(100)

            print(c * (1.618**100)/(60*60*24*365))

        Outcome: ~2688922 years (2688922.2032194394)
  


  
  Theoritical exercise: Assume that insertion sort and merge sort take the same amount of time for 1000
                        random numbers – say 1 second. How long does it take for each algorithm to sort
                        10^6 and 10^9 random numbers respectively? Answer with appropriate units!

    Insertion sort - time Θ(n^2):

        * t_ins_6 = (10^6)^2 / 1000 = 10^12 / 1000 = 10^9 sec or 31,7 approximately years (10^9/(60*60*24*365))

        * t_ins_9 = (10^9)^2 / 1000 = 10^15 / 1000 = 10^12 or 31709,79 years

    Merge sort - time Θ(nlog(n)):

        * t_merg_6 = 10^6 * log(10^6) / 1000 = 6000 sec or 100 minutes

        * t_merg_9 = 10^9 * log(10^9) / 1000 = 9 * 10^6 or 104 approximately days (104,166667)



  
  Theoretical exercise: Theoretical comparison of Θ(n) and Θ(n · log n). 
                        Suppose you can choose between two algorithms, A and B, to solve a problem. We
                        let n denote the number of elements in the data structure on which the algorithms
                        operate. You know that algorithm A solves a problem of size n in n seconds. The time
                        required for algorithm B is c · n · log(n) seconds, where c is a constant. You run a test
                        of algorithm B on your computer and ﬁnd that it takes 1 second to solve a problem
                        when n = 10. How big must n be for algorithm A to take less time than algorithm B?

  
    To exactly calculate for which n the algorithm A will be more efficient 
    than algorithm B we have to calculate the constant c of algorithm B:

    algA < algB
    n < c * n * log(n)
    1 < c * log(n)
    log(n) > 1/c
    n > e^(1/c)  (1)

    So in general for  n > e^(1/c) we expect the algA to be more time efficient than algB.

    Calculation of c:

    We know that algB takes 1' for n=10. Therefore:

    c * 10 * log(10) = 1
    c = 1 / (10*log(10)) ~= 0.04342  (2)

    Combining (1) & (2):

    n > e^(1/0.04342)
    n > 10050229974.40087
    n > ~10^10

    Hence, for algorithm A to take less time than algorithm B,  n > ~10^10.


    * Complimentary in the file ex21.png the growth rates of both algorithms are presented. Unfortunately,
      due to computational restrictions, I could not run it for n > ~10^10. I run it for n = 10000000 and 
      the tendency of algB towards passing algA can be discerned.

      Code:

      repeats = 10000000

      algB = [(n*math.log(n)* (1 / (10*math.log(10))))for n in range(1,repeats+1)]
      algA = [x for x in range(1,repeats+1)]

      x_values = list(range(1,repeats+1))
      plt.plot(x_values, algA, marker='o', linestyle='-', color = "red" , label='Algorithm A - Θ(n)')
      plt.plot(x_values, algB, marker='o', linestyle='-', color = "blue",label="Algorithm B - Θ(n · log n)" )
      plt.legend()
      plt.xlabel("Number of Elements, n="+str(repeats))

      plt.show()


"""
