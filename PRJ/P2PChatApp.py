import threading
from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_REUSEADDR


MAX_NODES = 10
BUFFER_SIZE = 1024

node_addresses = []  
message_counter = 0  


socket = socket(AF_INET, SOCK_DGRAM)
socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

def send_message(message):
    global message_counter
    message_counter += 1
    data = f"{message_counter}:{message}".encode('utf-8')
    
    for address in node_addresses:
        socket.sendto(data, address)

def receive_messages():
    while True:
        data, address = socket.recvfrom(BUFFER_SIZE)
        message_parts = data.decode('utf-8').split(':', 1)
        
        if len(message_parts) == 2:
            message_id = int(message_parts[0])
            message = message_parts[1]
            print(f"Received message {message_id} from {address}: {message}")

def add_node(address):
    if len(node_addresses) < MAX_NODES:
        node_addresses.append(address)
        print(f"Node {address} added successfully.")
    else:
        print("Maximum number of nodes reached.")

def start_chat():
    threading.Thread(target=receive_messages).start()
    
    while True:
        message = input("Enter your message (or 'exit' to quit): ")
        if message.lower() == "exit":
            break
        send_message(message)

if __name__ == "__main__":
    host = input("Enter the host address: ")
    port = int(input("Enter the port number: "))
    socket.bind((host, port))

    print("Chat application started.")
    print("Enter 'exit' to quit.")

    while True:
        command = input("Enter a command (add_node, start_chat): ")
        if command == "add_node":
            new_host = input("Enter the host address of the new node: ")
            new_port = int(input("Enter the port number of the new node: "))
            add_node((new_host, new_port))
        elif command == "start_chat":
            start_chat()
        else:
            print("Invalid command. Try again.")
