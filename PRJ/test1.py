import socket
import threading
import time

class Node:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.host, self.port))
        self.node_addresses = []
        self.message_counter = 0
        self.received_messages = []

    def send_message(self, message):
        data = f"{self.message_counter}:{message}".encode('utf-8')
        self.message_counter += 1

        for node_address in self.node_addresses:
            self.socket.sendto(data, node_address)

    def receive_messages(self):
        while True:
            data, addr = self.socket.recvfrom(1024)
            message_parts = data.decode('utf-8').split(':', 1)
            if len(message_parts) == 2:
                message_id = int(message_parts[0])
                message = message_parts[1]
                self.received_messages.append((message_id, message))
                self.process_received_messages()

    def process_received_messages(self):
        self.received_messages.sort(key=lambda x: x[0])  # Sort messages by message_id

        for message_id, message in self.received_messages:
            print(f"Received message {message_id}: {message}")

if __name__ == '__main__':
    node_addresses = [('localhost', 12346), ('localhost', 12347), ('localhost', 12348)]  # example addresses
    node = Node('localhost', 12345)
    node.node_addresses = node_addresses

    threading.Thread(target=node.receive_messages).start()

    while True:
        message = input('Enter your message (or press Enter to exit): ')
        if not message:
            break
        node.send_message(message)
