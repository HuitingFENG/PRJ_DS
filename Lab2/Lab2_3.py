import random 
import threading
import time

hairdressers = [threading.Semaphore(1) for i in range(4)]
seats = threading.Semaphore(15)
airlocks = threading.Semaphore(2)
 # a queue of clients (assuming 20 clients in total)
clients_remaining = threading.Semaphore(20)

def client(id_client):
    # arrive at the salon
    if not clients_remaining.acquire():
        print(f"Client {id_client} decided to leave the salon because it was ready full with clients.")
        return
    
    # find an available seat
    print(f"Client {id_client} was looking for an available seat inside the salon.")
    if seats.acquire():
        print(f"Client {id_client} found an available seat.")
    else:
        print(f"Client {id_client} decided to leave the salon because of without finding an available seat.")
        clients_remaining.release()
        return 
    
    # find an available airlock
    print(f"Client {id_client} was looking for an available airlock.")
    if airlocks.acquire():
        print(f"Client {id_client} found an available airlock and entered the airlock.")
    else:
        print(f"Client {id_client} decided to leave the salon because of without finding an available airlock.")
        seats.release()
        clients_remaining.release()
        return 
    
    # find an available hairdresser
    print(f"Client {id_client} was looking for an available hairdresser.")
    while True:
        for hairdresser in hairdressers:
            # client will stay at the airlock until find an available hairdresser
            if hairdresser.acquire():
                print(f"Client {id_client} found an available hairdresser.")
                airlocks.release()
                # do hairdressing then leave the salon 
                print(f"Client {id_client} was getting the hairdressing by the hairdresser.")
                # randomly choose duration between 1 and 3 seconds (duration of hairdressing)
                time.sleep(random.uniform(1,3))
                print(f"Client {id_client} got the hairdressing done by the hairdresser.")
                print(f"Client {id_client} left the salon after finishing the hairdressing.")
                hairdresser.release()
                seats.release()  
                clients_remaining.release()
                return         

# create thread_clients
thread_clients = []
for i in range(1, 21):
    c = threading.Thread(target=client, args=(i,))
    c.start()
    thread_clients.append(c)

# wait for each thread in thread_clients to be finished
for k in thread_clients:
    k.join()
print("Done! All clients finished their hairdressing.")