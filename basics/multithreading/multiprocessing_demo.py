
import multiprocessing
import time 
import numpy as np 

def mul_number(mat1:np.float32, mat2:np.float32)->np.float32:
    for i in mat1:
        for j in mat2:
            print(i*j)
            time.sleep(1)

def cube_numbers(mat1:np.float32)->np.float32:
    for i in mat1:
        for j in mat1:
            for k in mat1:
                print(i*j*k)
                time.sleep(0.25)
if __name__=='__main__':
    mat1=np.array([[3,4,5,6],[6,7,8,8]])
    mat2=np.array([[3,5,6,3],[23,4,1,4]])
    p1=multiprocessing.Process(target=mul_number,args=(mat1,mat2,))
    p2=multiprocessing.Process(target=cube_numbers,args=(mat1,))

    time1=time.time()
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    time2=time.time()

    time3=time.time()
    mul_number(mat1,mat2)
    cube_numbers(mat1)
    time4=time.time()
    print(time2-time1,time4-time3)


