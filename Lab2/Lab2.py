import threading

hairdressers_available = 4
waiting_seats = 15
airlock_capacity = 2

hairdressers_mutex = threading.Semaphore(1)
waiting_seats_mutex = threading.Semaphore(1)
airlock = threading.Semaphore(airlock_capacity)
client_seated = threading.Semaphore(0)

def client_thread(client_id):
    global hairdressers_available, waiting_seats

    # Try to enter the salon and occupy a seat
    waiting_seats_mutex.acquire()
    if waiting_seats > 0:
        waiting_seats -= 1
        print(f"Client {client_id} entered the salon and occupied a seat.")
        waiting_seats_mutex.release()
        airlock.acquire()
    else:
        waiting_seats_mutex.release()
        print(f"Client {client_id} couldn't find a seat and left the salon.")
        return

    # Get a hairdresser
    hairdressers_mutex.acquire()
    if hairdressers_available > 0:
        hairdressers_available -= 1
        hairdressers_mutex.release()
        airlock.release()
    else:
        hairdressers_mutex.release()
        print(f"Client {client_id} waiting for a hairdresser.")

    # Hairdressing process
    print(f"Client {client_id} is getting their hair done.")
    # Hairdressing time...
    print(f"Client {client_id} finished getting their hair done.")

    # Release the hairdresser and leave the salon
    hairdressers_mutex.acquire()
    hairdressers_available += 1
    hairdressers_mutex.release()

    client_seated.release()
    airlock.release()

def hairdresser_thread(hairdresser_id):
    global waiting_seats

    while True:
        client_seated.acquire()
        waiting_seats_mutex.acquire()
        waiting_seats += 1
        waiting_seats_mutex.release()

        print(f"Hairdresser {hairdresser_id} is cutting hair.")
        # Haircutting time...
        print(f"Hairdresser {hairdresser_id} finished cutting hair.")

        airlock.release()

# Create hairdresser threads
hairdresser_threads = []
for i in range(4):
    thread = threading.Thread(target=hairdresser_thread, args=(i+1,))
    thread.start()
    hairdresser_threads.append(thread)

# Create client threads
client_threads = []
for i in range(20):
    thread = threading.Thread(target=client_thread, args=(i+1,))
    thread.start()
    client_threads.append(thread)

# Wait for all client threads to finish
for thread in client_threads:
    thread.join()

# Terminate hairdresser threads
for thread in hairdresser_threads:
    thread.join()


print("Done!")