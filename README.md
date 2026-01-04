Distributed System Assignment
Distributed Matrix Multiplication using Multi-Server Computation

Prepared by
Debraj Dutta (220710007023)
Mayurakhya Nath (220710007034)
Lalhruaizela Khawlhring (220710007031)

Semester: 7th
Subject: Distributed Systems

1. Problem Statement

The objective of this assignment is to demonstrate distributed computation by performing matrix multiplication using multiple servers communicating over sockets.

We compute:

𝐶
=
𝐴
×
𝐵
C=A×B

Where:

Matrix A is of size (m × n)

Matrix B is of size (n × p)

Result matrix C is of size (m × p)

2. What is happening in this system

This system follows a client–server distributed architecture.

A client (master) sends the same matrix multiplication task to multiple servers.

Each server (worker) independently computes the matrix multiplication.

The client receives results from all servers and prints them.

🔹 This demonstrates:

Distributed execution

Socket-based inter-process communication

Parallel task execution across multiple servers

⚠️ Note:
In this implementation, all servers compute the same full matrix multiplication. The focus is on distributed communication, not load partitioning.

3. System Architecture (Conceptual)
Client (Master Node)

Reads input matrices A and B

Connects to multiple servers running on different ports

Sends matrices to each server

Receives computed results

Displays results from all servers

Servers (Worker Nodes)

Run on different ports (5000, 5001, 5002)

Accept matrix data from the client

Perform matrix multiplication

Send the result back to the client

This architecture follows a basic master–worker model.

4. Role of Each File
matrix_input.py

Contains the input matrices:

Matrix A

Matrix B

These matrices are imported by the client.

A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[9,8,7],[6,5,4],[3,2,1]]

client.py

Acts as the coordinator (master)

Responsibilities:

Imports matrices from matrix_input.py

Connects to all servers (5000, 5001, 5002)

Sends matrices using pickle serialization

Receives computed results from each server

Prints results received from servers

server_5000.py / server_5001.py / server_5002.py

Act as worker servers

Responsibilities:

Listen on a specific port

Accept client connection

Receive matrices A and B

Perform matrix multiplication

Send the computed result back to the client

All server files are identical except for the port number

5. Communication Mechanism

Socket Programming (TCP)

pickle module is used for:

Serializing Python objects before sending

Deserializing received data

6. How to Run the System
Step 1: Start the servers

Open three separate terminals and run:

python server_5000.py

python server_5001.py

python server_5002.py


Each server will display:

Server running on port XXXX

Step 2: Run the client

In another terminal:

python client.py

7. Expected Output

The client receives results from all servers:

Received results from servers:
[[30, 24, 18], [84, 69, 54], [138, 114, 90]]
[[30, 24, 18], [84, 69, 54], [138, 114, 90]]
[[30, 24, 18], [84, 69, 54], [138, 114, 90]]


Each server independently computes and returns the same result.
