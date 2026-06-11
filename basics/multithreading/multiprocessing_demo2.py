import time 
import multiprocessing
import math 
import sys 

sys.set_int_max_str_digits(1000000)

def compute_factorial(number):
    print(f'Computing factorial of number {number}')
    result=math.factorial(number)
    print(f'Factorial of {number} is {result}')
    return result

if __name__=='__main__':
    numbers=[50000,60000,70000,90000,10000,20000,40000,60000,20000,50000,60000,70000,90000,10000,20000,40000,60000,20000,50000,60000,70000,90000,10000,20000,40000,60000,20000,
             50000,60000,70000,90000,10000,20000,40000,60000,20000,50000,60000,70000,90000,10000,20000,40000,60000,20000,50000,60000,70000,90000,10000,20000,40000,60000,20000,
             50000,60000,70000,90000,10000,20000,40000,60000,20000,50000,60000,70000,90000,10000,20000,40000,60000,20000,50000,60000,70000,90000,10000,20000,40000,60000,20000,
             50000,60000,70000,90000,10000,20000,40000,60000,20000]
    start=time.time()
    with multiprocessing.Pool() as pool:
        results=pool.map(compute_factorial,numbers)
    end=time.time() 

    start2=time.time()
    all=[]
    for number in numbers:
        all.append(compute_factorial(number))
    end2=time.time()


    print(f'Result {all}')
    print(f'Time taken {end-start} seconds')
    print(f'Time taken {end2-start2} seconds')
