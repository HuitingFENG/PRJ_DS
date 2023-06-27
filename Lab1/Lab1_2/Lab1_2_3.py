
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
