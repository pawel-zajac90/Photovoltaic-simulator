import csv
import pika
import datetime
from meter_c import *
import math
from timer import time
timer = time()

# Saving all data to .csv file
def save(watts_value_list, pv_power_value_list, watts_PV_list, timer=timer):
    choose_name = input("If You want to choose name of file press 'Y' (or press any other key to use default)")
    if choose_name.upper() == 'Y':
        name = input("Type name of new file (if file exist, it will be overwritten):  ") + (".csv")
    else:
        name = 'results.csv'
    print("Saving to the file.")
    with open(name, 'w') as csvfile:
        fieldnames = ['Timestamp', 'Watts used (W)', 'PV power (kW)', 'Watts + PV (W)']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        n = 0
        simulator = PVSimulator()
        for t in timer:
            writer.writerow({'Timestamp': str(t), 'Watts used (W)' : watts_value_list[n], 'PV power (kW)' : pv_power_value_list[n],
                             'Watts + PV (W)' : watts_PV_list[n]})
            n += 1
    print("Saved succesfully.")
    return name


# Creating list with values: Watts plus PV power
def create_watts_pv_list(w_list, pv_list):
    watts_PV_list = []

    for wats, photovoltaic_kw in zip(w_list, pv_list):
        photovoltaic_watt = photovoltaic_kw * 1000
        watts_PV_list.append(wats + photovoltaic_watt)

    return watts_PV_list


class PVSimulator:
    def __init__(self):
        self.pv_power = 0
        self.seconds_of_the_day = 60*60*24 # number of records

# listening messages from broker and creating Watts value list.
    def read_from_rabbitMQ(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
        channel = connection.channel()
        channel.queue_declare(queue="test")

        seconds = self.seconds_of_the_day
        watts_value_list = []

        def callback(ch, method, properties, body):
            watts_value_list.append(int(body.decode()))
            if len(watts_value_list) == seconds:
                print("All messages received.")
                channel.stop_consuming()

        channel.basic_consume(queue="test", on_message_callback=callback, auto_ack=True)
        print("Receiving...Please wait.")
        channel.start_consuming()
        return watts_value_list

# Generating PV power values
    def main(self):
        print("Genereting PV power value...")
        pv_power_value_list = []
        z = 0  # This variable defines the 1second/24h ratio.
        for t in timer:
            if t.hour < 6:  # PV is not working before 6 o'clock, so power = 0
                pv_power_value_list.append(0)
            elif 6 <= t.hour <= 21:
                z += 0.0002777
                pv_power = (3.3 * (math.exp((-((z - 14) ** 2) / 2) / (math.sqrt(44 / 7)))))
                pv_power_value_list.append(round(pv_power, 4))
            else:
                pv_power_value_list.append(0) # PV is not working after 21 o'clock, so power = 0
        print("Genereted.")
        return pv_power_value_list