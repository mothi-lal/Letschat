import socket
import threading
from colorama import Fore, Style
import datetime
import sys

# Create a TCP/IP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server
try:
    client.connect(('10.184.17.122', 55556))  # Replace IP if server changes
except Exception as e:
    print(f"Could not connect to server: {e}")
    sys.exit()

# Ask for username
nickname = input("Choose your nickname: ")

log_file = "chat_history.txt"

def log_message(msg):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] {msg}\n")

# Function to receive messages from the server
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                if message.startswith(f"{nickname}:"):
                    # Print your own message in green
                    print(Fore.GREEN + message + Style.RESET_ALL)
                else:
                    # Print others' messages normally
                    print(message)
                log_message(message)
        except:
            print("Error! Connection to server lost.")
            client.close()
            break

# Function to write messages to the server
def write():
    while True:
        message = input("")
        if message.lower() == '/quit':
            quit_msg = f"{nickname} has left the chat."
            client.send(quit_msg.encode('utf-8'))
            client.close()
            print("Disconnected from chat.")
            break
        else:
            full_message = f"{nickname}: {message}"
            client.send(full_message.encode('utf-8'))



# Start threads for send and receive
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
