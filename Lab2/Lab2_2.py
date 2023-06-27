import threading
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

client_seated = threading.Semaphore(0)

def client(id_client):
    with waiting_seats_semaphore:
        with waiting_seats_lock:
            with airlock_semaphore:
                with airlock_lock:
                    airlock_num = airlocks.pop()
                print(f"Client {id_client} is entering an airlock.")
            waiting_seat_num = waiting_seats.pop()
        print(f"Client {id_client} is sitting in the waiting seats and is waiting for an available hairdresser.")
        with airlock_lock:
            airlocks.append(airlock_num)

        # Notify hairdresser about seated client
        client_seated.release()

        with hairdresser_semaphore:
            with hairdresser_lock:
                hairdresser_num = hairdressers.pop()
            print(f"Client {id_client} is doing the hairdressing with hairdresser {hairdresser_num}.")
            print(f"Client {id_client} finished the hairdressing.")
            with hairdresser_lock:
                hairdressers.append(hairdresser_num)

        with waiting_seats_lock:
            waiting_seats.append(waiting_seat_num)

def hairdresser(id_hairdresser):
    while True:
        print(f"Hairdresser {id_hairdresser} is waiting for a client.")
        # Sleep while waiting for clients
        client_seated.acquire()
        print(f"Hairdresser {id_hairdresser} is now attending to a client.")

if __name__ == "__main__":
    clients = [threading.Thread(target=client, args=(i,)) for i in range(1, 31)]
    hairdressers = [threading.Thread(target=hairdresser, args=(i,)) for i in range(1, num_hairdresser + 1)]

    for h in hairdressers:
        h.start()

    for c in clients:
        c.start()
    
    for c in clients:
        c.join()

    print("Done!")
