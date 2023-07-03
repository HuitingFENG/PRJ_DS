import socket
import threading
import time
import random
import heapq

from collections import defaultdict

class Node:
    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((host, port))
        self.node_addresses = []
        self.message_counter = 0
        self.received_messages = defaultdict(list)
        self.alive_nodes = defaultdict(int)


def send_message(self, message, recipient_node=None):
    data = f"{self.message_counter}:{message}".encode('utf-8')
    self.message_counter += 1
    if recipient_node:
        try:
            self.socket.sendto(data, recipient_node)
            if self.is_master:
                self.replicate_message(data, recipient_node)
        except Exception as e:
            print(f"Failed to send message to {recipient_node}: {e}")
    else:
        for node_address in self.node_addresses:
            try:
                self.socket.sendto(data, node_address)
                if not self.is_master:
                    duplicate_node_addresses = random.sample([node for node in self.node_addresses if node != node_address], 2) # Choose 2 other nodes
                    for duplicate_node in duplicate_node_addresses:
                        self.socket.sendto(data, duplicate_node)
            except Exception as e:
                print(f"Failed to send message to {node_address}: {e}")



def receive_messages(self):
    while True:
        data, addr = self.socket.recvfrom(1024)
        message_parts = data.decode('utf-8').split(':', 2)
        if len(message_parts) == 3:
            timestamp = float(message_parts[0])
            message_id = int(message_parts[1])
            message = message_parts[2]
            self.received_messages[addr].append((timestamp, message_id, message))
            self.process_received_messages()


def process_received_messages(self):
    while not self.message_heap.empty():
        message_id, message = heapq.heappop(self.message_heap)
        if message_id > self.message_counter:
            heapq.heappush(self.message_heap, (message_id, message))
            break
        if message_id == self.message_counter:
            print(f"Received message: {message}")
            self.message_counter += 1
            self.update_state(message.encode('utf-8'))  # Send state update to other nodes




def check_node_status(self):
    while True:
        current_time = time.time()
        inactive_nodes = [node_address for node_address, last_seen in self.alive_nodes.items() if current_time - last_seen > 5]

        for node_address in inactive_nodes:
            del self.alive_nodes[node_address]
            if node_address in self.node_addresses:
                self.node_addresses.remove(node_address)
                print(f"Node {node_address} removed due to inactivity.")

        time.sleep(1)  # Check every 1 second


def private_message(self):
    host = input('Enter the host of the node to message: ')
    port = int(input('Enter the port of the node to message: '))
    message = input('Enter your message: ')
    recipient_node = (host, port)
    self.send_message(message, recipient_node)

def start(self):
    threading.Thread(target=self.receive_messages).start()
    threading.Thread(target=self.check_node_status).start()
    threading.Thread(target=self.handle_election).start()

    while True:
        command = input('Enter a command (send/add/remove/private): ')
        if command == 'send':
            message = input('Enter your message: ')
            self.send_message(message)
        elif command == 'add':
            host = input('Enter the host of the node to add: ')
            port = int(input('Enter the port of the node to add: '))
            self.add_node(host, port)
        elif command == 'remove':
            host = input('Enter the host of the node to remove: ')
            port = int(input('Enter the port of the node to remove: '))
            self.remove_node(host, port)
        elif command == 'private':
            self.private_message()
        else:
            print('Invalid command. Try again.')


def update_state(self, state):
    for node_address in self.node_addresses:
        try:
            self.socket.sendto(state, node_address)
        except Exception as e:
            print(f"Failed to send state update to {node_address}: {e}")



if __name__ == '__main__':
    node_addresses = [('localhost', 12346), ('localhost', 12347), ('localhost', 12348)]  # example addresses
    node = Node('localhost', 12345)
    node.node_addresses = node_addresses
    
    node.start()
    

