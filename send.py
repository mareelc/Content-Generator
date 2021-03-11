# Laura Maree
# send.py
# 3.10.2021

from multiprocessing.connection import Client
import random
import csv

def sending():
    """Sends new request to Life Generator for data."""
    random_category = read_random()

    #Build string for Life Generator
    keys = "toys, " + random_category + ", " + str(random.randint(1, 10))
    connection = Client(("localhost", 5000), authkey=b"password")
    print("\nsending message")
    print(keys)
    connection.send(keys)
    message = connection.recv()
    print("\ndata received")
    print(message)
    connection.send("close")

def read_random():
    """Generate random category to feed to Life Generator."""
    # Read amazon csv and choose category to feed.
    with open("amazon_co-ecommerce_sample.csv", encoding="UTF-8") as f:
        reader = csv.reader(f)
        chosen_row = random.choice(list(reader))
        split_line = chosen_row[8].split(" > ")
        return split_line[0]
