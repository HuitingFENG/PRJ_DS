''' import threading
import time

i= 65

def T1():
    global i
    for _ in range(1000):
        i+=1
        time.sleep(0.01)
    
def T2():
    global i
    for _ in range(1000):
        i-=1
        time.sleep(0.01)    
    
T1 = threading.Thread(target=T1)
T2 = threading.Thread(target=T2)

T1.start()
T2.start()

T1.join()
T2.join()

print(i)
 '''

import threading
i = 65

def T1():
    global i
    i+=1

def T2():
    global i
    i-=1
    
T1 = threading.Thread(target=T1)
T2 = threading.Thread(target=T2)

T1.start()
T2.start()

T1.join()
T2.join()

print(i)