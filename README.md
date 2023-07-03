# PRJ_DS
## Efrei Paris M1 SE1
### FOUR & FENG

#### Project Distributed Fault-Tolerant Chat
In this project, you will be building a peer-to-peer distributed chat application.
The app should provide the following minimal functionalities :
1. Broadcasting messages up to 9 other chatters on 9 different nodes
2. Private texting between two nodes

Suggested Scenario
Constraints/Assumptions
1. The system accepts at the most a group of 10 nodes for chatting
2. Point-to-point (unreliable & unordered) messages (UDP) are used between nodes
3. Broadcasted messages should be received in a logical order (define it)
4. Private messages should be received in order (up to you to define it)

What I’m asking you to do...
1. Build an architecture on paper for such a system and write it in a small report (use the slides for that matter + other documents I’d be giving you)
2. Build some of the functions of your system (at least the messaging part – Step 1)

Step 1 – Group Communication (up to 10 nodes max)
Firstly, build a library of functions that would serve to exchange messages between nodes based on the identified sequence in which you would like these messages to be received.

Step 2 – Fault Tolerance
Fault tolerance solutions are mostly centered around redundancy schemes :
1. Duplicating messages
2. Replicating servers
3. ...





# Report
#### Step 0 - Architecture of the peer-to-peer distributed chat application

#### Step 1 - Group Communication
1. 9 old nodes + 1 new node + 1 authenticate server (login/signup)
2. Using UDP protocol during the communication betweens nodes:
    - create: each node creates a UDP socket to send or receive messages (python 'socket' module, 'socket.SOCK_DGRAM' parameter)
    - send: use 'socket' object's 'sendto' method for the message including the recipient's address (IP address and port)
    - receive: use 'socket' object's 'recvfrom' method for the received message (in python, each node has a thread to receive messages)
    - solve problem about potential packet loss and out-of-order message arrival:
        - reliable delivery: make an acknowledgment mechanism, which means after sending messages, if sender couldn't get an acknowledgment response within a certain timeout period, the sender can resend the message.
        - message ordering: give an id to each message, encode & decode the combination of id & message data, receiver use buffers to wait for all messages to arrive, receiver will wait if out-of-order messages and will send an acknowledgment message to sender after a certain timeout period so as to get the missing messages.
        - message data format (optional and some data can be null): send_all or send_one|sender_name|receiver_name|send_time|message_content (Before sending the message, it needs to be encoded into bytes using an encoding scheme like UTF-8. Upon receiving, the receiver decodes the message from bytes back into a readable format.)
3. Defining the logical order for the received broadcasted/public messages
    - sender gives id to each public message and sends a mixt of id+message to those who are in the same network (all other nodes)
    - receiver:
        - initialize the highest sequence number received so far in each chat discussion.
        - keep the highest sequent number in each discussion in the chat application (the next expected sequence number is the hightest sequence number received so far plus one.)
        - extract the message's id/sequence number after receiving the broadcasted/public message
        - if that id/sequence number is the next expected id/sequence number, this message will be processed immediately
        - otherwise, the receiver will store all arrival messages not having the next expected sequence number in the buffer until the messages are all in the correct order (from lowest sequence number to highest sequence number). In the meanwhile, all arrival messages will be sorted, and receiver will check periodically it the buffer contains the missing messages.
        - receiver will check the buffer from time to time, and will send an acknowledgment message to sender so as to get back the missing messages.
4. Defining the order for the received private messages 

5. About memory and resource usage
    - limit on the buffer size to limit the number of out-of-order messages that can be buffered. (list or queue in python).
    - limit the timeout duration to optimize the waiting time for missing messages. If receivers still cannot get the missing messages, they will process the arrival messages and then later process the missing messages which are arrived later.


#### Step 2 - Fault Tolerance
