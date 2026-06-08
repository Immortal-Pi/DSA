from concurrent.futures import ThreadPoolExecutor
import time
import numpy as np 

def cube_matrics(mat1,mat2):
    for i in mat1:
        for j in mat2:
            print(i*j)
            time.sleep(0.25)

if __name__=='__main__':
    mat1=np.array([[2,3,4,5,6],[6,3,1,3,5]])
    mat2=np.array([[2,3,4,5,6],[6,3,1,3,5]])
    t=time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        result=executor.map(cube_matrics,mat1,mat2)
    t2=time.time()
    f=t2-t
    for r in result:
        print(r)
    print(f)