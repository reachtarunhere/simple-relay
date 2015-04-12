import string
import random
import socket
import unittest
import threading
from simplerelay import Server

class RecieverClient(threading.Thread):
    """ Reciever for connecting to server and
        recieves string as message.
    """
    def __init__(self):
        threading.Thread.__init__(self)
        self.recived_message = ''
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):

        server_address = ('127.0.0.1', 9999)
        self.sock.connect(server_address)
        data = self.sock.recv(1000)
        self.recived_message += data

class SenderClient(threading.Thread):
    """ Sender for connecting to server and
        sends random string as message.
    """
    def __init__(self):

        threading.Thread.__init__(self)
        self.sent_message = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5))
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        server_address = ('127.0.0.1', 9999)
        self.sock.connect(server_address)
        self.sock.sendall(self.sent_message)

class Relay(threading.Thread):
    """ Starts relay server. """
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        s = Server(9999)

class RelayTest(unittest.TestCase):

    def test_relay(self):
        """ Main test for server. """
        # objects for sender reciver
        sender = SenderClient()
        reciever = RecieverClient()
        relay_server = Relay() # starting the server
        # starting all threads
        relay_server.start()
        reciever.start()
        sender.start()


        reciever.join()
        sender.join()
        # checking if message sent & recived are same
        self.assertEquals(sender.sent_message, reciever.recived_message)

if __name__ == '__main__':
    unittest.main()
