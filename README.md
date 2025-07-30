# Letschat 

**Letschat** is a simple real-time chatting app designed to help me learn full-stack development by building it hands-on.

## Creating client.py

Creating a chat server named client.py

Its main functons are :

Connects to the chat server (via IP + port).
Sends messages to the server.
Listens for messages from the server and prints them.
Keeps running until user quits.

dont run it still beacuse server.py has to br built

## Logic behind client.py

**step-1** is to import the socket

Socket is a Python module that allows us to create network connections between devices.

It gives us the ability to build clients and servers — like WhatsApp or Discord.

we use sockets to 
Connect to a server.
Sends messages to the server.
Receive messages from other clients via the server.

we used functions from the socket like :
socket.socket()
connect()
send()
recv()

**socket.socket() creates a new socket** 
used the parameters like AF_INET and SOCK_STREAM

**AF_INET :**is the ADDRESS FAMIlY means we are using IPv4  address like 127.0.0.1 and **SOCK_STREAM** is the socket type means here we are using TCP, a reliable connection based protocol. 

together we are saying to python to create a TCP socket that uses IPv4

**connect()** connects the client socket to the server. this is very important before sending/recieving messages 

Parammeters are IP address and Port number 

'127.0.0.1' → means localhost means my on own machine(laptop)
'55556' is the Port number that server is listening on

**send()** sends message from client tp server

it takes the parameter data(msg) and encodes it from string to bytes, 'utf-8' is the encoding format used for text

**recv()** recieves the message sent by the server 

here we docode the bytes into string by using .decode(utf-8)

## Creating server.py

now creating a server which will 
Accept multiple clients
Receive messages from each client
Broadcast messages to all other clients
