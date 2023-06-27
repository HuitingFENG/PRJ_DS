

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

