import multiprocessing

multiprocessing.set_start_method('fork')
m = multiprocessing.Manager()
t = m.list()
a, b, c, d, e, f = 1, 2, 3, 4, 5, 6
r1 = multiprocessing.Semaphore(0)
r2 = multiprocessing.Semaphore(0)
r3 = multiprocessing.Semaphore(0)

def T1(a, b):
    s = a + b
    t.append(s)
    r1.release()

def T2(c, d):
    s = c - d 
    t.append(s)
    r2.release()

def T3(e, f):
    s = e + f 
    t.append(s)
    r3.release()
    
def T4(r1, r2, r3):
    r1.acquire()
    r2.acquire()
    r3.acquire()
    temp_result = t[0] * t[1]
    result = temp_result * t[2]
    print(f"Result : ", {result})

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=T1, args=(a,b,))
    p2 = multiprocessing.Process(target=T2, args=(c,d,))
    p3 = multiprocessing.Process(target=T3, args=(e,f,))
    
    p1.start()
    p2.start()
    p3.start()
    
    p4 = multiprocessing.Process(target=T4, args=(r1, r2, r3))
    p4.start()
    
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    
    print("Question 2.4 is finished.")
    
    
    