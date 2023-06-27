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

