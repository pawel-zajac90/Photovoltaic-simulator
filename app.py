from photovoltanic_simulator.pv_power import *
from config import host_name, port, queue
from pika import ConnectionParameters, BlockingConnection

if __name__ == '__main__':
    simulator = PVSimulator()

    # Connection settings
    # ===================================
    con_params = ConnectionParameters(host=host_name)
    # ===================================
    meter = Meter(con_params)

    meter.run() # Starting Meter.run from meter_c.py, which send messages to rabbitMQ

    # Creating lists
    watts_value_list = simulator.read_from_rabbitMQ()
    pv_power_value_list = simulator.main()
    watts_PV_list = create_watts_pv_list(watts_value_list, pv_power_value_list)

    save(watts_value_list, pv_power_value_list, watts_PV_list) # Saving data to the file.

