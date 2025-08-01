import socket
import threading
from datetime import datetime


host = '0.0.0.0'
port = 55556

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message, sender_client=None):
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M")
    for client in clients:
        if client != sender_client:
            try:
                client.send(f"[{timestamp}] {message}".encode('utf-8'))
            except:
                client.close()
                if client in clients:
                    clients.remove(client)
                    nickname = nicknames[clients.index(client)]
                    broadcast(f"{nickname} has been disconnected.".encode('utf-8'))
                    nicknames.remove(nickname)

def handle(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if not message:
                raise Exception("No message received")
            broadcast(message, sender_client=client)
        except:
            if client in clients:
                index = clients.index(client)
                nickname = nicknames[index]
                clients.remove(client)
                nicknames.remove(nickname)
                client.close()
                broadcast(f'{nickname} left the chat!'.encode('utf-8'))
                break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} joined the chat!".encode('utf-8'))
        client.send("Connected to the server!".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print(f"Server running on {host}:{port}...")
receive()
