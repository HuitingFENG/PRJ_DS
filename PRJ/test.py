import socket
import threading

PORT_LIST = [5000, 5001, 5002, 5003, 5004, 5005, 5006, 5007]
name = input("Enter your name: ")
host = 'localhost'
host_port = None
user_list = []

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# --------- Function ---------

# Show user list
def print_user_list():
    print()
    print("User list:")
    for user in user_list:
        print(f"{user[0]}: {user[1][0]}:{user[1][1]}")
    print()

# Send message to all users about new user
def im_new():
    for i in PORT_LIST:
        if i != host_port:
            client.sendto(f"SIGNUP_TAG:{name}".encode(), ('localhost', i))

# Send message to a user to ask who is he
def who_are_you():
    for i in PORT_LIST:
        if i != host_port:
            client.sendto(f"WHO_ARE_YOU:{name}".encode(), ('localhost', i))

# Send message to a user about who am i
def who_am_i(addr):
    # print(f'Who_am_i:{addr[0]}, {addr[1]}')
    client.sendto(f"IM_USER:{name}".encode(), (addr[0], addr[1]))

# Send message to all users about quitting
def i_quit():
    for i in PORT_LIST:
        if i != host_port:
            client.sendto(f"I_QUIT:{name}".encode(), ('localhost', i))

def are_you_there():
    for i in PORT_LIST:
        if i != host_port:
            client.sendto(f"ARE_YOU_THERE:{name}".encode(), ('localhost', i))

# Add new user to user list
def add_new_user(name, addr, seq_num=0):
    user_name = name
    user_list.append([user_name, addr, seq_num])

# Check if a port is available
def is_port_available(port):
    try:
        # Create a socket and try to bind it to the specified port
        client.bind(('localhost', port))
        # Port is available
        return True
    except OSError:
        # Port is not available
        return False
    
def print_help():
    print()
    print("Command list:")
    print(":q - Quit")
    print(":to <user name> <message> - Send message to a user")
    print(":list - Show user list")
    print(":help or :h - Show command list")
    print()

def receive():
    while True:
        try:
            data, addr = client.recvfrom(1024)
            if data.decode().startswith('SIGNUP_TAG'):
                user_name = data.decode()[data.decode().index(":")+1:]
                add_new_user(user_name, addr)
                who_am_i(addr)
                print(f"{user_name} joined!")
            elif data.decode().startswith('IM_USER'):
                user_name = data.decode()[data.decode().index(":")+1:]
                add_new_user(user_name, addr)
                print(f"{user_name} joined!")
            elif decoded_data.startswith("seq="):
                seq_num, msg = decoded_data[4:].split(";", 1)
                # Extract the sequence number
                seq_num = int(seq_num)
                # Find the user who sent this message
                user = next((u for u in user_list if u[1] == addr), None)
                # If this is the next message in the sequence, print it
                if user and seq_num == user[2] + 1:
                    print(msg)
                    # Increment the sequence number for this user
                    user[2] += 1
            else:
                print(data.decode())

        except:
            pass

def send_message():
    while True:
        message = input()
        if message == ':h' or message == ':help':
            print_help()

        elif message == ':q':
            print("Closing...")
            client.close()
            print("Closed")
            print("Bye!")
            exit()

        elif message.startswith(':to'):
            to_user = message.split(' ')[1]
            message_content = message.split(' ')[2:]
            message_content = ' '.join(message_content)
            for user in user_list:
                if user[0].lower() == to_user.lower():
                    client.sendto(f"mp {name}: {message_content}".encode(), (user[1][0], user[1][1]))

        elif message == ':list':
            print_user_list()

        else:
            for user in user_list:
                if user[1][1] != host_port:
                    #client.sendto(f"{name}: {message}".encode(), (user[1][0], user[1][1]))
                    user[2] += 1
                    # Append sequence number to the message
                    msg_with_seq = f"seq={user[2]};{name}: {message}"
                    client.sendto(msg_with_seq.encode(), (user[1][0], user[1][1]))

# ---------------------------

# Check if a port is available and bind to it
for i in PORT_LIST:
    if is_port_available(i):
        host_port = i
        print(f"Port {host_port} is available")
        print()
        im_new()
        break
    else:
        host_port = None
        continue
if host_port is None:
    print("No port available")
    exit()





receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send_message)
send_thread.start()
