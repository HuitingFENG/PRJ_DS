import threading

total_hairdressers = 4
total_seats = 15
total_airlock = 2

mutex_hairdressers = threading.Semaphore(1)
mutex_seats = threading.Semaphore(1)
client_seated = threading.Semaphore(0)
airlock = threading.Semaphore(total_airlock)
  
# Create thread_hairdressers
def create_thread_hairdressers():
    # Use counting semaphore to create thread_hairdressers
    thread_hairdressers = []
    for i in (1, 5):
        thread_h = threading.Thread(target=thread_hairdresser, args=(i,))
        thread_h.start()
        thread_hairdressers.append(thread_h)
    return thread_hairdressers

def create_thread_clients():
    # Use counting semaphore to create client threads
    thread_clients = []
    for i in (1,100): 
        thread_c = threading.Thread(target=thread_clients, args=(i,))
        thread_c.start()
        thread_clients.append(thread_c)
    return thread_clients

# Main function
def thread_client(id_c):
    global total_hairdressers, total_seats
    # enter and sit
    mutex_seats.acquire()
    if total_seats > 0:
        total_seats -= 1
        print(f"Client N° {id_c} entered and got a seat.")
        mutex_seats.release()
        airlock.acquire()
    else:
        mutex_seats.release()
        print("Client N° {id_c} cannot find a seat and decided to leave.")
        return    
            
    # get a hairdresser
    mutex_hairdressers.acquire()
    if total_hairdressers > 0:
        total_hairdressers -= 1
        mutex_hairdressers.release()
        airlock.release()
    else:
        mutex_hairdressers.release()
        print(f"Client N° {id_c} waiting for a hairdresser.")

    # hairdressing process
    print(f"Client N° {id_c} is getting their hair done.")
    # hairdressing time
    print(f"Client N° {id_c} finished getting their hair done.")
    
    # release the hairdresser and leave the salon
    mutex_hairdressers.acquire()
    total_hairdressers += 1
    mutex_hairdressers.release()
    
    client_seated.release()
    airlock.release()    
    
    
def thread_hairdresser(id_h):
    global total_seats
    while True:
        client_seated.acquire()
        mutex_seats.acquire()
        total_seats += 1
        mutex_seats.release()

        print(f"Hairdresser N° {id_h} is cutting hair.")
        print(f"Hairdresser N° {id_h} finished cutting hair.")
        
        airlock.release()        

if __name__ == "__main__":
    t_h = create_thread_hairdressers()
    #t_c = create_thread_clients()
    
    ''' for i in t_h:
        i.join()
    
    for j in t_c:
        j.join()
         '''
 