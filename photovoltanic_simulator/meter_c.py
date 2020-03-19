from pika import BlockingConnection
import random
from photovoltanic_simulator.helpers import time
from config import queue
timer = time()

class Meter:
    def __init__(self, parameters):
        self.connection_parameters = parameters
        self.seconds_of_the_day = 60 * 60 * 24  # Number of records

    def generate_value(self):
        watts_value = random.randint(0, 9000)  # Genereting Watt values.
        return watts_value

    # Connecting to the server.
    def connect(self):
        print("Connecting...")
        self.connection = BlockingConnection(self.connection_parameters)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue)
        print("Connected.")
        connection = self.connection.is_open
        return connection


    # Send message.
    def send(self, message):
        self.channel.basic_publish(exchange="", routing_key="test", body=str(message))
        return

    # # Running program
    # def run(self):
    #     self.connect()
    #     print("Sending...please wait.")
    #     for _ in timer:
    #         message = '123'
    #         self.send(message)
    #     self.connection.close()  # Closing connection.
    #     print("Message sended.")


