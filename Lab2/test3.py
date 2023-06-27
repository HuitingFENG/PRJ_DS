import threading
import time

hairdressers = threading.Semaphore(4)
seats = threading.Semaphore(15)
airlocks = threading.Semaphore(2)
 # a queue of clients (assuming 20 clients in total)
clients_remaining = threading.Semaphore(20)

def client(id_client):
    # find an available seat
    print(f"Client {id_client} was looking for an available seat inside the salon.")
    if seats.acquire():
        print(f"Client {id_client} found an available seat.")
    else:
        print(f"Client {id_client} decided to leave the salon because of without finding an available seat.")
        return 
    
    # find an available airlock
    print(f"Client {id_client} was looking for an available airlock.")
    if airlocks.acquire():
        print(f"Client {id_client} found an available airlock and entered the airlock.")
    else:
        print(f"Client {id_client} decided to leave the salon because of without finding an available airlock.")
        seats.release()
        return 
    
    # find an available hairdresser
    print(f"Client {id_client} was looking for an available hairdresser.")
    hairdressers.acquire() # client will stay at the airlock until find an available hairdresser
    print(f"Client {id_client} found an available hairdresser.")
    airlocks.release()
    
    # do hairdressing then leave the salon 
    print(f"Client {id_client} was getting the hairdressing by the hairdresser.")
    time.sleep(0.01)
    print(f"Client {id_client} got the hairdressing done by the hairdresser.")
    time.sleep(0.01)
    print(f"Client {id_client} left the salon after finishing the hairdressing.")
    hairdressers.release()
    seats.release()
    clients_remaining.release()      

def hairdresser():
    # do hairdressing if there is at least a client in the queue of clients (clients_remaining)
    while clients_remaining.acquire():
        # check if having an available hairdresser, if so then do the hairdressing, if no then wait
        if hairdressers.acquire():
            time.sleep(0.01)
            hairdressers.release()

# create thread_clients and thread_hairdressers
thread_clients = []
thread_hairdressers = []
for i in range(1, 21):
    c = threading.Thread(target=client, args=(i,))
    c.start()
    thread_clients.append(c)
for j in range(1, 5):
    h = threading.Thread(target=hairdresser)
    h.start()
    thread_hairdressers.append(h)

# wait for each thread in thread_clients to be finished
for k in thread_clients:
    k.join()
print("Done!")