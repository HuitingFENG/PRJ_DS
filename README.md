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