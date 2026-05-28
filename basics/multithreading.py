import threading 
import time 

def task(name):
    print(f'Starting {name}')
    time.sleep(2)
    print(f'Finished {name}')

threads=[] 

for i in range(3):
    t=threading.Thread(target=task,args=(f'Task-{i}',))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All tasks completed")