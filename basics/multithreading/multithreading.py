import threading 
from time import time  
import time as t
def print_numbers(number):
    for i in range(number):
        print(f'number: {i}')
        t.sleep(1)

def print_letters(str):
    for letters in str:
        print(f'letter: {letters}')
        t.sleep(1)
number=26
str="this is amruth and he creates AGI"
time1=time()
print_numbers(number)
print_letters(str)
time2=time()



thread1=threading.Thread(target=print_numbers,args=(number,))
thread2=threading.Thread(target=print_letters,args=(str,))

time3=time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
time4=time()
print(f'time for execution without threading =: {time2-time1}')
print(f'time for execution with threading =: {time4-time3}')
