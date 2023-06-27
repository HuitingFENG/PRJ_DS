import threading

# Semaphores
available_seats = threading.Semaphore(15)
airlock_space = threading.Semaphore(2)
hairdresser_ready = [threading.Semaphore(0) for _ in range(4)]

def client(client_number, hairdresser_number):
    available_seats.acquire() # Wait for an available seat
    airlock_space.acquire() # Wait for airlock space
    # Client enters the airlock and takes a seat
    airlock_space.release() # Release the airlock space
    hairdresser_ready[hairdresser_number].release() # Notify the hairdresser
    # Client gets styled
    available_seats.release() # Release the seat

def hairdresser(hairdresser_number):
    while True:
        hairdresser_ready[hairdresser_number].acquire() # Wait for a client
        # Hairdresser styles the client

# Create threads for hairdressers
hairdresser_threads = [threading.Thread(target=hairdresser, args=(i,)) for i in range(4)]
for thread in hairdresser_threads:
    thread.start()

# Assume we have a list of clients with their preferred hairdressers
clients = [(1, 2), (2, 3), (3, 0), (4, 1)] # (client_number, hairdresser_number)
client_threads = [threading.Thread(target=client, args=(client_number, hairdresser_number)) for client_number, hairdresser_number in clients]
for thread in client_threads:
    thread.start()

# Wait for all clients to be done
for thread in client_threads:
    thread.join()



