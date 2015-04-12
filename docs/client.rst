Writing Clients
===============

The Basics
----------

Simple Relay allows 2 clients to connect at a time (2 different sockets) one to read and another to write. Depending on the requirements a client can be written such that it does both using two different sockets or two clients perform this function seperately.

The server stops as soon as any of the clients disconnect.

Workflow
--------

For both the clients (sender and reciever) one socket each needs to be initialized using socket.socket(). Then connection needs to be made to the server.
Once both clients are connected:-

Sender Side: Sends Data through socket (sendall method).
Reciver Client: Recives data from its socket (recv).