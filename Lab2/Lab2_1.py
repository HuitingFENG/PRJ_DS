''' import threading
import time
import random


num_airlock = 2
num_waiting_seats = 15
num_hairdresser = 4

airlock_semaphore = threading.Semaphore(num_airlock)
waiting_seats_semaphore = threading.Semaphore(num_waiting_seats)
hairdresser_semaphore = threading.Semaphore(num_hairdresser)

airlock_lock = threading.Lock()
waiting_seats_lock = threading.Lock()
hairdresser_lock = threading.Lock()

airlocks = list(range(num_airlock))
waiting_seats = list(range(num_waiting_seats))
hairdressers = list(range(num_hairdresser))

def client(id_client):

        
    with waiting_seats_semaphore:
        with waiting_seats_lock:
            with airlock_semaphore:
                with airlock_lock:
                    airlock_num = airlocks.pop()
                print(f"Client {id_client} is entering an airlock.")
            waiting_seat_num = waiting_seats.pop()
        print(f"Client {id_client} is sitting in the waiting seats and is waiting an available hairdresser.")
        with airlock_lock:
            airlocks.append(airlock_num)
        
        with hairdresser_semaphore:
            with hairdresser_lock:
                hairdresser_num = hairdressers.pop()
            print(f"Client {id_client} is doing the hairdressing with an hairdresser.")
            hairdresser_semaphore.release() 
            print(f"Client {id_client} finished the hairdressing.")
            with hairdresser_lock:
                hairdressers.append(hairdresser_num)
            
        with waiting_seats_lock:
            waiting_seats.append(waiting_seat_num)
        
    
def hairdresser(id_hairdresser):
    print(f"Client {id_hairdresser} is waiting..")
    

if __name__ == "__main__":
    clients = [threading.Thread(target=client, args=(f'Client {i}',)) for i in range(1, 31)]
    #hairdressers = [threading.Thread(target=hairdresser, args=(f'Hairdresser {i}',)) for i in range(1, 5)]
    
    for i in clients:
        i.start()
    
        
    for j in hairdressers:
        j.start()
        
    
    print("Done!")
        
    
         '''

import threading
import time
import random

total_seats = 15
total_hairdressers = 4

available_seats = threading.Semaphore(1)
available_hairdressers = threading.Semaphore(1)
available_airlocks = threading.Semaphore(2)
seated_client = threading.Semaphore(0)
    
    

# clients
def clients(id_c):
    global total_seats, total_hairdressers
    # enter the salon and search for a available seat inside (leave if without available seat)
    
    if total_seats > 0:
        available_seats.acquire()
        total_seats -= 1
        print(f"Client {id_c} found an available seat.")
        available_seats.release()
        # enter the airlock after entering the salon
        available_airlocks.acquire()
    else:
        print(f"Client {id_c} decided to leave the salon since without available seats.")
        return
    
    # find an available hairdresser
    if total_hairdressers > 0:
        available_hairdressers.acquire()
        total_hairdressers -= 1
        print(f"Client {id_c} found an available hairdresser.")
        available_hairdressers.release()
        available_airlocks.release()
    else:
        print(f"Client {id_c} couldn't find an available hairdresser.")

    # do the hairdressing 
    time.sleep(0.01)
    # leave the hairdresser alone and leave the salon
    print(f"Client {id_c} finished the hairdressing done by the hairdresser.")
    available_hairdressers.acquire()
    total_hairdressers += 1
    available_hairdressers.release()
    seated_client.release()
    available_airlocks.release()    

# hairdressers
def hairdressers(id_h):
    global available_seats
    # wait for a client to sit in one of those available seats
    while True:
        seated_client.acquire()
    # do hairdressing for the seated client

    # return to be available status after finishing hairdressing of that client
    
       
        

         
         
         