# heinl11
# listen.py
# 3.10.2021

import verify_search
from multiprocessing.connection import Listener

listener = Listener(("localhost", 4000), authkey=b"password")
listener._listener._socket.settimeout(3)
running = True
paragraph = ""

def listening():
    """Listens for data from Life Generator."""
    while running:
        # Listen for 3s for Life Generator data before opening GUI.
        try:
            connection = listener.accept()
        except:
            return
        while True:
            message = connection.recv()
            print('\nlistening message')
            print(message)
            if message == "close":
                connection.close()
                return paragraph
            else:
                send_paragraph(connection, message)


def send_paragraph(connection, message):
    """Send paragraph to Life Generator."""
    paragraph = verify_search.verify_keywords(message[0], message[1])
    print('\nresponse to Life Generator')
    print(paragraph[1])
    connection.send(paragraph)


