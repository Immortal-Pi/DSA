import multiprocessing
import time 


def task(name):
    print(f'starting {name}')
    time.sleep(2)
    print(f'finished {name}')


if __name__=="__main__":
    process=[]
    for i in range(3):
        t=multiprocessing.Process(target=task,args=(f'process{i}',))
        process.append(t)
        t.start()

    for p in process:
        p.join()

    print('All process completed')