import pv_power as classes
import meter_c
import os
import datetime
from timer import time
import pika
from queue import Queue


class MainTests:
    def __init__(self):
        pass

    def read_from_rabbitMQ_test(self):
        print("======= Running 'read from rabbitMQ test' =======")
        meter = meter_c.Meter()
        meter.run()
        pvsimulator = classes.PVSimulator()
        assert type(pvsimulator.read_from_rabbitMQ()) == list
        print("******* Test ended successfull *******")

    def main_function_test(self):
        print("======= Running 'main function test' =======")
        pvsimulator = classes.PVSimulator()
        assert type(pvsimulator.main()) == list
        print("******* Test ended successfull *******")

    def w_plus_pv_test(self):
        print("======= Running 'W plus PV test' =======")
        assert classes.create_watts_pv_list([1, 2, 3], [2, 2, 2]) == [2001, 2002, 2003]
        print("******* Test ended successfull *******")

    def saving_test(self):
        print("======= Running 'saving test' =======")
        name = classes.save([1, 2, 3], [2, 2, 2], [2001, 2002, 2003], [1,2,3])
        assert name in os.listdir()
        print("******* Test ended successfull *******")


class MeterTest:
    def __init__(self):
        self.queue = Queue()

    def value_test(self):
        print("======= Running 'value test' =======")
        meter = meter_c.Meter()
        assert 0 <= int(meter.generate_value()) <= 9000
        print("******* Test ended successfull *******")

    def meter_test(self):
        print("======= Running 'meter test' =======")
        test_message = 1234
        meter = meter_c.Meter()
        meter.connect()
        meter.send(test_message)
        self.receiv()
        body = self.queue.get()
        assert body == test_message
        print("******* Test ended successfull *******")

    def receiv(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
        channel = connection.channel()
        channel.queue_declare(queue="test")

        def callback(ch, method, properties, body):
            self.queue.put(int(body.decode()))
            channel.stop_consuming()

        channel.basic_consume(queue="test", on_message_callback=callback, auto_ack=True)
        channel.start_consuming()

class TimerTest:
    def __init__(self):
        pass
    def time_test(self):
        print("======= Running 'time test' =======")
        timer = time()
        for t in timer:
            assert t.date() == datetime.date.today()
        print("******* Test ended successfull *******")
