#  Simple Chat Application using Python

##  Project Overview

**Simple Chat Application** is a real-time, command-line chat application developed using Python.

The application allows two users to communicate with each other through a client-server architecture.

The project uses **Python sockets** to establish a connection between the client and server and uses **threading** to handle communication.

This is a beginner-friendly project for understanding:

* Computer networking
* Client-server architecture
* Python sockets
* TCP communication
* Threading
* Sending and receiving messages

---

#  Objectives

The main objectives of this project are:

* Create a simple real-time chat application.
* Understand client-server communication.
* Establish a connection using Python sockets.
* Send messages from a client to a server.
* Receive messages from the server.
* Allow continuous communication.
* Handle multiple communication tasks using threads.

---

# 🛠️ Technologies Used

| Technology   | Purpose                                     |
| ------------ | ------------------------------------------- |
| Python       | Main programming language                   |
| Socket       | Network communication                       |
| Threading    | Handle sending and receiving simultaneously |
| Command Line | User interface                              |
| TCP          | Reliable communication protocol             |

No external Python libraries are required for the basic version.

---

#  Project Structure

```text
Simple_Chat_Application/
│
├── server.py
├── client.py
└── README.md
```

---

#  Application Architecture

The application follows a **Client-Server Architecture**.

```text
              ┌──────────────────┐
              │      SERVER      │
              │                  │
              │  IP: 127.0.0.1  │
              │  Port: 5555      │
              └────────┬─────────┘
                       │
                       │ TCP Connection
                       │
             ┌─────────┴─────────┐
             │                   │
             ▼                   ▼
       ┌───────────┐       ┌───────────┐
       │  Client 1 │       │  Client 2 │
       │           │       │           │
       │ Send      │       │ Send      │
       │ Receive   │       │ Receive   │
       └───────────┘       └───────────┘
```

For the beginner version, the application can be implemented as a **two-user chat**.

---

#  How the Application Works

The basic workflow is:

```text
Start Server
      ↓
Server waits for connection
      ↓
Start Client
      ↓
Client connects to Server
      ↓
Connection Established
      ↓
Send / Receive Messages
      ↓
Chat Continues
      ↓
User Disconnects
      ↓
Connection Closed
```

---

#  What is a Socket?

A **socket** is an endpoint used for communication between two computers or two programs.

In this project:

```text
IP Address = 127.0.0.1
Port       = 5555
Protocol   = TCP
```

### 127.0.0.1

`127.0.0.1` refers to your own computer.

It is also called **localhost**.

### Port

The port identifies the communication endpoint.

For example:

```python
PORT = 5555
```

---

#  Server

The server waits for clients to connect.

Typical server operations are:

```text
1. Create socket
2. Bind IP address and port
3. Listen for connections
4. Accept client connection
5. Receive messages
6. Send responses
7. Close connection
```

Example:

```python
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 5555))

server.listen()

print("Server is waiting for connection...")

client, address = server.accept()

print("Connected:", address)
```

---

#  Client

The client connects to the server.

Typical client operations are:

```text
1. Create socket
2. Connect to server
3. Send messages
4. Receive messages
5. Continue chatting
6. Disconnect
```

Example:

```python
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 5555))

print("Connected to server!")
```

---

#  Why Threading is Used

Chat applications need to **send and receive messages continuously**.

Without threading, the program may get stuck waiting for a message.

For example:

```text
Thread 1
   ↓
Receive messages

Thread 2
   ↓
Send messages
```

This allows the user to type a message while simultaneously receiving messages from the other side.

Python's `threading` module can be used:

```python
import threading
```

---

#  How to Run the Project

## Step 1: Install Python

Check whether Python is installed:

```bash
python --version
```

You should see something similar to:

```text
Python 3.x.x
```

---

# Step 2: Open the Project

Open the project folder in VS Code or PyCharm.

For example:

```bash
cd "C:\Users\poornima\Downloads\Chat_Application"
```

---

# Step 3: Start the Server

Open the first terminal.

Run:

```bash
python server.py
```

You should see something similar to:

```text
[LISTENING] Chat server running on 127.0.0.1:5555
```

**Keep this terminal running.**

Do not stop or close the server.

---

# Step 4: Start the Client

Open a **second terminal**.

Run:

```bash
python client.py
```

You should see:

```text
Connected to server.
```

Now you can start chatting.

---

#  Important

Do **not** try to run the client in the same terminal while the server is still running.

Use:

```text
Terminal 1
──────────
python server.py
       ↓
Server running


Terminal 2
──────────
python client.py
       ↓
Client connected
```

If you are using PyCharm or VS Code's Run button, open a **separate terminal/process** for the second program.

---

#  Example Chat

### Server

```text
[LISTENING] Chat server running on 127.0.0.1:5555

Connected by ('127.0.0.1', 54321)

Client: Hello!
You: Hi! How are you?

Client: I am learning Python.
You: That's great!
```

### Client

```text
Connected to server.

You: Hello!

Server: Hi! How are you?

You: I am learning Python.

Server: That's great!
```

---

#  Message Flow

When the client sends:

```text
Hello Server!
```

the message travels like this:

```text
Client
   │
   │ "Hello Server!"
   ▼
Socket
   │
   ▼
Server
   │
   │ Receives message
   ▼
Server processes message
   │
   ▼
Socket
   │
   ▼
Client
```

---

#  Testing the Application

Test the application using different messages.

### Test 1

```text
Client: Hello
Server: Hi
```

### Test 2

```text
Client: How are you?
Server: I am fine.
```

### Test 3

```text
Client: What are you doing?
Server: I am learning Python.
```

### Test 4

Test disconnection:

```text
Client: exit
```

The application should close the connection properly.

---

# 🐛 Common Errors

## Error 1: Connection Refused

You may see:

```text
ConnectionRefusedError
```

### Reason

The client was started before the server.

### Solution

First run:

```bash
python server.py
```

Then run:

```bash
python client.py
```

---

# Error 2: Address Already in Use

You may see:

```text
OSError: [WinError 10048]
```

### Reason

Another server is already using the same port.

### Solution

Stop the previous server or use another port.

For example:

```python
PORT = 5556
```

Make sure both server and client use the same port.

---

# Error 3: Client Immediately Disconnects

If the client shows:

```text
Could not connect to the server.
Disconnected from server.
```

check that:

1. `server.py` is running.
2. The IP address is the same.
3. The port number is the same.
4. Windows Firewall is not blocking the connection.

---

#  IP Address and Port

Both programs must use matching values.

### Server

```python
HOST = "127.0.0.1"
PORT = 5555
```

### Client

```python
HOST = "127.0.0.1"
PORT = 5555
```

The client connects to the same address and port on which the server is listening.

---

# 📚 Python Concepts Used

This project helps you understand several important Python concepts.

### 1. Socket Programming

```python
socket.socket()
```

Used to create a network socket.

### 2. Bind

```python
server.bind((HOST, PORT))
```

Associates the server with an IP address and port.

### 3. Listen

```python
server.listen()
```

Makes the server wait for incoming connections.

### 4. Accept

```python
client, address = server.accept()
```

Accepts a client connection.

### 5. Connect

```python
client.connect((HOST, PORT))
```

Connects the client to the server.

### 6. Send

```python
client.send(message.encode())
```

Sends data.

### 7. Receive

```python
message = client.recv(1024).decode()
```

Receives data.

### 8. Threading

```python
threading.Thread(...)
```

Allows communication tasks to run concurrently.

---

#  Important Socket Functions

| Function    | Purpose               |
| ----------- | --------------------- |
| `socket()`  | Creates socket        |
| `bind()`    | Assigns IP and port   |
| `listen()`  | Waits for connections |
| `accept()`  | Accepts client        |
| `connect()` | Connects to server    |
| `send()`    | Sends data            |
| `recv()`    | Receives data         |
| `close()`   | Closes connection     |

---

#  Future Improvements

The basic chat application can be extended into a more advanced application.

Possible improvements include:

*  Multiple users
*  User authentication
*  Usernames
*  Private messaging
*  Multiple chat rooms
*  Graphical user interface
*  Internet-based communication
*  Store chat history
*  Encrypted messages
*  File sharing
*  Emojis
*  Online/offline status
*  Web-based chat using Flask or FastAPI

---

#  Project Learning Outcomes

After completing this project, you will understand:

* How client-server architecture works.
* How TCP communication works.
* How sockets are created.
* How a server accepts connections.
* How clients connect to servers.
* How data is sent and received.
* Why threading is useful in chat applications.
* How to troubleshoot connection errors.
* How real-time communication applications work.

---

#  Complete Project Flow

```text
                SERVER
                  │
                  │
          Create Socket
                  │
                  ↓
               Bind()
                  │
                  ↓
              Listen()
                  │
                  ↓
              Accept()
                  │
                  ↓
        Connection Established
                  │
                  │
        ┌─────────┴─────────┐
        │                   │
        ▼                   ▼
     Receive              Send
     Message              Message
        │                   │
        └─────────┬─────────┘
                  │
                  ▼
             Continue Chat
                  │
                  ▼
              Disconnect
```

---

#  Author

*Poornima H B*

Python Project
Socket Programming | Networking | Threading

---

#  Conclusion

The **Simple Chat Application** is a beginner-friendly project that demonstrates how two programs can communicate in real time using Python socket programming.

The key concept is:

```text
Client
   ↕
TCP Socket
   ↕
Server
```

By completing this project, you gain practical knowledge of **networking, sockets, client-server architecture, TCP communication, and multithreading**, which are useful concepts for building real-time applications.
 be used to automate text processing tasks efficiently. It is useful for beginners to understand file handling and regular expressions.
