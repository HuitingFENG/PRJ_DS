''' import threading

# Create a semaphore with a maximum of 3 allowed threads
semaphore = threading.Semaphore(3)

def access_shared_resource(thread_name):
    print(f'{thread_name} is waiting to access the shared resource.')
    
    # Acquire the semaphore
    semaphore.acquire()
    
    print(f'{thread_name} has acquired the semaphore and accessed the shared resource.')
    
    # Simulate some work
    print(f'{thread_name} is performing some work...')
    
    # Release the semaphore
    semaphore.release()
    
    print(f'{thread_name} has released the semaphore.')

# Create multiple threads that access the shared resource
threads = []
for i in range(5):
    thread = threading.Thread(target=access_shared_resource, args=(f'Thread-{i+1}',))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
'''


''' import multiprocessing

multiprocessing.set_start_method('fork')
def perform_work(process_name):
    print(f'{process_name} is performing some work...')

# Create multiple processes
processes = []
for i in range(5):
    process = multiprocessing.Process(target=perform_work, args=(f'Process-{i+1}',))
    processes.append(process)
    process.start()

multiprocessing.freeze_support()
# Wait for all processes to complete
for process in processes:   
    process.join()
 '''


import threading
import time
import random

# The number of printers we have.
num_printers = 4

# This will limit the number of employees that can use a printer at the same time.
printer_semaphore = threading.Semaphore(num_printers)

# A lock for printer list
printers_lock = threading.Lock()

# A list to represent our printers.
printers = list(range(num_printers))

def employee(n):
    print(f'Employee {n} is waiting to use a printer.')
    with printer_semaphore:
        with printers_lock:  # Add lock when accessing shared printer list
            printer_num = printers.pop()
        print(f'Employee {n} is using Printer {printer_num}.')
        time.sleep(random.randint(1, 3))  # Simulate the employee using the printer for a variable time
        print(f'Employee {n} is done using Printer {printer_num}.')
        with printers_lock:  # Add lock when accessing shared printer list
            printers.append(printer_num)

# Create and start threads for 5 employees
employees = [threading.Thread(target=employee, args=(n,)) for n in range(5)]
for e in employees:
    e.start()

# Wait for all employees to finish
for e in employees:
    e.join()

print('All employees are done.')
