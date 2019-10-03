import pika
from random import randint
import datetime
from timer import time
timer = time()

class Meter:
    def __init__(self):
        self.channel = None
        self.seconds_of_the_day = 60 * 60 * 24  # Number of records

    def generate_value(self):
        watts_value = randint(0, 9000)  # Genereting Watt values.
        return watts_value

    # Connecting to the server.
    def connect(self):
        print("Connecting...")
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue="test")
        print("Connected.")

    # Sending message.
    def send(self, message):
        self.channel.basic_publish(exchange="", routing_key="test", body=str(message))

    # Running program
    def run(self):
        self.connect()
        print("Sending...please wait.")
        for _ in timer:
            message = self.generate_value()
            self.send(message)
        self.connection.close()  # Closing connection.
        print("Message sended.")
