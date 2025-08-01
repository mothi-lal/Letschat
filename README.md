# LetsChat - A Lightweight Python Chat Application

LetsChat is a simple, lightweight, and terminal-based chat application built using Python **sockets** and **threading** . It was created as a personal learning project to understand **socket programming**, **multithreading**, and building real-time systems. This project supports multiple clients on different devices communicating with a central server — and it now includes quality-of-life features like graceful exits and message logging.

---

## Motivation & Journey

This project started with a simple goal: **build a basic chat system that works on your any machine**.

Over time, it evolved into:
- A multi-client terminal chat application 
- An actual client-server architecture 
- Functionality to support **local networks and different devices** 
- Rich terminal output and logging with `colorama` & timestamped messages 
- Exploring how to connect it with Discord and cloud-based options (planned but not integrated)

The project helped us dive deep into:
- `socket` module for TCP/IP communication
- `threading` for handling multiple clients simultaneously
- String parsing and formatting for a better user experience
- Logging and debugging multi-user message exchange

---

## Features

- Real-time communication between multiple clients
- Multi-threaded server handling each client connection
- Chat history saved locally with timestamps
- Exit command (`exit`) added for clean disconnection
- Self messages are highlighted in green for clarity
- Client username selection
- Runs on LAN by using actual device IP
- Clean and readable terminal interface

---

## 📁 Folder Structure

Letschat/
│
├── client.py # The chat client (connects to server)
├── server.py # The chat server (handles multiple clients)
├── chat_history.txt # Log of all messages with timestamps
└── README.md # Project documentation (you're reading it!)


---

## ⚙️ How to Run

### 1. Clone the repo

git clone https://github.com/mothi-lal/Letschat.git
cd Letschat

### 2. Start the server (run on one machine)
python3 server.py

### 3. Start the client (run on same or different machines on same LAN)
client.connect(('YOUR_SERVER_IP_HERE', 55556))

then run python3 client.py

### 4. Type messages and chat freely!

To exit the chat simply type:

**exit**

## Requirements

Python 3.x
colorama (for colored terminal output)
If not available then Install using:

pip install colorama in terminal

## Key Learnings

This project reinforced my understanding of:

How TCP/IP sockets work
Real-time message handling across threads
Clean code separation of client/server responsibilities
Debugging distributed communication

## Contribution

This is a solo learning project, but you're welcome to:

Fork the repo
Improve UI/UX
Add features (emoji support, typing indicator, etc.)

