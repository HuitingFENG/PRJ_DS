''' import threading
import time

i = 65

def T1():
    global i
    reg = i
    time.sleep(0.1)
    reg+=1
    i=reg

def T2():
    global i
    reg = i
    time.sleep(0.1)
    reg-=1
    i=reg

T1 = threading.Thread(target=T1)
T2 = threading.Thread(target=T2)

T1.start()
T2.start()

T1.join()
T2.join()

print(i) '''


import threading
import time

i = 65

def T1():
    global i
    reg = i
    time.sleep(0.1)
    reg+=1
    i=reg

def T2():
    global i
    reg = i
    time.sleep(0.1)
    reg-=1
    i=reg

T1 = threading.Thread(target=T1)
T2 = threading.Thread(target=T2)

T2.start()
T1.start()

T2.join()
T1.join()

print(i)
