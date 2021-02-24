# Laura Maree
# listen.py
# 2.24.2021

import verify_search
from multiprocessing.connection import Listener

listener = Listener(('localhost', 4000), authkey=b'password')
listener._listener._socket.settimeout(6)
running = True
paragraph = ""

def listening():
    """Listens for data from Life Generator."""
    while running:
        # Listen for 6s for Life Generator data before opening GUI.
        try:
            connection = listener.accept()
        except:
            return
        while True:
            message = connection.recv()
            if message == 'close':
                connection.close()
                return paragraph
            else:
                paragraph = verify_search.verify_keywords(message[0], message[1])
                connection.send(paragraph)

