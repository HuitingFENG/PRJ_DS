# Solving the Problem : Synchronizing access using semaphores 

# 1.1
# import threading

# ITERATIONS = 1000000
# counter = 65

# def increment():
#     global counter
#     for _ in range(ITERATIONS):
#         counter += 1

# def decrement():
#     global counter
#     for _ in range(ITERATIONS):
#         counter -= 1

# if __name__ == "__main__":
#     thread1 = threading.Thread(target=increment)
#     thread2 = threading.Thread(target=decrement)

#     thread1.start()
#     thread2.start()

#     thread1.join()
#     thread2.join()

#     print(f"Counter: {counter}")

# 1.2
# import threading
# import time

# ITERATIONS = 1000000
# counter = 65

# def increment():
#     global counter
#     for _ in range(ITERATIONS):
#         reg = counter
#         time.sleep(0.00001)  # Sleep for a short time
#         reg += 1
#         counter = reg

# def decrement():
#     global counter
#     for _ in range(ITERATIONS):
#         reg = counter
#         time.sleep(0.00001)  # Sleep for a short time
#         reg -= 1
#         counter = reg

# if __name__ == "__main__":
#     thread1 = threading.Thread(target=increment)
#     thread2 = threading.Thread(target=decrement)

#     thread1.start()
#     thread2.start()

#     thread1.join()
#     thread2.join()

#     print(f"Counter: {counter}")



# import threading
# import time

# ITERATIONS = 10
# SLEEP_DURATION = 0.001
# counter = 76 # or 74

# def increment():
#     global counter
#     for _ in range(ITERATIONS):
#         reg = counter
#         time.sleep(SLEEP_DURATION)  # Sleep for a short time
#         reg += 1
#         counter = reg

# def decrement():
#     global counter
#     for _ in range(ITERATIONS):
#         reg = counter
#         time.sleep(SLEEP_DURATION)  # Sleep for a short time
#         reg -= 1
#         counter = reg

# if __name__ == "__main__":
#     thread1 = threading.Thread(target=increment)
#     thread2 = threading.Thread(target=decrement)

#     thread1.start()
#     thread2.start()

#     thread1.join()
#     thread2.join()

#     print(f"Counter: {counter}")



# 2.1
# import time
# from multiprocessing import Process, Value, Semaphore

# def increment(shared_var, sem):
#     sem.acquire()
#     reg = shared_var.value
#     time.sleep(0.001)
#     reg += 1
#     shared_var.value = reg
#     sem.release()

# def decrement(shared_var, sem):
#     sem.acquire()
#     reg = shared_var.value
#     time.sleep(0.001)
#     reg -= 1
#     shared_var.value = reg
#     sem.release()

# if __name__ == "__main__":
#     i = Value('i', 65)
#     sem = Semaphore(1)
#     tasks = []

#     # Run 3 processes
#     tasks.append(Process(target=increment, args=(i, sem)))
#     tasks.append(Process(target=decrement, args=(i, sem)))
#     #tasks.append(Process(target=increment, args=(i, sem)))

#     for task in tasks:
#         task.start()

#     for task in tasks:
#         task.join()

#     print("Final value of i:", i.value)

# 2.1.1
# import multiprocessing
# import time

# counter_i = 0 
# counter_d = 0

# def incrementer(i, semaphore):
#     for counter_i in range(100):
#         semaphore.acquire()
#         i.value += 1
#         semaphore.release()
#         time.sleep(0.01)

# def decrementer(i, semaphore):
#     for counter_j in range(100):
#         semaphore.acquire()
#         i.value -= 1
#         semaphore.release()
#         time.sleep(0.01)

# if __name__ == "__main__":
#     i = multiprocessing.Value("i", 65)
#     semaphore = multiprocessing.Semaphore(1)
    
#     T1 = multiprocessing.Process(target=incrementer, args=(i, semaphore))
#     T2 = multiprocessing.Process(target=decrementer, args=(i, semaphore))

#     T1.start()
#     T2.start()

#     T1.join()
#     T2.join()

#     print(f"The final counter's value is {i.value}.")


# 2.1.2
# import time
# import multiprocessing 

# def incrementer(i, semaphore):
#     semaphore.acquire()
#     time.sleep(0.001)
#     i.value += 1
#     semaphore.release()

# def decrementer(i, semaphore):
#     semaphore.acquire()
#     time.sleep(0.001)
#     i.value -= 1
#     semaphore.release()

# if __name__ == "__main__":
#     i = multiprocessing.Value('i', 65)
#     semaphore = multiprocessing.Semaphore(1)
    
#     T1 = multiprocessing.Process(target=incrementer, args=(i, semaphore))
#     T2 = multiprocessing.Process(target=decrementer, args=(i, semaphore))
#     # the final counter's value will be 64 if the target below is decrementer.
#     T3 = multiprocessing.Process(target=incrementer, args=(i, semaphore))
   
#     T1.start()
#     T2.start()
#     T3.start()

#     T1.join()
#     T2.join()
#     T3.join()

#     print(f"The final counter's value is {i.value}.")


# 2.1.3
# import time
# import threading

# counter_i = 0
# counter_d = 0

# def incrementer(i, lock):
#     for counter_i in range(100):
#         time.sleep(0.001)
#         lock.acquire()
#         i[0] += int(1)
#         lock.release()

# def decrementer(i, lock):
#     for counter_d in range(100):
#         time.sleep(0.001)
#         lock.acquire()
#         i[0] -= int(1)
#         lock.release()

# if __name__ == "__main__":
#     i = [65]
#     lock = threading.Lock()
    
#     T1 = threading.Thread(target=incrementer, args=(i, lock))
#     T2 = threading.Thread(target=decrementer, args=(i, lock))
#     T3 = threading.Thread(target=incrementer, args=(i, lock))
   
#     T1.start()
#     T2.start()
#     T3.start()

#     T1.join()
#     T2.join()
#     T3.join()

#     print(f"The final counter's value is {i[0]}.")

# import time
# import threading

# counter_i = 0
# counter_d = 0

# def incrementer(i, lock):
#     global counter_i
#     for counter_i in range(100):
#         time.sleep(0.001)
#         with lock: 
#             i[0] += 1

# def decrementer(i, lock):
#     global counter_d
#     for counter_d in range(100):
#         time.sleep(0.001)
#         with lock:
#             i[0] -= 1

# if __name__ == "__main__":
#     i = [65]
#     lock = threading.Lock()
    
#     T1 = threading.Thread(target=incrementer, args=(i, lock))
#     T2 = threading.Thread(target=decrementer, args=(i, lock))
#     # the final counter's value will be 64 if the target below is decrementer.
#     T3 = threading.Thread(target=incrementer, args=(i, lock))
   
#     T1.start()
#     T2.start()
#     T3.start()

#     T1.join()
#     T2.join()
#     T3.join()

#     print(f"The final counter's value is {i[0]}.")




# import time
# import multiprocessing

# def incrementer(i, lock):
#     with lock:
#         time.sleep(0.001)
#         i.value += 1

# def decrementer(i, lock):
#     with lock:
#         time.sleep(0.001)
#         i.value -= 1

# if __name__ == "__main__":
#     i = multiprocessing.Value('i', 65)
#     lock = multiprocessing.Lock()

#     T1 = multiprocessing.Process(target=incrementer, args=(i, lock))
#     T2 = multiprocessing.Process(target=decrementer, args=(i, lock))
#     T3 = multiprocessing.Process(target=incrementer, args=(i, lock))

#     T1.start()
#     T2.start()
#     T3.start()

#     T1.join()
#     T2.join()
#     T3.join()

#     print(f"The final counter's value is {i.value}.")





# 2.2
# import multiprocessing

# def p_1(r1, r2):
#     print("p_1: Wait for r1 and r2")
#     r1.acquire()
#     r2.acquire()
#     print("p_1: Acquire r1 and r2")

# def p_2(r1, r2):
#     print("p_2: Wait for r1")
#     r1.acquire()
#     print("p_2: Acquire r1 and Wait for r2")
#     r2.acquire()
#     print("p_2: Acquire r1 and r2")

# def p_3(r1, r2):
#     print("p_3: Wait for r2")
#     r2.acquire()
#     print("p_3: Acquire r2 and Wait for r1")
#     r1.acquire()
#     print("p_3: Acquire r1 and r2")

# if __name__ == "__main__":
#     r1 = multiprocessing.Semaphore(1)
#     r2 = multiprocessing.Semaphore(1)

#     p1 = multiprocessing.Process(target=p_1, args=(r1, r2))
#     p2 = multiprocessing.Process(target=p_2, args=(r1, r2))
#     p3 = multiprocessing.Process(target=p_3, args=(r1, r2))

#     p1.start()
#     p2.start()
#     p3.start()

#     p1.join()
#     p2.join()
#     p3.join()

#     print("All processes are done.")



# 2.3
import multiprocessing
import subprocess

def run_firefox(s1, s2):
    s1.acquire()
    subprocess.run(["firefox"])
    s2.release()

def run_emacs(s2, s3):
    s2.acquire()
    subprocess.run(["emacs"])
    s3.release()

def run_vi(s3, s1):
    s3.acquire()
    subprocess.run(["vi"])
    s1.release()

if __name__ == "__main__":
    r1 = multiprocessing.Semaphore(1)
    r2 = multiprocessing.Semaphore(0)
    r3 = multiprocessing.Semaphore(0)

    p1 = multiprocessing.Process(target=run_firefox, args=(r1, r2))
    p2 = multiprocessing.Process(target=run_emacs, args=(r2, r3))
    p3 = multiprocessing.Process(target=run_vi, args=(r3, r1))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("Question 2.3 is finished.")


# 2.4